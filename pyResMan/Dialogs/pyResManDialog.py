# -*- coding:utf8 -*-

'''
Created on 2015-10-27

@author: javacardos@gmail.com
@organization: http://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from wx import ListItem, TreeItemId, TreeItemData
from pyResManReader import pyResManReader
from smartcard.Exceptions import NoCardException
from pyResManController import pyResManController, APDUItem
import os
from Util import Util
from datetime import datetime
from Dialogs.pyResManInstallDialog import pyResManInstallDialog
from BaseDialogs.pyResManDialogBase import pyResManDialogBase
import wx
from Dialogs.pyResManCommandDialog_Basic import CommandDialog_Basic
from Util import IDOK
from Dialogs.pyResManCommandDialog_AnticollisionSelect import CommandDialog_AnticollisionSelect
from Dialogs.pyResManCommandDialog_RATS import CommandDialog_RATS
from Dialogs.pyResManCommandDialog_REQBWUPB import CommandDialog_REQBWUPB
from Dialogs.pyResManCommandDialog_SlotMarker import CommandDialog_SlotMarker
from Dialogs.pyResManCommandDialog_PPS import CommandDialog_PPS
from Dialogs.pyResManCommandDialog_ATTRIB import CommandDialog_ATTRIB
from Dialogs.pyResManCommandDialog_HLTB import CommandDialog_HLTB
from wx.grid import Grid
import json
from Dialogs.pyResManCommandDialog_IBlock import CommandDialog_IBlock
from Dialogs.pyResManCommandDialog_RBlock import CommandDialog_RBlock
from Dialogs.pyResManCommandDialog_SBlock import CommandDialog_SBlock
from Dialogs.pyResManCommandDialog_MifareAuthentication import CommandDialog_MifareAuthentication
from Dialogs.pyResManCommandDialog_MifareBlockRead import CommandDialog_MifareBlockRead
from Dialogs.pyResManCommandDialog_MifareBlockWrite import CommandDialog_MifareBlockWrite
from Dialogs.pyResManCommandDialog_MifareIncrement import CommandDialog_MifareIncrement
from Dialogs.pyResManCommandDialog_MifareDecrement import CommandDialog_MifareDecrement
from Dialogs.pyResManCommandDialog_MifareDecrementTransfer import CommandDialog_MifareDecrementTransfer
from Dialogs.pyResManCommandDialog_MifareTransfer import CommandDialog_MifareTransfer
from Dialogs.pyResManCommandDialog_MifareRestore import CommandDialog_MifareRestore
import DebuggerUtils

COMMAND_LIST_COL_INDEX = 0
COMMAND_LIST_COL_COMMAND_NAME = 1
COMMAND_LIST_COL_COMMAND_VALUE = 2
COMMAND_LIST_COL_RESPONSE = 3
COMMAND_LIST_COL_DESCRIPTION = 4

class pyResManDialog (pyResManDialogBase):
    
    def __init__(self, parent):
        pyResManDialogBase.__init__(self, parent)
        
        readernames = pyResManReader.getReaderList()
        if len(readernames) > 0:
            for readername in readernames:
                self._comboReaderName.Insert(readername, self._comboReaderName.GetCount())
            self._comboReaderName.Select(0)
        
        self.__controller = pyResManController(self)
        
        self._textctrlCLA.SetValue('00')
        self._textctrlINS.SetValue('A4')
        self._textctrlP1.SetValue('04')
        self._textctrlP2.SetValue('00')
        self._textctrlLe.SetValue('00')
        
        self._listctrlScriptList.InsertColumn(0, 'Index', width=50)
        self._listctrlScriptList.InsertColumn(1, 'Command', width=200)
        self._listctrlScriptList.InsertColumn(2, 'Response', width=300)
        self._listctrlScriptList.InsertColumn(3, 'TimeSpent', width=100)
        self._listctrlScriptList.InsertColumn(4, 'DateTime', width=120)

        self._listctrlKeyData.InsertColumn(0, 'index', width=50)
        self._listctrlKeyData.InsertColumn(1, 'KVN', width=100)
        self._listctrlKeyData.InsertColumn(2, 'key index', width=100)
        self._listctrlKeyData.InsertColumn(3, 'key type', width=100)
        self._listctrlKeyData.InsertColumn(4, 'key length', width=100)

        self._listctrlApduList.InsertColumn(0, 'Index', width=50)
        self._listctrlApduList.InsertColumn(1, 'Command', width=200)
        self._listctrlApduList.InsertColumn(2, 'Response', width=300)
        self._listctrlApduList.InsertColumn(3, 'TimeSpent', width=100)
        self._listctrlApduList.InsertColumn(4, 'DateTime', width=120)
        
        defaultKeyValue = '404142434445464748494A4B4C4D4E4F'
        self._textctrlKey1.SetValue(defaultKeyValue)
        self._textctrlKey2.SetValue(defaultKeyValue)
        self._textctrlKey3.SetValue(defaultKeyValue)
        self._textctrlOldKVN.SetValue('00')
        self._textctrlNewKVN.SetValue('01')
        
        # Initialize debugger tab;
        # Commands list tree control;
        rootItemId = self._treectrlDebuggerCommands.AddRoot('Smartcard Debugger')
        contactlessItemId = self._treectrlDebuggerCommands.AppendItem(rootItemId, 'Contactless')
        typeaItemId = self._treectrlDebuggerCommands.AppendItem(rootItemId, 'ISO14443 TYPE A')
#         typebItemId = self._treectrlDebuggerCommands.AppendItem(rootItemId, 'ISO14443 TYPE B')
        blocktransmissionItemId = self._treectrlDebuggerCommands.AppendItem(rootItemId, 'ISO14443 BLOCK TRANSMISSION')
        mifareItemId = self._treectrlDebuggerCommands.AppendItem(rootItemId, 'MIFARE')
        self.__treelctrlDebuggerCommands_parentItemsId = (rootItemId, contactlessItemId, typeaItemId, blocktransmissionItemId, mifareItemId)
        
        # Contactless;
        self._treectrlDebuggerCommands.AppendItem(contactlessItemId, 'RF_ON')
        self._treectrlDebuggerCommands.AppendItem(contactlessItemId, 'RF_OFF')
        self._treectrlDebuggerCommands.AppendItem(contactlessItemId, 'RF_AUTO')
        self._treectrlDebuggerCommands.AppendItem(contactlessItemId, 'RF_MANUAL')
#         self._treectrlDebuggerCommands.AppendItem(contactlessItemId, '%UID%')
        # TypeA;
        self._treectrlDebuggerCommands.AppendItem(typeaItemId, 'REQA')
        self._treectrlDebuggerCommands.AppendItem(typeaItemId, 'WUPA')
        self._treectrlDebuggerCommands.AppendItem(typeaItemId, 'ANTICOLLISION')
        self._treectrlDebuggerCommands.AppendItem(typeaItemId, 'SELECT')
        self._treectrlDebuggerCommands.AppendItem(typeaItemId, 'RATS')
        self._treectrlDebuggerCommands.AppendItem(typeaItemId, 'HLTA')
        self._treectrlDebuggerCommands.AppendItem(typeaItemId, 'PPS')
#         # TypeB;
#         self._treectrlDebuggerCommands.AppendItem(typebItemId, 'REQB')
#         self._treectrlDebuggerCommands.AppendItem(typebItemId, 'WUPB')
#         self._treectrlDebuggerCommands.AppendItem(typebItemId, 'SLOT-MARKER')
#         self._treectrlDebuggerCommands.AppendItem(typebItemId, 'ATTRIB')
#         self._treectrlDebuggerCommands.AppendItem(typebItemId, 'HLTB')
        # Block Transmission;
        self._treectrlDebuggerCommands.AppendItem(blocktransmissionItemId, 'I-BLOCK')
        self._treectrlDebuggerCommands.AppendItem(blocktransmissionItemId, 'R-BLOCK')
        self._treectrlDebuggerCommands.AppendItem(blocktransmissionItemId, 'S-BLOCK')
        # Mifare;
#         self._treectrlDebuggerCommands.AppendItem(mifareItemId, 'LOAD_KEY')
        self._treectrlDebuggerCommands.AppendItem(mifareItemId, 'AUTHENTICATION')
        self._treectrlDebuggerCommands.AppendItem(mifareItemId, 'READ_BLOCK')
        self._treectrlDebuggerCommands.AppendItem(mifareItemId, 'WRITE_BLOCK')
        self._treectrlDebuggerCommands.AppendItem(mifareItemId, 'INCREMENT')
        self._treectrlDebuggerCommands.AppendItem(mifareItemId, 'DECREMENT')
#         self._treectrlDebuggerCommands.AppendItem(mifareItemId, 'DECREMENT_TRANSFER')
        self._treectrlDebuggerCommands.AppendItem(mifareItemId, 'TRANSFER')
        self._treectrlDebuggerCommands.AppendItem(mifareItemId, 'RESTORE')

        # Expand all;
#         self._treectrlDebuggerCommands.ExpandAll()
        
        # Script commands list;
        self._listctrlDebuggerScriptCommand.SetSelectionMode(Grid.wxGridSelectRows)
        
        self._listctrlDebuggerScriptCommand.InsertCols(0, 5)
        self._listctrlDebuggerScriptCommand.SetColSize(0, 50)
        self._listctrlDebuggerScriptCommand.SetColSize(1, 100)
        self._listctrlDebuggerScriptCommand.SetColSize(2, 100)
        self._listctrlDebuggerScriptCommand.SetColSize(3, 150)
        self._listctrlDebuggerScriptCommand.SetColLabelValue(COMMAND_LIST_COL_INDEX, 'Index')
        self._listctrlDebuggerScriptCommand.SetColLabelValue(COMMAND_LIST_COL_COMMAND_NAME, 'Command Name')
        self._listctrlDebuggerScriptCommand.SetColLabelValue(COMMAND_LIST_COL_COMMAND_VALUE, 'Command Value')
        self._listctrlDebuggerScriptCommand.SetColLabelValue(COMMAND_LIST_COL_RESPONSE, 'Response')
        self._listctrlDebuggerScriptCommand.SetColLabelValue(COMMAND_LIST_COL_DESCRIPTION, 'Description')
        self._listctrlDebuggerScriptCommand.SetColLabelSize(30)
        
        self._listctrlApduList.Bind(wx.EVT_CONTEXT_MENU, self._listctrlApduListOnContextMenu)
        self._listctrlScriptList.Bind(wx.EVT_CONTEXT_MENU, self._listctrlScriptListOnContextMenu)
        
        
    # Virtual event handlers, overide them in your derived class
    def _buttonConnectOnButtonClick(self, event):
        self._buttonConnect.Disable()
        if (self._buttonConnect.GetLabelText() == 'Connect'):
            try:
                # Get smartcard reader name;
                readername = self._comboReaderName.GetString(self._comboReaderName.GetSelection())
                protocolIndex = self._comboProtocol.GetSelection()
                
                # Get protocol value;
                protocol = pyResManReader.SCARD_PROTOCOL_T0 | pyResManReader.SCARD_PROTOCOL_T1
                if protocolIndex == 0:
                    protocol = pyResManReader.SCARD_PROTOCOL_T0
                elif protocolIndex == 1:
                    protocol = pyResManReader.SCARD_PROTOCOL_T1
                
                # Get mode value;
                modeIndex = self._comboMode.GetSelection()
                mode = pyResManReader.SCARD_SHARE_SHARED
                if modeIndex == 0:
                    mode = pyResManReader.SCARD_SHARE_EXCLUSIVE

                # Connect to the card;
                # Set AutoResponse when connect with protocol T0;
                if (protocol == pyResManReader.SCARD_PROTOCOL_T0):
                    self._checkboxAutoGetResponse.SetValue(True)
                
                self.__controller.connect(readername, protocol, mode)
                self.__controller.monitorCard()
                
                # Set status;
                self._buttonConnect.SetLabel('Disconnect')
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
                self._buttonConnect.SetLabel('Connect')
                self._Log('Disconnected.', wx.LOG_Info)
            except NoCardException, e:
                self._Log('NoCardException: %s' % (e.args[1]), wx.LOG_Error)
            except Exception, e:
                self._Log('Exception: %s' % (str(e)), wx.LOG_Error)
        self._buttonConnect.Enable()

    def _textctrlCLAOnChar(self, event):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _textctrlINSOnChar(self, event):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _textctrlP1OnChar(self, event):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _textctrlP2OnChar(self, event):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()

    def _textctrlDataOnChar(self, event):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()

    def _textctrlDataOnText(self, event):
        dataLen = len(self._textctrlData.GetValue())
        if dataLen & 0x01 != 0:
            self._textctrlData.SetBackgroundColour('#FF6347')
        else:
            self._textctrlData.SetBackgroundColour('WHITE')
        self._textctrlData.Refresh()
        dataLen = dataLen / 2
        self._textctrlLc.SetValue("%02X" % (dataLen))
    
    def _textctrlLeOnChar(self, event):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _buttonTransmitOnButtonClick(self, event):
        cls = self._textctrlCLA.GetValue()
        ins = self._textctrlINS.GetValue()
        p1 = self._textctrlP1.GetValue()
        p2 = self._textctrlP2.GetValue()
        lc = self._textctrlLc.GetValue()
        data = self._textctrlData.GetValue()
        le = self._textctrlLe.GetValue()
        
        if (len(cls) == 0) or (len(ins) == 0) or (len(p1) == 0) or (len(p2) == 0):
            self._Log('Please input command field.', wx.LOG_Warning)
            return
        
        commandText = ''
        if lc != '00':
            commandText = "%s%s%s%s%s %s %s" % (cls, ins, p1, p2, lc, data, le)
        else:
            commandText = "%s%s%s%s %s" % (cls, ins, p1, p2, le)            
        
        # Get t0 auto getresponse value;
        autoGetResponse = self._checkboxAutoGetResponse.GetValue()
        
        # Transmit;
        self.__controller.transmit(commandText, autoGetResponse, (self._listctrlApduList,))
        
    def _radioSCPInfoMethodOnRadioBox(self, event):
        event.Skip()
        
        if self._radioSCPInfoMethod.GetSelection() == 0:
            self._choiceSCP.Enable(False)
            self._textctrlSCPi.Enable(False)
        else:
            self._choiceSCP.Enable(True)
            self._textctrlSCPi.Enable(True)
    
    def _textctrlSCPiOnChar(self, event):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()

    def _buttonMutualAuthOnButtonClick(self, event):
        scp = -1
        scpi = -1
        if self._radioSCPInfoMethod.GetSelection() == 1:
            scp = self._choiceSCP.GetSelection() + 1
            scpi = int(self._textctrlSCPi.GetValue(), 0x10)
        key1 = Util.s2vs(self._textctrlKey1.GetValue())
        key2 = Util.s2vs(self._textctrlKey2.GetValue())
        key3 = Util.s2vs(self._textctrlKey3.GetValue())
        self.__controller.doMutualAuth(scp, scpi, key1, key2, key3)
    
    def _filepickerCapFileOnFileChanged(self, event):
        self._buttonLoad.Disable()
        self._buttonInstall.Disable()
        self._treectrlCapFileInformation.DeleteAllItems()
        capFilePath = self._filepickerCapFile.GetPath()
        self.__controller.readCapFileInfo(capFilePath)
    
    def _buttonLoadOnButtonClick(self, event):
        capFilePath = self._filepickerCapFile.GetPath()
        self.__controller.loadCapFile(capFilePath)

    def _buttonInstallOnButtonClick(self, event):
        appletItem = self._treectrlCapFileInformation.GetSelection()
        appletData = self._treectrlCapFileInformation.GetItemData(appletItem)
        if appletData.GetData()['type'] != 'applet':
            self._Log('Please select the applet item to install.', wx.LOG_Warning)
            return
        
        packageItem = self._treectrlCapFileInformation.GetItemParent(appletItem)
        packageData = self._treectrlCapFileInformation.GetItemData(packageItem)
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

    def _treectrlCardContentOnTreeSelChanged(self, event):
        event.Skip()
        self._buttonInstallCardContent.Enable(False)
        self._buttonSelectCardContent.Enable(False)
        self._buttonDeleteCardContent.Enable(True)
        selectedId = self._treectrlCardContent.GetSelection();
        selectedItemData = self._treectrlCardContent.GetItemData(selectedId)
        if selectedItemData == None:
            return
        itemData = selectedItemData.GetData()
        itemType = itemData['type']
        if itemType == 'applet':
            self._buttonDeleteCardContent.Enable(False)
            
            parentId = self._treectrlCardContent.GetItemParent(selectedId)
            parentItemData = self._treectrlCardContent.GetItemData(parentId)
            parentData = parentItemData.GetData()
            if parentData['type'] == 'package':
                self._buttonInstallCardContent.Enable()
        elif itemType == 'instance':
            self._buttonSelectCardContent.Enable()
        
    def _buttonRefreshCardContentOnButtonClick(self, event):
        event.Skip()
        self.__controller.getStatus()
    
    def _buttonInstallCardContentOnButtonClick(self, event):
        selectedId = self._treectrlCardContent.GetSelection();
        selectedItemData = self._treectrlCardContent.GetItemData(selectedId)
        if selectedItemData.GetData()['type'] != 'applet':
            return
        parentId = self._treectrlCardContent.GetItemParent(selectedId)
        parentItemData = self._treectrlCardContent.GetItemData(parentId)
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

    def _buttonSelectCardContentOnButtonClick(self, event):
        event.Skip()
        
        self._buttonSelectCardContent.Disable()
        
        selectedId = self._treectrlCardContent.GetSelection();
        selectedItemData = self._treectrlCardContent.GetItemData(selectedId)
        itemData = selectedItemData.GetData()
        itemType = itemData['type']
        if itemType != 'instance':
            return
        instanceAID = itemData['aid']
        self.__controller.selectApplication(instanceAID)

    def _buttonDeleteCardContentOnButtonClick(self, event):
        selectedItem = self._treectrlCardContent.GetSelection()
        if selectedItem.IsOk():
            selectedItemData = self._treectrlCardContent.GetItemData(selectedItem)
            aid = selectedItemData.GetData()['aid']
            self.__controller.deleteApplication(aid)
        event.Skip()
    
    def _listctrlKeyDataOnListItemSelected(self, event):
        event.Skip()
        
        item = event.GetItem()
        kvn = self._listctrlKeyData.GetItemText(item.GetId(), 1)
        if kvn == 'FF':
            self._textctrlOldKVN.SetValue('0')
            self._textctrlNewKVN.SetValue('1')
        else:
            self._textctrlOldKVN.SetValue(kvn)
            self._textctrlNewKVN.SetValue(kvn)

    def _textctrlKey1OnChar(self, event):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _textctrlKey1OnText(self, event):
        event.Skip()
        keyStrLen = len(self._textctrlKey1.GetValue())
        self._textctrlKey1Length.SetValue('%02X' % (keyStrLen / 2))
        if (keyStrLen & 1) != 0:
            self._textctrlKey1.SetBackgroundColour('#FF6347')
        else:
            self._textctrlKey1.SetBackgroundColour('WHITE')
        self._textctrlKey1.Refresh()
    
    def _textctrlKey2OnChar(self, event):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _textctrlKey2OnText(self, event):
        event.Skip()
        keyStrLen = len(self._textctrlKey2.GetValue())
        self._textctrlKey2Length.SetValue('%02X' % (keyStrLen / 2))
        if (keyStrLen & 1) != 0:
            self._textctrlKey2.SetBackgroundColour('#FF6347')
        else:
            self._textctrlKey2.SetBackgroundColour('WHITE')
        self._textctrlKey2.Refresh()
    
    def _textctrlKey3OnChar(self, event):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _textctrlKey3OnText(self, event):
        event.Skip()
        keyStrLen = len(self._textctrlKey3.GetValue())
        self._textctrlKey3Length.SetValue('%02X' % (keyStrLen / 2))
        if (keyStrLen & 1) != 0:
            self._textctrlKey3.SetBackgroundColour('#FF6347')
        else:
            self._textctrlKey3.SetBackgroundColour('WHITE')
        self._textctrlKey3.Refresh()
    
    def _textctrlOldKVNOnChar(self, event):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _textctrlOldKVNOnText(self, event):
        event.Skip()
        kvn = int(self._textctrlOldKVN.GetValue(), 0x10)
        self._textctrlOldKVN.SetBackgroundColour('WHITE')
        if not ((kvn >= 0) and (kvn <= 0x7F)): 
            self._textctrlOldKVN.SetBackgroundColour('#FF6347')
        self._textctrlOldKVN.Refresh()

    def _textctrlNewKVNOnChar(self, event):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _textctrlNewKVNOnText(self, event):
        event.Skip()
        kvn = int(self._textctrlNewKVN.GetValue(), 0x10)
        self._textctrlNewKVN.SetBackgroundColour('WHITE')
        if not ((kvn >= 1) and (kvn <= 0x7F)): 
            self._textctrlNewKVN.SetBackgroundColour('#FF6347')
        self._textctrlNewKVN.Refresh()

    
    def _buttonPutKeyOnButtonClick(self, event):
        event.Skip()
        
        if self._textctrlOldKVN.IsEmpty():
            self._Log('Please input the old key version number.', wx.LOG_Warning)
            self._textctrlOldKVN.SetBackgroundColour('#FF6347')
            self._textctrlOldKVN.Refresh()
            return
        if self._textctrlNewKVN.IsEmpty():
            self._Log('Please input the new key version number.', wx.LOG_Warning)
            self._textctrlNewKVN.SetBackgroundColour('#FF6347')
            self._textctrlNewKVN.Refresh()
            return
        
        oldKVN = int(self._textctrlOldKVN.GetValue(), 0x10)
        newKVN = int(self._textctrlNewKVN.GetValue(), 0x10)
        
        key1 = Util.s2vs(self._textctrlKey1.GetValue())
        key2 = Util.s2vs(self._textctrlKey2.GetValue())
        key3 = Util.s2vs(self._textctrlKey3.GetValue())
        self.__controller.putKey(oldKVN, newKVN, key1, key2, key3)

    def _buttonDeleteKeyOnButtonClick(self, event):
        event.Skip()

        keysInfo = []
        i = self._listctrlKeyData.GetFirstSelected()
        while i != -1:
            kvn = int(self._listctrlKeyData.GetItemText(i, 1), 0x10)
            keyIndex = int(self._listctrlKeyData.GetItemText(i, 2), 0x10)
            keysInfo.append((kvn, keyIndex,))
            i = self._listctrlKeyData.GetNextSelected(i)
        self.__controller.deleteKey(keysInfo)

    def _buttonGetKeyTemplateInfoOnButtonClick(self, event):
        event.Skip()
        self.__controller.getKeyTemplateInfo()
    
    def _buttonKeyDefaultOnButtonClick(self, event):
        event.Skip()
        defaultKey = '404142434445464748494A4B4C4D4E4F'
        self._textctrlKey1.SetValue(defaultKey)
        self._textctrlKey2.SetValue(defaultKey)
        self._textctrlKey3.SetValue(defaultKey)

    def _textctrlScriptLoopCountOnChar(self, event):
        if Util.isnumchar_kc(event.KeyCode):
            event.Skip()
        else:
            pass

    def _loadScript(self):
        scriptPathName = self._filepickerScriptFile.GetPath()
        if os.path.exists(scriptPathName):
            self.__controller.loadScript(scriptPathName)
    
    def _filepickerScriptFileOnFileChanged(self, event):
        event.Skip()
        self._loadScript()
    
    def _buttonScriptRefreshOnButtonClick(self, event):
        event.Skip()
        self._loadScript()
    
    def _buttonScriptRunOnButtonClick(self, event):
        event.Skip()
        apduItems = []
        itemCount = self._listctrlScriptList.GetItemCount()
        for itemIndex in xrange(itemCount):
            listItem = self._listctrlScriptList.GetItem(itemIndex, 1)
            apduItem = APDUItem(listItem.GetText(), (self._listctrlScriptList, listItem.GetId()))
            apduItems.append(apduItem)
        
        t0AutoGetResponse = self._checkboxAutoGetResponse.GetValue()
        loopCount = int(self._textctrlScriptLoopCount.GetValue())
        self.__controller.transmitAPDUItems(apduItems, t0AutoGetResponse, loopCount)
    
    def _buttonScriptClearResultOnButtonClick(self, event):
        event.Skip()
        self._listctrlScriptList.DeleteAllItems()
        self._loadScript()
    
    def m_splitter2OnIdle(self, event):
        self.m_splitter2.SetSashPosition(0)
        self.m_splitter2.Unbind(wx.EVT_IDLE)
    
    def _listctrlApduListOnContextMenu(self, event):
        """Display apdu list view popup menu;"""
        self._listctrlApduListPopupMenu = wx.Menu()
        self._listctrlApduListPopupMenu.Append(1, "Run")
        self._listctrlApduListPopupMenu.AppendSeparator()
        self._listctrlApduListPopupMenu.Append(0, "Clear")
        self._listctrlApduListPopupMenu.Bind(wx.EVT_MENU, self._listCtrlOnContextMenuClick)
        self._listctrlApduList.PopupMenu(self._listctrlApduListPopupMenu)

    def _listctrlScriptListOnContextMenu(self, event):
        """Display apdu list view popup menu;"""
        self._listctrlScriptListPopupMenu = wx.Menu()
        self._listctrlScriptListPopupMenu.Append(1, "Run")
        self._listctrlScriptListPopupMenu.AppendSeparator()
        self._listctrlScriptListPopupMenu.Append(0, "Clear")
        self._listctrlScriptListPopupMenu.Bind(wx.EVT_MENU, self._listCtrlOnContextMenuClick)
        self._listctrlScriptList.PopupMenu(self._listctrlScriptListPopupMenu)
    
    def _listCtrlOnContextMenuClick(self, event):
        menuItemIndex = event.Id
        theListCtrl = event.GetEventObject().GetInvokingWindow()
        if not isinstance(theListCtrl, wx.ListCtrl):
            theListCtrl = theListCtrl.GetParent()
        if menuItemIndex == 0:
            theListCtrl.DeleteAllItems()
            # Load script again;
            if theListCtrl == self._listctrlScriptList:
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
        
        t0AutoGetResponse = self._checkboxAutoGetResponse.GetValue()
        self.__controller.transmitAPDUItems(apduItems, t0AutoGetResponse, 1)
    
    def _onEventButton(self, event):
        controlId = event.Id
        if (controlId == self._buttonConnect.Id):
            self._onConnect()
        elif (controlId == self._buttonTransmit.Id):
            self._onTransmit()
        elif (controlId == self._filepickerScriptFile.Id):
            self._onBrowseScriptFile()
        elif (controlId == self._buttonScriptRun.Id):
            self._onRunScript()
    
    def _InitController(self):
        """Init controller for logical operations, self as the view;"""
        self.__controller = pyResManController(self)
    
    def handleCardRemoved(self, name):
        self._Log('Card is removed.', wx.LOG_Warning)
        self._buttonConnect.SetLabel('Connect')

    def handleCardInserted(self, name):
        pass
    
    def _relistReaders(self):
        """Relist reader names, when reader added/removed;"""
        readers = self.__controller.getReaderList()
        self._comboReaderName.Clear()
        for reader in readers:
            self._comboReaderName.Append(reader)
        self._comboReaderName.SetSelection(0)

    def __handleReaderAdded(self, name):
        self._relistReaders()

    def handleReaderAdded(self, name):
        wx.CallAfter(self.__handleReaderAdded, name)
    
    def __handleReaderRemoved(self, name):
        self._relistReaders()
    
    def handleReaderRemoved(self, name):
        wx.CallAfter(self.__handleReaderRemoved, name)
    
    def _onBrowseScriptFile(self):
        defaultDir = self._filepickerScriptFile.GetValue()
        if not os.path.exists(defaultDir):
            defaultDir = os.getcwd()
        fileDialog = wx.FileDialog(self, defaultDir=defaultDir)
        ret = fileDialog.ShowModal()
        if (ret != wx.ID_CANCEL):
            filepath = fileDialog.GetPath()
            self._filepickerScriptFile.SetValue(filepath)
        else:
            pass
    
    def _onRunScript(self):
        if (not self.__controller.runningScript()):
            scriptPathName = self._filepickerScriptFile.GetValue()
            if not os.path.exists(scriptPathName):
                self._onBrowseScriptFile()
                scriptPathName = self._filepickerScriptFile.GetValue()
            if not os.path.exists(scriptPathName):
                self._Log('User cancel operation.', wx.LOG_Info)
                return
    
            # Get t0 auto getresponse value;
            autoGetResponse = self._checkboxAutoGetResponse.GetValue()
            # Get loop count;
            scriptLoopCount = self._textctrlScriptLoopCounter.GetValue()
    
            self.__controller.runScript(scriptPathName, scriptLoopCount, autoGetResponse)
        else:
            self.__controller.stopScript()
    
    def __handleAPDUCommand(self, commandStr, args):
        theListCtrl = args[0]

        itemIndex = 0
        if len(args) > 1:
            itemIndex = args[1]
            indexItem = ListItem()
            indexItem.SetId(itemIndex)
            indexItem.SetColumn(0)
            indexItem.SetText('> %d' % (itemIndex))
            theListCtrl.SetItem(indexItem)
        else:
            itemIndex = theListCtrl.GetItemCount()
            indexItem = ListItem()
            indexItem.SetId(itemIndex)
            indexItem.SetColumn(0)
            indexItem.SetText('> %d' % (itemIndex))
            theListCtrl.InsertItem(indexItem)
         
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
    
    def handleAPDUCommand(self, commandStr, args=tuple()):
        """Handle controller's apdu command event, to display apdu command;"""
        wx.CallAfter(self.__handleAPDUCommand, commandStr, args)
    
    def __handleAPDUResponse(self, responseStr, transtime, args):
        theListCtrl = args[0]

        itemIndex = 0
        if len(args) > 1:
            itemIndex = args[1]
        else:
            itemIndex = theListCtrl.GetItemCount() - 1
        
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
        indexItem.SetText('%d' % (itemIndex))
        theListCtrl.SetItem(indexItem)
        theListCtrl.Refresh()
 
        theListCtrl.EnsureVisible(itemIndex)
    
    def handleAPDUResponse(self, responseStr, transtime, args=tuple()):
        """Handle controller's apdu response event, to display apdu result informations;"""
        wx.CallAfter(self.__handleAPDUResponse, responseStr, transtime, args)

    def _Log(self, msg, level=wx.LOG_Message):
        """Display log with levels"""
        if msg.endswith('\r'):
            msg = msg[ : len(msg) - 1]
        if msg.endswith('\n'):
            msg = msg[ : len(msg) - 1]
        
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

        self._textctrlLog.SetDefaultStyle(wx.TextAttr(colText=textColor))
        self._textctrlLog.AppendText(msg + '\n')
        curSelTo = self._textctrlLog.GetSelection()[1]
        self._textctrlLog.ShowPosition(curSelTo)
    
    def __handleLog(self, msg, level=wx.LOG_Message):
        self._Log(msg, level)
    
    def handleLog(self, msg, level=wx.LOG_Message):
        wx.CallAfter(self.__handleLog, msg, level)
        
    def __handleScriptBegin(self, status):
        self._buttonScriptRun.SetLabel('Stop')

    def handleScriptBegin(self, status):
        wx.CallAfter(self.__handleScriptBegin, status)

    def __handleScriptEnd(self, status):
        self._buttonScriptRun.SetLabel('Start')

    def handleScriptEnd(self, status):
        wx.CallAfter(self.__handleScriptEnd, status)

    def __handleException(self, e):
        try:
            self._Log('Exception: %s' % (e.message), wx.LOG_Error)
        except:
            try:
                self._Log('Exception: %s' % (str(e)), wx.LOG_Error)
            except:
                self._Log('Transmit exceptin occured.', wx.LOG_Error)

    def handleException(self, e):
        wx.CallAfter(self.__handleException, e)
        
    def __handleCapFileInfo(self, info):
        self._treectrlCapFileInformation.DeleteAllItems()
        tr = self._treectrlCapFileInformation.AddRoot(self._filepickerCapFile.GetPath())
        packageAID = info['loadFileAID']
        ti = self._treectrlCapFileInformation.InsertItem(tr, TreeItemId(), "".join("%02X" % (ord(c)) for c in packageAID), data=TreeItemData({ 'type' : 'package', 'aid' : packageAID }))
        tic = TreeItemId()
        for appletAID in info['applets']:
            tic = self._treectrlCapFileInformation.InsertItem(ti, tic, "".join("%02X" % (ord(c)) for c in appletAID), data=TreeItemData({ 'type' : 'applet', 'aid' : appletAID }))
        self._treectrlCapFileInformation.ExpandAll()
        self._buttonLoad.Enable()
    
    def handleCapFileInfo(self, info):
        wx.CallAfter(self.__handleCapFileInfo, info)
    
    def __handleStatus(self, theStatus):
        self._treectrlCardContent.DeleteAllItems()
        ri = self._treectrlCardContent.AddRoot('STATUS')
        tir = TreeItemId()
        status_names = { 0x80 : 'ISD', 0x40 : 'SSD/Applets', 0x20 : 'ExecutableFiles', 0x10 : 'ExecutableFileAndModules' }
        for theElement in theStatus.keys():
            tir = self._treectrlCardContent.InsertItem(ri, tir, status_names[theElement], data=TreeItemData({ 'type' : 'root' }))
            ti = TreeItemId()
            if theElement == 0x10:
                statusData = theStatus[theElement]
                if statusData != None:
                    executableModulesData = statusData[1]
                    for executableModuleData in executableModulesData:
                        packageAID = executableModuleData['aid']
                        packageLifeCycleState = executableModuleData['lifeCycleState']
                        ti = self._treectrlCardContent.InsertItem(tir, ti, "AID: " + "".join("%02X" % (ord(c)) for c in packageAID) + " - LifeCycle: %02X" % (packageLifeCycleState), data=TreeItemData({ 'type' : 'package', 'aid' : packageAID}))
                        executableModules = executableModuleData['executableModules']
                        ti2 = TreeItemId()
                        for executableModule in executableModules:
                            ti2 = self._treectrlCardContent.InsertItem(ti, ti2, "AID: " + "".join("%02X" % (ord(c)) for c in executableModule), data=TreeItemData({ 'type' : 'applet', 'aid' : executableModule}))
            else:
                statusData = theStatus[theElement]
                if statusData != None:
                    appletInfos = statusData[0]
                    for appletInfo in appletInfos:
                        appletAID = appletInfo['aid']
                        appletLifeCycleState = appletInfo['lifeCycleState']
                        appletPrivileges = appletInfo['privileges']
                        ti = self._treectrlCardContent.InsertItem(tir, ti, "AID: " + "".join("%02X" % (ord(c)) for c in appletAID) + " - LifeCycle: %02X - Privileges: %02X" % (appletLifeCycleState, appletPrivileges), data=TreeItemData({ 'type' : 'package' if theElement == 0x20 else 'instance', 'aid' : appletAID}))
        self._treectrlCardContent.ExpandAll()
    
    def handleStatus(self, theStatus):
        wx.CallAfter(self.__handleStatus, theStatus)
    
    def __handleLoadScriptBegin(self):
        self._listctrlScriptList.DeleteAllItems()
    
    def handleLoadScriptBegin(self):
        wx.CallAfter(self.__handleLoadScriptBegin)
    
    def __handleLoadScriptItem(self, scriptItemStr):
        itemIndex = self._listctrlScriptList.GetItemCount()
        scriptItem = ListItem()
        scriptItem.SetId(itemIndex)
        scriptItem.SetColumn(0)
        scriptItem.SetText('%d' % (itemIndex))
        self._listctrlScriptList.InsertItem(scriptItem)
        
        scriptItem.SetId(itemIndex)
        scriptItem.SetColumn(1)
        scriptItem.SetText(scriptItemStr)
        self._listctrlScriptList.SetItem(scriptItem)
    
    def handleLoadScriptItem(self, scriptItemStr):
        wx.CallAfter(self.__handleLoadScriptItem, scriptItemStr)
    
    def handleLoadScriptEnd(self):
        pass
    
    def __handleKeyInformationTemplates(self, kits):
        self._listctrlKeyData.DeleteAllItems()
        kitsLen = len(kits)
        kitsCount = kitsLen / 4
        for i in xrange(kitsCount):
            keySetVersion = ord(kits[i * 4 + 0])
            keyIndex = ord(kits[i * 4 + 1])
            keyType = ord(kits[i * 4 + 2])
            keyLength = ord(kits[i * 4 + 3])
            i = self._listctrlKeyData.GetItemCount()
            keyItem = ListItem()
            keyItem.SetId(i)
            keyItem.SetColumn(0)
            keyItem.SetText("%d" % (i))
            self._listctrlKeyData.InsertItem(keyItem)
            keyItem.SetColumn(1)
            keyItem.SetText("%02X" % (keySetVersion))
            self._listctrlKeyData.SetItem(keyItem)
            keyItem.SetColumn(2)
            keyItem.SetText("%02X" % (keyIndex))
            self._listctrlKeyData.SetItem(keyItem)
            keyItem.SetColumn(3)
            keyItem.SetText("%02X" % (keyType))
            self._listctrlKeyData.SetItem(keyItem)
            keyItem.SetColumn(4)
            keyItem.SetText("%02X" % (keyLength))
            self._listctrlKeyData.SetItem(keyItem)
    
    def handleKeyInformationTemplates(self, kits):
        wx.CallAfter(self.__handleKeyInformationTemplates, kits)
    
    def __handleSCPInfo(self, scp, scpi):
        self._choiceSCP.SetSelection(scp - 1)
        self._textctrlSCPi.SetValue('%02X' % (scpi))
    
    def handleSCPInfo(self, scp, scpi):
        wx.CallAfter(self.__handleSCPInfo, scp, scpi)
        
    def handleKeyChanged(self):
        self.__controller.getKeyTemplateInfo()
    
    def handleCardContentChanged(self):
        self.__controller.getStatus()
    
    def __handleActionBegin(self, action):
        if action == "do mutual authentication":
            self._buttonMutualAuth.Disable()
        elif action == "read cap file information":
            self._filepickerCapFile.Disable()
        elif action == "get status":
            self._buttonRefreshCardContent.Disable()
            self._buttonInstallCardContent.Disable()
            self._buttonSelectCardContent.Disable()
            self._buttonDeleteCardContent.Disable()
        elif action == "select application":
            self._buttonSelectCardContent.Disable()
        elif action == "delete application":
            self._buttonDeleteCardContent.Disable()
        elif action == "get key template information":
            self._buttonGetKeyTemplateInfo.Disable()
        elif action == "put key":
            self._buttonPutKey.Disable()
        elif action == "delete key":
            self._buttonDeleteKey.Disable()
        else:
            pass
    
    def handleActionBegin(self, action):
        wx.CallAfter(self.__handleActionBegin, action)
    
    def __handleActionEnd(self, action):
        if action == "do mutual authentication":
            self._buttonMutualAuth.Enable()
        elif action == "read cap file information":
            self._filepickerCapFile.Enable()
        elif action == "get status":
            self._buttonRefreshCardContent.Enable()
        elif action == "select application":
            self._buttonSelectCardContent.Enable()
        elif action == "delete application":
            self._buttonDeleteCardContent.Enable()
        elif action == "get key template information":
            self._buttonGetKeyTemplateInfo.Enable()
        elif action == "put key":
            self._buttonPutKey.Enable()
        elif action == "delete key":
            self._buttonDeleteKey.Enable()
        else:
            pass
    
    def handleActionEnd(self, action):
        wx.CallAfter(self.__handleActionEnd, action)
    
    def _treectrlCapFileInformationOnTreeSelChanged(self, event):
        event.Skip()
        self._buttonInstall.Disable()
        selectedId = self._treectrlCapFileInformation.GetSelection()
        if not selectedId.IsOk():
            return
        
        selectedItemData = self._treectrlCapFileInformation.GetItemData(selectedId)
        if selectedItemData != None:
            if selectedItemData.GetData()['type'] == 'applet':
                self._buttonInstall.Enable()
    
    def AddDebuggerCommandListItem(self, commandName, commandValue):
        # Append to the last or insert before selected rows;
        rowIndex = 0
        selectedRows = self._listctrlDebuggerScriptCommand.GetSelectedRows()
        if len(selectedRows) > 0:
            rowIndex = selectedRows[0] + 1
        else:
            rowIndex = self._listctrlDebuggerScriptCommand.GetNumberRows()
        
        # Insert the item;
        self._listctrlDebuggerScriptCommand.InsertRows(rowIndex, 1)
        self._listctrlDebuggerScriptCommand.SetCellValue(rowIndex, COMMAND_LIST_COL_COMMAND_NAME, commandName)
        self._listctrlDebuggerScriptCommand.SetCellValue(rowIndex, COMMAND_LIST_COL_COMMAND_VALUE, commandValue)
        
        # Refresh index;
        self.__refreshCommandItemIndex()
        
    def __inputCommandInfo(self, commandName, commandValue):
        commandDialog = None
        defaultCommandValue = ''
        if commandName == 'RF_ON':
            defaultCommandValue = ''
        elif commandName == 'RF_OFF':
            defaultCommandValue = ''
        elif commandName == 'RF_AUTO':
            defaultCommandValue = ''
        elif commandName == 'RF_MANUAL':
            defaultCommandValue = ''
        elif commandName == '%UID%':
            commandDialog = CommandDialog_Basic(self, 4)
            defaultCommandValue = '00000000'
        elif commandName == 'REQA':
            commandDialog = CommandDialog_Basic(self, 1)
            defaultCommandValue = '26'
        elif commandName == 'WUPA':
            commandDialog = CommandDialog_Basic(self, 1)
            defaultCommandValue = '52'
        elif commandName == 'ANTICOLLISION':
            commandDialog = CommandDialog_AnticollisionSelect(self)
            defaultCommandValue = '9320'
        elif commandName == 'SELECT':
            commandDialog = CommandDialog_AnticollisionSelect(self, True)
            defaultCommandValue = '9370 00000000'
        elif commandName == 'RATS':
            commandDialog = CommandDialog_RATS(self)
            defaultCommandValue = 'E000'
        elif commandName == 'PPS':
            commandDialog = CommandDialog_PPS(self)
            defaultCommandValue = 'D01100'
        elif commandName == 'HLTA':
            commandDialog = CommandDialog_Basic(self, 2)
            defaultCommandValue = '5000'
        elif commandName == 'REQB':
            commandDialog = CommandDialog_REQBWUPB(self)
            defaultCommandValue = '050000'
        elif commandName == 'WUPB':
            commandDialog = CommandDialog_REQBWUPB(self)
            defaultCommandValue = '050008'
        elif commandName == 'SLOT-MARKER':
            commandDialog = CommandDialog_SlotMarker(self)
            defaultCommandValue = '15'
        elif commandName == 'ATTRIB':
            commandDialog = CommandDialog_ATTRIB(self)
            defaultCommandValue = '1D 00000000 00 08 01 00'
        elif commandName == 'HLTB':
            commandDialog = CommandDialog_HLTB(self)
            defaultCommandValue = '50 00000000'
        elif commandName == 'I-BLOCK':
            commandDialog = CommandDialog_IBlock(self)
            defaultCommandValue = '0A00 00A4040000'
        elif commandName == 'R-BLOCK':
            commandDialog = CommandDialog_RBlock(self)
            defaultCommandValue = 'A2'
        elif commandName == 'S-BLOCK':
            commandDialog = CommandDialog_SBlock(self)
            defaultCommandValue = 'F201'
        elif commandName == 'AUTHENTICATION':
            commandDialog = CommandDialog_MifareAuthentication(self)
            defaultCommandValue = '60 00 FFFFFFFFFFFF 00000000'
        elif commandName == 'READ_BLOCK':
            commandDialog = CommandDialog_MifareBlockRead(self)
            defaultCommandValue = '30 00'
        elif commandName == 'WRITE_BLOCK':
            commandDialog = CommandDialog_MifareBlockWrite(self)
            defaultCommandValue = 'A0 00 000102030405060708090A0B0C0D0E0F'
        elif commandName == 'INCREMENT':
            commandDialog = CommandDialog_MifareIncrement(self)
            defaultCommandValue = 'C1 00 00000000'
        elif commandName == 'DECREMENT':
            commandDialog = CommandDialog_MifareDecrement(self)
            defaultCommandValue = 'C0 00 00000000'
        elif commandName == 'DECREMENT_TRANSFER':
            commandDialog = CommandDialog_MifareDecrementTransfer(self)
            defaultCommandValue = 'xx 00 00000000'
        elif commandName == 'TRANSFER':
            commandDialog = CommandDialog_MifareTransfer(self)
            defaultCommandValue = 'B0 00'
        elif commandName == 'RESTORE':
            commandDialog = CommandDialog_MifareRestore(self)
            defaultCommandValue = 'C2 00'
        else:
            pass
        
        if commandValue == None:
            commandValue = defaultCommandValue 
        if commandDialog != None:
            commandValue = commandValue.replace(' ', '') 
            commandDialog.setCommandName(commandName)
            commandDialog.setCommandValue(commandValue)
            dlgRet = commandDialog.ShowModal()
            if dlgRet == IDOK:
                commandName = commandDialog.getCommandName()
                commandValue = commandDialog.getCommandValue()
                commandValue = commandValue.replace(' ', '')
            else:
                commandName = None
                commandValue = None
        return commandName, commandValue
    
    def _treectrlDebuggerCommandsOnLeftDClick(self, event):
        selectedItemId = self._treectrlDebuggerCommands.GetSelection()
        if selectedItemId in self.__treelctrlDebuggerCommands_parentItemsId:
            if self._treectrlDebuggerCommands.IsExpanded(selectedItemId):
                self._treectrlDebuggerCommands.Collapse(selectedItemId)
            else:
                self._treectrlDebuggerCommands.Expand(selectedItemId)
            return
        
        selectedItemText = self._treectrlDebuggerCommands.GetItemText(selectedItemId)
        
        commandName, commandValue = self.__inputCommandInfo(selectedItemText, None)
        if (commandName != None) and (commandValue != None):
            self.AddDebuggerCommandListItem(commandName, commandValue)
    
    def _listctrlDebuggerScriptCommandOnGridCellLeftDClick(self, event):
        rowIndex = event.Row
        colIndex = event.Col
        if (colIndex == COMMAND_LIST_COL_COMMAND_NAME) or (colIndex == COMMAND_LIST_COL_COMMAND_VALUE):
            commandName = self._listctrlDebuggerScriptCommand.GetCellValue(rowIndex, COMMAND_LIST_COL_COMMAND_NAME)
            commandValue = self._listctrlDebuggerScriptCommand.GetCellValue(rowIndex, COMMAND_LIST_COL_COMMAND_VALUE)
            commandName, commandValue = self.__inputCommandInfo(commandName, commandValue)
            if (commandName != None) and (commandValue != None):
                self._listctrlDebuggerScriptCommand.SetCellValue(rowIndex, COMMAND_LIST_COL_COMMAND_NAME, commandName)
                self._listctrlDebuggerScriptCommand.SetCellValue(rowIndex, COMMAND_LIST_COL_COMMAND_VALUE, commandValue)
    
    def __handleDebuggerResponse(self, args):
        rsp = args[0]
        commandInfo = args[1]
        commandIndex = commandInfo[0]
        commandName = commandInfo[1]
        commandValue = commandInfo[2]
        
        if rsp[0]:
            self._listctrlDebuggerScriptCommand.SetCellTextColour(commandIndex, COMMAND_LIST_COL_RESPONSE, '#000000')
            self._listctrlDebuggerScriptCommand.SetCellValue(commandIndex, COMMAND_LIST_COL_RESPONSE, Util.vs2s(rsp[1], ''))
            self._listctrlDebuggerScriptCommand.SetCellValue(commandIndex, COMMAND_LIST_COL_DESCRIPTION, 'OK')
            self._listctrlDebuggerScriptCommand.SetCellTextColour(commandIndex, COMMAND_LIST_COL_DESCRIPTION, '#008B00')
        else:
            errorcode = ord(rsp[1])
            errorString = self.getDebuggerErrorString(errorcode)
            self._Log('Command %d-%s-%s failed, error: %s (0x%02X). \n' %(commandIndex, commandName, Util.vs2s(commandValue, ''), errorString, errorcode), wx.LOG_Error)
            self._listctrlDebuggerScriptCommand.SetCellValue(commandIndex, COMMAND_LIST_COL_DESCRIPTION, 'Error: %s (0x%02X)' %(errorString, errorcode))
            self._listctrlDebuggerScriptCommand.SetCellTextColour(commandIndex, COMMAND_LIST_COL_DESCRIPTION, '#FF0000')
            self._listctrlDebuggerScriptCommand.SetCellValue(commandIndex, COMMAND_LIST_COL_RESPONSE, '')

    def getDebuggerErrorString(self, errocode):
        return DebuggerUtils.getErrorString(errocode)
    
    def handleDebuggerResponse(self, rsp, commandInfo):
        wx.CallAfter(self.__handleDebuggerResponse, (rsp, commandInfo))
        
    def _buttonDebuggerScriptStepOnButtonClick(self, event):
        # Get selected item;
        selectedRows = self._listctrlDebuggerScriptCommand.GetSelectedRows()
        rowIndex = 0
        if len(selectedRows) > 0:
            rowIndex = selectedRows[0]
        
        # Run current selected item;
        commandName = self._listctrlDebuggerScriptCommand.GetCellValue(rowIndex, COMMAND_LIST_COL_COMMAND_NAME)
        commandValue = self._listctrlDebuggerScriptCommand.GetCellValue(rowIndex, COMMAND_LIST_COL_COMMAND_VALUE)
        self.__controller.debuggerCommand(rowIndex, commandName, Util.s2vs(commandValue))
        
        # Select next item;
        if (rowIndex + 1) < self._listctrlDebuggerScriptCommand.GetNumberRows():
            self._listctrlDebuggerScriptCommand.SelectRow(rowIndex + 1)
    
    def __refreshCommandItemIndex(self):
        rowsNumber = self._listctrlDebuggerScriptCommand.GetNumberRows()
        for i in range(rowsNumber):
            self._listctrlDebuggerScriptCommand.SetCellValue(i, COMMAND_LIST_COL_INDEX, '%d' %(i))
        
    def _buttonDebuggerScriptRunOnButtonClick(self, event):
        commands = []
        
        rowsNumber = self._listctrlDebuggerScriptCommand.GetNumberRows()
        for i in range(rowsNumber):
            commandName = self._listctrlDebuggerScriptCommand.GetCellValue(i, COMMAND_LIST_COL_COMMAND_NAME)
            commandValue = self._listctrlDebuggerScriptCommand.GetCellValue(i, COMMAND_LIST_COL_COMMAND_VALUE)
            commands.append((i, commandName, Util.s2vs(commandValue)))
        
        self.__controller.clearDebuggerVariables()
        self.__controller.debuggerCommands(commands)
    
    def _buttonDebuggerScriptItemDeleteOnButtonClick(self, event):
        selectedRows = self._listctrlDebuggerScriptCommand.GetSelectedRows()
        if len(selectedRows) == 0:
            return

        selectedRows.sort()
        selectedRows.reverse()
        for selectedRow in selectedRows:
            self._listctrlDebuggerScriptCommand.DeleteRows(selectedRow)
        
        self.__refreshCommandItemIndex()
    
    def __debuggerScriptItemSwitch(self, item1, item2):
        commandName1 = self._listctrlDebuggerScriptCommand.GetCellValue(item1, COMMAND_LIST_COL_COMMAND_NAME)
        commandValue1 = self._listctrlDebuggerScriptCommand.GetCellValue(item1, COMMAND_LIST_COL_COMMAND_VALUE)
        commandDescription1 = self._listctrlDebuggerScriptCommand.GetCellValue(item1, COMMAND_LIST_COL_DESCRIPTION)
        commandName2 = self._listctrlDebuggerScriptCommand.GetCellValue(item2, COMMAND_LIST_COL_COMMAND_NAME)
        commandValue2 = self._listctrlDebuggerScriptCommand.GetCellValue(item2, COMMAND_LIST_COL_COMMAND_VALUE)
        commandDescription2 = self._listctrlDebuggerScriptCommand.GetCellValue(item2, COMMAND_LIST_COL_DESCRIPTION)
        
        self._listctrlDebuggerScriptCommand.SetCellValue(item1, COMMAND_LIST_COL_COMMAND_NAME, commandName2)
        self._listctrlDebuggerScriptCommand.SetCellValue(item1, COMMAND_LIST_COL_COMMAND_VALUE, commandValue2)
        self._listctrlDebuggerScriptCommand.SetCellValue(item1, COMMAND_LIST_COL_RESPONSE, '')
        self._listctrlDebuggerScriptCommand.SetCellValue(item1, COMMAND_LIST_COL_DESCRIPTION, commandDescription2)

        self._listctrlDebuggerScriptCommand.SetCellValue(item2, COMMAND_LIST_COL_COMMAND_NAME, commandName1)
        self._listctrlDebuggerScriptCommand.SetCellValue(item2, COMMAND_LIST_COL_COMMAND_VALUE, commandValue1)
        self._listctrlDebuggerScriptCommand.SetCellValue(item2, COMMAND_LIST_COL_RESPONSE, '')
        self._listctrlDebuggerScriptCommand.SetCellValue(item2, COMMAND_LIST_COL_DESCRIPTION, commandDescription1)
    
    def __debuggerScriptItemUp(self, item):
        if item == 0:
            return

        itemUpped = item - 1;
        self.__debuggerScriptItemSwitch(item, itemUpped)
        self._listctrlDebuggerScriptCommand.SelectRow(itemUpped)
    
    def __debuggerScriptItemDown(self, item):
        itemDowned = item + 1;
        if itemDowned >= self._listctrlDebuggerScriptCommand.GetNumberRows():
            return
        
        self.__debuggerScriptItemSwitch(item, itemDowned)
        self._listctrlDebuggerScriptCommand.SelectRow(itemDowned)
    
    def _buttonDebuggerScriptItemUpOnButtonClick(self, event):
        selectedRows = self._listctrlDebuggerScriptCommand.GetSelectedRows()
        if len(selectedRows) == 0:
            return
        
        selectedRows.sort()
        for selectedRow in selectedRows:
            self.__debuggerScriptItemUp(selectedRow);
    
    def _buttonDebuggerScriptItemDownOnButtonClick(self, event):
        selectedRows = self._listctrlDebuggerScriptCommand.GetSelectedRows()
        if len(selectedRows) == 0:
            return

        selectedRows.sort()
        for selectedRow in selectedRows:
            self.__debuggerScriptItemDown(selectedRow);

    def __handleDebuggerProcessing(self, commandInfo):
        commandIndex = commandInfo[0]
        self._listctrlDebuggerScriptCommand.SetCellTextColour(commandIndex, COMMAND_LIST_COL_DESCRIPTION, 'Processing ...')
    
    def handleDebuggerProcessing(self, commandInfo):
        wx.CallAfter(self.__handleDebuggerProcessing, commandInfo)

    def __debuggerScript_Load(self, scriptPathName):
        self.__controller.loadDebuggerScript(scriptPathName)

    def __debuggerScript_Save(self, scriptPathName):
        rowsinfo = []
        for i in range(self._listctrlDebuggerScriptCommand.GetNumberRows()):
            commandName = self._listctrlDebuggerScriptCommand.GetCellValue(i, COMMAND_LIST_COL_COMMAND_NAME)
            commandValue = self._listctrlDebuggerScriptCommand.GetCellValue(i, COMMAND_LIST_COL_COMMAND_VALUE)
            rowsinfo.append((commandName, commandValue))
        
        self.__controller.saveDebuggerScript(scriptPathName, rowsinfo)
    
    def _buttonDebuggerScriptLoadFileOnButtonClick(self, event):
#         scriptPathName = self._textctrlDebuggerScriptFilePathName.GetValue()
#         if len(scriptPathName) == 0:
        saveFileDialog = wx.FileDialog(self, "Load smartcard debugger script file ...", "", "", "SCD files (*.scd)|*.scd", wx.FD_OPEN | wx.FILE_MUST_EXIST )
        if saveFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        scriptPathName = saveFileDialog.GetPath()
        self._textctrlDebuggerScriptFilePathName.SetValue(scriptPathName)
        self.__debuggerScript_Load(scriptPathName);
    
    def _buttonDebuggerScriptSaveFileOnButtonClick(self, event):
        scriptPathName = self._textctrlDebuggerScriptFilePathName.GetValue()
        if len(scriptPathName) == 0:
            saveFileDialog = wx.FileDialog(self, "Save smartcard debugger script file ...", "", "", "SCD files (*.scd)|*.scd", wx.FD_SAVE )
            if saveFileDialog.ShowModal() == wx.ID_CANCEL:
                return
            scriptPathName = saveFileDialog.GetPath()
            self._textctrlDebuggerScriptFilePathName.SetValue(scriptPathName)
        self.__debuggerScript_Save(scriptPathName);
    
    def _buttonDebuggerScriptStopOnButtonClick(self, event):
        self.__controller.debuggerCommandsStop()

    def _buttonClearLogOnButtonClick(self, event):
        self._textctrlLog.SetValue('')
        
    def __handleLoadDebuggerScriptEnd(self, commandsInfo):
        self._listctrlDebuggerScriptCommand.InsertRows(0, len(commandsInfo))
        for i in range(len(commandsInfo)):
            commandInfo = commandsInfo[i]
            self._listctrlDebuggerScriptCommand.SetCellValue(i, COMMAND_LIST_COL_INDEX, '%d' %(i))
            self._listctrlDebuggerScriptCommand.SetCellValue(i, COMMAND_LIST_COL_COMMAND_NAME, commandInfo[0])
            self._listctrlDebuggerScriptCommand.SetCellValue(i, COMMAND_LIST_COL_COMMAND_VALUE, commandInfo[1])
    
    def handleLoadDebuggerScriptEnd(self, commandsInfo):
        wx.CallAfter(self.__handleLoadDebuggerScriptEnd, commandsInfo)
    
    def __handleLoadDebuggerScriptBegin(self):
        rowsNumber = self._listctrlDebuggerScriptCommand.GetNumberRows()
        if rowsNumber > 0:
            self._listctrlDebuggerScriptCommand.DeleteRows(0, rowsNumber)
     
    def handleLoadDebuggerScriptBegin(self):
        wx.CallAfter(self.__handleLoadDebuggerScriptBegin)
    
