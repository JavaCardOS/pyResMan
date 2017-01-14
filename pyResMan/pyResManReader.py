# -*- coding:utf8 -*-

'''
Created on 2015-10-28

@author: javacardos@gmail.com
@organization: http://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from smartcard.pcsc.PCSCReader import PCSCReader
from smartcard.ReaderMonitoring import ReaderObserver, ReaderMonitor
from smartcard.CardMonitoring import CardMonitor, CardObserver
from pyGlobalPlatform import globalplatformlib as gp

class pyResManReader(object):
    '''
    classdocs
    '''
    
    """
        WinSCard.h
        //
        ////////////////////////////////////////////////////////////////////////////////
        //
        //  Smart Card Database Management Services
        //
        //      The following services provide for managing the Smart Card Database.
        //
        
        #define SCARD_ALL_READERS       TEXT("SCard$AllReaders\000")
        #define SCARD_DEFAULT_READERS   TEXT("SCard$DefaultReaders\000")
        #define SCARD_LOCAL_READERS     TEXT("SCard$LocalReaders\000")
        #define SCARD_SYSTEM_READERS    TEXT("SCard$SystemReaders\000")
        
        #define SCARD_PROVIDER_PRIMARY  1   // Primary Provider Id
        #define SCARD_PROVIDER_CSP      2   // Crypto Service Provider Id
        #define SCARD_PROVIDER_KSP      3   // Key Storage Provider Id
    """
    SCARD_ALL_READERS       = "SCard$AllReaders\000"
    SCARD_DEFAULT_READERS   = "SCard$DefaultReaders\000"
    SCARD_LOCAL_READERS     = "SCard$LocalReaders\000"
    SCARD_SYSTEM_READERS    = "SCard$SystemReaders\000"
    
    SCARD_PROVIDER_PRIMARY  = 1
    SCARD_PROVIDER_CSP      = 2
    SCARD_PROVIDER_KSP      = 3
    
    STATUS_CONNECTED = 1
    STATUS_DISCONNECTED = 2

    """
        WinSCard.h
        //
        ////////////////////////////////////////////////////////////////////////////////
        //
        //  Card/pyResManReader Communication Services
        //
        //      The following services provide means for communication with the card.
        //
        
        #define SCARD_SHARE_EXCLUSIVE 1 // This application is not willing to share this
                                        // card with other applications.
        #define SCARD_SHARE_SHARED    2 // This application is willing to share this
                                        // card with other applications.
        #define SCARD_SHARE_DIRECT    3 // This application demands direct control of
                                        // the reader, so it is not available to other
                                        // applications.
        
        #define SCARD_LEAVE_CARD      0 // Don't do anything special on close
        #define SCARD_RESET_CARD      1 // Reset the card on close
        #define SCARD_UNPOWER_CARD    2 // Power down the card on close
        #define SCARD_EJECT_CARD      3 // Eject the card on close
    """
    
    SCARD_SHARE_EXCLUSIVE = 1
    SCARD_SHARE_SHARED = 2
    SCARD_SHARE_DIRECT = 3

    SCARD_PROTOCOL_UNDEFINED = 0x00000000
    SCARD_PROTOCOL_T0 = 0x00000001
    SCARD_PROTOCOL_T1 = 0x00000002
    SCARD_PROTOCOL_RAW = 0x00010000
    
    def __init__(self):
        '''
        Constructor
        '''
        self.readername = ''
        self.reader = None
        self.readerConnection = None
        self.readerObserver = None
        self.readerMonitor = None
        self.readerMonitorHandlers = []
        self.status = pyResManReader.STATUS_DISCONNECTED

        self.cardObserver = None
        self.cardMonitor = None
        self.cardMonitorHandlers = []
    
    @staticmethod
    def getReaderList():
        readernames = []
        c = gp.establishContext()
        for reader in gp.listReaders(c):
            readernames.append(str(reader))
        gp.releaseContext(c)
        return readernames
    
    def getName(self):
        return self.readername
    
    def connect(self, readername, protocol, mode):
        self.readername = readername
        self.reader = PCSCReader(readername)
        self.readerConnection = self.reader.createConnection()
        self.readerConnection.connect(protocol, mode)
        self.status = pyResManReader.STATUS_CONNECTED
    
    def getatr(self):
        return self.readerConnection.getATR()
    
    def getStatus(self):
        return self.status
    
    def getProtocol(self):
        protocol = self.readerConnection.getProtocol()
        if protocol == self.readerConnection.T0_protocol:
            return pyResManReader.SCARD_PROTOCOL_T0
        elif protocol == self.readerConnection.T1_protocol:
            return pyResManReader.SCARD_PROTOCOL_T1
        else:
            raise NotImplementedError
    
    def disconnect(self):
        self.readerConnection.disconnect()
        self.readerConnection = None
        self.reader = None
        self.readername = None
        self.status = pyResManReader.STATUS_DISCONNECTED
    
    def transmit(self, cmd):
        return self.readerConnection.transmit(cmd, self.readerConnection.getProtocol())
        
    class __ReaderObserver(ReaderObserver):
        def __init__(self, monitorHandlers):
            self.monitorHandlers = monitorHandlers
        
        def notifyEvent(self, event, args):
            for monitorHandler in self.monitorHandlers:
                monitorHandler.handleReaderEvent(event, args)
         
        def update(self, observable, (addedreaders, removedreaders)):
            if len(addedreaders) != 0:
                self.notifyEvent(IReaderMonitorEventHandler.MONITOR_EVENT_ADDED, addedreaders)
            if len(removedreaders) != 0:
                self.notifyEvent(IReaderMonitorEventHandler.MONITOR_EVENT_REMOVED, removedreaders)
        
    def monitorReaders(self):
        if self.readerMonitor == None:
            self.readerMonitor = ReaderMonitor()
            self.readerObserver = pyResManReader.__ReaderObserver(self.readerMonitorHandlers)
            self.readerMonitor.addObserver(self.readerObserver)
    
    def addReaderMonitorHandler(self, monitorHandler):
        self.readerMonitorHandlers.append(monitorHandler)
    
    def removeReaderMonitorHandler(self, monitorHandler):
        self.readerMonitorHandlers.remove(monitorHandler)
    
    def stopReaderMonitor(self):
        self.readerMonitor.deleteObserver(self.readerObserver)
        self.readerMonitor = None
        self.readerObserver = None

    class __CardObserver(CardObserver):
        def __init__(self, readername, monitorHandlers):
            self.readername = readername
            self.monitorHandlers = monitorHandlers
         
        def handleEvent(self, event, args):
            for monitorHandler in self.monitorHandlers:
                monitorHandler.handleCardEvent(event, args)
            
        def update(self, observable, (addedcards, removedcards)):
            for addedcard in addedcards:
                if addedcard.reader == self.readername:
                    self.handleEvent(ICardMonitorEventHandler.MONITOR_EVENT_INSERT, (self.readername))
            for removedCard in removedcards:
                if removedCard.reader == self.readername:
                    self.handleEvent(ICardMonitorEventHandler.MONITOR_EVENT_REMOVE, (self.readername))
    
    def monitorCard(self, readername):
        if (self.cardMonitor == None):
            self.cardMonitor = CardMonitor()
        if self.cardObserver == None:
            self.cardObserver = pyResManReader.__CardObserver(readername, self.cardMonitorHandlers)
        self.cardMonitor.addObserver(self.cardObserver)
    
    def addCardMonitorHandler(self, monitorHandler):
        if not monitorHandler in self.cardMonitorHandlers:
            self.cardMonitorHandlers.append(monitorHandler)
    
    def removeCardMonitorHandler(self, monitorHandler):
        if monitorHandler in self.cardMonitorHandlers:
            self.cardMonitorHandlers.remove(monitorHandler)
    
    def stopCardMonitor(self):
        self.cardMonitor.deleteObserver(self.cardObserver)
        self.cardMonitor = None
        self.cardObserver = None
    
class IReaderMonitorEventHandler(object):
    MONITOR_EVENT_ADDED = 0xDEAD
    MONITOR_EVENT_REMOVED = 0xDEEE
    
    def handleReaderEvent(self, eventType, args=()):
        pass

class ICardMonitorEventHandler(object):
    MONITOR_EVENT_INSERT = 0xCDAD
    MONITOR_EVENT_REMOVE = 0xCDEE
    
    def handleCardEvent(self, eventType, args=()):
        pass
