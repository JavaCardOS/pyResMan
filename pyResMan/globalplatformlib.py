# -*- coding:utf-8 -*-

'''
Created on 2015-11-20

@author: javacardos@gmail.com
@organization: http://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

import pyglobalplatform as gp


def establishContext():
    '''
    This function establishes a context to connection layer. 
    @return: The context.
    @raise Exception: If establish failed.  
    '''
    return gp.establishContext()

def releaseContext(context):
    '''
    This function releases the context to the connection layer established by establish_context(). 
    '''
    return gp.releaseContext(context)
    
def listReaders(context):
    '''
    This function returns a list of currently available readers.
    '''
    return gp.listReaders(context)


'''
Issuer security domain AID;
'''
AID_ISD = '\xA0\x00\x00\x00\x03\x00\x00\x00'

'''
Protocol values;
'''
SCARD_PROTOCOL_UNDEFINED    = 0x00000000
SCARD_PROTOCOL_T0           = 0x00000001
SCARD_PROTOCOL_T1           = 0x00000002
SCARD_PROTOCOL_RAW          = 0x00010000
SCARD_PROTOCOL_Tx           = (SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1)

def connectCard(context, readerName, protocol):
    """
    This function connects to a reader. 
    """
    return gp.connectCard(context, readerName, protocol)

def disconnectCard(context, cardInfo):
    """
    This function disconnects a reader.
    """
    return gp.disconnectCard(context, cardInfo)

def selectApplication(context, cardInfo, aid):
    """
    Selects an application on a card by AID.
    """
    return gp.OPGP_select_application(context, cardInfo, aid)

'''
GET STATUS p1 values;
'''
GET_STATUS_P1_ISD = 0x80
GET_STATUS_P1_APP_SSD = 0x40
GET_STATUS_P1_EXECUTABLE_LOAD_FILES = 0x20
GET_STATUS_P1_EXECUTABLE_LOAD_FILES_MODULES = 0x10

def getStatus(context, cardInfo, securityInfo, cardElement):
    """
    Gets the life cycle status of Applications, the Issuer Security Domains, Security Domains and Executable Load Files and their privileges or information about Executable Modules of the Executable Load Files.
    """
    return gp.GP211_get_status(context, cardInfo, securityInfo, cardElement)

def setStatus(context, cardInfo, securityInfo, cardElement, aid, lifeCycleState):
    """
    Sets the life cycle status of Applications, Security Domains or the Card Manager. 
    """
    return gp.GP211_set_status(context, cardInfo, securityInfo, cardElement, aid, lifeCycleState)

'''
Default SCP key value;
'''
DEFAULT_KEY = '\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4A\x4B\x4C\x4D\x4E\x4F'

def mutualAuthentication(context, cardInfo, baseKey, sencKey, smacKey, dekKey, keySetVersion, keyIndex, scp, scpi, securityLevel, derivationMethod):
    """
    Mutual authentication.
    """
    return gp.GP211_mutual_authentication(context, cardInfo, baseKey, sencKey, smacKey, dekKey, keySetVersion, keyIndex, scp, scpi, securityLevel, derivationMethod)

def initImplicitSecureChannel(aid, baseKey, sencKey, smacKey, dekKey, scpi, sequenceCounter):
    """
    Inits a Secure Channel implicitly.
    """
    return gp.GP211_init_implicit_secure_channel(aid, baseKey, sencKey, smacKey, dekKey, scpi, sequenceCounter)

def closeImplicitSecureChannel(securityInfo):
    """
    Closes a Secure Channel implicitly.
    """
    return gp.GP211_close_implicit_secure_channel(securityInfo)

'''
GET DATA tag values;
'''
TAG_DATA_IIN = '\x42'
TAG_DATA_CIN = '\x45'
TAG_DATA_CARD_DATA = '\x66'
TAG_DATA_KEY_INFORMATION_TEMPLATE = '\xE0'
TAG_DATA_SECURITY_LEVEL = '\xD3'
TAG_DATA_APPLICATIONS = '\x2F00'
TAG_DATA_EXTENDED_CARD_RESOURCE_INFORMATION = '\xFF\x21'
TAG_CONFIRMATION_COUNTER = '\xC2'
TAG_SEQUENCE_COUNTER = '\xC1'

def getData(context, cardInfo, securityInfo, identifier):
    """
    Retrieve card data.
    """
    return gp.GP211_get_data(context, cardInfo, securityInfo, identifier)

def getData_ISO7816_4(context, cardInfo, identifier):
    """
    Retrieve card data according ISO/IEC 7816-4 command not within a secure channel. 
    """
    return gp.GP211_get_data_iso7816_4(context, cardInfo, identifier)

def getSCPDetails(context, cardInfo):
    """
    This returns the Secure Channel Protocol and the Secure Channel Protocol implementation.
    """
    return gp.GP211_get_secure_channel_protocol_details(context, cardInfo)

def getSequenceCounter(context, cardInfo):
    """
    This returns the current Sequence Counter.
    """
    return gp.GP211_get_sequence_counter(context, cardInfo)

def putData(context, cardInfo, securityInfo, identifier, data):
    """
    Put card data.
    """
    return gp.GP211_put_data(context, cardInfo, securityInfo, identifier, data)

def changePIN(context, cardInfo, securityInfo, tryLimit, newPIN):
    """
    Changes or unblocks the global PIN.
    """
    return gp.GP211_pin_change(context, cardInfo, securityInfo, tryLimit, newPIN)

def put3DESKey(context, cardInfo, securityInfo, keySetVersion, keyIndex, newKeySetVersion, keyData):
    """
    Replaces a single 3DES key in a key set or adds a new 3DES key.
    """
    return gp.GP211_put_3des_key(context, cardInfo, securityInfo, keySetVersion, keyIndex, newKeySetVersion, keyData)

def putRSAKey(context, cardInfo, securityInfo, keysetVersion, keyIndex, newKeySetVersion, pemKeyFileName, passPhrase):
    """
    Replaces a single public RSA key in a key set or adds a new public RSA key. 
    """
    return gp.GP211_put_rsa_key(context, cardInfo, securityInfo, keysetVersion, keyIndex, newKeySetVersion, pemKeyFileName, passPhrase)

def putSCKey(context, cardInfo, securityInfo, keysetVersion, newKeySetVersion, newBaseKey, newSEncKey, newSMacKey, newDEKKey):
    """
    Replaces or adds a secure channel key set consisting of S-ENC, S-MAC and DEK. 
    """
    return gp.GP211_put_secure_channel_keys(context, cardInfo, securityInfo, keysetVersion, newKeySetVersion, newBaseKey, newSEncKey, newSMacKey, newDEKKey)

def deleteKey(context, cardInfo, securityInfo, keysetVersion, keyIndex):
    """
    Deletes a key or multiple keys.
    """
    return gp.GP211_delete_key(context, cardInfo, securityInfo, keysetVersion, keyIndex)

def getKeyInformationTemplates(context, cardInfo, securityInfo, num):
    """
    Retrieves key information of keys on the card.
    """
    return gp.GP211_get_key_information_templates(context, cardInfo, securityInfo, num)

def deleteApplication(context, cardInfo, securityInfo, aids):
    """
    Deletes a Executable Load File or an application. 
    """
    return gp.GP211_delete_application(context, cardInfo, securityInfo, aids)

def installForLoad(context, cardInfo, securityInfo, packageAID, sdAID, dataBlockHash, loadToken, nonVolatileCodeSpaceLimit, volatileDataSpaceLimit, nonVolatileDataSpaceLimit):
    """
    Prepares the card for loading an application. 
    """
    return gp.GP211_install_for_load(context, cardInfo, securityInfo, packageAID, sdAID, dataBlockHash, loadToken, nonVolatileCodeSpaceLimit, volatileDataSpaceLimit, nonVolatileDataSpaceLimit)

def getExtraditionTokenSignatureData(sdAID, aid, tokenSignData):
    """
    Function to retrieve the data to sign by the Card Issuer in an Extradition Token.
    """
    return gp.GP211_get_extradition_token_signature_data(sdAID, aid, tokenSignData)

def getLoadTokenSignatureData(aid, sdAID, loadFileDataBlockHash, nonVolatileCodeSpaceLimit, volatileDataSpaceLimit, noVolatileDataSpaceLimit):
    """
    Function to retrieve the data to sign by the Card Issuer in a Load Token.
    """
    return gp.GP211_get_load_token_signature_data(aid, sdAID, loadFileDataBlockHash, nonVolatileCodeSpaceLimit, volatileDataSpaceLimit, noVolatileDataSpaceLimit)

def getInstallTokenSignatureData(p1, packageAID, moduleAID, appletAID, privileges, volatileDataSpaceLimit, nonVolatileDataSpaceLimit, installParameters):
    """
    Function to retrieve the data to sign by the Card Issuer in an Install Token.
    """
    return gp.GP211_get_install_token_signature_data(p1, packageAID, moduleAID, appletAID, privileges, volatileDataSpaceLimit, nonVolatileDataSpaceLimit, installParameters)

def calculateLoadToken(packageAID, sdAID, loadFileDataBlockHash, nonVolatileCodeSpaceLimit, volatileDataSpaceLimit, nonVolatileDataSpaceLimit, pemKeyFileName, passPhrase):
    """
    Calculates a Load Token using PKCS#1.
    """
    return gp.GP211_calculate_load_token(packageAID, sdAID, loadFileDataBlockHash, nonVolatileCodeSpaceLimit, volatileDataSpaceLimit, nonVolatileDataSpaceLimit, pemKeyFileName, passPhrase)

def calculateInstallToken(packageAID, moduleAID, appletAID, privileges, volatileDataSpaceLimit, nonVolatileDataSpaceLimit, installParameters, pemKeyFileName, passPhrase):
    """
    Calculates an Install Token using PKCS#1.
    """
    return gp.GP211_calculate_install_token(packageAID, moduleAID, appletAID, privileges, volatileDataSpaceLimit, nonVolatileDataSpaceLimit, installParameters, pemKeyFileName, passPhrase)

def calculateLoadFileDataBlockHash(pemKeyFileName):
    """
    Calculates a Load File Data Block Hash.
    """
    return gp.GP211_calculate_load_file_data_block_hash(pemKeyFileName)

def load(context, cardInfo, securityInfo, dapBlock, packageFileName):
    """
    Loads a Executable Load File (containing an application) to the card.
    """
    return gp.GP211_load(context, cardInfo, securityInfo, dapBlock, packageFileName)

def loadFromBuffer(context, cardInfo, securityInfo, dapBlock, packageBuf):
    """
    Loads a Executable Load File (containing an application) from a buffer to the card.
    """
    return gp.GP211_load_from_buffer(context, cardInfo, securityInfo, dapBlock, packageBuf)

def installForInstall(context, cardInfo, securityInfo, packageAID, moduleAID, appletAID, privileges, volatileDataSpaceLimit, nonVolatileDataSpaceLimit, installParameters, installToken):
    """
    Installs an application on the card.
    """
    return gp.GP211_install_for_install(context, cardInfo, securityInfo, packageAID, moduleAID, appletAID, privileges, volatileDataSpaceLimit, nonVolatileDataSpaceLimit, installParameters, installToken)

def installForMakeSelectable(context, cardInfo, securityInfo, appletAID, privileges, installToken):
    """
    Makes an installed application selectable.
    """
    return gp.GP211_install_for_make_selectable(context, cardInfo, securityInfo, appletAID, privileges, installToken)

def installForInstallAndMakeSelectable(context, cardInfo, securityInfo, packageAID, moduleAID, appletAID, privileges, volatileDataSpaceLimit, nonVolatileDataSpaceLimit, installParameters, installToken):
    """
    Installs and makes an installed application selectable.
    """
    return gp.GP211_install_for_install_and_make_selectable(context, cardInfo, securityInfo, packageAID, moduleAID, appletAID, privileges, volatileDataSpaceLimit, nonVolatileDataSpaceLimit, installParameters, installToken)

def installForPersonalization(context, cardInfo, securityInfo, appAID):
    """
    Informs a Security Domain that a associated application will retrieve personalization data.
    """
    return gp.GP211_install_for_personalization(context, cardInfo, securityInfo, appAID)

def insatllForExtradition(context, cardInfo, securityInfo, sdAID, appletAID, extrationToken):
    """
    Associates an application with another Security Domain.
    """
    return gp.GP211_install_for_extradition(context, cardInfo, securityInfo, sdAID, appletAID, extrationToken)

def putDelegatedManagementKeys(context, cardInfo, securityInfo, keysetVersion, newKeySetVersion, pemKeyFileName, passPhrase, receiptKey):
    """
    Adds a key set for Delegated Management.
    """
    return gp.GP211_put_delegated_management_keys(context, cardInfo, securityInfo, keysetVersion, newKeySetVersion, pemKeyFileName, passPhrase, receiptKey)

def sendApdu(context, cardInfo, securityInfo, capdu):
    """
    Sends an application protocol data unit.
    """
    return gp.GP211_send_APDU(context, cardInfo, securityInfo, capdu)

def calculate3DESDap(loadFileDataBlockHash, sdAID, dapCalculationKey):
    """
    Calculates a Load File Data Block Signature using 3DES.
    """
    return gp.GP211_calculate_3des_DAP(loadFileDataBlockHash, sdAID, dapCalculationKey)

def calculateRSADap(loadFileDataBlockHash, sdAID, pemKeyFileName, passPhrase):
    """
    Calculates a Load File Data Block Signature using SHA-1 and PKCS#1 (RSA).
    """
    return gp.GP211_calculate_rsa_DAP(loadFileDataBlockHash, sdAID, pemKeyFileName, passPhrase)

def validateDeleteReceipt(confirmationCounter, cardUniqueData, receiptKey, receiptData, aid):
    """
    Validates a Load Receipt.
    """
    return gp.GP211_validate_delete_receipt(confirmationCounter, cardUniqueData, receiptKey, receiptData, aid)

def validateInstallReceipt(confirmationCounter, cardUniqueData, receiptKey, receiptData, packageAID, appletAID):
    """
    Validates an Install Receipt.
    """
    return gp.GP211_validate_install_receipt(confirmationCounter, cardUniqueData, receiptKey, receiptData, packageAID, appletAID)

def validateLoadReceipt(confirmationCounter, cardUniqueData, receiptKey, receiptData, packageAID, sdAID):
    """
    Validates a Load Receipt.
    """
    return gp.GP211_validate_load_receipt(confirmationCounter, cardUniqueData, receiptKey, receiptData, packageAID, sdAID)

def validateExtraditionReceipt(confirmationCounter, cardUniqueData, receiptKey, receiptData, oldSdAid, newSdAid, aid):
    """
    Validates an Extradition Receipt.
    """
    return gp.GP211_validate_extradition_receipt(confirmationCounter, cardUniqueData, receiptKey, receiptData, oldSdAid, newSdAid, aid)

def manageChannel(context, cardInfo, securityInfo, openClose, channelToClose):
    """
    Opens or closes a Logical Channel.
    """
    return gp.OPGP_manage_channel(context, cardInfo, securityInfo, openClose, channelToClose)

def selectChannel(cardInfo, channelNUmber):
    """
    If multiple Logical Channels are open or a new Logical Channel is opened with select_application(), selects the Logical Channel.
    """
    return gp.OPGP_select_channel(channelNUmber)

def storeData(context, cardInfo, securityInfo, data):
    """
    The STORE DATA command is used to transfer data to an Application or the Security Domain processing the command.
    """
    return gp.GP211_store_data(context, cardInfo, securityInfo, data)

def readExecutableLoadFileParameters(fileName):
    """
    Gets the life cycle status of Applications, the Card Manager and Executable Load Files and their privileges.
    """
    return gp.OPGP_read_executable_load_file_parameters(fileName)

def enableTraceMode(v):
    """
    Enables the trace mode.
    """
    return gp.OPGP_enable_trace_mode(v)
