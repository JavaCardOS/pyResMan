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
        
        try:
            for apduItem in apduItems:
                self.__transmit((apduItem.getCommand(), autoGetResponse, apduItem.getTransArgs()))
        except Exception, e:
            self.__handler.handleException(e)
    
    def transmitAPDUItems(self, apduItems, autoGetResponse):
        """Create one thread to Transmit apdu items"""
        self.transmitThread = _MethodThread(self.__handler, self.__transmitAPDUItems, (apduItems, autoGetResponse), name="Transmit APDU items thread")
        self.transmitThread.start()

    def __runScript(self, args):
        """Thread method to run script;"""
        scriptPathName = args[0]
        loopCount = args[1]
        t0AutoGetResponse = args[2]
        
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
    
    def doMutualAuth(self):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        
        try:
            self.__handler.handleLog('doMutualAuth(): Start...')
            # Select Card Manager first;
            gp.selectApplication(self.__context, self.__cardInfo, '')
            # Get SCP informations;
            scpDetails = gp.getSCPDetails(self.__context, self.__cardInfo)
            if scpDetails == -1:
                self.__handler.handleLog('doMutualAuth(): Get SCP data failed.')
            else:
                scp, scpi = scpDetails
                sencKey = '\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4A\x4B\x4C\x4D\x4E\x4F'
                smacKey = '\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4A\x4B\x4C\x4D\x4E\x4F'
                dekKey = '\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4A\x4B\x4C\x4D\x4E\x4F'
                kvn = 0
                self.__securityInfo = gp.mutualAuthentication(self.__context, self.__cardInfo, None, sencKey, smacKey, dekKey, kvn, 0, scp, scpi, 0, 0)
                self.__handler.handleLog('doMutualAuth(): Succeeded.')
        except Exception, e:
            self.__handler.handleException(e)

    def readCapFileInfo(self, capFilePath):
        try:
            self.__handler.handleLog('readCapFileInfo(): Start ...')
            capFileInfo = gp.readExecutableLoadFileParameters(capFilePath)
            self.__handler.handleCapFileInfo(capFileInfo)
            self.__handler.handleLog('readCapFileInfo(): Succeeded.')
        except Exception, e:
            self.__handler.handleException(e)
    
    def loadCapFile(self, capFilePath):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        if not self.__checkSecurityInfo(): return

        try:
            self.__handler.handleLog('loadCapFile(): Start ...')
            capFileInfo = gp.readExecutableLoadFileParameters(capFilePath)
            gp.installForLoad(self.__context, self.__cardInfo, self.__securityInfo, capFileInfo['loadFileAID'], gp.AID_ISD, '', '', 0, 0, 0)
            gp.load(self.__context, self.__cardInfo, self.__securityInfo, '', capFilePath)
            self.__handler.handleLog('loadCapFile(): Succeeded.')
        except Exception, e:
            self.__handler.handleException(e)
    
    def installApplet(self, packageAID, moduleAID, appletAID, privileges, installParameters):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        if not self.__checkSecurityInfo(): return

        try:
            self.__handler.handleLog('installApplet(): Start ...')
            gp.installForInstallAndMakeSelectable(self.__context, self.__cardInfo, self.__securityInfo, packageAID, moduleAID, appletAID, privileges, 0, 0, installParameters, '')
            self.__handler.handleLog('installApplet(): Succeeded.')
        except Exception, e:
            self.__handler.handleException(e)
            
    def getStatus(self):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        if not self.__checkSecurityInfo(): return

        try:
            self.__handler.handleLog('getStatus: Start ...')
            status80 = None
            status40 = None
            status20 = None
            status10 = None
            try:
                status80 = gp.getStatus(self.__context, self.__cardInfo, self.__securityInfo, 0x80)
            except:
                status80 = None
                pass
            try:
                status40 = gp.getStatus(self.__context, self.__cardInfo, self.__securityInfo, 0x40)
            except:
                status40 = None
                pass
            try:
                status20 = gp.getStatus(self.__context, self.__cardInfo, self.__securityInfo, 0x20)
            except:
                status20 = None
                pass
            try:
                status10 = gp.getStatus(self.__context, self.__cardInfo, self.__securityInfo, 0x10)
            except:
                status10 = None
                pass
            self.__handler.handleStatus({ 0x80 : status80, 0x40 : status40, 0x20 : status20, 0x10 : status10})
            self.__handler.handleLog('getStatus: succeeded.')
        except Exception, e:
            self.__handler.handleException(e)
    
    def selectApplication(self, instanceAID):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return

        try:
            self.__handler.handleLog('selectApplication: Start ...')
            gp.selectApplication(self.__context, self.__cardInfo, instanceAID)
            self.__handler.handleLog('selectApplication: succeeded.')
        except Exception, e:
            self.__handler.handleException(e)
    
    def deleteApplication(self, appAID):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        if not self.__checkSecurityInfo(): return

        try:
            self.__handler.handleLog('deleteApplication: Start ...')
            gp.deleteApplication(self.__context, self.__cardInfo, self.__securityInfo, (appAID, ))
            self.__handler.handleLog('deleteApplication: succeeded.')
        except Exception, e:
            self.__handler.handleException(e)
            
    def loadScript(self, scriptPathName):
        if not os.path.exists(scriptPathName):
            return
        
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        
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
    
    def getKeyTemplateInfo(self):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        if not self.__checkSecurityInfo(): return

        try:
            self.__handler.handleLog('getKeyTemplateInfo: Start ...')
            kits = gp.getKeyInformationTemplates(self.__context, self.__cardInfo, self.__securityInfo, 0)
            self.__handler.handleKeyInformationTemplates(kits)
            self.__handler.handleLog('getKeyTemplateInfo: succeeded.')
        except Exception, e:
            self.__handler.handleException(e)
            
    def putKey(self, oldKVN, newKVN, key1, key2, key3):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        if not self.__checkSecurityInfo(): return

        try:
            self.__handler.handleLog('putKey: Start ...')
            gp.putSCKey(self.__context, self.__cardInfo, self.__securityInfo, oldKVN, newKVN, None, key1, key2, key3)
            self.__handler.handleLog('putKey: succeeded.')
        except Exception, e:
            self.__handler.handleException(e)

    def deleteKey(self, keysInfo):
        if not self.__checkContext(): return
        if not self.__checkCardInfo(): return
        if not self.__checkSecurityInfo(): return

        for keyInfo in keysInfo:
            kvn = keyInfo[0]
            keyIndex = keyInfo[1]
            try:
                self.__handler.handleLog('deleteKey(%02X, %02X): Start ...' %(kvn, keyIndex))
                gp.deleteKey(self.__context, self.__cardInfo, self.__securityInfo, kvn, keyIndex)
                self.__handler.handleLog('deleteKey(%02X, %02X): succeeded.' %(kvn, keyIndex))
            except Exception, e:
                self.__handler.handleException(e)

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
    
    