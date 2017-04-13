'''
Created on 2017/4/12

@author: zhenkui
'''

from desfire.protocol import DESFire

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


class DESFireEx(DESFire):
    '''
    Extended DESFire class.
    '''

#     def __init__(self, device):
#         '''
#         Constructor
#         '''
#         super(self, device)
    
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
