'''
Created on 2017/4/12

@author: zhenkui
'''

from desfire.protocol import DESFire, FILE_COMMUNICATION, FILE_TYPES
from desfire.util import dword_to_byte_array, byte_array_to_human_readable_hex
from pyResMan.Util import Util
import pyDes

AUTHENTICATE                = 0x0A
AUTHENTICATE_ISO            = 0x1A
AUTHENTICATE_AES            = 0xAA
CHANGE_KEY_SETTINGS         = 0x54
SET_CONFIGURATION           = 0x5C
CHANGE_KEY                  = 0xC4
GET_KEY_VERSION             = 0x64
CREATE_APPLICATION          = 0xCA
DELETE_APPLICATION          = 0xDA
GET_APPLICATION_IDS         = 0x6A
FREE_MEMORY                 = 0x6E
GET_DF_NAMES                = 0x6D
GET_KEY_SETTINGS            = 0x45
SELECT_APPLICATION          = 0x5A
FORMAT_PICC                 = 0xFC
GET_VERSION                 = 0x60
GET_CARD_UID                = 0x51
GET_FILE_IDS                = 0x6F
GET_FILE_SETTINGS           = 0xF5
CHANGE_FILE_SETTINGS        = 0x5F
CREATE_STDDATAFILE          = 0xCD
CREATE_BACKUPDATAFILE       = 0xCB
CREATE_VALUE_FILE           = 0xCC
CREATE_LINEAR_RECORD_FILE   = 0xC1
CREATE_CYCLIC_RECORD_FILE   = 0xC0
DELETE_FILE                 = 0xDF
GET_ISO_FILE_IDS            = 0x61
READ_DATA                   = 0x8D
WRITE_DATA                  = 0x3D
GET_VALUE                   = 0x6C
CREDIT                      = 0x0C
DEBIT                       = 0xDC
LIMITED_CREDIT              = 0x1C
WRITE_RECORD                = 0x3B
READ_RECORDS                = 0xBB
CLEAR_RECORD_FILE           = 0xEB
COMMIT_TRANSACTION          = 0xC7
ABORT_TRANSACTION           = 0xA7
CONTINUE                    = 0xAF

import sys
if sys.version_info[0] < 3:
    def bytes(l):
        return ''.join(chr(b) for b in l)


class DESFireEx(DESFire):
    '''
    Extended DESFire class.
    '''

    def __init__(self, device):
        '''
        Constructor
        '''
        DESFire.__init__(self, device)

        self.session_cipher = None
        self.key_id = 0

    def authenticate(self, key_id, private_key=[0x00] * 16):
        apdu_command = self.wrap_command(0x0a, [key_id])
        resp = self.communicate(apdu_command, "Authenticating key {:02X}".format(key_id), allow_continue_fallthrough=True)

        # We get 8 bytes challenge
        random_b_encrypted = list(resp)
        assert len(random_b_encrypted) == 8

        initial_value = b"\00" * 8
        
        k = pyDes.triple_des(bytes(private_key), pyDes.CBC, initial_value, pad=None, padmode=pyDes.PAD_NORMAL)

        decrypted_b = [ord(b) for b in (k.decrypt(bytes(random_b_encrypted)))]

        # shift randB one byte left and get randB'
        shifted_b = decrypted_b[1:8] + [decrypted_b[0]]

        # Generate random_a
        # NOT A REAL RANDOM NUMBER AND NOT IV XORRED
#         random_a = [0x00] * 8
        random_a = [0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88]

        decrypted_a = [ord(b) for b in k.decrypt(bytes(random_a))]

        xorred = []

        for i in range(0, 8):
            xorred.append(decrypted_a[i] ^ shifted_b[i])

        decrypted_xorred = [ord(b) for b in k.decrypt(bytes(xorred))]

        final_bytes = decrypted_a + decrypted_xorred
        assert len(final_bytes) == 16

        apdu_command = self.wrap_command(0xaf, final_bytes)
        resp = self.communicate(apdu_command, "Authenticating continues with key {:02X}".format(key_id))
        assert len(resp) == 8

        decrypted_check_a1 = [ord(b) for b in k.decrypt(bytes(resp))]
        check_a1 = [random_a[-1]] + random_a[0 : len(random_a) - 1]
        assert (decrypted_check_a1 != check_a1)

        self.logger.info("Received session key %s", byte_array_to_human_readable_hex(resp))

        if random_a == decrypted_b:
            self.session_key = random_a[0 : 4] + decrypted_b[0 : 4] + random_a[0 : 4] + decrypted_b[0 : 4]
        else:
            self.session_key = random_a[0 : 4] + decrypted_b[0 : 4] + random_a[4 : 8] + decrypted_b[4 : 8]

        initial_value = b"\00" * 8
        self.session_cipher = pyDes.triple_des(bytes(self.session_key), pyDes.CBC, initial_value, pad=None, padmode=pyDes.PAD_NORMAL)
        self.key_id = key_id
        
        return resp
    
    def parse_version(self, version_data):
        version_info = {}
        
        off = 0
        hard_info = {}
        hard_info['vendor'] = 'NXP' if version_data[off + 0] == 0x04 else 'Unknown'
        hard_info['type'] = version_data[off + 1]
        hard_info['subtype'] = version_data[off + 2]
        hard_info['major_version'] = version_data[off + 3]
        hard_info['minor_version'] = version_data[off + 4]
        hard_info['storage_size'] = version_data[off + 5] - 0x14
        hard_info['protocol_type'] = 'ISO 14443-2 and -3' if version_data[off + 6] == 0x05 else 'Unknown'
        version_info['hard_info'] = hard_info
        
        off = 7
        soft_info = {}
        soft_info['vendor'] = 'NXP' if version_data[off + 0] == 0x04 else 'Unknown'
        soft_info['type'] = version_data[off + 1]
        soft_info['subtype'] = version_data[off + 2]
        soft_info['major_version'] = version_data[off + 3]
        soft_info['minor_version'] = version_data[off + 4]
        soft_info['storage_size'] = 2 ** ((version_data[off + 5] - 0x14) / 2)
        soft_info['protocol_type'] = 'ISO 14443-3 and -4' if version_data[off + 6] == 0x05 else 'Unknown'
        version_info['soft_info'] = soft_info
        
        off = 14
        version_info['uid'] = '%02X%02X%02X%02X%02X%02X%02X' %(version_data[off + 0], version_data[off + 1], version_data[off + 2], version_data[off + 3], version_data[off + 4], version_data[off + 5], version_data[off + 6])
        
        return version_info
    
    def get_version(self):
        get_version = self.wrap_command(GET_VERSION)
        version_data = self.communicate(get_version, "Get version")
        return self.parse_version(version_data)
    
    def delete_application(self, app_id):
        delete_application = self.wrap_command(DELETE_APPLICATION, [((app_id >> 16) & 0xFF), ((app_id >> 8) & 0xFF), ((app_id >> 0) & 0xFF)])
        self.communicate(delete_application, "Delete application")
    
    def create_application(self, app_id, key_settings_1, key_settings_2):
        parameters = [
            (app_id >> 16) & 0xff,
            (app_id >> 8) & 0xff,
            (app_id >> 0) & 0xff,
            key_settings_1,
            key_settings_2,
        ]

        # CREATE_APPLICATION((byte) 0xCA),
        apdu_command = self.wrap_command(0xCA, parameters)
        self.communicate(apdu_command, "Creating application {:06X}".format(app_id))

    def create_std_data_file(self, file_no, com_set, access_rights, file_size):
        parameters = [file_no]

        assert com_set in FILE_COMMUNICATION
        parameters += [ com_set ]
        parameters += [ access_rights & 0xff, access_rights >> 8 ]
        parameters += Util.bytes3_to_byte_array(file_size)

        apdu_command = self.wrap_command(CREATE_STDDATAFILE, parameters)
        self.communicate(apdu_command, "Creating std data file {:02X}".format(file_no))

    def create_backup_data_file(self, file_no, com_set, access_rights, file_size):
        parameters = [file_no]

        assert com_set in FILE_COMMUNICATION
        parameters += [ com_set ]
        parameters += [ access_rights & 0xff, access_rights >> 8 ]
        parameters += Util.bytes3_to_byte_array(file_size)

        apdu_command = self.wrap_command(CREATE_BACKUPDATAFILE, parameters)
        self.communicate(apdu_command, "Creating backup data file {:02X}".format(file_no))

    def create_linear_record_file(self, file_no, com_set, access_rights, record_size, max_num_of_records):
        parameters = [file_no]

        assert com_set in FILE_COMMUNICATION
        parameters += [ com_set ]
        parameters += [ access_rights & 0xff, access_rights >> 8 ]
        parameters += Util.bytes3_to_byte_array(record_size)
        parameters += Util.bytes3_to_byte_array(max_num_of_records)

        apdu_command = self.wrap_command(CREATE_LINEAR_RECORD_FILE, parameters)
        self.communicate(apdu_command, "Creating linear record file {:02X}".format(file_no))

    def create_cyclic_record_file(self, file_no, com_set, access_rights, record_size, max_num_of_records):
        parameters = [file_no]

        assert com_set in FILE_COMMUNICATION
        parameters += [ com_set ]
        parameters += [ access_rights & 0xff, access_rights >> 8 ]
        parameters += Util.bytes3_to_byte_array(record_size)
        parameters += Util.bytes3_to_byte_array(max_num_of_records)

        apdu_command = self.wrap_command(CREATE_CYCLIC_RECORD_FILE, parameters)
        self.communicate(apdu_command, "Creating cyclic record file {:02X}".format(file_no))

    def get_file_settings(self, file_id):

        apdu_command = self.wrap_command(GET_FILE_SETTINGS, [file_id])
        resp = self.communicate(apdu_command, "Reading file settings {:02X}".format(file_id))

        file_type = resp[0]

        file_settings = {
            "type": file_type,
            "type_str": FILE_TYPES[file_type],
            "com_set": FILE_COMMUNICATION[resp[1]],
            "access_rights": resp[2:4],
        }

        if (file_type == 0x00) or (file_type == 0x01):
            # Data file
            file_settings.update({
                "file_size": Util.byte_array3_to_dword(resp[4:7]),
            })
        elif (file_type == 0x02):
            # Value file
            file_settings.update({
                "lower_limit": Util.byte_array4_to_dword(resp[4:8]),
                "upper_limit": Util.byte_array4_to_dword(resp[8:12]),
                "value": Util.byte_array4_to_dword(resp[12:16]),
                "limited_credit_enabled": True if (resp[16] != 0) else False
            })
        elif (file_type == 0x03) or (file_type == 0x04):
            # Linear record file
            file_settings.update({
                # Length of ONE records
                "record_size": Util.byte_array3_to_dword(resp[4:7]),
                "max_num_of_records": Util.byte_array3_to_dword(resp[7:10]),
                "current_num_of_records": Util.byte_array3_to_dword(resp[10:13]),
            })
        else:
            pass

        return file_settings

    def change_key(self, cur_key_id, key_id, key, new_key):
        if len(key) != 16:
            raise Exception('Invalid key length.')
        if len(new_key) != 16:
            raise Exception('Invalid key length.')

        data = []
        if self.key_id != key_id:
            xored_key = []
            for i in range(len(new_key)):
                xored_key.append(key[i] ^ new_key[i])
            crc1 = Util.calculate_crc(xored_key, len(xored_key), 0x6363)
            crc2 = Util.calculate_crc(new_key, len(new_key), 0x6363)
            data = xored_key + [(crc1 & 0xFF), (crc1 >> 8) & 0xFF] + [(crc2 & 0xFF), (crc2 >> 8) & 0xFF] + [0x00, 0x00, 0x00, 0x00]
        else:
            crc = Util.calculate_crc(new_key, len(new_key), 0x6363)
            data = new_key + [((crc >> 8) & 0xFF), (crc & 0xFF)] + [0x00] * 6
        decrypted_data = self.session_cipher.decrypt(bytes(data))
        decrypted_data = [ord(b) for b in decrypted_data]

        apdu_command = self.wrap_command(CHANGE_KEY, [key_id] + decrypted_data)
        self.communicate(apdu_command, "Change key")

    def get_key_settings(self):
        apdu_command = self.wrap_command(GET_KEY_SETTINGS)
        resp = self.communicate(apdu_command, "Get key settings")
        return resp

    def clear_record_file(self, file_id):
        apdu_command = self.wrap_command(CLEAR_RECORD_FILE, [file_id])
        self.communicate(apdu_command, "Clear record file")
    
    def commit_transaction(self):
        self.commit()

    def abort_transaction(self):
        apdu_command = self.wrap_command(ABORT_TRANSACTION)
        self.communicate(apdu_command, "Abort file changes")
