# -*- coding:utf8 -*-

'''
Created on 2015-10-30

@author: javacardos@gmail.com
@organization: http://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from pyResManReader import pyResManReader, ICardMonitorEventHandler, IReaderMonitorEventHandler
from Util import Util
import threading
import timeit
import globalplatformlib as gp
import wx
import os

class _MethodThread(threading.Thread):
    """""Thread class to run method as a thread;"""
    
    def __init__(self, eventHandler, method, args=tuple(), name="Method Thread"):
        threading.Thread.__init__(self, name=name)
        self.eventHandler = eventHandler
        self._method = method
        self._args = args
    
    def run(self):
        threading.Thread.run(self)
        try:
            self._method(self._args)
        except Exception, e:
            self.eventHandler.handleException(e)

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
        self.__context = gp.establishContext()
        self.__cardInfo = None
        self.__securityInfo = None
        gp.enableTraceMode(1)
    
    def getReaderList(self):
        return self.__reader.getReaderList()
    
    def connect(self, readername, protocol, mode):
        """ Connect to the reader;"""
        self.__handler.handleLog('Connect to %s.' %(readername))

        self.__readername = readername
        self.__cardInfo = gp.connectCard(self.__context, str(readername), protocol)
        
    def __checkContext(self):
        if self.__context == None:
            self.__handler.handleLog('Please establish context first.', wx.LOG_Error)
            return False
        return True

    def __checkCardInfo(self):
        if self.__cardInfo == None:
            self.__handler.handleLog('Please connect first.', wx.LOG_Error)
            return False
        return True

    def __checkSecurityInfo(self):
        if self.__securityInfo== None:
            self.__handler.handleLog('Please establish secure channel.', wx.LOG_Error)
            return False
        return True

    def handleCardEvent(self, eventType, args):
        readername = args[0]
        if eventType == ICardMonitorEventHandler.MONITOR_EVENT_INSERT:
            self.__handler.handleCardInserted(readername)
        elif eventType == ICardMonitorEventHandler.MONITOR_EVENT_REMOVE:
            self.__cardInfo = None
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
#         self.__reader.disconnect()
        if self.__cardInfo != None:
            gp.disconnectCard(self.__context, self.__cardInfo)
        self.__reader.removeCardMonitorHandler(self)
        self.__reader.stopCardMonitor()
    
    def __transmit(self, args):
        """Thread method to transmit an apdu;"""
        
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        
        cmd = args[0]
        t0AutoGetResponse = args[1]
        handlerArgs = args[2]
        
        transtime = 0
        try:
            commandValue = Util.s2vs(cmd)
            
            self.__handler.handleAPDUCommand("".join("%02X " %(ord(vb)) for vb in commandValue), handlerArgs)
            timeStart = timeit.default_timer()
            rsp = gp.sendApdu(self.__context, self.__cardInfo, None, Util.s2vs(cmd))
            timeStop = timeit.default_timer()
            transtime = timeStop - timeStart
            self.__handler.handleAPDUResponse("".join("%02X " %(ord(vb)) for vb in rsp), transtime, handlerArgs)
            
            if t0AutoGetResponse and (rsp[0] == '\x61') and (len(handlerArgs) == 0):
                cmd = '\x00\xC0\x00\x00' + rsp[1]
                self.__handler.handleAPDUCommand("".join("%02X " %(ord(vb)) for vb in cmd))
                timeStart = timeit.default_timer()
                rsp = gp.sendApdu(self.__context, self.__cardInfo, None, cmd)
                timeStop = timeit.default_timer()
                transtime = timeStop - timeStart
                self.__handler.handleAPDUResponse("".join("%02X " %(ord(vb)) for vb in rsp), transtime)
        except Exception, e:
            self.__handler.handleAPDUResponse('', transtime, handlerArgs)
            self.__handler.handleException(e)
    
    def transmit(self, commandText, autoGetResponse, handlerArgs=tuple()):
        """Create one thread to transmit apdu;"""
        transmitThread = _MethodThread(self.__handler, self.__transmit, (commandText, autoGetResponse, handlerArgs), name="Transmit thread")
        transmitThread.start()
    
    def __transmitAPDUItems(self, args):
        """Thread method to transmit apdu items;"""
        apduItems = args[0]
        autoGetResponse = args[1]
        loopCount = args[2]

        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        
        for loopIndex in xrange(loopCount):
            self.__handler.handleLog('Transmit APDUs, loop: %d / %d' %(loopIndex + 1, loopCount))
            try:
                for apduItem in apduItems:
                    self.__transmit((apduItem.getCommand(), autoGetResponse, apduItem.getTransArgs()))
            except Exception, e:
                self.__handler.handleException(e)
    
    def transmitAPDUItems(self, apduItems, autoGetResponse, loopCount):
        """Create one thread to Transmit apdu items"""
        self.transmitThread = _MethodThread(self.__handler, self.__transmitAPDUItems, (apduItems, autoGetResponse, loopCount), name="Transmit APDU items thread")
        self.transmitThread.start()

    def __runScript(self, args):
        """Thread method to run script;"""
        scriptPathName = args[0]
        loopCount = args[1]
        t0AutoGetResponse = args[2]
        
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return

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
                        self.__transmit((scriptLine, t0AutoGetResponse, tuple()))
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
        self.__runScriptThread = _MethodThread(self.__handler, self.__runScript, (scriptPathName, loopCount, t0AutoGetResponse), name="Run script thread")
        self.__runScriptThread.start()
    
    def __doMutualAuth(self, args):
        scp, scpi, sencKey, smacKey, dekKey = args
        
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        
        self.__handler.handleActionBegin("do mutual authentication")
        
        try:
            self.__handler.handleLog('doMutualAuth(): Start...')
            # Select Card Manager first;
            gp.selectApplication(self.__context, self.__cardInfo, '')
            # Get SCP informations;
            if scp == -1 and scpi == -1:
                scp, scpi = gp.getSCPDetails(self.__context, self.__cardInfo)
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
            self.__securityInfo = gp.mutualAuthentication(self.__context, self.__cardInfo, None, sencKey, smacKey, dekKey, kvn, 0, scp, scpi, 0, 0)
            self.__handler.handleLog('doMutualAuth(): Succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)

        self.__handler.handleActionEnd("do mutual authentication")
    
    def doMutualAuth(self, scp, scpi, sencKey, smacKey, dekKey):
        self.__doMutualAuthThread = _MethodThread(self.__handler, self.__doMutualAuth, (scp, scpi, sencKey, smacKey, dekKey), name="Do mutual auth thread")
        self.__doMutualAuthThread.start()

    def __readCapFileInfo(self, args):
        self.__handler.handleActionBegin("read cap file information")
        capFilePath = args[0]
        try:
            self.__handler.handleLog('readCapFileInfo(): Start ...')

            capFileInfo = gp.readExecutableLoadFileParameters(capFilePath)
            
            self.__handler.handleCapFileInfo(capFileInfo)
            self.__handler.handleLog('readCapFileInfo(): Succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)
        self.__handler.handleActionEnd("read cap file information")
    
    def readCapFileInfo(self, capFilePath):
        self.__readCapFileInfoThread = _MethodThread(self.__handler, self.__readCapFileInfo, (capFilePath, ), name="Read cap file information thread")
        self.__readCapFileInfoThread.start()

    def __loadCapFile(self, args):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        if not self.__checkSecurityInfo(): return

        capFilePath = args[0]
        try:
            self.__handler.handleLog('loadCapFile(): Start ...')
            capFileInfo = gp.readExecutableLoadFileParameters(capFilePath)
            gp.installForLoad(self.__context, self.__cardInfo, self.__securityInfo, capFileInfo['loadFileAID'], gp.AID_ISD, '', '', 0, 0, 0)
            gp.load(self.__context, self.__cardInfo, self.__securityInfo, '', capFilePath)
            self.__handler.handleLog('loadCapFile(): Succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)

        self.__handler.handleCardContentChanged()

    def loadCapFile(self, capFilePath):
        self.__loadCapFileThread = _MethodThread(self.__handler, self.__loadCapFile, (capFilePath, ), name="Load cap file thread")
        self.__loadCapFileThread.start()
    
    def __installApplet(self, args):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        if not self.__checkSecurityInfo(): return
        
        self.__handler.handleActionBegin("install application")

        packageAID, moduleAID, appletAID, privileges, installParameters = args
        
        try:
            self.__handler.handleLog('installApplet(): Start ...')
            gp.installForInstallAndMakeSelectable(self.__context, self.__cardInfo, self.__securityInfo, packageAID, moduleAID, appletAID, privileges, 0, 0, installParameters, '')
            self.__handler.handleLog('installApplet(): Succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)

        self.__handler.handleActionEnd("install application")
        self.__handler.handleCardContentChanged()
    
    def installApplet(self, packageAID, moduleAID, appletAID, privileges, installParameters):
        self.__installAppletThread = _MethodThread(self.__handler, self.__installApplet, (packageAID, moduleAID, appletAID, privileges, installParameters), name="Install applet thread")
        self.__installAppletThread.start()
    
    def __getStatus(self, args):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        if not self.__checkSecurityInfo(): return

        self.__handler.handleActionBegin("get status")
        try:
            self.__handler.handleLog('getStatus: Start ...')
            status80 = None
            status40 = None
            status20 = None
            status10 = None
            try:
                status80 = gp.getStatus(self.__context, self.__cardInfo, self.__securityInfo, 0x80)
            except Exception, e:
                self.__handler.handleLog('GetStatus(0x80): ' + e.message, wx.LOG_Error)
                pass
            try:
                status40 = gp.getStatus(self.__context, self.__cardInfo, self.__securityInfo, 0x40)
            except Exception, e:
                self.__handler.handleLog('GetStatus(0x40): ' + e.message, wx.LOG_Error)
                pass
            try:
                status20 = gp.getStatus(self.__context, self.__cardInfo, self.__securityInfo, 0x20)
            except Exception, e:
                self.__handler.handleLog('GetStatus(0x20): ' + e.message, wx.LOG_Error)
                pass
            try:
                status10 = gp.getStatus(self.__context, self.__cardInfo, self.__securityInfo, 0x10)
            except Exception, e:
                self.__handler.handleLog('GetStatus(0x10): ' + e.message, wx.LOG_Error)
                pass
            self.__handler.handleStatus({ 0x80 : status80, 0x40 : status40, 0x20 : status20, 0x10 : status10})
            self.__handler.handleLog('getStatus: succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)
        self.__handler.handleActionEnd("get status")
    
    def getStatus(self):
        self.__getStatusThread = _MethodThread(self.__handler, self.__getStatus, (), name="Get status thread")
        self.__getStatusThread.start()
        
    def __selectApplication(self, args):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        
        self.__handler.handleActionBegin("select application")

        instanceAID = args[0]
        
        try:
            self.__handler.handleLog('selectApplication: Start ...')
            gp.selectApplication(self.__context, self.__cardInfo, instanceAID)
            self.__handler.handleLog('selectApplication: succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)

        self.__handler.handleActionEnd("select application")
        
    def selectApplication(self, instanceAID):
        self.__selectApplicationThread = _MethodThread(self.__handler, self.__selectApplication, (instanceAID, ), name="Select application thread")
        self.__selectApplicationThread.start()
    
    def __deleteApplication(self, args):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        if not self.__checkSecurityInfo(): return
        
        self.__handler.handleActionBegin("delete application")
        
        appAID = args[0]

        try:
            self.__handler.handleLog('deleteApplication: Start ...')
            gp.deleteApplication(self.__context, self.__cardInfo, self.__securityInfo, (appAID, ))
            self.__handler.handleLog('deleteApplication: succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)

        self.__handler.handleActionEnd("delete application")
        self.__handler.handleCardContentChanged()

    def deleteApplication(self, appAID):
        self.__deleteApplicationThread = _MethodThread(self.__handler, self.__deleteApplication, (appAID, ), name="Delete application thread")
        self.__deleteApplicationThread.start()
    
    def __loadScript(self, args):
        scriptPathName = args[0]
        
        if not os.path.exists(scriptPathName):
            self.__handler.handleLog('Script file not exists. %s' %(scriptPathName), wx.LOG_Error)
            return
        
        self.__handler.handleLoadScriptBegin()
        try:
            self.__handler.handleLog('Load script: %s' %(scriptPathName))
            
            scriptFile = open(scriptPathName, 'r')
            scriptLines = scriptFile.readlines()
            scriptFile.close()
            
            for scriptLine in scriptLines:
                scriptLine = Util.removespace(scriptLine)
                if len(scriptLine) > 0 and  Util.ishexstr(scriptLine):
                    self.__handler.handleLoadScriptItem(scriptLine)
            
        except Exception, e:
            self.__handler.handleException(e)
        self.__handler.handleLoadScriptEnd()

    def loadScript(self, scriptPathName):
        self.__loadScriptThread = _MethodThread(self.__handler, self.__loadScript, (scriptPathName, ), name="Load script thread")
        self.__loadScriptThread.start()
    
    def __getKeyTemplateInfo(self, args):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        if not self.__checkSecurityInfo(): return

        self.__handler.handleActionBegin("get key template information")
        
        try:
            self.__handler.handleLog('getKeyTemplateInfo: Start ...')
            kits = gp.getKeyInformationTemplates(self.__context, self.__cardInfo, self.__securityInfo, 0)
            self.__handler.handleKeyInformationTemplates(kits)
            self.__handler.handleLog('getKeyTemplateInfo: succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)

        self.__handler.handleActionEnd("get key template information")
    
    def getKeyTemplateInfo(self):
        self.__getkeyTemplateInfoThread = _MethodThread(self.__handler, self.__getKeyTemplateInfo, (), name="Get key template information thread")
        self.__getkeyTemplateInfoThread.start() 
            
    def __putKey(self, args):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        if not self.__checkSecurityInfo(): return
        
        self.__handler.handleActionBegin("put key")

        oldKVN, newKVN, key1, key2, key3 = args
        
        try:
            self.__handler.handleLog('putKey: Start ...')
            gp.putSCKey(self.__context, self.__cardInfo, self.__securityInfo, oldKVN, newKVN, None, key1, key2, key3)
            self.__handler.handleLog('putKey: succeeded.', wx.LOG_Info)
        except Exception, e:
            self.__handler.handleException(e)
        
        self.__handler.handleActionEnd("put key")
        self.__handler.handleKeyChanged()

    def putKey(self, oldKVN, newKVN, key1, key2, key3):
        if wx.CANCEL == wx.MessageBox('Make sure your new key has been stored well!', caption='Put key', style=wx.ICON_WARNING|wx.OK|wx.CANCEL|wx.CANCEL_DEFAULT):
            return
        self.__putKeyThread = _MethodThread(self.__handler, self.__putKey, (oldKVN, newKVN, key1, key2, key3), name="Put key thread")
        self.__putKeyThread.start()
    
    def __deleteKey(self, args):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        if not self.__checkSecurityInfo(): return
        
        self.__handler.handleActionBegin("delete key")
        
        keysInfo = args[0]

        for keyInfo in keysInfo:
            kvn = keyInfo[0]
            keyIndex = keyInfo[1]
            try:
                self.__handler.handleLog('deleteKey(%02X, %02X): Start ...' %(kvn, keyIndex))
                gp.deleteKey(self.__context, self.__cardInfo, self.__securityInfo, kvn, keyIndex)
                self.__handler.handleLog('deleteKey(%02X, %02X): succeeded.' %(kvn, keyIndex), wx.LOG_Info)
            except Exception, e:
                self.__handler.handleException(e)

        self.__handler.handleActionEnd("delete key")
        self.__handler.handleKeyChanged()

    def deleteKey(self, keysInfo):
        if wx.CANCEL == wx.MessageBox('Are you sure to do this operation?', caption='Delete key', style=wx.ICON_WARNING|wx.OK|wx.CANCEL|wx.CANCEL_DEFAULT):
            return
        self.__deleteKeyThread = _MethodThread(self.__handler, self.__deleteKey, (keysInfo, ), name="Delete key thread")
        self.__deleteKeyThread.start()

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

    def handleException(self):
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