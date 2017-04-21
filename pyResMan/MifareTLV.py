'''
Created on 2017/3/15

@author: javacardos@gmail.com
@organization: https://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

_TAG_BLOCK_NUMBER = '\x01'
_TAG_BLOCK_DATA = '\x02'
_TAG_INCDEC_OPERAND = '\x03'
_TAG_KEY_TYPE = '\x04'
_TAG_KEY_VALUE = '\x05'
_TAG_UID = '\x06'
_TAG_RW_LEN = '\x07'

_TAG_DESFIRE_DATA = '\x08'

COMMAND_TAG_AUTHENTICATION = '\x01'
COMMAND_TAG_READ_BLOCK = '\x02'
COMMAND_TAG_WRITE_BLOCK = '\x03'
COMMAND_TAG_INCREMENT = '\x04'
COMMAND_TAG_DECREMENT = '\x05'
COMMAND_TAG_RESTORE = '\x06'
COMMAND_TAG_TRANSFER = '\x07'
COMMAND_TAG_SETUP = '\x10'

COMMAND_TAG_DESFIRE_COMMAND = '\x20'

_TAG_ERROR = '\x80'

class MifareCommandTLV(object):
    '''
    @brief Class to build mifare command tlv data;
    '''
    def __init__(self, command_tag):
        self.__data = ''
        self.command_tag = command_tag
    
    def set_block_number(self, n):
        self.__data += (_TAG_BLOCK_NUMBER + '\x01' + chr(n))
    
    def set_block_data(self, d):
        self.__data += (_TAG_BLOCK_DATA + chr(len(d)) + d)
    
    def set_incdec_operand(self, v):
        self.__data += (_TAG_INCDEC_OPERAND + chr(len(v)) + v)
    
    def set_key_type(self, t):
        self.__data += (_TAG_KEY_TYPE + '\x01' + chr(t))
    
    def set_key_value(self, k):
        self.__data += (_TAG_KEY_VALUE + chr(len(k)) + k)
    
    def set_uid(self, uid):
        self.__data += (_TAG_UID + chr(len(uid)) + uid)
    
    def set_rw_len(self, rw_len):
        self.__data += (_TAG_RW_LEN + '\x01' + chr(rw_len))
    
    def set_command(self, cmd):
        self.__data += (_TAG_DESFIRE_DATA + chr(len(cmd)) + cmd)
    
    def serialize(self):
        return '\xFF' + self.command_tag + chr(len(self.__data)) + self.__data


class MifareResponseTLV(object):
    '''
    Class to parse mifare response tlv data;
    '''
    def __init__(self, data):
        self.__data = data
        self.__error = 0
        self.__block_data = ''
        self.__desfire_data = ''
        self.parse()

    def parse(self):
        if ord(self.__data[0]) != 0x7F:
            raise Exception('Invalid response tag.')
        
        tlv_data_len = ord(self.__data[2])
        offset = 3
        while True:
            tag = ord(self.__data[offset])
            value_len = ord(self.__data[offset + 1])
            if tag == ord(_TAG_ERROR):
                if value_len != 0x01:
                    raise Exception('Invalid error length.')
                self.__error = self.__data[offset + 2]
                offset += 3
            elif tag == ord(_TAG_BLOCK_DATA):
                offset += 1
                value_len = ord(self.__data[offset])
                offset += 1
                self.__block_data = self.__data[offset : offset + value_len]
                offset += value_len
            elif tag == ord(_TAG_DESFIRE_DATA):
                offset += 1
                value_len = ord(self.__data[offset])
                offset += 1
                self.__desfire_data = self.__data[offset : offset + value_len]
                offset += value_len
            else:
                raise Exception('Invalid tag value.')
            
            if offset >= tlv_data_len:
                break;
    
    def get_error(self):
        return ord(self.__error)
    
    def get_block_data(self):
        return self.__block_data
    
    def get_desfire_data(self):
        return self.__desfire_data
    