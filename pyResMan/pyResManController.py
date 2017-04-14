# -*- coding:utf8 -*-

'''
Created on 2015-10-30

@author: javacardos@gmail.com
@organization: https://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from pyResManReader import pyResManReader, ICardMonitorEventHandler, IReaderMonitorEventHandler
from Util import Util
import threading
import timeit
from pyGlobalPlatform import globalplatformlib as gp
import wx
import os
from GPInterface import GPInterface
from R502SpyLibrary import R502SpyLibrary
from DebuggerScriptFile import DebuggerScriptFile
from pyResMan.R502Device import R502Device
from pyResMan.pyLibSC import LibSC
from pyResMan import DebuggerUtils
from pyResMan import DESFireEx

class APDUItem(object):
    """Class for APDU item data;"""
        
    def __init__(self, command, transArgs):
        self._command = command
        self._transArgs = transArgs
    
    def getCommand(self):
        return self._command
    
    def getTransArgs(self):
        return self._transArgs


class pyResManController(object):
    """The controller of reResManDialog;"""

    def __init__(self, handler):
        """""Constructor"""
        self.__readername = None
        self.__reader = pyResManReader()
        self.__handler = handler
        self.__reader.addReaderMonitorHandler(self)
        self.__reader.monitorReaders()
        self.__runScriptThread = None
        self.__gpInterface = GPInterface()
        self.__scDebugger = R502SpyLibrary(self.__gpInterface)
        self.__r502_device = R502Device(self.__gpInterface)
        self.__libsc = LibSC(self.__r502_device)
        self.__desfire = DESFireEx.DESFireEx(self.__r502_device)
        
        gp.enableTraceMode(1)
        
        self.__debuggerVariables = {}
    
    def getReaderList(self):
        return self.__reader.getReaderList()
    
    def getReaderName(self):
        return self.__readername
    
    def connect(self, readername, protocol, mode):
        """ Connect to the reader. """
        self.__readername = readername
        self.__handler.handleLog('Connect to %s.' %(readername))
        self.__gpInterface.connect(str(readername), protocol)
        if self.__readername.find('R502 SPY') != -1:
            self.__scDebugger.init()

    def handleCardEvent(self, eventType, args):
        readername = args[0]
        if eventType == ICardMonitorEventHandler.MONITOR_EVENT_INSERT:
            self.__handler.handleCardInserted(readername)
        elif eventType == ICardMonitorEventHandler.MONITOR_EVENT_REMOVE:
            self.__handler.handleCardRemoved(readername)
            self.__reader.removeCardMonitorHandler(self)
            self.__reader.stopCardMonitor()

    def handleReaderEvent(self, eventType, args):
        if eventType == IReaderMonitorEventHandler.MONITOR_EVENT_ADDED:
            for readername in args:
                self.__handler.handleReaderAdded(readername)
        elif eventType == IReaderMonitorEventHandler.MONITOR_EVENT_REMOVED:
            for readername in args:
                self.__handler.handleReaderRemoved(readername)

    def monitorCard(self):
        self.__reader.addCardMonitorHandler(self)
        self.__reader.monitorCard(self.__readername)

    def disconnect(self):
        if self.__readername.find('R502 SPY') != -1:
            self.__scDebugger.rfAuto()
            self.__scDebugger.rfOn()
        self.__gpInterface.disconnect()
        try:
            self.__reader.removeCardMonitorHandler(self)
            self.__reader.stopCardMonitor()
        except:
            pass
    
    def __transmit_impl(self, cmd, t0AutoGetResponse, handlerArgs):
        commandValue = Util.s2vs(cmd)
        
        self.__handler.handleAPDUCommand("".join("%02X " %(ord(vb)) for vb in commandValue), handlerArgs)
        timeStart = timeit.default_timer()
        rsp = self.__gpInterface.transmit(Util.s2vs(cmd))
        timeStop = timeit.default_timer()
        transtime = timeStop - timeStart
        self.__handler.handleAPDUResponse("".join("%02X " %(ord(vb)) for vb in rsp), transtime, handlerArgs)
        
        if t0AutoGetResponse and (rsp[0] == '\x61') and (len(handlerArgs) == 0):
            cmd = '\x00\xC0\x00\x00' + rsp[1]
            self.__handler.handleAPDUCommand("".join("%02X " %(ord(vb)) for vb in cmd))
            timeStart = timeit.default_timer()
            rsp = gp.sendApdu(cmd)
            timeStop = timeit.default_timer()
            transtime = timeStop - timeStart
            self.__handler.handleAPDUResponse("".join("%02X " %(ord(vb)) for vb in rsp), transtime)

    def __transmit(self, cmd, t0AutoGetResponse, handlerArgs):
        """Thread method to transmit an apdu;"""
        try:
            self.__transmit_impl(cmd, t0AutoGetResponse, handlerArgs)
        except Exception, e:
            self.__handler.handleException(e)
    
    def transmit(self, commandText, autoGetResponse, handlerArgs=tuple()):
        """Create one thread to transmit apdu;"""
        transmitThread = threading.Thread(target=self.__transmit, args=(commandText, autoGetResponse, handlerArgs), name="Transmit thread")
        transmitThread.start()
    
    def __transmitAPDUItems(self, apduItems, autoGetResponse, loopCount):
        """Thread method to transmit apdu items;"""
        
        try:
            for loopIndex in xrange(loopCount):
                self.__handler.handleLog('Transmit APDUs, loop: %d / %d' %(loopIndex + 1, loopCount))
                for apduItem in apduItems:
                    self.__transmit_impl(apduItem.getCommand(), autoGetResponse, apduItem.getTransArgs())
        except Exception, e:
            self.__handler.handleException(e)
    
    def transmitAPDUItems(self, apduItems, autoGetResponse, loopCount):
        """Create one thread to Transmit apdu items"""
        self.transmitThread = threading.Thread(target=self.__transmitAPDUItems, args=(apduItems, autoGetResponse, loopCount), name="Transmit APDU items thread")
        self.transmitThread.start()

    def __runScript(self, scriptPathName, loopCount, t0AutoGetResponse):
        """Thread method to run script;"""

        self.__handler.handleScriptBegin(scriptPathName);
        
        self.__stopFlag = False
        
        try:
            for i in xrange(loopCount):
                if self.__stopFlag:
                    break
                
                self.__handler.handleLog("Run script on loop: %d/%d" %(i + 1, loopCount))
                with open(scriptPathName, 'r') as scriptFile:
                    while (True):
                        if self.__stopFlag:
                            break
                        
                        scriptLine = scriptFile.readline()
                        if len(scriptLine) == 0:
                            break
                        self.__transmit(scriptLine, t0AutoGetResponse, tuple())
        except Exception, e:
            self.__handler.handleException(e)

        self.__handler.handleScriptEnd(scriptPathName);
        self.__runScriptThread = None
    
    def runningScript(self):
        """Return status of script run thread"""
        return (self.__runScriptThread != None)

    def stopScript(self):
        self.__stopFlag = True
    
    def runScript(self, scriptPathName, loopCount, t0AutoGetResponse):
        """Create one thread to run script;"""
        self.__runScriptThread = threading.Thread(target=self.__runScript, args=(scriptPathName, loopCount, t0AutoGetResponse), name="Run script thread")
        self.__runScriptThread.start()
    
    def __doMutualAuth(self, scp, scpi, sencKey, smacKey, dekKey):
        
        self.__handler.handleActionBegin("do mutual authentication")
        
        try:
            self.__handler.handleLog('doMutualAuth(): Start...')
            # Select Card Manager first;
            self.__gpInterface.selectApplication('')
            # Get SCP informations;
            if scp == -1 and scpi == -1:
                scp, scpi = self.__gpInterface.getSCPDetails()
                self.__handler.handleSCPInfo(scp, scpi)
            
            if (scp in (1, 2)):
                if (len(sencKey) != 16) or (len(smacKey) != 16) or (len(dekKey) != 16):
                    self.__handler.handleLog('The key of SCP01 shall be 16 bytes long.', wx.LOG_Warning)
                    return
            elif scp == 3:
                keyLen1 = len(sencKey)
                keyLen2 = len(smacKey)
                keyLen3 = len(dekKey)
                if (keyLen1 not in (16, 24, 32)) or (keyLen2 not in (16, 24, 32)) or (keyLen3 not in (16, 24, 32)):
                    self.__handler.handleLog('The key of SCP03 shall be (16 or 24 or 32) bytes long.', wx.LOG_Warning)
                    return
            
            kvn = 0
            self.__gpInterface.establishSecurityChannel(sencKey, smacKey, dekKey, kvn, scp, scpi)
            self.__handler.handleLog('doMutualAuth(): Succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)

        self.__handler.handleActionEnd("do mutual authentication")
    
    def doMutualAuth(self, scp, scpi, sencKey, smacKey, dekKey):
        self.__doMutualAuthThread = threading.Thread(target=self.__doMutualAuth, args=(scp, scpi, sencKey, smacKey, dekKey), name="Do mutual auth thread")
        self.__doMutualAuthThread.start()

    def __readCapFileInfo(self, capFilePath):
        self.__handler.handleActionBegin("read cap file information")

        try:
            self.__handler.handleLog('readCapFileInfo(): Start ...')

            capFileInfo = gp.readExecutableLoadFileParameters(capFilePath)
            
            self.__handler.handleCapFileInfo(capFileInfo)
            self.__handler.handleLog('readCapFileInfo(): Succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)
        self.__handler.handleActionEnd("read cap file information")
    
    def readCapFileInfo(self, capFilePath):
        self.__readCapFileInfoThread = threading.Thread(target=self.__readCapFileInfo, args=(capFilePath, ), name="Read cap file information thread")
        self.__readCapFileInfoThread.start()

    def __loadCapFile(self, capFilePath):
        try:
            self.__handler.handleLog('loadCapFile(): Start ...')
            self.__gpInterface.installForLoad(capFilePath)
            self.__gpInterface.load(capFilePath)
            self.__handler.handleLog('loadCapFile(): Succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)

        self.__handler.handleCardContentChanged()

    def loadCapFile(self, capFilePath):
        self.__loadCapFileThread = threading.Thread(target=self.__loadCapFile, args=(capFilePath, ), name="Load cap file thread")
        self.__loadCapFileThread.start()
    
    def __installApplet(self, packageAID, moduleAID, appletAID, privileges, installParameters):
        self.__handler.handleActionBegin("install application")
        
        try:
            self.__handler.handleLog('installApplet(): Start ...')
            self.__gpInterface.installForInstallAndMakeSelectable(packageAID, moduleAID, appletAID, privileges, installParameters)
            self.__handler.handleLog('installApplet(): Succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)

        self.__handler.handleActionEnd("install application")
        self.__handler.handleCardContentChanged()
    
    def installApplet(self, packageAID, moduleAID, appletAID, privileges, installParameters):
        self.__installAppletThread = threading.Thread(target=self.__installApplet, args=(packageAID, moduleAID, appletAID, privileges, installParameters), name="Install applet thread")
        self.__installAppletThread.start()
    
    def __getStatus(self):
        self.__handler.handleActionBegin("get status")
        try:
            self.__handler.handleLog('getStatus: Start ...')
            status80 = None
            status40 = None
            status20 = None
            status10 = None
            try:
                status80 = self.__gpInterface.getStatus(0x80)
            except Exception, e:
                self.__handler.handleLog('GetStatus(0x80): ' + e.message, wx.LOG_Error)
                pass
            try:
                status40 = self.__gpInterface.getStatus(0x40)
            except Exception, e:
                self.__handler.handleLog('GetStatus(0x40): ' + e.message, wx.LOG_Error)
                pass
            try:
                status20 = self.__gpInterface.getStatus(0x20)
            except Exception, e:
                self.__handler.handleLog('GetStatus(0x20): ' + e.message, wx.LOG_Error)
                pass
            try:
                status10 = self.__gpInterface.getStatus(0x10)
            except Exception, e:
                self.__handler.handleLog('GetStatus(0x10): ' + e.message, wx.LOG_Error)
                pass
            self.__handler.handleStatus({ 0x80 : status80, 0x40 : status40, 0x20 : status20, 0x10 : status10})
            self.__handler.handleLog('getStatus: succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)
        self.__handler.handleActionEnd("get status")
    
    def getStatus(self):
        self.__getStatusThread = threading.Thread(target=self.__getStatus, args=(), name="Get status thread")
        self.__getStatusThread.start()
        
    def __selectApplication(self, instanceAID):
        self.__handler.handleActionBegin("select application")
        
        try:
            self.__handler.handleLog('selectApplication: Start ...')
            self.__gpInterface.selectApplication(instanceAID)
            self.__handler.handleLog('selectApplication: succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)

        self.__handler.handleActionEnd("select application")
        
    def selectApplication(self, instanceAID):
        self.__selectApplicationThread = threading.Thread(target=self.__selectApplication, args=(instanceAID, ), name="Select application thread")
        self.__selectApplicationThread.start()
    
    def __deleteApplication(self, appAID):
        self.__handler.handleActionBegin("delete application")

        try:
            self.__handler.handleLog('deleteApplication: Start ...')
            self.__gpInterface.deleteApplication((appAID, ))
            self.__handler.handleLog('deleteApplication: succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)

        self.__handler.handleActionEnd("delete application")
        self.__handler.handleCardContentChanged()

    def deleteApplication(self, appAID):
        self.__deleteApplicationThread = threading.Thread(target=self.__deleteApplication, args=(appAID, ), name="Delete application thread")
        self.__deleteApplicationThread.start()
    
    def __loadScript(self, scriptPathName):
        if not os.path.exists(scriptPathName):
            self.__handler.handleLog('Script file not exists. %s' %(scriptPathName), wx.LOG_Error)
            return
        
        self.__handler.handleLoadScriptBegin()
        try:
            self.__handler.handleLog('Load script: %s' %(scriptPathName))
            
            scriptLines = []
            with open(scriptPathName, 'r') as scriptFile:
                scriptLines = scriptFile.readlines()
            
            for scriptLine in scriptLines:
                scriptLine = Util.removespace(scriptLine)
                if len(scriptLine) > 0 and  Util.ishexstr(scriptLine):
                    self.__handler.handleLoadScriptItem(scriptLine)
            
        except Exception, e:
            self.__handler.handleException(e)
        self.__handler.handleLoadScriptEnd()

    def loadScript(self, scriptPathName):
        self.__loadScriptThread = threading.Thread(target=self.__loadScript, args=(scriptPathName, ), name="Load script thread")
        self.__loadScriptThread.start()
    
    def __loadDebuggerScript(self, scriptPathName):
        if not os.path.exists(scriptPathName):
            self.__handler.handleLog('Debugger script file not exists. %s' %(scriptPathName), wx.LOG_Error)
            return
        
        try:
            self.__handler.handleLoadDebuggerScriptBegin()
            self.__handler.handleLog('Load debugger script: %s' %(scriptPathName))
            
            scriptFile = DebuggerScriptFile(scriptPathName)
            ret, info = scriptFile.parse()
            if ret:
                self.__handler.handleLoadDebuggerScriptEnd(info)
            else:
                self.__handler.handleException(info)
        except Exception, e:
            self.__handler.handleException(e)
    
    def loadDebuggerScript(self, scriptPathName):
        self.__loadDebuggerScriptThread = threading.Thread(target=self.__loadDebuggerScript, args=(scriptPathName, ), name="Load debugger script thread")
        self.__loadDebuggerScriptThread.start()
    
    def __saveDebuggerScript(self, scriptPathName, commandsInfo):
        self.__handler.handleLog('Save debugger script ...', wx.LOG_Info)
        scriptFile = DebuggerScriptFile(scriptPathName)
        scriptFile.save(commandsInfo)
        self.__handler.handleLog('Debugger script is saved to file: %s.' %(scriptPathName), wx.LOG_Info)

    def saveDebuggerScript(self, scriptPathName, commandsInfo):
        self.__saveDebuggerScriptThread = threading.Thread(target=self.__saveDebuggerScript, args=(scriptPathName, commandsInfo), name="Save debugger script thread")
        self.__saveDebuggerScriptThread.start()
    
    def __getKeyTemplateInfo(self):
        self.__handler.handleActionBegin("get key template information")
        
        try:
            self.__handler.handleLog('getKeyTemplateInfo: Start ...')
            kits = self.__gpInterface.getKeyInformationTemplates()
            self.__handler.handleKeyInformationTemplates(kits)
            self.__handler.handleLog('getKeyTemplateInfo: succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)

        self.__handler.handleActionEnd("get key template information")
    
    def getKeyTemplateInfo(self):
        self.__getkeyTemplateInfoThread = threading.Thread(target=self.__getKeyTemplateInfo, args=(), name="Get key template information thread")
        self.__getkeyTemplateInfoThread.start() 
            
    def __putKey(self, oldKVN, newKVN, key1, key2, key3):
        self.__handler.handleActionBegin("put key")
        
        try:
            self.__handler.handleLog('putKey: Start ...')
            self.__gpInterface.putSCKey(oldKVN, newKVN, key1, key2, key3)
            self.__handler.handleLog('putKey: succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)
        
        self.__handler.handleActionEnd("put key")
        self.__handler.handleKeyChanged()

    def putKey(self, oldKVN, newKVN, key1, key2, key3):
        if wx.CANCEL == wx.MessageBox('Make sure your new key has been stored well!', caption='Put key', style=wx.ICON_WARNING|wx.OK|wx.CANCEL|wx.CANCEL_DEFAULT):
            return
        self.__putKeyThread = threading.Thread(target=self.__putKey, args=(oldKVN, newKVN, key1, key2, key3), name="Put key thread")
        self.__putKeyThread.start()
    
    def __deleteKey(self, keysInfo):
        self.__handler.handleActionBegin("delete key")

        for keyInfo in keysInfo:
            kvn = keyInfo[0]
            keyIndex = keyInfo[1]
            try:
                self.__handler.handleLog('deleteKey(%02X, %02X): Start ...' %(kvn, keyIndex))
                self.__gpInterface.deleteKey(kvn, keyIndex)
                self.__handler.handleLog('deleteKey(%02X, %02X): succeeded.' %(kvn, keyIndex), wx.LOG_Info)
            except Exception, e:
                self.__handler.handleException(e)

        self.__handler.handleActionEnd("delete key")
        self.__handler.handleKeyChanged()

    def deleteKey(self, keysInfo):
        if wx.CANCEL == wx.MessageBox('Are you sure to do this operation?', caption='Delete key', style=wx.ICON_WARNING|wx.OK|wx.CANCEL|wx.CANCEL_DEFAULT):
            return
        self.__deleteKeyThread = threading.Thread(target=self.__deleteKey, args=(keysInfo, ), name="Delete key thread")
        self.__deleteKeyThread.start()
    
    def __debuggerCommand(self, commandIndex, commandName, commandValue):
        self.__debuggerRunOneCommand(commandIndex, commandName, commandValue)
    
    def __debuggerRunOneCommand(self, commandIndex, commandName, commandValue):
        self.__handler.handleDebuggerProcessing((commandIndex, commandName, commandValue))
        
        rsp = None
        
        if commandName == 'RF_ON':
            rsp = [self.__scDebugger.rfOn(), '']
        elif commandName == 'RF_OFF':
            rsp = [self.__scDebugger.rfOff(), '']
        elif commandName == 'RF_AUTO':
            rsp = [self.__scDebugger.rfAuto(), '']
        elif commandName == 'RF_MANUAL':
            rsp = [self.__scDebugger.rfManaul(), '']
#         elif commandName == '%UID%':
#             self.setDebuggerVariables('%UID%', commandValue)
#             rsp = (True, '')
        elif commandName == 'REQA':
            rsp = self.__scDebugger.claREQA(commandValue)
        elif commandName == 'WUPA':
            rsp = self.__scDebugger.claWUPA(commandValue)
        elif commandName == 'ANTICOLLISION':
            rsp = self.__scDebugger.claAnticollision(commandValue)
        elif commandName == 'SELECT':
#             if len(commandValue) != 2:
#                 rsp = (False, chr(0x80))
#             else:
#                 if not self.__debuggerVariables.has_key('%UID%'):
#                     rsp = (False, chr(0x81))
#                 else:
#                     commandValue += self.__debuggerVariables['%UID%']
#                     rsp = self.__scDebugger.claSelect(commandValue)
            rsp = self.__scDebugger.claSelect(commandValue)
        elif commandName == 'RATS':
            rsp = self.__scDebugger.claRATS(commandValue)
        elif commandName == 'HLTA':
            rsp = self.__scDebugger.claHLTA(commandValue)
        elif commandName == 'PPS':
            rsp = self.__scDebugger.claPPS(commandValue)
        elif commandName == 'REQB':
            raise NotImplementedError()
        elif commandName == 'WUPB':
            raise NotImplementedError()
        elif commandName == 'SLOT-MARKER':
            raise NotImplementedError()
        elif commandName == 'ATTRIB':
            raise NotImplementedError()
        elif commandName == 'HLTB':
            raise NotImplementedError()
        elif commandName == 'I-BLOCK':
            rsp = self.__scDebugger.clTransmit(commandValue)
        elif commandName == 'R-BLOCK':
            rsp = self.__scDebugger.clTransmit(commandValue)
        elif commandName == 'S-BLOCK':
            rsp = self.__scDebugger.clTransmit(commandValue)
        elif commandName == 'AUTHENTICATION':
#             if len(commandValue) != 8:
#                 rsp = (False, chr(0x80))
#             else:
#                 if not self.__debuggerVariables.has_key('%UID%'):
#                     rsp = (False, chr(0x81))
#                 else:
#                     commandValue += self.__debuggerVariables['%UID%']
#                     rsp = self.__scDebugger.mifareAuthentication(commandValue)
            rsp = self.__scDebugger.mifareAuthentication(commandValue)
        elif commandName == 'READ_BLOCK':
            rsp = self.__scDebugger.mifareBlockRead(commandValue)
        elif commandName == 'WRITE_BLOCK':
            rsp = self.__scDebugger.mifareBlockWrite(commandValue)
        elif commandName == 'INCREMENT':
            rsp = self.__scDebugger.mifareIncrement(commandValue)
        elif commandName == 'DECREMENT':
            rsp = self.__scDebugger.mifareDecrement(commandValue)
        elif commandName == 'RESTORE':
            rsp = self.__scDebugger.mifareRestore(commandValue)
        elif commandName == 'TRANSFER':
            rsp = self.__scDebugger.mifareTransfer(commandValue)
        else:
            pass
        
        self.__handler.handleDebuggerResponse(rsp, (commandIndex, commandName, commandValue))
    
    def __debuggerCommands(self, commands):
        try:
            for command in commands:
                commandIndex = command[0]
                commandName = command[1]
                commandValue = command[2]
                
                self.__debuggerRunOneCommand(commandIndex, commandName, commandValue)
        except Exception, e:
            self.__handler.handleException(str(e))
    
    def debuggerCommand(self, commandIndex, commandName, commandValue):
        self.__debuggerCommandThread = threading.Thread(target=self.__debuggerCommand, args=(commandIndex, commandName, commandValue), name="Debugger command thread")
        self.__debuggerCommandThread.start()
    
    def debuggerCommands(self, commands):
        self.__debuggerCommandsThread = threading.Thread(target=self.__debuggerCommands, args=(commands, ), name="Debugger commands thread")
        self.__debuggerCommandsThread.start()
    
    def debuggerCommandsStop(self):
        try:
            del self.__debuggerCommandsThread
            self.__debuggerCommandsThread = None
        except:
            pass
    
    def clearDebuggerVariables(self):
        self.__debuggerVariables.clear()
    
    def setDebuggerVariables(self, name, value):
        self.__debuggerVariables[name] = value
    
    def __mifareSelectCard(self):
        # Select the card;
        self.__scDebugger.rfOn()
        self.__scDebugger.rfManaul()
        self.__scDebugger.claWUPA2(chr(0x52))
        error, uid = self.__scDebugger.claAnticollision2(chr(0x93), chr(0x20))
        error, data = self.__scDebugger.claSelect2(chr(0x93), chr(0x70), uid)
        return error, uid

    def __mifareSetup(self):
        self.__scDebugger.rfOn()
        self.__scDebugger.rfManaul()
        self.__scDebugger.claWUPA2(chr(0x52))
        error, data = self.__scDebugger.claAnticollision2(chr(0x93), chr(0x20))
        if not error:
            self.__handler.handleException(Exception(data))
            return
        uid = data
        error, data = self.__scDebugger.claSelect2(chr(0x93), chr(0x70), uid)
        if not error:
            self.__handler.handleException(Exception(data))
            return
        self.__scDebugger.claHLTA2()
        error = self.__libsc.M1_setup()
        if error != 0:
            self.__handler.handleException(Exception(DebuggerUtils.getErrorString(error)))
            return
        return error, uid
        
    def __mifareDumpCard(self, key_a):
        # Read card data;
        result = True
        need_select = True
        for block_index in range(64):
            self.__handler.handleLog('Read block data, block: %d.' %(block_index))
            if need_select:
                # Select the card;
                try:
                    error, uid = self.__mifareSelectCard()
                    if not error:
                        self.__handler.handleException(Exception('Select card failed, %s' %(DebuggerUtils.getErrorString(error))))
                        return
                    else:
                        self.__handler.handleLog('Card selected: %s' %(''.join('%02X' %(ord(b)) for b in uid)), wx.LOG_Info)
                        need_select = False
                except Exception, e:
                    self.__handler.handleException(e)
                    continue

            error = self.__libsc.M1_authentication(block_index, 0, key_a, uid)
            if error == 0x00:
                error, data = self.__libsc.M1_read_block(block_index)
                if error == 0x00:
                    self.__handler.handleMifareResponse(2, error, (block_index, data))
                    need_select = False
                else:
                    self.__handler.handleException(Exception('Authenticate failed, %s' %(DebuggerUtils.getErrorString(error))))
                    result = False
                    need_select = True
            else:
                self.__handler.handleException(Exception('Authenticate failed, %s' %(DebuggerUtils.getErrorString(error))))
                result = False
                need_select = True
        if result:
            self.__handler.handleLog('Dump card data succeeded.', wx.LOG_Info)
    
    def __mifareCloneCard(self, card_data, key_a):
        # Prepare;
        try:
            self.__mifareSetup()
        except Exception, e:
            self.__handler.handleException(e)
            return

        # Write data to the card;
        for row_index in range(0, len(card_data)):
            block_data = card_data[row_index]
            if row_index in (3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63):
                block_data = key_a + block_data[6:]
            error = self.__libsc.M1_write_block(row_index, block_data)
            if error != 0:
                self.__handler.handleException(Exception(DebuggerUtils.getErrorString(error)))
            else:
                self.__handler.handleMifareResponse(1, error, row_index)
    
    def __mifareReadSaveData(self, data, file_path_name):
        with open(file_path_name, 'wb') as f:
            f.write(data)
            self.__handler.handleLog('Mifare card data saved.', wx.LOG_Info)
    
    def __mifareFixBrickedUID(self):
        try:
            self.__mifareSetup()
            error = self.__libsc.M1_write_block(0, '\x01\x02\x03\x04\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
            if error != 0:
                self.__handler.handleException(Exception(DebuggerUtils.getErrorString(error)))
            else:
                self.__handler.handleLog('Mifare card bricked UID is fixed.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)
            return
    
    def __mifareChangeUID(self, new_uid):
        # Read data of block 0;
        try:
            error, data = self.__mifareSelectCard()
            if not error:
                self.__handler.handleException(Exception('Select card failed, %s' %(DebuggerUtils.getErrorString(error))))
                return
        except Exception, e:
            self.__handler.handleException(e)
            return
        
        uid = data
        self.__handler.handleLog('Card selected: %s' %(''.join('%02X' %(ord(b)) for b in uid)), wx.LOG_Info)
        error = self.__scDebugger.mifareAuthentication2(0, 0, '\xFF\xFF\xFF\xFF\xFF\xFF', uid)
        if not error:
            self.__handler.handleException(Exception('Authenticate failed, %s' %(DebuggerUtils.getErrorString(error))))
            return
        
        error, data = self.__libsc.M1_read_block(0)
        if error != 0:
            self.__handler.handleException(Exception(DebuggerUtils.getErrorString(error)))
            return
        block_data = data
        
        # Write data to block 0;
        try:
            self.__mifareSetup()
        except Exception, e:
            self.__handler.handleException(e)
            return
        
        tck = 0
        for i in range(len(new_uid)):
            tck ^= ord(new_uid[i])
        tck = chr(tck)
        error = self.__libsc.M1_write_block(0, new_uid + tck + block_data[5 : ])
        if error != 0:
            self.__handler.handleException(Exception(DebuggerUtils.getErrorString(error)))
        else:
            self.__handler.handleLog('Mifare card UID changed, from: %s, to: %s.' %(''.join('%02X' %(ord(b)) for b in uid), ''.join('%02X' %(ord(b)) for b in new_uid)), wx.LOG_Info)
    
    def __desfireSendCommand(self, cmd):
        error, resp  = self.__libsc.DESFire_send_command(cmd)
        if error != 0:
            self.__handler.handleLog(DebuggerUtils.getErrorString(error), wx.LOG_Error)
        else:
            self.__handler.handleLog(''.join('%02X' %(ord(c)) for c in resp))
        
    def mifareDumpCard(self, key_a):
        self.__mifareCommandThread = threading.Thread(target=self.__mifareDumpCard, args=(key_a, ))
        self.__mifareCommandThread.start()
    
    def mifareCloneCard(self, card_data, key_a):
        self.__mifareCommandThread = threading.Thread(target=self.__mifareCloneCard, args=(card_data, key_a, ))
        self.__mifareCommandThread.start()
    
    def mifareReadCardData(self):
        self.__mifareCommandThread = threading.Thread(target=self.__mifareReadCardData)
        self.__mifareCommandThread.start()
    
    def mifareSaveData(self, card_data, file_path_name):
        self.__mifareCommandThread = threading.Thread(target=self.__mifareReadSaveData, args = (card_data, file_path_name, ))
        self.__mifareCommandThread.start()
    
    def mifareFixBrickedUID(self):
        self.__mifareCommandThread = threading.Thread(target=self.__mifareFixBrickedUID)
        self.__mifareCommandThread.start()
    
    def mifareChangeUID(self, uid):
        self.__mifareCommandThread = threading.Thread(target=self.__mifareChangeUID, args=(uid, ))
        self.__mifareCommandThread.start()
    
    def __desfireAuthenticate(self):
        try:
            self.__desfire.authenticate(0)
            self.__handler.handleLog('DESFire authenticated.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleLog(str(e), wx.LOG_Error)
    
    def desfireAuthenticate(self):
        self.__desfireCommandThread = threading.Thread(target=self.__desfireAuthenticate)
        self.__desfireCommandThread.start()

    def __desfireGetVersion(self):
        version_info = self.__desfire.get_version()
        self.__handler.handleDESFireResponse(DESFireEx.GET_VERSION, version_info)
    
    def desfireGetVersion(self):
        self.__desfireCommandThread = threading.Thread(target=self.__desfireGetVersion)
        self.__desfireCommandThread.start()

    def __desfireFormatPICC(self):
        try:
            self.__desfire.format()
            self.__handler.handleLog('DESFire format PICC succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleLog('DESFire format PICC, exception: %s' %(e), wx.LOG_Error)
        
    def desfireFormatPICC(self):
        self.__desfireCommandThread = threading.Thread(target=self.__desfireFormatPICC)
        self.__desfireCommandThread.start()
    
    def __desfireGetApplicationIDs(self):
        try:
            app_ids = self.__desfire.get_applications()
            self.__handler.handleDESFireResponse(DESFireEx.GET_APPLICATION_IDS, app_ids)
            self.__handler.handleLog('DESFire get application ids succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleLog('DESFire get application ids, exception: %s' %(e), wx.LOG_Error)

    def desfireGetApplicationIDs(self):
        self.__desfireCommandThread = threading.Thread(target=self.__desfireGetApplicationIDs)
        self.__desfireCommandThread.start()
    
    def __desfireDeleteApplication(self, app_id):
        try:
            self.__desfire.delete_application(app_id)
            self.__handler.handleLog('DESFire delete application succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleLog('DESFire delete application, exception: %s' %(e), wx.LOG_Error)
        # Refresh application list;
        self.__desfireGetApplicationIDs()

    def desfireDeleteApplication(self, app_id):
        self.__desfireCommandThread = threading.Thread(target=self.__desfireDeleteApplication, args=(app_id, ))
        self.__desfireCommandThread.start()
    
    def __desfireSelectApplication(self, app_id):
        try:
            self.__desfire.select_application(app_id)
            self.__handler.handleLog('DESFire select application: %06X selected.' %(app_id), wx.LOG_Info)
        except Exception, e:
            self.__handler.handleLog('DESFire select application, exception: %s' %(e), wx.LOG_Error)

    def desfireSelectApplication(self, app_id):
        self.__desfireCommandThread = threading.Thread(target=self.__desfireSelectApplication, args=(app_id, ))
        self.__desfireCommandThread.start()
    
    def __desfireCreateApplication(self, aid, key_settings, num_of_keys):
        try:
            self.__desfire.create_application(aid, key_settings, num_of_keys)
            self.__handler.handleLog('DESFire create application succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleLog('DESFire create application, exception: %s' %(e), wx.LOG_Error)
        # Refresh application list;
        self.__desfireGetApplicationIDs()

    def desfireCreateApplication(self, aid, key_settings, num_of_keys):
        self.__desfireCommandThread = threading.Thread(target=self.__desfireCreateApplication, args=(aid, key_settings, num_of_keys))
        self.__desfireCommandThread.start()
    
    def __desfireGetFileIDs(self):
        try:
            file_ids = self.__desfire.get_file_ids()
            self.__handler.handleDESFireResponse(DESFireEx.GET_FILE_IDS, file_ids)
            self.__handler.handleLog('DESFire get file ids succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleLog('DESFire get file ids, exception: %s' %(e), wx.LOG_Error)

    def desfireGetFileIDs(self):
        self.__desfireCommandThread = threading.Thread(target=self.__desfireGetFileIDs)
        self.__desfireCommandThread.start()
    
    def __desfireCreateStdDataFile(self, file_no, com_set, access_rights, file_size):
        try:
            self.__desfire.create_std_data_file(file_no, com_set, access_rights, file_size)
            self.__handler.handleLog('DESFire create std data file succeeded.', wx.LOG_Info)
            self.__desfireGetFileIDs()
        except Exception, e:
            self.__handler.handleLog('DESFire create std data file, exception: %s' %(e), wx.LOG_Error)
        
    def desfireCreateStdDataFile(self, file_no, com_set, access_rights, file_size):
        self.__desfireCommandThread = threading.Thread(target=self.__desfireCreateStdDataFile, args=(file_no, com_set, access_rights, file_size))
        self.__desfireCommandThread.start()
    
    def __desfireCreateBackupDataFile(self, file_no, com_set, access_rights, file_size):
        try:
            self.__desfire.create_backup_data_file(file_no, com_set, access_rights, file_size)
            self.__handler.handleLog('DESFire create backup data file succeeded.', wx.LOG_Info)
            self.__desfireGetFileIDs()
        except Exception, e:
            self.__handler.handleLog('DESFire create backup data file, exception: %s' %(e), wx.LOG_Error)
    
    def desfireCreateBackupDataFile(self, file_no, com_set, access_rights, file_size):
        self.__desfireCommandThread = threading.Thread(target=self.__desfireCreateBackupDataFile, args=(file_no, com_set, access_rights, file_size))
        self.__desfireCommandThread.start()
    
    def __desfireCreateValueFile(self, file_no, com_set, access_rights, lower_limit, upper_limit, value, limit_debit_enabled):
        try:
            self.__desfire.create_value_file(file_no, com_set, access_rights, lower_limit, upper_limit, value, limit_debit_enabled)
            self.__handler.handleLog('DESFire create value file succeeded.', wx.LOG_Info)
            self.__desfireGetFileIDs()
        except Exception, e:
            self.__handler.handleLog('DESFire create value file, exception: %s' %(e), wx.LOG_Error)
    
    def desfireCreateValueFile(self, file_no, com_set, access_rights, lower_limit, upper_limit, value, limit_debit_enabled):
        self.__desfireCommandThread = threading.Thread(target=self.__desfireCreateValueFile, args=(file_no, com_set, access_rights, lower_limit, upper_limit, value, limit_debit_enabled))
        self.__desfireCommandThread.start()

    def __desfireCreateLinearRecordFile(self, file_no, com_set, access_rights, record_size, max_num_of_records):
        try:
            self.__desfire.create_linear_record_file(file_no, com_set, access_rights, record_size, max_num_of_records)
            self.__handler.handleLog('DESFire create linear record file succeeded.', wx.LOG_Info)
            self.__desfireGetFileIDs()
        except Exception, e:
            self.__handler.handleLog('DESFire create linear record file, exception: %s' %(e), wx.LOG_Error)
    
    def desfireCreateLinearRecordFile(self, file_no, com_set, access_rights, record_size, max_num_of_records):
        self.__desfireCommandThread = threading.Thread(target=self.__desfireCreateLinearRecordFile, args=(file_no, com_set, access_rights, record_size, max_num_of_records))
        self.__desfireCommandThread.start()
    
    def __desfireCreateCyclicRecordFile(self, file_no, com_set, access_rights, record_size, max_num_of_records):
        try:
            self.__desfire.create_cyclic_record_file(file_no, com_set, access_rights, record_size, max_num_of_records)
            self.__handler.handleLog('DESFire create cyclic record file succeeded.', wx.LOG_Info)
            self.__desfireGetFileIDs()
        except Exception, e:
            self.__handler.handleLog('DESFire create cyclic record file, exception: %s' %(e), wx.LOG_Error)
    
    def desfireCreateCyclicRecordFile(self, file_no, com_set, access_rights, record_size, max_num_of_records):
        self.__desfireCommandThread = threading.Thread(target=self.__desfireCreateCyclicRecordFile, args=(file_no, com_set, access_rights, record_size, max_num_of_records))
        self.__desfireCommandThread.start()
    
    
class pyResManControllerEventHandler(object):
    '''
    Methods to handle controller's event; The viewer (pyRsaMan) implements these methods as usual;
    '''
    
    def handleCardInserted(self):
        pass
    
    def handleCardRemoved(self):
        pass
    
    def handleReaderAdded(self):
        pass
    
    def handleReaderRemoved(self):
        pass
    
    def handleAPDUCommand(self, cmd, args=tuple()):
        pass
    
    def handleAPDUResponse(self, rsp, transtime, args=tuple()):
        pass
    
    def handleScriptBegin(self, status):
        pass

    def handleScriptEnd(self, status):
        pass

    def handleLog(self):
        pass

    def handleException(self, e):
        pass
    
    def handleCapFileInfo(self, info):
        pass
    
    def handleStatus(self, status):
        pass

    def handleLoadScriptBegin(self):
        pass
    
    def handleLoadScriptItem(self, args):
        pass
    
    def handleLoadScriptEnd(self):
        pass
    
    def handleKeyInformationTemplates(self, kits):
        pass
    
    def handleSCPInfo(self, scp, scpi):
        pass
    
    def handleKeyChanged(self):
        pass
    
    def handleActionBegin(self, action):
        pass
    
    def handleActionEnd(self, action):
        pass
    
    def handleDebuggerResponse(self, response, cmdinfo):
        pass

    def handleDebuggerProcessing(self, cmdinfo):
        pass

    def handleMifareResponse(self, action_type, result, data):
        pass
    
    def handleDESFireResponse(self, command_type, response):
        pass
    