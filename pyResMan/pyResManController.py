# -*- coding:utf8 -*-

'''
Created on 2015-10-30

@author: javacardos@gmail.com
@organization: http://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from pyResManReader import pyResManReader, ICardMonitorEventHandler, IReaderMonitorEventHandler
from Util import Util
import timeit
import threading

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
        self.__reader = pyResManReader()
        self.__handler = handler
        self.__reader.addReaderMonitorHandler(self)
        self.__reader.monitorReaders()
        self.__runScriptThread = None
    
    def getReaderList(self):
        return self.__reader.getReaderList()
    
    def connect(self, readername, protocol, mode):
        """ Connect to the reader;"""
        self.__handler.handleLog('Connect to %s.' %(readername))
        self.__reader.connect(readername, protocol, mode)
        self.__handler.handleLog('Connected.')

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
        self.__reader.monitorCard()

    def disconnect(self):
        self.__reader.disconnect()
        self.__reader.removeCardMonitorHandler(self)
        self.__reader.stopCardMonitor()
        self.__handler.handleLog('Disconnected.')
    
    def __transmit(self, args):
        """Thread method to transmit an apdu;"""
        cmd = args[0]
        t0AutoGetResponse = args[1]
        handlerArgs = args[2]
        
        try:
            commandValue = Util.s2vl(cmd)
            if not self.__reader:
                raise Exception("Please connect first.")
            if self.__reader.getStatus() == pyResManReader.STATUS_DISCONNECTED:
                raise Exception("Please connect first.")
            
            self.__handler.handleAPDUCommand("".join("%02X " %(vb) for vb in commandValue), handlerArgs)
            timeStart = timeit.default_timer()
            rsp = self.__reader.transmit(commandValue)
            timeStop = timeit.default_timer()
            transtime = timeStop - timeStart
            rspValue = list(rsp[0])
            rspValue.append(rsp[1])
            rspValue.append(rsp[2])
            self.__handler.handleAPDUResponse("".join("%02X " %(vb) for vb in rspValue), transtime, handlerArgs)
            
            if (self.__reader.getProtocol() == pyResManReader.SCARD_PROTOCOL_T0) and t0AutoGetResponse and (rsp[1] == 0x61) and (len(handlerArgs) == 0):
                cmd = [0x00, 0xC0, 0x00, 0x00, rsp[2]]
                self.__handler.handleAPDUCommand("".join("%02X " %(vb) for vb in cmd))
                timeStart = timeit.default_timer()
                rsp = self.__reader.transmit(cmd)
                timeStop = timeit.default_timer()
                transtime = timeStop - timeStart
                rspValue = list(rsp[0])
                rspValue.append(rsp[1])
                rspValue.append(rsp[2])
                self.__handler.handleAPDUResponse("".join("%02X " %(vb) for vb in rspValue), transtime)
        except Exception, e:
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