'''
Created on 2016-5-7

@author: zhenkui
'''

import globalplatformlib as gp
from SCInterface import SCInterface

from globalplatformlib import AID_ISD
from globalplatformlib import SCARD_PROTOCOL_T0
from globalplatformlib import SCARD_PROTOCOL_T1
from globalplatformlib import SCARD_PROTOCOL_Tx


class GPInterface(SCInterface):
    '''
    classdocs
    '''
    
    

    def __init__(self):
        '''
        Constructor
        '''
        self.__context = gp.establishContext()
        self.__cardInfo = None
        self.__securityInfo = None
        self.__readername = None
        
    def connect(self, readername, protocol):
        self.__checkContext()
        self.__readername = readername
        self.__cardInfo = gp.connectCard(self.__context, str(readername), protocol)
    
    def listreaders(self):
        return gp.listReaders(self.__context)
    
    def disconnect(self):
        self.__checkContext()
        if self.__cardInfo != None:
            gp.disconnectCard(self.__context, self.__cardInfo)

    def transmit(self, cmd):
        self.__checkContext()
        self.__checkCardInfo()
        return gp.sendApdu(self.__context, self.__cardInfo, None, cmd)

    def selectApplication(self, aid):
        self.__checkContext()
        return gp.selectApplication(self.__context, self.__cardInfo, aid)
    
    def establishSecurityChannel(self, sencKey, smacKey, dekKey, kvn, scp, scpi):
        self.__checkContext()
        self.__checkCardInfo()
        self.__securityInfo = gp.mutualAuthentication(self.__context, self.__cardInfo, None, sencKey, smacKey, dekKey, kvn, 0, scp, scpi, 0, 0)
    
    def installForLoad(self, capFilePath):
        self.__checkContext()
        self.__checkCardInfo()
        self.__checkSecurityInfo()
        capFileInfo = gp.readExecutableLoadFileParameters(capFilePath)
        gp.installForLoad(self.__context, self.__cardInfo, self.__securityInfo, capFileInfo['loadFileAID'], gp.AID_ISD, '', '', 0, 0, 0)
    
    def load(self, capFilePath):
        self.__checkContext()
        self.__checkCardInfo()
        self.__checkSecurityInfo()
        gp.load(self.__context, self.__cardInfo, self.__securityInfo, '', capFilePath)

    def installForInstallAndMakeSelectable(self, packageAID, moduleAID, appletAID, privileges, installParameters):
        self.__checkContext()
        self.__checkCardInfo()
        self.__checkSecurityInfo()
        gp.installForInstallAndMakeSelectable(self.__context, self.__cardInfo, self.__securityInfo, packageAID, moduleAID, appletAID, privileges, 0, 0, installParameters, '')

    def getStatus(self, cardElement):
        self.__checkContext()
        self.__checkCardInfo()
        self.__checkSecurityInfo()
        return gp.getStatus(self.__context, self.__cardInfo, self.__securityInfo, cardElement)
    
    def deleteApplication(self, appAIDs):
        self.__checkContext()
        self.__checkCardInfo()
        self.__checkSecurityInfo()
        gp.deleteApplication(self.__context, self.__cardInfo, self.__securityInfo, appAIDs)
    
    def getKeyInformationTemplates(self):
        self.__checkContext()
        self.__checkCardInfo()
        self.__checkSecurityInfo()
        return gp.getKeyInformationTemplates(self.__context, self.__cardInfo, self.__securityInfo, 0)
    
    def putSCKey(self, oldKVN, newKVN, key1, key2, key3):
        self.__checkContext()
        self.__checkCardInfo()
        self.__checkSecurityInfo()
        gp.putSCKey(self.__context, self.__cardInfo, self.__securityInfo, oldKVN, newKVN, None, key1, key2, key3)
        
    def deleteKey(self, kvn, keyIndex):
        self.__checkContext()
        self.__checkCardInfo()
        self.__checkSecurityInfo()
        gp.deleteKey(self.__context, self.__cardInfo, self.__securityInfo, kvn, keyIndex)
        
    def getSCPDetails(self):
        self.__checkContext()
        self.__checkCardInfo()
        return gp.getSCPDetails(self.__context, self.__cardInfo)
        
    def __checkContext(self):
        if self.__context == None:
            raise Exception('Context not established.')

    def __checkCardInfo(self):
        if self.__cardInfo == None:
            raise Exception('Smart card not connected.')

    def __checkSecurityInfo(self):
        if self.__securityInfo== None:
            raise Exception('Security channel not established.')
        