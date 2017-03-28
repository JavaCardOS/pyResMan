# -*- coding:utf8 -*-

'''
Created on 2016-7-20

@author: javacardos@gmail.com
@organization: https://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

__DEBUGGER_ERRORS = {
      0x02: 'Invalid frame format.'
    , 0x03: 'Invalid frame parameter(s).'
    , 0x04: 'RF module reset.'
    , 0x05: 'RF interface error.'
    , 0x06: 'Command is unknown.'
    , 0x0F: 'Force exit.'
    , 0x1B: 'Card not present.'
    , 0x40: 'Invalid M1 key.'
    , 0x41: 'M1 authentication failed.'
    , 0x42: 'M1 card not authenticated.'
    , 0x43: 'Write M1 block failed.'
    , 0x44: 'Value error.'
    , 0x45: 'Card parity error.'
    , 0x46: 'Invalid code.'
    , 0x47: 'Card SN error.'
    , 0x48: 'Cards are in collision.'
    , 0x49: 'Bit error.'
    , 0x4A: 'Byte error.'
    , 0x4B: 'Invalid command parameter(s).'
    , 0x4C: 'FIFO overflow.'
    , 0x4D: 'Unknown command.'
    , 0x4E: 'Command not implemented.'
    , 0x60: 'RF timeout.'
    , 0x61: 'Timeout.'
    , 0x62: 'Invalid response frame format.'
    , 0x63: 'Response parity error.'
    , 0x64: 'Tag not present.'
    , 0x80: 'Invalid command format.'
    , 0x81: 'The variable UID is not set!'
}

def getErrorString(errorcode):
    errorString = 'Unknown error.'
    if __DEBUGGER_ERRORS.has_key(errorcode):
        errorString = __DEBUGGER_ERRORS[errorcode]
    return errorString
