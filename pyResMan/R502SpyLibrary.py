'''
Created on 2016-05-07

@author: javacardos@gmail.com
@organization: https://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

class ISO7816(object):
    OFFSET_CLA = 0
    OFFSET_INS = 0
    OFFSET_P1 = 0
    OFFSET_P2 = 0
    OFFSET_LC = 0
    OFFSET_CDATA = 0


class R502SpyLibrary(object):
    '''
    classdocs
    '''
    
    CLA_RF          = 0x81
    CLA_CB          = 0x82
    CLA_MIFARE      = 0x83
    
    INS_RF_ON       = 0x00
    INS_RF_OFF      = 0x01
    INS_RF_AUTO     = 0x02
    
    INS_RF_REQA     = 0x03
    INS_RF_WUPA     = 0x03
    INS_RF_ANTI     = 0x04
    INS_RF_SEL      = 0x05
    INS_RF_RATS     = 0x06
    INS_RF_HLTA     = 0x07
    INS_RF_PPS      = 0x08
    INS_RF_APDU     = 0x09
    
    INS_MIFARE_AUTHENTICATIONA      = 0x60
    INS_MIFARE_AUTHENTICATIONB      = 0x61
    INS_MIFARE_BLOCK_READ           = 0x30
    INS_MIFARE_BLOCK_WRITE          = 0xA0
    INS_MIFARE_INCREMENT            = 0xC1
    INS_MIFARE_DECREMENT            = 0xC0
    INS_MIFARE_TRANSFER             = 0xB0
    INS_MIFARE_RESTORE              = 0xC2
    
    INS_MIFARE_DUMP                 = 0xA5
    INS_MIFARE_CLONE                = 0x5A
    INS_MIFARE_READ_CARD_DATA       = 0xAA

    RF_AUTO_MODE_MANUAL  = 0x00
    RF_AUTO_MODE_AUTO    = 0x01

    def __init__(self, scinterface):
        '''
        Constructor
        '''
        self.__scInterface = scinterface
    
    def __checkSCInterface(self):
        if self.__scInterface == None:
            raise Exception('Smartcard interface is not assigned.')
    
    def init(self):
        self.rfOn()
        self.rfManaul()
    
    def rfOn(self):
        cmd = '%s%s\x00\x00\x00' %(chr(self.CLA_RF), chr(self.INS_RF_ON))
        rsp = self.__scInterface.transmit(cmd)
        if rsp != '\x90\x00':
            return False, ''
        return True, ''
    
    def rfOff(self):
        cmd = '%s%s\x00\x00\x00' %(chr(self.CLA_RF), chr(self.INS_RF_OFF))
        rsp = self.__scInterface.transmit(cmd)
        if rsp != '\x90\x00':
            return False, ''
        return True, ''
    
    def rfAuto(self):
        cmd = '%s%s%s\x00\x00' %(chr(self.CLA_RF), chr(self.INS_RF_AUTO), chr(self.RF_AUTO_MODE_AUTO))
        rsp = self.__scInterface.transmit(cmd)
        if rsp != chr(self.RF_AUTO_MODE_AUTO) + '\x90\x00':
            return False, ''
        return True, ''
    
    def rfManaul(self):
        cmd = '%s%s%s\x00\x00' %(chr(self.CLA_RF), chr(self.INS_RF_AUTO), chr(self.RF_AUTO_MODE_MANUAL))
        rsp = self.__scInterface.transmit(cmd)
        if rsp != chr(self.RF_AUTO_MODE_MANUAL) + '\x90\x00':
            return False, ''
        return True, ''
    
    def claREQA(self, commandValue):
        if len(commandValue) != 1:
            raise Exception('Invalid command value.')
        cmd = '%s%s%s\x00\x00' %(chr(self.CLA_RF), chr(self.INS_RF_REQA), commandValue[0])
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def claWUPA(self, commandValue):
        if len(commandValue) != 1:
            raise Exception('Invalid command value.')
        cmd = '%s%s%s\x00\x00' %(chr(self.CLA_RF), chr(self.INS_RF_WUPA), commandValue[0])
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def claAnticollision(self, commandValue):
        if len(commandValue) != 2:
            raise Exception('Invalid command value.')
        cmd = '%s%s%s%s\x00' %(chr(self.CLA_RF), chr(self.INS_RF_ANTI), commandValue[0], commandValue[1])
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
        
    def claSelect(self, commandValue):
        if len(commandValue) != 6:
            raise Exception('Invalid command value.')
        cmd = '%s%s%s%s\x05%s' %(chr(self.CLA_RF), chr(self.INS_RF_SEL), commandValue[0], commandValue[1], commandValue[2 : ])
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def claRATS(self, commandValue):
        if (len(commandValue) != 2) or (commandValue[0] != '\xE0'):
            raise Exception('Invalid command value.')
        cmd = '%s%s%s\x00\x00' %(chr(self.CLA_RF), chr(self.INS_RF_RATS), commandValue[1])
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def claHLTA(self, commandValue):
        if (len(commandValue) != 2) or (commandValue != '\x50\x00'):
            raise Exception('Invalid command value.')
        cmd = '%s%s\x00\x00\x00' %(chr(self.CLA_RF), chr(self.INS_RF_HLTA))
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def claPPS(self, commandValue):
        commandLength = len(commandValue)
        if (commandLength != 2) and (commandLength != 3):
            raise Exception('Invalid command value.')
        cmd = '%s%s\x00\x00%s%s' %(chr(self.CLA_RF), chr(self.INS_RF_PPS), chr(commandLength), commandValue)
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def clbREQB(self):
        raise NotImplementedError()
    
    def clbWUPB(self):
        raise NotImplementedError()
    
    def clbSlotMarker(self):
        raise NotImplementedError()
    
    def clbATQB(self):
        raise NotImplementedError()
    
    def clbATTRIB(self):
        raise NotImplementedError()
    
    def clbHLTB(self):
        raise NotImplementedError()
    
    def clTransmit(self, commandValue):
        commandLength = len(commandValue)
        cmd = '%s%s\x00\x00%s%s' %(chr(self.CLA_RF), chr(self.INS_RF_APDU), chr(commandLength), commandValue)
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]

    def mifareAuthentication(self, commandValue):
        cmd = '%s%s%s\x00%s%s' %(chr(self.CLA_MIFARE), commandValue[0], commandValue[1], chr(len(commandValue) - 2), commandValue[2 :])
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def mifareBlockRead(self, commandValue):
        cmd = '%s%s%s\x00\x10' %(chr(self.CLA_MIFARE), chr(R502SpyLibrary.INS_MIFARE_BLOCK_READ), commandValue[1])
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def mifareBlockWrite(self, commandValue):
        cmd = '%s%s%s\x00%s%s' %(chr(self.CLA_MIFARE), chr(R502SpyLibrary.INS_MIFARE_BLOCK_WRITE), commandValue[1], chr(len(commandValue) - 2), commandValue[2 :])
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def mifareIncrement(self, commandValue):
        cmd = '%s%s%s\x00\x04%s' %(chr(self.CLA_MIFARE), chr(R502SpyLibrary.INS_MIFARE_INCREMENT), commandValue[1], commandValue[2 : ])
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def mifareDecrement(self, commandValue):
        cmd = '%s%s%s\x00\x04%s' %(chr(self.CLA_MIFARE), chr(R502SpyLibrary.INS_MIFARE_DECREMENT), commandValue[1], commandValue[2 : ])
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def mifareRestore(self, commandValue):
        cmd = '%s%s%s\x00\x00' %(chr(self.CLA_MIFARE), chr(R502SpyLibrary.INS_MIFARE_RESTORE), commandValue[1])
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def mifareTransfer(self, commandValue):
        cmd = '%s%s%s\x00\x00' %(chr(self.CLA_MIFARE), chr(R502SpyLibrary.INS_MIFARE_TRANSFER), commandValue[1])
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]

    '''
        ISO14443-3 command;
    '''
    def claREQA2(self, req_value):
        '''
        @brief: 
        @return: True and response data / False and the error code.
        '''
        cmd = '%s%s%s\x00\x00' %(chr(self.CLA_RF), chr(self.INS_RF_REQA), req_value)
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def claWUPA2(self, req_value):
        '''
        @brief: 
        @return: True and response data / False and the error code.
        '''
        cmd = '%s%s%s\x00\x00' %(chr(self.CLA_RF), chr(self.INS_RF_WUPA), req_value)
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def claAnticollision2(self, sel, nvb):
        '''
        @brief: 
        @return: True and response data / False and the error code.
        '''
        cmd = '%s%s%s%s\x00' %(chr(self.CLA_RF), chr(self.INS_RF_ANTI), sel, nvb)
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
        
    def claSelect2(self, sel, nvb, uid):
        '''
        @brief: 
        @return: True and response data / False and the error code.
        '''
        cmd = '%s%s%s%s\x04%s' %(chr(self.CLA_RF), chr(self.INS_RF_SEL), sel, nvb, uid)
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]

    def claHLTA2(self):
        '''
        @brief: 
        @return: True and response data / False and the error code.
        '''
        cmd = '%s%s\x00\x00\x00' %(chr(self.CLA_RF), chr(self.INS_RF_HLTA))
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]

    '''
        ### Methods version 2; ###
    '''
    def mifareAuthentication2(self, keyType, blockNumber, key, uid):
        '''
        @brief: 
        @return: True and response data / False and the error code.
        '''
        if keyType not in [0, 1]:
            raise Exception('Invalid key type.')
        if len(key) != 6:
            raise Exception('Wrong key length.')
        if len(uid) != 4:
            raise Exception('Wrong uid length.')
        
        cmd = '%s%s%s\x00%s%s' %(chr(self.CLA_MIFARE), chr(0x60 + keyType), chr(blockNumber), chr(len(key) + len(uid)), key + uid)
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]

    def mifareBlockRead2(self, blockNumber):
        '''
        @brief: 
        @return: True and response data / False and the error code.
        '''
        cmd = '%s%s%s\x00\x10' %(chr(self.CLA_MIFARE), chr(R502SpyLibrary.INS_MIFARE_BLOCK_READ), chr(blockNumber))
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]

    def mifareBlockWrite2(self, blockNumber, value):
        '''
        @brief: 
        @return: True and response data / False and the error code.
        '''
        if len(value) != 0x10:
            raise Exception('Wrong value length.')
        
        cmd = '%s%s%s\x00%s%s' %(chr(self.CLA_MIFARE), chr(R502SpyLibrary.INS_MIFARE_BLOCK_WRITE), chr(blockNumber), chr(len(value)), value)
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]

    def mifareIncrement2(self, blockNumber, incValue):
        '''
        @brief: 
        @return: True and response data / False and the error code.
        '''
        cmd = '%s%s%s\x00\x04%s' %(chr(self.CLA_MIFARE), chr(R502SpyLibrary.INS_MIFARE_INCREMENT), chr(blockNumber), incValue)
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]

    def mifareDecrement2(self, blockNumber, decValue):
        '''
        @brief: 
        @return: True and response data / False and the error code.
        '''
        cmd = '%s%s%s\x00\x04%s' %(chr(self.CLA_MIFARE), chr(R502SpyLibrary.INS_MIFARE_DECREMENT), chr(blockNumber), decValue)
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def mifareRestore2(self, blockNumber):
        '''
        @brief: 
        @return: True and response data / False and the error code.
        '''
        cmd = '%s%s%s\x00\x00' %(chr(self.CLA_MIFARE), chr(R502SpyLibrary.INS_MIFARE_RESTORE), chr(blockNumber))
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def mifareTransfer2(self, blockNumber):
        '''
        @brief: 
        @return: True and response data / False and the error code.
        '''
        cmd = '%s%s%s\x00\x00' %(chr(self.CLA_MIFARE), chr(R502SpyLibrary.INS_MIFARE_TRANSFER), chr(blockNumber))
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
    
    def mifareDumpCard(self):
        '''
        @brief: 
        @return: True and response data / False and the error code.
        '''
        cmd = '%s%s\x00\x00\x00' %(chr(self.CLA_MIFARE), chr(R502SpyLibrary.INS_MIFARE_DUMP))
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]

    def mifareCloneCard(self):
        '''
        @brief: 
        @return: True and response data / False and the error code.
        '''
        cmd = '%s%s\x00\x00\x00' %(chr(self.CLA_MIFARE), chr(R502SpyLibrary.INS_MIFARE_CLONE))
        rsp = self.__scInterface.transmit(cmd)
        if rsp[-2 : ] == '\x90\x00':
            return True, rsp[ : -2]
        return False, rsp[0]
