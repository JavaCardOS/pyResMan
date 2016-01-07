# -*- coding:utf8 -*-

'''
Created on 2015-10-27

@author: javacardos@gmail.com
@organization: http://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from wx import ListItem,  TreeItemId, TreeItemData
from pyResManReader import pyResManReader
from smartcard.Exceptions import NoCardException
from pyResManController import pyResManController, APDUItem
import os
from Util import Util
from datetime import datetime
from pyResManInstallDialog import pyResManInstallDialog
from pyResManDialogBase import pyResManDialogBase
import wx
import threading
import time

class pyResManDialog ( pyResManDialogBase ):
    
    def __init__(self, parent):
        pyResManDialogBase.__init__(self, parent)
        
        readernames = pyResManReader.getReaderList()
        if len(readernames) > 0:
            for readername in readernames:
                self._readernameComboBox.Insert(readername, self._readernameComboBox.GetCount())
            self._readernameComboBox.Select(0)
        
        self.__controller = pyResManController(self)
        
        self._claTextCtrl.SetValue('00')
        self._insTextCtrl.SetValue('A4')
        self._p1TextCtrl.SetValue('04')
        self._p2TextCtrl.SetValue('00')
        self._leTextCtrl.SetValue('00')
        
        self._scriptListCtrl.InsertColumn(0, 'Index', width=50)
        self._scriptListCtrl.InsertColumn(1, 'Command', width=200)
        self._scriptListCtrl.InsertColumn(2, 'Response', width=300)
        self._scriptListCtrl.InsertColumn(3, 'TimeSpent', width=100)
        self._scriptListCtrl.InsertColumn(4, 'DateTime', width=120)

        self._keyDataListCtrl.InsertColumn(0, 'index', width=50)
        self._keyDataListCtrl.InsertColumn(1, 'KVN', width=100)
        self._keyDataListCtrl.InsertColumn(2, 'key index', width=100)
        self._keyDataListCtrl.InsertColumn(3, 'key type', width=100)
        self._keyDataListCtrl.InsertColumn(4, 'key length', width=100)

        self._apduListCtrl.InsertColumn(0, 'Index', width=50)
        self._apduListCtrl.InsertColumn(1, 'Command', width=200)
        self._apduListCtrl.InsertColumn(2, 'Response', width=300)
        self._apduListCtrl.InsertColumn(3, 'TimeSpent', width=100)
        self._apduListCtrl.InsertColumn(4, 'DateTime', width=120)
        
        defaultKeyValue = '404142434445464748494A4B4C4D4E4F'
        self._key1TextCtrl.SetValue(defaultKeyValue)
        self._key2TextCtrl.SetValue(defaultKeyValue)
        self._key3TextCtrl.SetValue(defaultKeyValue)
        self._oldKVNTextCtrl.SetValue('00')
        self._newKVNTextCtrl.SetValue('01')
        
        self._apduListCtrl.Bind(wx.EVT_CONTEXT_MENU, self._apduListCtrlOnContextMenu)
        self._scriptListCtrl.Bind(wx.EVT_CONTEXT_MENU, self._scriptListCtrlOnContextMenu)
        
        
    # Virtual event handlers, overide them in your derived class
    def _connectButtonOnButtonClick( self, event ):
        self._connectButton.Disable()
        if (self._connectButton.GetLabelText() == 'Connect'):
            try:
                # Get smartcard reader name;
                readername = self._readernameComboBox.GetString(self._readernameComboBox.GetSelection())
                protocolIndex = self._protocolComboBox.GetSelection()
                
                # Get protocol value;
                protocol = pyResManReader.SCARD_PROTOCOL_T0 | pyResManReader.SCARD_PROTOCOL_T1
                if protocolIndex == 0:
                    protocol = pyResManReader.SCARD_PROTOCOL_T0
                elif protocolIndex == 1:
                    protocol = pyResManReader.SCARD_PROTOCOL_T1
                
                # Get mode value;
                modeIndex = self._modeComboBox.GetSelection()
                mode = pyResManReader.SCARD_SHARE_SHARED
                if modeIndex == 0:
                    mode = pyResManReader.SCARD_SHARE_EXCLUSIVE

                # Connect to the card;
                # Set AutoResponse when connect with protocol T0;
                if (protocol == pyResManReader.SCARD_PROTOCOL_T0):
                    self._autoGetResponseCheckBox.SetValue(True)
                
                self.__controller.connect(readername, protocol, mode)
                self.__controller.monitorCard()
                
                # Set status;
                self._connectButton.SetLabel('Disconnect')
                self._Log('Connected.', wx.LOG_Info)
            except NoCardException, e:
                self._Log('NoCardException: ' + e.args[1], wx.LOG_Error)
            except Exception, e:
                self._Log('Exception: ' + str(e), wx.LOG_Error)
        else:
            try:
                # Disconnect;
                self.__controller.disconnect()
                
                # Set status;
                self._connectButton.SetLabel('Connect')
                self._Log('Disconnected.', wx.LOG_Info)
            except NoCardException, e:
                self._Log('NoCardException: %s' %(e.args[1]), wx.LOG_Error)
            except Exception, e:
                self._Log('Exception: ' %(str(e)), wx.LOG_Error)
        self._connectButton.Enable()

    def _claTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _insTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _p1TextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _p2TextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()

    def _dataTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()

    def _dataTextCtrlOnText( self, event ):
        dataLen = len(self._dataTextCtrl.GetValue())
        if dataLen & 0x01 != 0:
            self._dataTextCtrl.SetBackgroundColour('#FF6347')
        else:
            self._dataTextCtrl.SetBackgroundColour('WHITE')
        self._dataTextCtrl.Refresh()
        dataLen = dataLen / 2
        self._lcTextCtrl.SetValue("%02X" %(dataLen))
    
    def _leTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _transmitButtonOnButtonClick( self, event ):
        cls = self._claTextCtrl.GetValue()
        ins = self._insTextCtrl.GetValue()
        p1 = self._p1TextCtrl.GetValue()
        p2 = self._p2TextCtrl.GetValue()
        lc = self._lcTextCtrl.GetValue()
        data = self._dataTextCtrl.GetValue()
        le = self._leTextCtrl.GetValue()
        
        if (len(cls) == 0) or (len(ins) == 0) or (len(p1) == 0) or (len(p2) == 0):
            self._Log('Please input command field.', wx.LOG_Warning)
            return
        
        commandText = ''
        if lc != '00':
            commandText = "%s%s%s%s%s %s %s" %(cls, ins, p1, p2, lc, data, le)
        else:
            commandText = "%s%s%s%s %s" %(cls, ins, p1, p2, le)            
        
        # Get t0 auto getresponse value;
        autoGetResponse = self._autoGetResponseCheckBox.GetValue()
        
        # Transmit;
        self.__controller.transmit(commandText, autoGetResponse, (self._apduListCtrl, ))
        
    def _scpinfoMethodOnRadioBox( self, event ):
        event.Skip()
        
        if self._scpinfoMethod.GetSelection() == 0:
            self._scpChoice.Enable(False)
            self._scpiTextCtrl.Enable(False)
        else:
            self._scpChoice.Enable(True)
            self._scpiTextCtrl.Enable(True)
    
    def _scpiTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()

    def _mutualAuthButtonOnButtonClick( self, event ):
        scp = -1
        scpi = -1
        if self._scpinfoMethod.GetSelection() == 1:
            scp = self._scpChoice.GetSelection() + 1
            scpi = int(self._scpiTextCtrl.GetValue(), 0x10)
        key1 = Util.s2vs(self._key1TextCtrl.GetValue())
        key2 = Util.s2vs(self._key2TextCtrl.GetValue())
        key3 = Util.s2vs(self._key3TextCtrl.GetValue())
        self.__controller.doMutualAuth(scp, scpi, key1, key2, key3)
    
    def _capFilePickerOnFileChanged( self, event ):
        self._loadButton.Disable()
        self._installButton.Disable()
        self._capFileInformationTreeCtrl.DeleteAllItems()
        capFilePath = self._capFilePicker.GetPath()
        self.__controller.readCapFileInfo(capFilePath)
    
    def _loadButtonOnButtonClick( self, event ):
        capFilePath = self._capFilePicker.GetPath()
        self.__controller.loadCapFile(capFilePath)
    
    def _installButtonOnButtonClick( self, event ):
        appletItem = self._capFileInformationTreeCtrl.GetSelection()
        appletData = self._capFileInformationTreeCtrl.GetItemData(appletItem)
        if appletData.GetData()['type'] != 'applet':
            self._Log('Please select the applet item to install.', wx.LOG_Warning)
            return
        
        packageItem = self._capFileInformationTreeCtrl.GetItemParent(appletItem)
        packageData = self._capFileInformationTreeCtrl.GetItemData(packageItem)
        if packageData.GetData()['type'] != 'package':
            self._Log('Invalid selected item.', wx.LOG_Warning)
            return

        packageAID = packageData.GetData()['aid']
        appletAID = appletData.GetData()['aid']
        instanceAID = appletAID
        
        installDialog = pyResManInstallDialog(self)
        installDialog.setPackageAID(packageAID)
        installDialog.setAppletAID(appletAID)
        installDialog.setInstanceAID(instanceAID)
        ret = installDialog.ShowModal()
        if ret == wx.ID_OK:
            packageAID = installDialog.getPackageAID()
            appletAID = installDialog.getAppletAID()
            instanceAID = installDialog.getInstanceAID()
            privileges = installDialog.getPrivileges()
            installParameters = installDialog.getInstallParameters()
            self.__controller.installApplet(packageAID, appletAID, instanceAID, privileges, installParameters)
        else:
            pass

    def _contentTreeCtrlOnTreeSelChanged( self, event ):
        event.Skip()
        self._installCardContent.Enable(False)
        self._selectCardContent.Enable(False)
        self._deleteCardContent.Enable(True)
        selectedId = self._contentTreeCtrl.GetSelection();
        selectedItemData = self._contentTreeCtrl.GetItemData(selectedId)
        if selectedItemData == None:
            return
        itemData = selectedItemData.GetData()
        itemType = itemData['type']
        if itemType == 'applet':
            self._deleteCardContent.Enable(False)
            
            parentId = self._contentTreeCtrl.GetItemParent(selectedId)
            parentItemData = self._contentTreeCtrl.GetItemData(parentId)
            parentData = parentItemData.GetData()
            if parentData['type'] == 'package':
                self._installCardContent.Enable()
        elif itemType == 'instance':
            self._selectCardContent.Enable()
        
    def _refreshCardContentOnButtonClick( self, event ):
        event.Skip()
        self.__controller.getStatus()
    
    def _installCardContentOnButtonClick( self, event ):
        selectedId = self._contentTreeCtrl.GetSelection();
        selectedItemData = self._contentTreeCtrl.GetItemData(selectedId)
        if selectedItemData.GetData()['type'] != 'applet':
            return
        parentId = self._contentTreeCtrl.GetItemParent(selectedId)
        parentItemData = self._contentTreeCtrl.GetItemData(parentId)
        if parentItemData.GetData()['type'] != 'package':
            return
        packageAID = parentItemData.GetData()['aid']
        appletAID = selectedItemData.GetData()['aid']
        instanceAID = appletAID
        installDialog = pyResManInstallDialog(self)
        installDialog.setPackageAID(packageAID)
        installDialog.setAppletAID(appletAID)
        installDialog.setInstanceAID(instanceAID)
        ret = installDialog.ShowModal()
        if ret == wx.ID_OK:
            packageAID = installDialog.getPackageAID()
            appletAID = installDialog.getAppletAID()
            instanceAID = installDialog.getInstanceAID()
            privileges = installDialog.getPrivileges()
            installParameters = installDialog.getInstallParameters()
            self.__controller.installApplet(packageAID, appletAID, instanceAID, privileges, installParameters)
        else:
            pass

    def _selectCardContentOnButtonClick( self, event ):
        event.Skip()
        
        self._selectCardContent.Disable()
        
        selectedId = self._contentTreeCtrl.GetSelection();
        selectedItemData = self._contentTreeCtrl.GetItemData(selectedId)
        itemData = selectedItemData.GetData()
        itemType = itemData['type']
        if itemType != 'instance':
            return
        instanceAID = itemData['aid']
        self.__controller.selectApplication(instanceAID)

    def _deleteCardContentOnButtonClick( self, event ):
        selectedItem = self._contentTreeCtrl.GetSelection()
        if selectedItem.IsOk():
            selectedItemData = self._contentTreeCtrl.GetItemData(selectedItem)
            aid = selectedItemData.GetData()['aid']
            self.__controller.deleteApplication(aid)
        event.Skip()
    
    def _keyDataListCtrlOnListItemSelected( self, event ):
        event.Skip()
        
        item = event.GetItem()
        kvn = self._keyDataListCtrl.GetItemText(item.GetId(), 1)
        if kvn == 'FF':
            self._oldKVNTextCtrl.SetValue('0')
            self._newKVNTextCtrl.SetValue('1')
        else:
            self._oldKVNTextCtrl.SetValue(kvn)
            self._newKVNTextCtrl.SetValue(kvn)

    def _key1TextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _key1TextCtrlOnText( self, event ):
        event.Skip()
        keyStrLen = len(self._key1TextCtrl.GetValue())
        self._keyLen1TextCtrl.SetValue('%02X' %(keyStrLen / 2))
        if (keyStrLen & 1) != 0:
            self._key1TextCtrl.SetBackgroundColour('#FF6347')
        else:
            self._key1TextCtrl.SetBackgroundColour('WHITE')
        self._key1TextCtrl.Refresh()
    
    def _key2TextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _key2TextCtrlOnText( self, event ):
        event.Skip()
        keyStrLen = len(self._key2TextCtrl.GetValue())
        self._keyLen2TextCtrl.SetValue('%02X' %(keyStrLen / 2))
        if (keyStrLen & 1) != 0:
            self._key2TextCtrl.SetBackgroundColour('#FF6347')
        else:
            self._key2TextCtrl.SetBackgroundColour('WHITE')
        self._key2TextCtrl.Refresh()
    
    def _key3TextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _key3TextCtrlOnText( self, event ):
        event.Skip()
        keyStrLen = len(self._key3TextCtrl.GetValue())
        self._keyLen3TextCtrl.SetValue('%02X' %(keyStrLen / 2))
        if (keyStrLen & 1) != 0:
            self._key3TextCtrl.SetBackgroundColour('#FF6347')
        else:
            self._key3TextCtrl.SetBackgroundColour('WHITE')
        self._key3TextCtrl.Refresh()
    
    def _oldKVNTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _oldKVNTextCtrlOnText( self, event ):
        event.Skip()
        kvn = int(self._oldKVNTextCtrl.GetValue(), 0x10)
        self._oldKVNTextCtrl.SetBackgroundColour('WHITE')
        if not ((kvn >= 0) and (kvn <= 0x7F)): 
            self._oldKVNTextCtrl.SetBackgroundColour('#FF6347')
        self._oldKVNTextCtrl.Refresh()

    def _newKVNTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _newKVNTextCtrlOnText( self, event ):
        event.Skip()
        kvn = int(self._newKVNTextCtrl.GetValue(), 0x10)
        self._newKVNTextCtrl.SetBackgroundColour('WHITE')
        if not ((kvn >= 1) and (kvn <= 0x7F)): 
            self._newKVNTextCtrl.SetBackgroundColour('#FF6347')
        self._newKVNTextCtrl.Refresh()

    
    def _putKeyButtonOnButtonClick( self, event ):
        event.Skip()
        
        if self._oldKVNTextCtrl.IsEmpty():
            self._Log('Please input the old key version number.', wx.LOG_Warning)
            self._oldKVNTextCtrl.SetBackgroundColour('#FF6347')
            self._oldKVNTextCtrl.Refresh()
            return
        if self._newKVNTextCtrl.IsEmpty():
            self._Log('Please input the new key version number.', wx.LOG_Warning)
            self._newKVNTextCtrl.SetBackgroundColour('#FF6347')
            self._newKVNTextCtrl.Refresh()
            return
        
        oldKVN = int(self._oldKVNTextCtrl.GetValue(), 0x10)
        newKVN = int(self._newKVNTextCtrl.GetValue(), 0x10)
        
        key1 = Util.s2vs(self._key1TextCtrl.GetValue())
        key2 = Util.s2vs(self._key2TextCtrl.GetValue())
        key3 = Util.s2vs(self._key3TextCtrl.GetValue())
        self.__controller.putKey(oldKVN, newKVN, key1, key2, key3)

    def _deleteKeyButtonOnButtonClick( self, event ):
        event.Skip()

        keysInfo = []
        i = self._keyDataListCtrl.GetFirstSelected()
        while i != -1:
            kvn = int(self._keyDataListCtrl.GetItemText(i, 1), 0x10)
            keyIndex = int(self._keyDataListCtrl.GetItemText(i, 2), 0x10)
            keysInfo.append((kvn, keyIndex, ))
            i = self._keyDataListCtrl.GetNextSelected(i)
        self.__controller.deleteKey(keysInfo)
    
    def _getKeyTemplateInfoButtonOnButtonClick( self, event ):
        event.Skip()
        self.__controller.getKeyTemplateInfo()
    
    def _resetKeyButtonOnButtonClick( self, event ):
        event.Skip()
        defaultKey = '404142434445464748494A4B4C4D4E4F'
        self._key1TextCtrl.SetValue(defaultKey)
        self._key2TextCtrl.SetValue(defaultKey)
        self._key3TextCtrl.SetValue(defaultKey)

    def _scriptLoopCountTextCtrlOnChar( self, event ):
        if Util.isnumchar_kc(event.KeyCode):
            event.Skip()
        else:
            pass

    def _loadScript(self):
        scriptPathName = self._scriptFilePicker.GetPath()
        if os.path.exists(scriptPathName):
            self.__controller.loadScript(scriptPathName)
    
    def _scriptFilePickerOnFileChanged( self, event ):
        event.Skip()
        self._loadScript()
    
    def _scriptRefreshButtonOnButtonClick( self, event ):
        event.Skip()
        self._loadScript()
    
    def _scriptRunButtonOnButtonClick( self, event ):
        event.Skip()
        apduItems = []
        itemCount = self._scriptListCtrl.GetItemCount()
        for itemIndex in xrange(itemCount):
            listItem = self._scriptListCtrl.GetItem(itemIndex, 1)
            apduItem = APDUItem(listItem.GetText(), (self._scriptListCtrl, listItem.GetId()))
            apduItems.append(apduItem)
        
        t0AutoGetResponse = self._autoGetResponseCheckBox.GetValue()
        loopCount = int(self._scriptLoopCountTextCtrl.GetValue())
        self.__controller.transmitAPDUItems(apduItems, t0AutoGetResponse, loopCount)
    
    def _scriptClearResultButtonOnButtonClick( self, event ):
        event.Skip()
        self._scriptListCtrl.DeleteAllItems()
        self._loadScript()
    
    def m_splitter2OnIdle( self, event ):
        self.m_splitter2.SetSashPosition( 0 )
        self.m_splitter2.Unbind( wx.EVT_IDLE )
    
    def _apduListCtrlOnContextMenu(self, event):
        """Display apdu list view popup menu;"""
        self._apduListCtrlPopupMenu = wx.Menu()
        self._apduListCtrlPopupMenu.Append(1, "Run")
        self._apduListCtrlPopupMenu.AppendSeparator()
        self._apduListCtrlPopupMenu.Append(0, "Clear")
        self._apduListCtrlPopupMenu.Bind(wx.EVT_MENU, self._listCtrlOnContextMenuClick)
        self._apduListCtrl.PopupMenu(self._apduListCtrlPopupMenu)

    def _scriptListCtrlOnContextMenu(self, event):
        """Display apdu list view popup menu;"""
        self._scriptListCtrlPopupMenu = wx.Menu()
        self._scriptListCtrlPopupMenu.Append(1, "Run")
        self._scriptListCtrlPopupMenu.AppendSeparator()
        self._scriptListCtrlPopupMenu.Append(0, "Clear")
        self._scriptListCtrlPopupMenu.Bind(wx.EVT_MENU, self._listCtrlOnContextMenuClick)
        self._scriptListCtrl.PopupMenu(self._scriptListCtrlPopupMenu)
    
    def _listCtrlOnContextMenuClick(self, event):
        menuItemIndex = event.Id
        theListCtrl = event.GetEventObject().GetInvokingWindow()
        if menuItemIndex == 0:
            theListCtrl.DeleteAllItems()
            # Load script again;
            if theListCtrl == self._scriptListCtrl:
                self._loadScript()
        elif menuItemIndex == 1:
            self._listCtrlRunSelectedItems(theListCtrl)
# 
#     def _onLogTextCtrl_MenuClick(self, event):
#         menuItemIndex = event.Id
#         if menuItemIndex == 0:
#             self._logTextCtrl.Clear()
    
    def _listCtrlRunSelectedItems(self, listCtrl):
        """Transmit selected items apdu in the apdu list view;"""
        apduItems = []
        selectedItem = listCtrl.GetFirstSelected()
        while (selectedItem != -1):
            listItem = listCtrl.GetItem(selectedItem, 1)
            apduItem = APDUItem(listItem.GetText(), (listCtrl, selectedItem))
            apduItems.append(apduItem)
            selectedItem = listCtrl.GetNextSelected(selectedItem)
        
        t0AutoGetResponse = self._autoGetResponseCheckBox.GetValue()
        self.__controller.transmitAPDUItems(apduItems, t0AutoGetResponse, 1)
    
    def _onEventButton(self, event):
        controlId = event.Id
        if (controlId == self._connectButton.Id):
            self._onConnect()
        elif (controlId == self._transmitButton.Id):
            self._onTransmit()
        elif (controlId == self._scriptBrowseButton.Id):
            self._onBrowseScriptFile()
        elif (controlId == self._scriptRunScriptButton.Id):
            self._onRunScript()
    
    def _InitController(self):
        """Init controller for logical operations, self as the view;"""
        self.__controller = pyResManController(self)
    
    def handleCardRemoved(self, name):
        self._Log('Card is removed.', wx.LOG_Warning)
        self._connectButton.SetLabel('Connect')

    def handleCardInserted(self, name):
        pass
    
    def _relistReaders(self):
        """Relist reader names, when reader added/removed;"""
        readers = self.__controller.getReaderList()
        self._readernameComboBox.Clear()
        for reader in readers:
            self._readernameComboBox.Append(reader)
        self._readernameComboBox.SetSelection(0)

    def handleReaderAdded(self, name):
        self._relistReaders()
    
    def handleReaderRemoved(self, name):
        self._relistReaders()
    
    def _onBrowseScriptFile(self):
        defaultDir = self._scriptPathNameEditor.GetValue()
        if not os.path.exists(defaultDir):
            defaultDir = os.getcwd()
        fileDialog = wx.FileDialog(self, defaultDir = defaultDir)
        ret = fileDialog.ShowModal()
        if (ret != wx.ID_CANCEL):
            filepath = fileDialog.GetPath()
            self._scriptPathNameEditor.SetValue(filepath)
        else:
            pass
    
    def _onRunScript(self):
        if (not self.__controller.runningScript()):
            scriptPathName = self._scriptPathNameEditor.GetValue()
            if not os.path.exists(scriptPathName):
                self._onBrowseScriptFile()
                scriptPathName = self._scriptPathNameEditor.GetValue()
            if not os.path.exists(scriptPathName):
                self._Log('User cancel operation.', wx.LOG_Info)
                return
    
            # Get t0 auto getresponse value;
            autoGetResponse = self._autoGetResponseCheckBox.GetValue()
            # Get loop count;
            scriptLoopCount = self._scriptLoopCountEditor.GetValue()
    
            self.__controller.runScript(scriptPathName, scriptLoopCount, autoGetResponse)
        else:
            self.__controller.stopScript()
    
    def handleAPDUCommand(self, commandStr, args=tuple()):
        """Handle controller's apdu command event, to display apdu command;"""
        theListCtrl = args[0]
         
        itemIndex = 0
        if len(args) == 1:
            itemIndex = theListCtrl.GetItemCount()
            indexItem = ListItem()
            indexItem.SetId(itemIndex)
            indexItem.SetColumn(0)
            indexItem.SetText('> %d' %(itemIndex))
            theListCtrl.InsertItem(indexItem)
        else:
            itemIndex = args[1]
            indexItem = ListItem()
            indexItem.SetId(itemIndex)
            indexItem.SetColumn(0)
            indexItem.SetText('> %d' %(itemIndex))
            theListCtrl.SetItem(indexItem)
        
        commandItem = ListItem()
        commandItem.SetId(itemIndex)
        commandItem.SetColumn(1)
        commandItem.SetText(commandStr)
        theListCtrl.SetItem(commandItem)

        datetimeItem = ListItem()
        datetimeItem.SetId(itemIndex)
        datetimeItem.SetColumn(4)
        datetimeItem.SetText(datetime.now().strftime("%c"))
        theListCtrl.SetItem(datetimeItem)
        
        theListCtrl.EnsureVisible(itemIndex)
    
    def handleAPDUResponse(self, responseStr, transtime, args=tuple()):
        """Handle controller's apdu response event, to display apdu result informations;"""
        theListCtrl = args[0]

        itemIndex = 0
        if len(args) == 1:
            itemIndex = theListCtrl.GetItemCount() - 1
        else:
            itemIndex = args[1]
        responseItem = ListItem()
        responseItem.SetId(itemIndex)
        responseItem.SetColumn(2)
        responseItem.SetText(responseStr)
        theListCtrl.SetItem(responseItem)

        timeItem = ListItem()
        timeItem.SetId(itemIndex)
        timeItem.SetColumn(3)
        timeItem.SetText(Util.getTimeStr(transtime))
        theListCtrl.SetItem(timeItem)

        indexItem = ListItem()
        indexItem.SetId(itemIndex)
        indexItem.SetColumn(0)
        indexItem.SetText('%d' %(itemIndex))
        theListCtrl.SetItem(indexItem)

        theListCtrl.EnsureVisible(itemIndex)

    def _Log(self, msg, level=wx.LOG_Message):
        """Display log with levels"""
        if msg.endswith('\r'):
            msg= msg[ : len(msg) - 1]
        if msg.endswith('\n'):
            msg= msg[ : len(msg) - 1]
        
        textColor = "#000000"
        if level == wx.LOG_Info:
            textColor = "#228B22"
        elif level == wx.LOG_Error:
            textColor = "#FF0000"
        elif level == wx.LOG_Warning:
            textColor = "#D2691E"
        elif level == wx.LOG_Message:
            pass
        else:
            pass

        self._logTextCtrl.SetDefaultStyle(wx.TextAttr(colText=textColor))
        self._logTextCtrl.AppendText(msg + '\n')
        curSelTo = self._logTextCtrl.GetSelection()[1]
        self._logTextCtrl.ShowPosition(curSelTo)
    
    def handleLog(self, msg, level=wx.LOG_Message):
        self._Log(msg, level)
    
    def handleScriptBegin(self, status):
        self._scriptRunScriptButton.SetLabel('Stop')

    def handleScriptEnd(self, status):
        self._scriptRunScriptButton.SetLabel('Start')

    def handleException(self, e):
        try:
            self._Log('Exception: %s' %(e.message), wx.LOG_Error)
        except:
            try:
                self._Log('Exception: %s' %(str(e)), wx.LOG_Error)
            except:
                self._Log('Transmit exceptin occured.', wx.LOG_Error)

    def handleCapFileInfo(self, info):
        self._capFileInformationTreeCtrl.DeleteAllItems()
        tr = self._capFileInformationTreeCtrl.AddRoot(self._capFilePicker.GetPath())
        packageAID = info['loadFileAID']
        ti = self._capFileInformationTreeCtrl.InsertItem(tr, TreeItemId(), "".join("%02X" %(ord(c)) for c in packageAID), data=TreeItemData({ 'type' : 'package', 'aid' : packageAID }))
        tic = TreeItemId()
        for appletAID in info['applets']:
            tic = self._capFileInformationTreeCtrl.InsertItem(ti, tic, "".join("%02X" %(ord(c)) for c in appletAID), data=TreeItemData( { 'type' : 'applet', 'aid' : appletAID }))
        self._capFileInformationTreeCtrl.ExpandAll()
        self._loadButton.Enable()
    
    def handleStatus(self, theStatus):
        self._contentTreeCtrl.DeleteAllItems()
        ri = self._contentTreeCtrl.AddRoot('STATUS')
        tir = TreeItemId()
        status_names = { 0x80 : 'ISD', 0x40 : 'SSD/Applets', 0x20 : 'ExecutableFiles', 0x10 : 'ExecutableFileAndModules' }
        for theElement in theStatus.keys():
            tir = self._contentTreeCtrl.InsertItem(ri, tir, status_names[theElement], data=TreeItemData({ 'type' : 'root' }))
            ti = TreeItemId()
            if theElement == 0x10:
                statusData = theStatus[theElement]
                if statusData != None:
                    executableModulesData = statusData[1]
                    for executableModuleData in executableModulesData:
                        packageAID = executableModuleData['aid']
                        packageLifeCycleState = executableModuleData['lifeCycleState']
                        ti = self._contentTreeCtrl.InsertItem(tir, ti, "AID: " + "".join("%02X" %(ord(c)) for c in packageAID) + " - LifeCycle: %02X" %(packageLifeCycleState), data = TreeItemData({ 'type' : 'package', 'aid' : packageAID}))
                        executableModules = executableModuleData['executableModules']
                        ti2 = TreeItemId()
                        for executableModule in executableModules:
                            ti2 = self._contentTreeCtrl.InsertItem(ti, ti2, "AID: " + "".join("%02X" %(ord(c)) for c in executableModule), data = TreeItemData({ 'type' : 'applet', 'aid' : executableModule}))
            else:
                statusData = theStatus[theElement]
                if statusData != None:
                    appletInfos = statusData[0]
                    for appletInfo in appletInfos:
                        appletAID = appletInfo['aid']
                        appletLifeCycleState = appletInfo['lifeCycleState']
                        appletPrivileges = appletInfo['privileges']
                        ti = self._contentTreeCtrl.InsertItem(tir, ti, "AID: " + "".join("%02X" %(ord(c)) for c in appletAID) + " - LifeCycle: %02X - Privileges: %02X" %(appletLifeCycleState, appletPrivileges), data = TreeItemData({ 'type' : 'package' if theElement == 0x20 else 'instance', 'aid' : appletAID}))
        self._contentTreeCtrl.ExpandAll()
    
    def handleLoadScriptBegin(self):
        self._scriptListCtrl.DeleteAllItems()
    
    def handleLoadScriptItem(self, scriptItemStr):
        itemIndex = self._scriptListCtrl.GetItemCount()
        scriptItem = ListItem()
        scriptItem.SetId(itemIndex)
        scriptItem.SetColumn(0)
        scriptItem.SetText('%d' %(itemIndex))
        self._scriptListCtrl.InsertItem(scriptItem)
        
        scriptItem.SetId(itemIndex)
        scriptItem.SetColumn(1)
        scriptItem.SetText(scriptItemStr)
        self._scriptListCtrl.SetItem(scriptItem)
    
    def handleLoadScriptEnd(self):
        pass
    
    def handleKeyInformationTemplates(self, kits):
        self._keyDataListCtrl.DeleteAllItems()
        kitsLen = len(kits)
        kitsCount = kitsLen / 4
        for i in xrange(kitsCount):
            keySetVersion = ord(kits[i * 4 + 0])
            keyIndex = ord(kits[i * 4 + 1])
            keyType = ord(kits[i * 4 + 2])
            keyLength = ord(kits[i * 4 + 3])
            i = self._keyDataListCtrl.GetItemCount()
            keyItem = ListItem()
            keyItem.SetId(i)
            keyItem.SetColumn(0)
            keyItem.SetText("%d" %(i))
            self._keyDataListCtrl.InsertItem(keyItem)
            keyItem.SetColumn(1)
            keyItem.SetText("%02X" %(keySetVersion))
            self._keyDataListCtrl.SetItem(keyItem)
            keyItem.SetColumn(2)
            keyItem.SetText("%02X" %(keyIndex))
            self._keyDataListCtrl.SetItem(keyItem)
            keyItem.SetColumn(3)
            keyItem.SetText("%02X" %(keyType))
            self._keyDataListCtrl.SetItem(keyItem)
            keyItem.SetColumn(4)
            keyItem.SetText("%02X" %(keyLength))
            self._keyDataListCtrl.SetItem(keyItem)
    
    def handleSCPInfo(self, scp, scpi):
        self._scpChoice.SetSelection(scp - 1)
        self._scpiTextCtrl.SetValue('%02X' %(scpi))
    
    def handleKeyChanged(self):
        self.__controller.getKeyTemplateInfo()
    
    def handleCardContentChanged(self):
        self.__controller.getStatus()
    
    def handleActionBegin(self, action):
        if action == "do mutual authentication":
            self._mutualAuthButton.Disable()
        elif action == "read cap file information":
            self._capFilePicker.Disable()
        elif action == "get status":
            self._refreshCardContent.Disable()
            self._installCardContent.Disable()
            self._selectCardContent.Disable()
            self._deleteCardContent.Disable()
        elif action == "select application":
            self._selectCardContent.Disable()
        elif action == "delete application":
            self._deleteCardContent.Disable()
        elif action == "get key template information":
            self._getKeyTemplateInfoButton.Disable()
        elif action == "put key":
            self._putKeyButton.Disable()
        elif action == "delete key":
            self._deleteKeyButton.Disable()
        else:
            pass
    
    def handleActionEnd(self, action):
        if action == "do mutual authentication":
            self._mutualAuthButton.Enable()
        elif action == "read cap file information":
            self._capFilePicker.Enable()
        elif action == "get status":
            self._refreshCardContent.Enable()
        elif action == "select application":
            self._selectCardContent.Enable()
        elif action == "delete application":
            self._deleteCardContent.Enable()
        elif action == "get key template information":
            self._getKeyTemplateInfoButton.Enable()
        elif action == "put key":
            self._putKeyButton.Enable()
        elif action == "delete key":
            self._deleteKeyButton.Enable()
        else:
            pass
    
    def _capFileInformationTreeCtrlOnTreeSelChanged( self, event ):
        event.Skip()
        self._installButton.Disable()
        selectedId = self._capFileInformationTreeCtrl.GetSelection()
        if not selectedId.IsOk():
            return
        
        selectedItemData = self._capFileInformationTreeCtrl.GetItemData(selectedId)
        if selectedItemData != None:
            if selectedItemData.GetData()['type'] == 'applet':
                self._installButton.Enable()
        