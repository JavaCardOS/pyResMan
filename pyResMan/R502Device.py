'''
Created on 2017/3/19

@author: javacardos@gmail.com
@organization: https://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''
from desfire.device import Device

class R502Device(Device):
    '''
    Interface for device R502 to send TLV comamnd and recv TLV response.
    '''

    def __init__(self, low_level_interface):
        '''
        '''
        self._low_interface = low_level_interface
    
    def transmit_sc_command(self, sc_command):
        cla = 0x8E
        lc = len(sc_command)
        # Create APDU command;
        low_command = '%s\x00\x00\x00%s' %(chr(cla), chr(lc)) + sc_command
        low_response = self._low_interface.transmit(low_command)
        # Get APDU response;
        return low_response[0 : -2]

    def transceive(self, cmd_bytes):
        resp = self._low_interface.transmit(''.join('%s' %(chr(b)) for b in cmd_bytes))
        return [ord(c) for c in resp]
