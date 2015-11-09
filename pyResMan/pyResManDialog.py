# -*- coding:utf8 -*-

'''
Created on 2015-10-27

@author: javacardos@gmail.com
@organization: http://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

import wx
from wx import DEFAULT_DIALOG_STYLE, Size, BoxSizer, ListItem, StaticLine, TextAttr
from pyResManReader import pyResManReader
from smartcard.Exceptions import NoCardException
from pyResManController import pyResManController, APDUItem
from APDUEditCtrl import APDUByteEditCtrl
import os
from wx.lib.masked.numctrl import NumCtrl
from Util import Util
from datetime import datetime


class pyResManDialog(wx.Dialog):
    '''
    The main frame of this application.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        wx.Dialog.__init__(self, None, title="pyResMan", style=DEFAULT_DIALOG_STYLE)
        
        self.__InitControls()
        self.__InitControlsData()
        self.__InitController()
        self.__BindControlEvents()
    
    def __InitControls(self):
        # Main panel;
        self.__panel = wx.Panel(self)

        # Sizers;
        # Main sizer;
        self.__mainSizer = BoxSizer(wx.VERTICAL)
        # Reader sizer;
        self.__readerSizer = BoxSizer(wx.HORIZONTAL)
        # Transmit sizer;
        self.__transmitSizer = BoxSizer(wx.VERTICAL)
        self.__commandSizer = BoxSizer(wx.HORIZONTAL)
        self.__flagSizer = BoxSizer(wx.HORIZONTAL)
        # Script send sizer;
        self.__scriptSizer = BoxSizer(wx.HORIZONTAL)
        # Log sizer;
        self.__logSizer = BoxSizer(wx.VERTICAL)
        # Status bar sizer;
        self.__aboutBarSizer = BoxSizer(wx.HORIZONTAL)
 
        # Reader list;
        self.__readerListBox = wx.ComboBox(self.__panel, size=Size(530, 25), style=wx.CB_DROPDOWN | wx.CB_READONLY)
        # Protocol list;
        self.__protocolListBox = wx.ComboBox(self.__panel, size=Size(60, 25), style=wx.CB_DROPDOWN | wx.CB_READONLY)
        # Mode list;
        self.__modeListBox = wx.ComboBox(self.__panel, size=Size(85, 25), style=wx.CB_DROPDOWN | wx.CB_READONLY)
        # Connect button;
        self.__connectButton = wx.Button(self.__panel, size=Size(75, 25), label="&Connect")
        # Transmit controls;
        byteSize = Size(25, 20)
        self.__clsEditor = APDUByteEditCtrl(self.__panel, size=byteSize, value='00')
        self.__insEditor = APDUByteEditCtrl(self.__panel, size=byteSize, value='A4')
        self.__p1Editor = APDUByteEditCtrl(self.__panel, size=byteSize, value='04')
        self.__p2Editor = APDUByteEditCtrl(self.__panel, size=byteSize, value='00')
        self.__lcEditor = APDUByteEditCtrl(self.__panel, size=byteSize, value='00', style=wx.TE_READONLY)
        self.__dataEditor = wx.TextCtrl(self.__panel, size=Size(800 - (25 * 6) - (10 * 8), 20))
        self.__leEditor = APDUByteEditCtrl(self.__panel, size=byteSize, value='00')
        self.__transmitButton = wx.Button(self.__panel, label="&Transmit")
        self.__autoGetResponseCheckBox = wx.CheckBox(self.__panel, label="&Auto GetResponse")
        
        # Script controls;
        self.__scriptPathNameEditor = wx.TextCtrl(self.__panel, style=wx.TE_READONLY, size=wx.Size(800 - 80 * 4, wx.DefaultSize[1]))
        self.__scriptBrowseButton = wx.Button(self.__panel, label='...')
        self.__scriptLoopCountEditor = NumCtrl(self.__panel, value=1)
        self.__scriptRunScriptButton = wx.Button(self.__panel, label='&Run')

        # Reader sizer elements;
        self.__readerSizer.AddSpacer(10)
        self.__readerSizer.Add(self.__readerListBox)
        self.__readerSizer.AddSpacer(10)
        self.__readerSizer.Add(self.__protocolListBox)
        self.__readerSizer.AddSpacer(10)
        self.__readerSizer.Add(self.__modeListBox)
        self.__readerSizer.AddSpacer(10)
        self.__readerSizer.Add(self.__connectButton)
        
        # Command sizer elements;
        self.__commandSizer.AddSpacer(10)
        self.__commandSizer.Add(self.__clsEditor)
        self.__commandSizer.AddSpacer(10)
        self.__commandSizer.Add(self.__insEditor)
        self.__commandSizer.AddSpacer(10)
        self.__commandSizer.Add(self.__p1Editor)
        self.__commandSizer.AddSpacer(10)
        self.__commandSizer.Add(self.__p2Editor)
        self.__commandSizer.AddSpacer(10)
        self.__commandSizer.Add(self.__lcEditor)
        self.__commandSizer.AddSpacer(10)
        self.__commandSizer.Add(self.__dataEditor)
        self.__commandSizer.AddSpacer(10)
        self.__commandSizer.Add(self.__leEditor)

        # Flag sizer elements;
        self.__flagSizer.AddSpacer(10)
        self.__flagSizer.Add(self.__autoGetResponseCheckBox)
        self.__flagSizer.AddSpacer(10)
        self.__flagSizer.Add(self.__transmitButton)
        
        # Transmit sizer elements;
        self.__transmitSizer.Add(self.__commandSizer)
        self.__transmitSizer.AddSpacer(10)
        self.__transmitSizer.Add(self.__flagSizer)
        
        self.__scriptSizer.AddSpacer(10)
        self.__scriptSizer.Add(self.__scriptPathNameEditor)
        self.__scriptSizer.AddSpacer(10)
        self.__scriptSizer.Add(self.__scriptBrowseButton)
        self.__scriptSizer.AddSpacer(10)
        self.__scriptSizer.Add(self.__scriptLoopCountEditor)
        self.__scriptSizer.AddSpacer(10)
        self.__scriptSizer.Add(self.__scriptRunScriptButton)
        self.__scriptSizer.AddSpacer(10)

        # Log elements;
        self.__logTextCtrl = wx.TextCtrl(self.__panel, size = Size(800, 300), style=wx.TE_RICH | wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_AUTO_SCROLL | wx.TE_DONTWRAP)
        self.__logger = wx.LogTextCtrl(self.__logTextCtrl)
        self.__apduListView = wx.ListView(self.__panel, size = Size(800, 350))
        self.__apduListView.InsertColumn(0, 'Index', width=50)
        self.__apduListView.InsertColumn(1, 'Command', width=200)
        self.__apduListView.InsertColumn(2, 'Response', width=300)
        self.__apduListView.InsertColumn(3, 'TimeSpent', width=100)
        self.__apduListView.InsertColumn(4, 'DateTime', width=120)
        self.__logSizer.AddSpacer(10)
        self.__logSizer.Add(self.__apduListView)
        self.__logSizer.AddSpacer(10)
        self.__logSizer.Add(self.__logTextCtrl)
        
        # Status bar elements;
        self.__aboutBarSizer.AddSpacer(15)
        self.__authorCtrl = wx.StaticText(self.__panel, label="JavaCardOS Technologies. All rights reserved.")
        self.__aboutBarSizer.Add(self.__authorCtrl)
        self.__aboutBarSizer.AddSpacer(15)
        self.__websiteCtrl = wx.HyperlinkCtrl(self.__panel, label="Website: http://www.javacardos.com/", url="http://www.javacardos.com/")
        self.__aboutBarSizer.Add(self.__websiteCtrl)
        self.__aboutBarSizer.AddSpacer(15)
        self.__forumCtrl = wx.HyperlinkCtrl(self.__panel, label="Discussion: http://www.javacardos.com/javacardforum/", url="http://www.javacardos.com/javacardforum/viewforum.php?f=39")
        self.__aboutBarSizer.Add(self.__forumCtrl)
        
        self.__mainSizer.AddSpacer(10)
        self.__mainSizer.Add(self.__readerSizer)
        self.__mainSizer.AddSpacer(10)
        self.__mainSizer.Add(StaticLine(self.__panel, size=Size(800, 3)))
        self.__mainSizer.AddSpacer(10)
        self.__mainSizer.Add(self.__transmitSizer)
        self.__mainSizer.AddSpacer(10)
        self.__mainSizer.Add(StaticLine(self.__panel, size=Size(800, 3)))
        self.__mainSizer.AddSpacer(10)
        self.__mainSizer.Add(self.__scriptSizer)
        self.__mainSizer.AddSpacer(10)
        self.__mainSizer.Add(StaticLine(self.__panel, size=Size(800, 3)))
        self.__mainSizer.AddSpacer(10)
        self.__mainSizer.Add(self.__logSizer)
        self.__mainSizer.AddSpacer(10)
        self.__mainSizer.Add(self.__aboutBarSizer)
        self.__mainSizer.AddSpacer(5)
        
        self.__panel.SetSizerAndFit(self.__mainSizer)
        self.Fit()

    def __InitControlsData(self):
        
        # Initialize readername list;
        self.__readernames = pyResManReader.getReaderList()
        self.__readerListBox.Set(self.__readernames)
        self.__readerListBox.SetSelection(0)
        
        self.protocols = ['T0', 'T1', 'T0/T1']
        self.__protocolListBox.Set(self.protocols)
        self.__protocolListBox.SetSelection(0)
        
        self.__modes = ['EXCLUSIVE', 'SHARED']
        self.__modeListBox.Set(self.__modes)
        self.__modeListBox.SetSelection(0)
    
    def __BindControlEvents(self):
        
        self.Bind(wx.EVT_BUTTON, self._onEventButton)
        self.Bind(wx.EVT_TEXT, self._onEventText)
        self.__apduListView.Bind(wx.EVT_CONTEXT_MENU, self._onApduListView_ContextMenu)
#         self.__logTextCtrl.Bind(wx.EVT_CONTEXT_MENU, self._onLogTextCtrl_ContextMenu)
    
    def _onApduListView_ContextMenu(self, event):
        """Display apdu list view popup menu;"""
        self.__apduListViewPopupMenu = wx.Menu()
        self.__apduListViewPopupMenu.Append(1, "Run")
        self.__apduListViewPopupMenu.AppendSeparator()
        self.__apduListViewPopupMenu.Append(0, "Clear")
        self.__apduListViewPopupMenu.Bind(wx.EVT_MENU, self.__onApduListView_MenuClick)
        self.__apduListView.PopupMenu(self.__apduListViewPopupMenu)
# 
#     def _onLogTextCtrl_ContextMenu(self, event):
#         """Display log text edit popup menu;"""
#         self.logTextCtrlPopupMenu = wx.Menu()
#         self.logTextCtrlPopupMenu.Append(0, "Clear")
#         self.logTextCtrlPopupMenu.Bind(wx.EVT_MENU, self._onLogTextCtrl_MenuClick)
#         self.__logTextCtrl.PopupMenu(self.logTextCtrlPopupMenu)
    
    def __onApduListView_MenuClick(self, event):
        menuItemIndex = event.Id
        if menuItemIndex == 0:
            self.__apduListView.DeleteAllItems()
        elif menuItemIndex == 1:
            self.__runApduListSelectItems()
# 
#     def _onLogTextCtrl_MenuClick(self, event):
#         menuItemIndex = event.Id
#         if menuItemIndex == 0:
#             self.__logTextCtrl.Clear()
    
    def __runApduListSelectItems(self):
        """Transmit selected items apdu in the apdu list view;"""
        apduItems = []
        selectedItem = self.__apduListView.GetFirstSelected()
        while (selectedItem != -1):
            listItem = self.__apduListView.GetItem(selectedItem, 1)
            apduItem = APDUItem(listItem.GetText(), (selectedItem, ))
            apduItems.append(apduItem)
            selectedItem = self.__apduListView.GetNextSelected(selectedItem)
        
        t0AutoGetResponse = self.__autoGetResponseCheckBox.GetValue()
        self.__controller.transmitAPDUItems(apduItems, t0AutoGetResponse)

    def __onConnect(self):
        if (self.__connectButton.GetLabelText() == 'Connect'):
            try:
                # Get smartcard reader name;
                readername = self.__readerListBox.GetString(self.__readerListBox.GetSelection())
                protocolIndex = self.__protocolListBox.GetSelection()
                
                # Get protocol value;
                protocol = pyResManReader.SCARD_PROTOCOL_UNDEFINED
                if protocolIndex == 0:
                    protocol = pyResManReader.SCARD_PROTOCOL_T0
                elif protocolIndex == 1:
                    protocol = pyResManReader.SCARD_PROTOCOL_T1
                
                # Get mode value;
                modeIndex = self.__modeListBox.GetSelection()
                mode = pyResManReader.SCARD_SHARE_SHARED
                if modeIndex == 0:
                    mode = pyResManReader.SCARD_SHARE_EXCLUSIVE

                # Connect to the card;
                # Set AutoResponse when connect with protocol T0;
                if (protocol == pyResManReader.SCARD_PROTOCOL_T0):
                    self.__autoGetResponseCheckBox.SetValue(True)
                
                self.__controller.connect(readername, protocol, mode)
                self.__controller.monitorCard()
                
                # Set status;
                self.__connectButton.SetLabel('Disconnect')
            except NoCardException, e:
                self.__Log('NoCardException: ' + e.args[1], wx.LOG_Error)
            except Exception, e:
                self.__Log('Exception: ' + str(e), wx.LOG_Error)
        else:
            try:
                # Disconnect;
                self.__controller.disconnect()
                
                # Set status;
                self.__connectButton.SetLabel('Connect')
            except NoCardException, e:
                self.__Log('NoCardException: %s' %(e.args[1]), wx.LOG_Error)
            except Exception, e:
                self.__Log('Exception: ' %(str(e)), wx.LOG_Error)
    
    def __onTransmit(self):
        cls = self.__clsEditor.GetValue()
        ins = self.__insEditor.GetValue()
        p1 = self.__p1Editor.GetValue()
        p2 = self.__p2Editor.GetValue()
        lc = self.__lcEditor.GetValue()
        data = self.__dataEditor.GetValue()
        le = self.__leEditor.GetValue()
        
        if (len(cls) == 0) or (len(ins) == 0) or (len(p1) == 0) or (len(p2) == 0):
            self.__Log('Please input command field.', wx.LOG_Error)
            return
        
        commandText = ''
        if lc != '00':
            commandText = "%s%s%s%s%s %s %s" %(cls, ins, p1, p2, lc, data, le)
        else:
            commandText = "%s%s%s%s %s" %(cls, ins, p1, p2, le)            
        
        # Get t0 auto getresponse value;
        autoGetResponse = self.__autoGetResponseCheckBox.GetValue()
        
        # Transmit;
        self.__controller.transmit(commandText, autoGetResponse)
    
    def _onEventButton(self, event):
        controlId = event.Id
        if (controlId == self.__connectButton.Id):
            self.__onConnect()
        elif (controlId == self.__transmitButton.Id):
            self.__onTransmit()
        elif (controlId == self.__scriptBrowseButton.Id):
            self.__onBrowseScriptFile()
        elif (controlId == self.__scriptRunScriptButton.Id):
            self.__onRunScript()
    
    def _onEventText(self, event):
        if (event.Id == self.__clsEditor.Id):
            self.__onChar_Cls(event)
        elif (event.Id == self.__insEditor.Id):
            self.__onChar_Ins(event)
        elif (event.Id == self.__p1Editor.Id):
            self.__onChar_P1(event)
        elif (event.Id == self.__p2Editor.Id):
            self.__onChar_P2(event)
        elif (event.Id == self.__dataEditor.Id):
            self.__onChar_Data(event)
        elif (event.Id == self.__leEditor.Id):
            self.__onChar_Le(event)
        else:
            pass
    
    def __onChar_Cls(self, event):
        """Implement next version;"""
        pass
    
    def __onChar_Ins(self, event):
        """Implement next version;"""
        pass
    
    def __onChar_P1(self, event):
        """Implement next version;"""
        pass
    
    def __onChar_P2(self, event):
        """Implement next version;"""
        pass
    
    def __onChar_Data(self, event):
        """Implement next version;"""
        dataLen = len(event.String)
        dataLen = dataLen / 2
        self.__lcEditor.SetValue("%02X" %(dataLen))
    
    def __onChar_Le(self, event):
        """Implement next version;"""
        pass
    
    def __InitController(self):
        """Init controller for logical operations, self as the view;"""
        self.__controller = pyResManController(self)
    
    def handleCardRemoved(self, name):
        self.__Log('Card is removed.', wx.LOG_Warning)
        self.__connectButton.SetLabel('Connect')

    def handleCardInserted(self, name):
        pass
    
    def __relistReaders(self):
        """Relist reader names, when reader added/removed;"""
        readers = self.__controller.getReaderList()
        self.__readerListBox.Clear()
        for reader in readers:
            self.__readerListBox.Append(reader)
        self.__readerListBox.SetSelection(0)
        self.__readerListBox.Fit()

    def handleReaderAdded(self, name):
        self.__relistReaders()
    
    def handleReaderRemoved(self, name):
        self.__relistReaders()
    
    def __onBrowseScriptFile(self):
        defaultDir = self.__scriptPathNameEditor.GetValue()
        if not os.path.exists(defaultDir):
            defaultDir = os.getcwd()
        fileDialog = wx.FileDialog(self, defaultDir = defaultDir)
        ret = fileDialog.ShowModal()
        if (ret != wx.ID_CANCEL):
            filepath = fileDialog.GetPath()
            self.__scriptPathNameEditor.SetValue(filepath)
        else:
            pass
    
    def __onRunScript(self):
        if (not self.__controller.runningScript()):
            scriptPathName = self.__scriptPathNameEditor.GetValue()
            if not os.path.exists(scriptPathName):
                self.__onBrowseScriptFile()
                scriptPathName = self.__scriptPathNameEditor.GetValue()
            if not os.path.exists(scriptPathName):
                self.__Log('User cancel operation.', wx.LOG_Warning)
                return
    
            # Get t0 auto getresponse value;
            autoGetResponse = self.__autoGetResponseCheckBox.GetValue()
            # Get loop count;
            scriptLoopCount = self.__scriptLoopCountEditor.GetValue()
    
            self.__controller.runScript(scriptPathName, scriptLoopCount, autoGetResponse)
        else:
            self.__controller.stopScript()
            
    def __apduListView_scrollToLine(self, lineIndex):
        scrollPos = self.__apduListView.GetScrollPos(wx.VERTICAL)
        self.__apduListView.ScrollLines(lineIndex - scrollPos)
    
    def handleAPDUCommand(self, commandStr, args=tuple()):
        """Handle controller's apdu command event, to display apdu command;"""
        itemIndex = 0
        if len(args) == 0:
            itemIndex = self.__apduListView.GetItemCount()
            indexItem = ListItem()
            indexItem.SetId(itemIndex)
            indexItem.SetColumn(0)
            indexItem.SetText('> %d' %(itemIndex))
            self.__apduListView.InsertItem(indexItem)
        else:
            itemIndex = args[0]
            indexItem = ListItem()
            indexItem.SetId(itemIndex)
            indexItem.SetColumn(0)
            indexItem.SetText('> %d' %(itemIndex))
            self.__apduListView.SetItem(indexItem)
        
        commandItem = ListItem()
        commandItem.SetId(itemIndex)
        commandItem.SetColumn(1)
        commandItem.SetText(commandStr)
        self.__apduListView.SetItem(commandItem)

        datetimeItem = ListItem()
        datetimeItem.SetId(itemIndex)
        datetimeItem.SetColumn(4)
        datetimeItem.SetText(datetime.now().strftime("%c"))
        self.__apduListView.SetItem(datetimeItem)
        
        self.__apduListView_scrollToLine(itemIndex)
    
    def handleAPDUResponse(self, responseStr, transtime, args=tuple()):
        """Handle controller's apdu response event, to display apdu result informations;"""
        itemIndex = 0
        if len(args) == 0:
            itemIndex = self.__apduListView.GetItemCount() - 1
        else:
            itemIndex = args[0]
        responseItem = ListItem()
        responseItem.SetId(itemIndex)
        responseItem.SetColumn(2)
        responseItem.SetText(responseStr)
        self.__apduListView.SetItem(responseItem)

        timeItem = ListItem()
        timeItem.SetId(itemIndex)
        timeItem.SetColumn(3)
        timeItem.SetText(Util.getTimeStr(transtime))
        self.__apduListView.SetItem(timeItem)

        indexItem = ListItem()
        indexItem.SetId(itemIndex)
        indexItem.SetColumn(0)
        indexItem.SetText('%d' %(itemIndex))
        self.__apduListView.SetItem(indexItem)

    def __Log(self, msg, level=wx.LOG_Info):
        """Display log with levels"""
        color = wx.Colour(0, 0, 0)
        if level == wx.LOG_Info:
            color = wx.Colour(0x22, 0x8B, 0x22)
        elif level == wx.LOG_Error:
            color = wx.Colour(255, 0, 0)
        elif level == wx.LOG_Warning:
            color = wx.Colour(0, 0, 255)
        else:
            pass
        
        self.__logTextCtrl.SetDefaultStyle(TextAttr(color))
        self.__logger.LogText(msg)
    
    def handleLog(self, msg, level=wx.LOG_Info):
        self.__Log(msg, level)
    
    def handleScriptBegin(self, status):
        self.__scriptRunScriptButton.SetLabel('Stop')

    def handleScriptEnd(self, status):
        self.__scriptRunScriptButton.SetLabel('Start')

    def handleException(self, e):
        try:
            self.__Log('Exception: %s' %(e.message), wx.LOG_Error)
        except:
            try:
                self.__Log('Exception: %s' %(str(e)), wx.LOG_Error)
            except:
                self.__Log('Transmit exceptin occured.', wx.LOG_Error)
