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
from pyResMan_InstallDialog import pyResMan_InstallDialog

# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class MyFrame1
###########################################################################

# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

###########################################################################
## Class MyFrame1
###########################################################################

class pyResManDialog ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 983,568 ), style = wx.DEFAULT_FRAME_STYLE|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        mainSizer = wx.BoxSizer( wx.VERTICAL )
        
        __connectSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"ReaderName", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        __connectSizer.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        __readernameComboBoxChoices = pyResManReader.getReaderList()
        self.__readernameComboBox = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), __readernameComboBoxChoices, wx.CB_READONLY )
        self.__readernameComboBox.SetSelection( 0 )
        __connectSizer.Add( self.__readernameComboBox, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Protocol", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        __connectSizer.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        __protocolComboBoxChoices = [ u"T0", u"T1", u"T0/T1" ]
        self.__protocolComboBox = wx.ComboBox( self, wx.ID_ANY, u"T0/T1", wx.DefaultPosition, wx.Size( 75,-1 ), __protocolComboBoxChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
        self.__protocolComboBox.SetSelection( 2 )
        __connectSizer.Add( self.__protocolComboBox, 0, wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Mode", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        __connectSizer.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        __modeComboBoxChoices = [ u"EXCLUSIVE", u"SHARED" ]
        self.__modeComboBox = wx.ComboBox( self, wx.ID_ANY, u"SHARED", wx.DefaultPosition, wx.DefaultSize, __modeComboBoxChoices, wx.CB_READONLY )
        self.__modeComboBox.SetSelection( 1 )
        __connectSizer.Add( self.__modeComboBox, 0, wx.ALL, 5 )
        
        self.__connectButton = wx.Button( self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
        __connectSizer.Add( self.__connectButton, 0, wx.ALL, 5 )
        
        
        mainSizer.Add( __connectSizer, 0, wx.EXPAND, 5 )
        
        bSizer46 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_splitter2 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
        self.m_splitter2.SetSashGravity( 0.6 )
        self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )
        self.m_splitter2.SetMinimumPaneSize( 1 )
        
        self.m_panel14 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer47 = wx.BoxSizer( wx.VERTICAL )
        
        self.__pagesNoteBook = wx.Notebook( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.__pagesNoteBook.SetMinSize( wx.Size( -1,300 ) )
        
        self.__apduPagePanel = wx.Panel( self.__pagesNoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        __apduPageSizer = wx.BoxSizer( wx.VERTICAL )
        
        __apduSizer = wx.BoxSizer( wx.VERTICAL )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.__claTextCtrl = wx.TextCtrl( self.__apduPagePanel, wx.ID_ANY, '00', wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self.__claTextCtrl.SetMaxLength( 2 ) 
        bSizer4.Add( self.__claTextCtrl, 0, wx.ALL, 5 )
        
        self.__insTextCtrl = wx.TextCtrl( self.__apduPagePanel, wx.ID_ANY, 'A4', wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self.__insTextCtrl.SetMaxLength( 2 ) 
        bSizer4.Add( self.__insTextCtrl, 0, wx.ALL, 5 )
        
        self.__p1TextCtrl = wx.TextCtrl( self.__apduPagePanel, wx.ID_ANY, '04', wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self.__p1TextCtrl.SetMaxLength( 2 ) 
        bSizer4.Add( self.__p1TextCtrl, 0, wx.ALL, 5 )
        
        self.__p2TextCtrl = wx.TextCtrl( self.__apduPagePanel, wx.ID_ANY, '00', wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self.__p2TextCtrl.SetMaxLength( 2 ) 
        bSizer4.Add( self.__p2TextCtrl, 0, wx.ALL, 5 )
        
        self.__lcTextCtrl = wx.TextCtrl( self.__apduPagePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.TE_READONLY )
        self.__lcTextCtrl.SetMaxLength( 2 ) 
        bSizer4.Add( self.__lcTextCtrl, 0, wx.ALL, 5 )
        
        self.__dataTextCtrl = wx.TextCtrl( self.__apduPagePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer4.Add( self.__dataTextCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.__leTextCtrl = wx.TextCtrl( self.__apduPagePanel, wx.ID_ANY, '00', wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self.__leTextCtrl.SetMaxLength( 2 ) 
        bSizer4.Add( self.__leTextCtrl, 0, wx.ALL, 5 )
        
        bSizer5.Add( bSizer4, 0, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.__autoGetResponseCheckBox = wx.CheckBox( self.__apduPagePanel, wx.ID_ANY, u"Auto GET RESPONSE", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.__autoGetResponseCheckBox, 0, wx.ALL, 5 )
        
        self.__transmitButton = wx.Button( self.__apduPagePanel, wx.ID_ANY, u"Transmit", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.__transmitButton, 0, wx.ALL, 5 )
        
        
        bSizer5.Add( bSizer6, 0, wx.EXPAND, 5 )
        
        
        __apduSizer.Add( bSizer5, 0, wx.EXPAND, 5 )
        
        
        __apduPageSizer.Add( __apduSizer, 0, wx.EXPAND, 5 )
        
        self.__apduListCtrl = wx.ListCtrl( self.__apduPagePanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 820,-1 ), wx.LC_REPORT )
        self.__apduListCtrl.InsertColumn(0, 'Index', width=50)
        self.__apduListCtrl.InsertColumn(1, 'Command', width=200)
        self.__apduListCtrl.InsertColumn(2, 'Response', width=300)
        self.__apduListCtrl.InsertColumn(3, 'TimeSpent', width=100)
        self.__apduListCtrl.InsertColumn(4, 'DateTime', width=120)
        __apduPageSizer.Add( self.__apduListCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.__apduPagePanel.SetSizer( __apduPageSizer )
        self.__apduPagePanel.Layout()
        __apduPageSizer.Fit( self.__apduPagePanel )
        self.__pagesNoteBook.AddPage( self.__apduPagePanel, u"Basic APDU", True )
        self.__gpPagePanel = wx.Panel( self.__pagesNoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        __gpPageSizer = wx.BoxSizer( wx.VERTICAL )
        
        bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
        
        __scpRadioBoxChoices = [ u"SCP01", u"SCP02", u"SCP03" ]
        self.__scpRadioBox = wx.RadioBox( self.__gpPagePanel, wx.ID_ANY, u"Secure Channel Protocol", wx.DefaultPosition, wx.Size( -1,-1 ), __scpRadioBoxChoices, 1, wx.RA_SPECIFY_ROWS )
        self.__scpRadioBox.SetSelection( 2 )
        bSizer41.Add( self.__scpRadioBox, 0, wx.ALL|wx.EXPAND, 5 )
        
        bSizer52 = wx.BoxSizer( wx.VERTICAL )
        
        
        bSizer52.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        bSizer53 = wx.BoxSizer( wx.VERTICAL )
        
        self.__mutualAuthButton = wx.Button( self.__gpPagePanel, wx.ID_ANY, u"Mutual Authentication", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer53.Add( self.__mutualAuthButton, 0, wx.ALL, 5 )
        
        
        bSizer52.Add( bSizer53, 0, wx.EXPAND, 5 )
        
        
        bSizer52.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )
        
        
        __gpPageSizer.Add( bSizer41, 0, wx.EXPAND, 5 )
        
        self.m_notebook2 = wx.Notebook( self.__gpPagePanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,500 ), wx.NB_TOP )
        self.__contentManagerPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer231 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer30 = wx.BoxSizer( wx.VERTICAL )
        
        self.__capFilePicker = wx.FilePickerCtrl( self.__contentManagerPage, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.cap", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer30.Add( self.__capFilePicker, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer231.Add( bSizer30, 0, wx.EXPAND, 5 )
        
        bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.__capFileInformationTreeCtrl = wx.TreeCtrl( self.__contentManagerPage, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TR_DEFAULT_STYLE )
        bSizer31.Add( self.__capFileInformationTreeCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        bSizer50 = wx.BoxSizer( wx.VERTICAL )
        
        
        bSizer50.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.__loadButton = wx.Button( self.__contentManagerPage, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer50.Add( self.__loadButton, 0, wx.ALL, 5 )
        
        self.__installButton = wx.Button( self.__contentManagerPage, wx.ID_ANY, u"Install", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer50.Add( self.__installButton, 0, wx.ALL, 5 )
        
        
        bSizer50.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer31.Add( bSizer50, 0, wx.EXPAND, 5 )
        
        
        bSizer231.Add( bSizer31, 1, wx.EXPAND, 5 )
        
        
        self.__contentManagerPage.SetSizer( bSizer231 )
        self.__contentManagerPage.Layout()
        bSizer231.Fit( self.__contentManagerPage )
        self.m_notebook2.AddPage( self.__contentManagerPage, u"Content Manager", True )
        self.__contentViewerPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.__contentTreeCtrl = wx.TreeCtrl( self.__contentViewerPage, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TR_DEFAULT_STYLE )
        bSizer23.Add( self.__contentTreeCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        bSizer26 = wx.BoxSizer( wx.VERTICAL )
        
        self.__refreshCardContent = wx.Button( self.__contentViewerPage, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer26.Add( self.__refreshCardContent, 0, wx.ALL, 5 )
        
        self.__installCardContent = wx.Button( self.__contentViewerPage, wx.ID_ANY, u"Install", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.__installCardContent.Enable( False )
        bSizer26.Add( self.__installCardContent, 0, wx.ALL, 5 )

        self.__selectCardContent = wx.Button( self.__contentViewerPage, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.__selectCardContent.Enable( False )
        bSizer26.Add( self.__selectCardContent, 0, wx.ALL, 5 )

        self.__deleteCardContent = wx.Button( self.__contentViewerPage, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer26.Add( self.__deleteCardContent, 0, wx.ALL, 5 )
        
        
        bSizer23.Add( bSizer26, 0, wx.EXPAND, 5 )
        
        
        self.__contentViewerPage.SetSizer( bSizer23 )
        self.__contentViewerPage.Layout()
        bSizer23.Fit( self.__contentViewerPage )
        self.m_notebook2.AddPage( self.__contentViewerPage, u"Content Viewer", False )
        self.__keyManagerPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer342 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.__keyDataListCtrl = wx.ListCtrl( self.__keyManagerPage, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_REPORT )
        self.__keyDataListCtrl.InsertColumn(0, 'index', width=50)
        self.__keyDataListCtrl.InsertColumn(1, 'KVN', width=100)
        self.__keyDataListCtrl.InsertColumn(2, 'key index', width=100)
        self.__keyDataListCtrl.InsertColumn(3, 'key type', width=100)
        self.__keyDataListCtrl.InsertColumn(4, 'key length', width=100)
        bSizer51.Add( self.__keyDataListCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer34.Add( bSizer51, 1, wx.EXPAND, 5 )
        
        bSizer40 = wx.BoxSizer( wx.VERTICAL )
        
        self.__getKeyTemplateInfoButton = wx.Button( self.__keyManagerPage, wx.ID_ANY, u"Get Key Template Information", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer40.Add( self.__getKeyTemplateInfoButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer28 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.__keyManagerPage, wx.ID_ANY, u"Key1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer29.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.__keyLen1TextCtrl = wx.TextCtrl( self.__keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.TE_READONLY )
        bSizer29.Add( self.__keyLen1TextCtrl, 0, wx.ALL, 5 )
        
        self.__key1TextCtrl = wx.TextCtrl( self.__keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.__key1TextCtrl.SetMinSize( wx.Size( 300,-1 ) )
        
        bSizer29.Add( self.__key1TextCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer28.Add( bSizer29, 1, wx.EXPAND, 5 )
        
        bSizer301 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self.__keyManagerPage, wx.ID_ANY, u"Key2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer301.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        self.__keyLen2TextCtrl = wx.TextCtrl( self.__keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.TE_READONLY )
        bSizer301.Add( self.__keyLen2TextCtrl, 0, wx.ALL, 5 )
        
        self.__key2TextCtrl = wx.TextCtrl( self.__keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.__key2TextCtrl.SetMinSize( wx.Size( 300,-1 ) )
        
        bSizer301.Add( self.__key2TextCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer28.Add( bSizer301, 1, wx.EXPAND, 5 )
        
        bSizer311 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self.__keyManagerPage, wx.ID_ANY, u"Key3", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer311.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self.__keyLen3TextCtrl = wx.TextCtrl( self.__keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.TE_READONLY )
        bSizer311.Add( self.__keyLen3TextCtrl, 0, wx.ALL, 5 )
        
        self.__key3TextCtrl = wx.TextCtrl( self.__keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.__key3TextCtrl.SetMinSize( wx.Size( 300,-1 ) )
        
        bSizer311.Add( self.__key3TextCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer28.Add( bSizer311, 1, wx.EXPAND, 5 )
        
        
        bSizer40.Add( bSizer28, 0, wx.EXPAND, 5 )
        
        bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText10 = wx.StaticText( self.__keyManagerPage, wx.ID_ANY, u"Old KVN", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        bSizer33.Add( self.m_staticText10, 0, wx.ALL, 5 )
        
        self.__oldKVNTextCtrl = wx.TextCtrl( self.__keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self.__oldKVNTextCtrl.SetMaxLength( 2 ) 
        bSizer33.Add( self.__oldKVNTextCtrl, 0, wx.ALL, 5 )
        
        self.m_staticText9 = wx.StaticText( self.__keyManagerPage, wx.ID_ANY, u"NewKVN", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer33.Add( self.m_staticText9, 0, wx.ALL, 5 )
        
        self.__newKVNTextCtrl = wx.TextCtrl( self.__keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self.__newKVNTextCtrl.SetMaxLength( 2 ) 
        bSizer33.Add( self.__newKVNTextCtrl, 0, wx.ALL, 5 )
        
        self.__putKeyButton = wx.Button( self.__keyManagerPage, wx.ID_ANY, u"Put Key", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer33.Add( self.__putKeyButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.__deleteKeyButton = wx.Button( self.__keyManagerPage, wx.ID_ANY, u"Delete Key", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer33.Add( self.__deleteKeyButton, 0, wx.ALL, 5 )
        
        self.__resetKeyButton = wx.Button( self.__keyManagerPage, wx.ID_ANY, u"Default", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer33.Add( self.__resetKeyButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        bSizer40.Add( bSizer33, 0, wx.EXPAND, 5 )
        
        
        bSizer40.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer34.Add( bSizer40, 0, wx.EXPAND, 5 )
        
        
        bSizer342.Add( bSizer34, 1, wx.EXPAND, 5 )
        
        
        self.__keyManagerPage.SetSizer( bSizer342 )
        self.__keyManagerPage.Layout()
        bSizer342.Fit( self.__keyManagerPage )
        self.m_notebook2.AddPage( self.__keyManagerPage, u"Key Manager", True )
        
        __gpPageSizer.Add( self.m_notebook2, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self.__gpPagePanel.SetSizer( __gpPageSizer )
        self.__gpPagePanel.Layout()
        __gpPageSizer.Fit( self.__gpPagePanel )
        self.__pagesNoteBook.AddPage( self.__gpPagePanel, u"GlobalPlatform", False )
        self.__scriptPagePanel = wx.Panel( self.__pagesNoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer44 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer45 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.__scriptFilePicker = wx.FilePickerCtrl( self.__scriptPagePanel, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 650,-1 ), wx.FLP_DEFAULT_STYLE )
        bSizer45.Add( self.__scriptFilePicker, 1, wx.ALL, 5 )
        
        self.__scriptRefreshButton = wx.Button( self.__scriptPagePanel, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer45.Add( self.__scriptRefreshButton, 0, wx.ALL, 5 )
        
#         self.m_staticText4 = wx.StaticText( self.__scriptPagePanel, wx.ID_ANY, u"Loop count:", wx.DefaultPosition, wx.DefaultSize, 0 )
#         self.m_staticText4.Wrap( -1 )
#         bSizer45.Add( self.m_staticText4, 0, wx.ALL, 5 )
#         
#         self.__scriptLoopCountTextCtrl = wx.TextCtrl( self.__scriptPagePanel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
#         bSizer45.Add( self.__scriptLoopCountTextCtrl, 0, wx.ALL, 5 )
        
        self.__scriptRunButton = wx.Button( self.__scriptPagePanel, wx.ID_ANY, u"Run Script", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer45.Add( self.__scriptRunButton, 0, wx.ALL, 5 )
        
        self.__scriptClearResultButton = wx.Button( self.__scriptPagePanel, wx.ID_ANY, u"Clear Result", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer45.Add( self.__scriptClearResultButton, 0, wx.ALL, 5 )
        
        
        bSizer44.Add( bSizer45, 0, wx.EXPAND, 5 )
        
        self.__scriptListCtrl = wx.ListCtrl( self.__scriptPagePanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_REPORT )
        self.__scriptListCtrl.InsertColumn(0, 'Index', width=50)
        self.__scriptListCtrl.InsertColumn(1, 'Command', width=200)
        self.__scriptListCtrl.InsertColumn(2, 'Response', width=300)
        self.__scriptListCtrl.InsertColumn(3, 'TimeSpent', width=100)
        self.__scriptListCtrl.InsertColumn(4, 'DateTime', width=120)
        bSizer44.Add( self.__scriptListCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.__scriptPagePanel.SetSizer( bSizer44 )
        self.__scriptPagePanel.Layout()
        bSizer44.Fit( self.__scriptPagePanel )
        self.__pagesNoteBook.AddPage( self.__scriptPagePanel, u"Script", False )
        self.__aboutPagePanel = wx.Panel( self.__pagesNoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer43 = wx.BoxSizer( wx.VERTICAL )
        
        
        bSizer43.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_hyperlink1 = wx.HyperlinkCtrl( self.__aboutPagePanel, wx.ID_ANY, u"JavaCardOS Technologies. All rights reserved.", u"http://www.javacardos.com", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
        bSizer43.Add( self.m_hyperlink1, 0, wx.ALL, 5 )
        
        self.m_hyperlink2 = wx.HyperlinkCtrl( self.__aboutPagePanel, wx.ID_ANY, u"Website: http://www.javacardos.com/", u"http://www.javacardos.com", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
        bSizer43.Add( self.m_hyperlink2, 0, wx.ALL, 5 )
        
        self.m_hyperlink3 = wx.HyperlinkCtrl( self.__aboutPagePanel, wx.ID_ANY, u"Discussion: http://www.javacardos.com/javacardforum/", u"http://www.javacardos.com/javacardforum/", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
        bSizer43.Add( self.m_hyperlink3, 0, wx.ALL, 5 )
        
        
        bSizer43.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        self.__aboutPagePanel.SetSizer( bSizer43 )
        self.__aboutPagePanel.Layout()
        bSizer43.Fit( self.__aboutPagePanel )
        self.__pagesNoteBook.AddPage( self.__aboutPagePanel, u"About", False )
        
        bSizer47.Add( self.__pagesNoteBook, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel14.SetSizer( bSizer47 )
        self.m_panel14.Layout()
        bSizer47.Fit( self.m_panel14 )
        self.m_panel15 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer49 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.__logTextCtrl = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer49.Add( self.__logTextCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel15.SetSizer( bSizer49 )
        self.m_panel15.Layout()
        bSizer49.Fit( self.m_panel15 )
        self.m_splitter2.SplitHorizontally( self.m_panel14, self.m_panel15, 0 )
        bSizer46.Add( self.m_splitter2, 1, wx.EXPAND, 5 )
        
        
        mainSizer.Add( bSizer46, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( mainSizer )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.__connectButton.Bind( wx.EVT_BUTTON, self.__connectButtonOnButtonClick )
        self.__claTextCtrl.Bind( wx.EVT_CHAR, self.__claTextCtrlOnChar )
        self.__insTextCtrl.Bind( wx.EVT_CHAR, self.__insTextCtrlOnChar )
        self.__p1TextCtrl.Bind( wx.EVT_CHAR, self.__p1TextCtrlOnChar )
        self.__p2TextCtrl.Bind( wx.EVT_CHAR, self.__p2TextCtrlOnChar )
        self.__dataTextCtrl.Bind( wx.EVT_CHAR, self.__dataTextCtrlOnChar )
        self.__dataTextCtrl.Bind( wx.EVT_TEXT, self.__dataTextCtrlOnText )
        self.__leTextCtrl.Bind( wx.EVT_CHAR, self.__leTextCtrlOnChar )
        self.__transmitButton.Bind( wx.EVT_BUTTON, self.__transmitButtonOnButtonClick )
        self.__mutualAuthButton.Bind( wx.EVT_BUTTON, self.__mutualAuthButtonOnButtonClick )
        self.__capFilePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.__capFilePickerOnFileChanged )
        self.__loadButton.Bind( wx.EVT_BUTTON, self.__loadButtonOnButtonClick )
        self.__installButton.Bind( wx.EVT_BUTTON, self.__installButtonOnButtonClick )
        self.__contentTreeCtrl.Bind( wx.EVT_TREE_SEL_CHANGED, self.__contentTreeCtrlOnTreeSelChanged )
        self.__refreshCardContent.Bind( wx.EVT_BUTTON, self.__refreshCardContentOnButtonClick )
        self.__installCardContent.Bind( wx.EVT_BUTTON, self.__installCardContentOnButtonClick )
        self.__selectCardContent.Bind( wx.EVT_BUTTON, self.__selectCardContentOnButtonClick )
        self.__deleteCardContent.Bind( wx.EVT_BUTTON, self.__deleteCardContentOnButtonClick )
        self.__keyDataListCtrl.Bind( wx.EVT_LIST_ITEM_SELECTED, self.__keyDataListCtrlOnListItemSelected )
        self.__getKeyTemplateInfoButton.Bind( wx.EVT_BUTTON, self.__getKeyTemplateInfoButtonOnButtonClick )
        self.__key1TextCtrl.Bind( wx.EVT_CHAR, self.__key1TextCtrlOnChar )
        self.__key1TextCtrl.Bind( wx.EVT_TEXT, self.__key1TextCtrlOnText )
        self.__key2TextCtrl.Bind( wx.EVT_CHAR, self.__key2TextCtrlOnChar )
        self.__key2TextCtrl.Bind( wx.EVT_TEXT, self.__key2TextCtrlOnText )
        self.__key3TextCtrl.Bind( wx.EVT_CHAR, self.__key3TextCtrlOnChar )
        self.__key3TextCtrl.Bind( wx.EVT_TEXT, self.__key3TextCtrlOnText )
        self.__oldKVNTextCtrl.Bind( wx.EVT_CHAR, self.__oldKVNTextCtrlOnChar )
        self.__oldKVNTextCtrl.Bind( wx.EVT_TEXT, self.__oldKVNTextCtrlOnText )
        self.__newKVNTextCtrl.Bind( wx.EVT_CHAR, self.__newKVNTextCtrlOnChar )
        self.__newKVNTextCtrl.Bind( wx.EVT_TEXT, self.__newKVNTextCtrlOnText )
        self.__putKeyButton.Bind( wx.EVT_BUTTON, self.__putKeyButtonOnButtonClick )
        self.__deleteKeyButton.Bind( wx.EVT_BUTTON, self.__deleteKeyButtonOnButtonClick )
        self.__resetKeyButton.Bind( wx.EVT_BUTTON, self.__resetKeyButtonOnButtonClick )
        self.__scriptFilePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.__scriptFilePickerOnFileChanged )
        self.__scriptRefreshButton.Bind( wx.EVT_BUTTON, self.__scriptRefreshButtonOnButtonClick )
#         self.__scriptLoopCountTextCtrl.Bind( wx.EVT_CHAR, self.__scriptLoopCountTextCtrlOnChar )
        self.__scriptRunButton.Bind( wx.EVT_BUTTON, self.__scriptRunButtonOnButtonClick )
        self.__scriptClearResultButton.Bind( wx.EVT_BUTTON, self.__scriptClearResultButtonOnButtonClick )
        
        self.__apduListCtrl.Bind(wx.EVT_CONTEXT_MENU, self.__apduListCtrlOnContextMenu, self.__apduListCtrl )
        self.__scriptListCtrl.Bind(wx.EVT_CONTEXT_MENU, self.__scriptListCtrlOnContextMenu, self.__scriptListCtrl )
        
        self.__InitController()
        self.__logger = wx.LogTextCtrl(self.__logTextCtrl)
    
    def __del__( self ):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def __connectButtonOnButtonClick( self, event ):
        if (self.__connectButton.GetLabelText() == 'Connect'):
            try:
                # Get smartcard reader name;
                readername = self.__readernameComboBox.GetString(self.__readernameComboBox.GetSelection())
                protocolIndex = self.__protocolComboBox.GetSelection()
                
                # Get protocol value;
                protocol = pyResManReader.SCARD_PROTOCOL_T0 | pyResManReader.SCARD_PROTOCOL_T1
                if protocolIndex == 0:
                    protocol = pyResManReader.SCARD_PROTOCOL_T0
                elif protocolIndex == 1:
                    protocol = pyResManReader.SCARD_PROTOCOL_T1
                
                # Get mode value;
                modeIndex = self.__modeComboBox.GetSelection()
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
                self.__Log('Connected.')
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
                self.__Log('Disconnected.')
            except NoCardException, e:
                self.__Log('NoCardException: %s' %(e.args[1]), wx.LOG_Error)
            except Exception, e:
                self.__Log('Exception: ' %(str(e)), wx.LOG_Error)
    
    def __claTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def __insTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def __p1TextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def __p2TextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()

    def __dataTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()

    def __dataTextCtrlOnText( self, event ):
        dataLen = len(self.__dataTextCtrl.GetValue())
        if dataLen & 0x01 != 0:
            self.__dataTextCtrl.SetBackgroundColour('#FF6347')
        else:
            self.__dataTextCtrl.SetBackgroundColour('WHITE')
        self.__dataTextCtrl.Refresh()
        dataLen = dataLen / 2
        self.__lcTextCtrl.SetValue("%02X" %(dataLen))
    
    def __leTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def __transmitButtonOnButtonClick( self, event ):
        cls = self.__claTextCtrl.GetValue()
        ins = self.__insTextCtrl.GetValue()
        p1 = self.__p1TextCtrl.GetValue()
        p2 = self.__p2TextCtrl.GetValue()
        lc = self.__lcTextCtrl.GetValue()
        data = self.__dataTextCtrl.GetValue()
        le = self.__leTextCtrl.GetValue()
        
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
        self.__controller.transmit(commandText, autoGetResponse, (self.__apduListCtrl, ))
    
    def __mutualAuthButtonOnButtonClick( self, event ):
        self.__controller.doMutualAuth()
    
    def __capFilePickerOnFileChanged( self, event ):
        capFilePath = self.__capFilePicker.GetPath()
        self.__controller.readCapFileInfo(capFilePath)
    
    def __loadButtonOnButtonClick( self, event ):
        capFilePath = self.__capFilePicker.GetPath()
        self.__controller.loadCapFile(capFilePath)
    
    def __installButtonOnButtonClick( self, event ):
        appletItem = self.__capFileInformationTreeCtrl.GetSelection()
        appletData = self.__capFileInformationTreeCtrl.GetItemData(appletItem)
        if appletData.GetData()['type'] != 'applet':
            self.__Log('Please select the applet item to install.', wx.LOG_Warning)
            return
        
        packageItem = self.__capFileInformationTreeCtrl.GetItemParent(appletItem)
        packageData = self.__capFileInformationTreeCtrl.GetItemData(packageItem)
        if packageData.GetData()['type'] != 'package':
            self.__Log('Invalid selected item.', wx.LOG_Warning)
            return

        packageAID = packageData.GetData()['aid']
        appletAID = appletData.GetData()['aid']
        instanceAID = appletAID
        
        installDialog = pyResMan_InstallDialog(self)
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

    def __contentTreeCtrlOnTreeSelChanged( self, event ):
        event.Skip()
        self.__installCardContent.Enable(False)
        self.__selectCardContent.Enable(False)
        selectedId = self.__contentTreeCtrl.GetSelection();
        selectedItemData = self.__contentTreeCtrl.GetItemData(selectedId)
        if selectedItemData == None:
            return
        itemData = selectedItemData.GetData()
        itemType = itemData['type']
        if itemType == 'applet':
            parentId = self.__contentTreeCtrl.GetItemParent(selectedId)
            parentItemData = self.__contentTreeCtrl.GetItemData(parentId)
            parentData = parentItemData.GetData()
            if parentData['type'] == 'package':
                self.__installCardContent.Enable()
        elif itemType == 'instance':
            self.__selectCardContent.Enable()
        
    def __refreshCardContentOnButtonClick( self, event ):
        event.Skip()
        self.__controller.getStatus()
    
    def __installCardContentOnButtonClick( self, event ):
        selectedId = self.__contentTreeCtrl.GetSelection();
        selectedItemData = self.__contentTreeCtrl.GetItemData(selectedId)
        if selectedItemData.GetData()['type'] != 'applet':
            return
        parentId = self.__contentTreeCtrl.GetItemParent(selectedId)
        parentItemData = self.__contentTreeCtrl.GetItemData(parentId)
        if parentItemData.GetData()['type'] != 'package':
            return
        packageAID = parentItemData.GetData()['aid']
        appletAID = selectedItemData.GetData()['aid']
        instanceAID = appletAID
        installDialog = pyResMan_InstallDialog(self)
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
            
            self.__controller.getStatus()
        else:
            pass

    def __selectCardContentOnButtonClick( self, event ):
        event.Skip()
        
        selectedId = self.__contentTreeCtrl.GetSelection();
        selectedItemData = self.__contentTreeCtrl.GetItemData(selectedId)
        itemData = selectedItemData.GetData()
        itemType = itemData['type']
        if itemType != 'instance':
            return
        instanceAID = itemData['aid']
        self.__controller.selectApplication(instanceAID)

    def __deleteCardContentOnButtonClick( self, event ):
        selectedItem = self.__contentTreeCtrl.GetSelection()
        selectedItemData = self.__contentTreeCtrl.GetItemData(selectedItem)
        aid = selectedItemData.GetData()['aid']
        self.__controller.deleteApplication(aid)
        self.__controller.getStatus()
        event.Skip()
    
    def __keyDataListCtrlOnListItemSelected( self, event ):
        event.Skip()
        
        item = event.GetItem()
        kvn = self.__keyDataListCtrl.GetItemText(item.GetId(), 1)
        if kvn == 'FF':
            self.__oldKVNTextCtrl.SetValue('0')
            self.__newKVNTextCtrl.SetValue('1')
        else:
            self.__oldKVNTextCtrl.SetValue(kvn)
            self.__newKVNTextCtrl.SetValue(kvn)

    def __key1TextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def __key1TextCtrlOnText( self, event ):
        event.Skip()
        self.__keyLen1TextCtrl.SetValue('%02X' %(len(self.__key1TextCtrl.GetValue()) / 2))
    
    def __key2TextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def __key2TextCtrlOnText( self, event ):
        event.Skip()
        self.__keyLen2TextCtrl.SetValue('%02X' %(len(self.__key2TextCtrl.GetValue()) / 2))
    
    def __key3TextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def __key3TextCtrlOnText( self, event ):
        event.Skip()
        self.__keyLen3TextCtrl.SetValue('%02X' %(len(self.__key3TextCtrl.GetValue()) / 2))
    
    def __oldKVNTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def __oldKVNTextCtrlOnText( self, event ):
        event.Skip()
        kvn = int(self.__oldKVNTextCtrl.GetValue(), 0x10)
        self.__oldKVNTextCtrl.SetBackgroundColour('WHITE')
        if not ((kvn >= 0) and (kvn <= 0x7F)): 
            self.__oldKVNTextCtrl.SetBackgroundColour('#FF6347')
        self.__oldKVNTextCtrl.Refresh()

    def __newKVNTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def __newKVNTextCtrlOnText( self, event ):
        event.Skip()
        kvn = int(self.__newKVNTextCtrl.GetValue(), 0x10)
        self.__newKVNTextCtrl.SetBackgroundColour('WHITE')
        if not ((kvn >= 1) and (kvn <= 0x7F)): 
            self.__newKVNTextCtrl.SetBackgroundColour('#FF6347')
        self.__newKVNTextCtrl.Refresh()

    
    def __putKeyButtonOnButtonClick( self, event ):
        event.Skip()
        
        if self.__oldKVNTextCtrl.IsEmpty():
            self.__Log('Please input the old key version number.')
            self.__oldKVNTextCtrl.SetBackgroundColour('#FF6347')
            self.__oldKVNTextCtrl.Refresh()
            return
        if self.__newKVNTextCtrl.IsEmpty():
            self.__Log('Please input the new key version number.')
            self.__newKVNTextCtrl.SetBackgroundColour('#FF6347')
            self.__newKVNTextCtrl.Refresh()
            return
        
        oldKVN = int(self.__oldKVNTextCtrl.GetValue(), 0x10)
        newKVN = int(self.__newKVNTextCtrl.GetValue(), 0x10)
        
        key1 = Util.s2vs(self.__key1TextCtrl.GetValue())
        key2 = Util.s2vs(self.__key2TextCtrl.GetValue())
        key3 = Util.s2vs(self.__key3TextCtrl.GetValue())
        self.__controller.putKey(oldKVN, newKVN, key1, key2, key3)
        
        self.__controller.getKeyTemplateInfo()

    def __deleteKeyButtonOnButtonClick( self, event ):
        event.Skip()

        keysInfo = []
        i = self.__keyDataListCtrl.GetFirstSelected()
        while i != -1:
            kvn = int(self.__keyDataListCtrl.GetItemText(i, 1), 0x10)
            keyIndex = int(self.__keyDataListCtrl.GetItemText(i, 2), 0x10)
            keysInfo.append((kvn, keyIndex, ))
            i = self.__keyDataListCtrl.GetNextSelected(i)
        self.__controller.deleteKey(keysInfo)
        
        self.__controller.getKeyTemplateInfo()
    
    def __getKeyTemplateInfoButtonOnButtonClick( self, event ):
        event.Skip()
        self.__controller.getKeyTemplateInfo()
    
    def __resetKeyButtonOnButtonClick( self, event ):
        event.Skip()
        defaultKey = '404142434445464748494A4B4C4D4E4F'
        self.__key1TextCtrl.SetValue(defaultKey)
        self.__key2TextCtrl.SetValue(defaultKey)
        self.__key3TextCtrl.SetValue(defaultKey)

    def __scriptLoopCountTextCtrlOnChar( self, event ):
        if Util.isnumchar_kc(event.KeyCode):
            event.Skip()
        else:
            pass

    def __loadScript(self):
        scriptPathName = self.__scriptFilePicker.GetPath()
        if os.path.exists(scriptPathName):
            self.__controller.loadScript(scriptPathName)
    
    def __scriptFilePickerOnFileChanged( self, event ):
        event.Skip()
        self.__loadScript()
    
    def __scriptRefreshButtonOnButtonClick( self, event ):
        event.Skip()
        self.__loadScript()
    
    def __scriptRunButtonOnButtonClick( self, event ):
        event.Skip()
        apduItems = []
        itemCount = self.__scriptListCtrl.GetItemCount()
        for itemIndex in xrange(itemCount):
            listItem = self.__scriptListCtrl.GetItem(itemIndex, 1)
            apduItem = APDUItem(listItem.GetText(), (self.__scriptListCtrl, listItem.GetId()))
            apduItems.append(apduItem)
        
        t0AutoGetResponse = self.__autoGetResponseCheckBox.GetValue()
        self.__controller.transmitAPDUItems(apduItems, t0AutoGetResponse)
    
    def __scriptClearResultButtonOnButtonClick( self, event ):
        event.Skip()
    
    def m_splitter2OnIdle( self, event ):
        self.m_splitter2.SetSashPosition( 0 )
        self.m_splitter2.Unbind( wx.EVT_IDLE )
    
    def __apduListCtrlOnContextMenu(self, event):
        """Display apdu list view popup menu;"""
        self.__apduListCtrlPopupMenu = wx.Menu()
        self.__apduListCtrlPopupMenu.Append(1, "Run")
        self.__apduListCtrlPopupMenu.AppendSeparator()
        self.__apduListCtrlPopupMenu.Append(0, "Clear")
        self.__apduListCtrlPopupMenu.Bind(wx.EVT_MENU, self.__listCtrlOnContextMenuClick)
        self.__apduListCtrl.PopupMenu(self.__apduListCtrlPopupMenu)

    def __scriptListCtrlOnContextMenu(self, event):
        """Display apdu list view popup menu;"""
        self.__scriptListCtrlPopupMenu = wx.Menu()
        self.__scriptListCtrlPopupMenu.Append(1, "Run")
        self.__scriptListCtrlPopupMenu.AppendSeparator()
        self.__scriptListCtrlPopupMenu.Append(0, "Clear")
        self.__scriptListCtrlPopupMenu.Bind(wx.EVT_MENU, self.__listCtrlOnContextMenuClick)
        self.__scriptListCtrl.PopupMenu(self.__scriptListCtrlPopupMenu)
    
    def __listCtrlOnContextMenuClick(self, event):
        menuItemIndex = event.Id
        theListCtrl = event.GetEventObject().GetInvokingWindow()
        if menuItemIndex == 0:
            theListCtrl.DeleteAllItems()
        elif menuItemIndex == 1:
            self.__listCtrlRunSelectedItems(theListCtrl)
# 
#     def _onLogTextCtrl_MenuClick(self, event):
#         menuItemIndex = event.Id
#         if menuItemIndex == 0:
#             self.__logTextCtrl.Clear()
    
    def __listCtrlRunSelectedItems(self, listCtrl):
        """Transmit selected items apdu in the apdu list view;"""
        apduItems = []
        selectedItem = listCtrl.GetFirstSelected()
        while (selectedItem != -1):
            listItem = listCtrl.GetItem(selectedItem, 1)
            apduItem = APDUItem(listItem.GetText(), (listCtrl, selectedItem))
            apduItems.append(apduItem)
            selectedItem = listCtrl.GetNextSelected(selectedItem)
        
        t0AutoGetResponse = self.__autoGetResponseCheckBox.GetValue()
        self.__controller.transmitAPDUItems(apduItems, t0AutoGetResponse)
    
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
            
    def __scrollToLine(self, listCtrl, lineIndex):
        scrollPos = listCtrl.GetScrollPos(wx.VERTICAL)
        listCtrl.ScrollLines(lineIndex - scrollPos)
    
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
        
        self.__scrollToLine(theListCtrl, itemIndex)
    
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

        self.__scrollToLine(theListCtrl, itemIndex)

    def __Log(self, msg, level=wx.LOG_Info):
        """Display log with levels"""
        if msg.endswith('\r'):
            msg= msg[ : len(msg) - 1]
        if msg.endswith('\n'):
            msg= msg[ : len(msg) - 1]
        self.__logger.LogTextAtLevel(level, msg)
    
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

    def handleCapFileInfo(self, info):
        self.__capFileInformationTreeCtrl.DeleteAllItems()
        tr = self.__capFileInformationTreeCtrl.AddRoot(self.__capFilePicker.GetPath())
        packageAID = info['loadFileAID']
        ti = self.__capFileInformationTreeCtrl.InsertItem(tr, TreeItemId(), "".join("%02X" %(ord(c)) for c in packageAID), data=TreeItemData({ 'type' : 'package', 'aid' : packageAID }))
        tic = TreeItemId()
        for appletAID in info['applets']:
            tic = self.__capFileInformationTreeCtrl.InsertItem(ti, tic, "".join("%02X" %(ord(c)) for c in appletAID), data=TreeItemData( { 'type' : 'applet', 'aid' : appletAID }))
        self.__capFileInformationTreeCtrl.ExpandAll()
    
    def handleStatus(self, theStatus):
        self.__contentTreeCtrl.DeleteAllItems()
        ri = self.__contentTreeCtrl.AddRoot('STATUS')
        tir = TreeItemId()
        status_names = { 0x80 : 'ISD', 0x40 : 'SSD/Applets', 0x20 : 'ExecutableFiles', 0x10 : 'ExecutableFileAndModules' }
        for theElement in theStatus.keys():
            tir = self.__contentTreeCtrl.InsertItem(ri, tir, status_names[theElement], data=TreeItemData({ 'type' : 'root' }))
            ti = TreeItemId()
            if theElement == 0x10:
                statusData = theStatus[theElement]
                if statusData != None:
                    executableModulesData = statusData[1]
                    for executableModuleData in executableModulesData:
                        packageAID = executableModuleData['aid']
                        packageLifeCycleState = executableModuleData['lifeCycleState']
                        ti = self.__contentTreeCtrl.InsertItem(tir, ti, "AID: " + "".join("%02X" %(ord(c)) for c in packageAID) + " - LifeCycle: %02X" %(packageLifeCycleState), data = TreeItemData({ 'type' : 'package', 'aid' : packageAID}))
                        executableModules = executableModuleData['executableModules']
                        ti2 = TreeItemId()
                        for executableModule in executableModules:
                            ti2 = self.__contentTreeCtrl.InsertItem(ti, ti2, "AID: " + "".join("%02X" %(ord(c)) for c in executableModule), data = TreeItemData({ 'type' : 'applet', 'aid' : executableModule}))
            else:
                statusData = theStatus[theElement]
                if statusData != None:
                    appletInfos = statusData[0]
                    for appletInfo in appletInfos:
                        appletAID = appletInfo['aid']
                        appletLifeCycleState = appletInfo['lifeCycleState']
                        appletPrivileges = appletInfo['privileges']
                        ti = self.__contentTreeCtrl.InsertItem(tir, ti, "AID: " + "".join("%02X" %(ord(c)) for c in appletAID) + " - LifeCycle: %02X - Privileges: %02X" %(appletLifeCycleState, appletPrivileges), data = TreeItemData({ 'type' : 'package' if theElement == 0x20 else 'instance', 'aid' : appletAID}))
        self.__contentTreeCtrl.ExpandAll()
    
    def handleLoadScriptBegin(self):
        self.__scriptListCtrl.DeleteAllItems()
    
    def handleLoadScriptItem(self, scriptItemStr):
        itemIndex = self.__scriptListCtrl.GetItemCount()
        scriptItem = ListItem()
        scriptItem.SetId(itemIndex)
        scriptItem.SetColumn(0)
        scriptItem.SetText('%d' %(itemIndex))
        self.__scriptListCtrl.InsertItem(scriptItem)
        
        scriptItem.SetId(itemIndex)
        scriptItem.SetColumn(1)
        scriptItem.SetText(scriptItemStr)
        self.__scriptListCtrl.SetItem(scriptItem)
    
    def handleLoadScriptEnd(self):
        pass
    
    def handleKeyInformationTemplates(self, kits):
        self.__keyDataListCtrl.DeleteAllItems()
        kitsLen = len(kits)
        kitsCount = kitsLen / 4
        for i in xrange(kitsCount):
            keySetVersion = ord(kits[i * 4 + 0])
            keyIndex = ord(kits[i * 4 + 1])
            keyType = ord(kits[i * 4 + 2])
            keyLength = ord(kits[i * 4 + 3])
            i = self.__keyDataListCtrl.GetItemCount()
            keyItem = ListItem()
            keyItem.SetId(i)
            keyItem.SetColumn(0)
            keyItem.SetText("%d" %(i))
            self.__keyDataListCtrl.InsertItem(keyItem)
            keyItem.SetColumn(1)
            keyItem.SetText("%02X" %(keySetVersion))
            self.__keyDataListCtrl.SetItem(keyItem)
            keyItem.SetColumn(2)
            keyItem.SetText("%02X" %(keyIndex))
            self.__keyDataListCtrl.SetItem(keyItem)
            keyItem.SetColumn(3)
            keyItem.SetText("%02X" %(keyType))
            self.__keyDataListCtrl.SetItem(keyItem)
            keyItem.SetColumn(4)
            keyItem.SetText("%02X" %(keyLength))
            self.__keyDataListCtrl.SetItem(keyItem)
        