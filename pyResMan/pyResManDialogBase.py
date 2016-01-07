# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class pyResManDialogBase
###########################################################################

class pyResManDialogBase ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"pyResMan v2.1", pos = wx.DefaultPosition, size = wx.Size( 983,687 ), style = wx.DEFAULT_DIALOG_STYLE|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        
        mainSizer = wx.BoxSizer( wx.VERTICAL )
        
        _connectSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"ReaderName", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        _connectSizer.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        _readernameComboBoxChoices = []
        self._readernameComboBox = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), _readernameComboBoxChoices, wx.CB_READONLY )
        self._readernameComboBox.SetSelection( 0 )
        _connectSizer.Add( self._readernameComboBox, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Protocol", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        _connectSizer.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        _protocolComboBoxChoices = [ u"T0", u"T1", u"T0/T1" ]
        self._protocolComboBox = wx.ComboBox( self, wx.ID_ANY, u"T0/T1", wx.DefaultPosition, wx.Size( 75,-1 ), _protocolComboBoxChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
        self._protocolComboBox.SetSelection( 2 )
        _connectSizer.Add( self._protocolComboBox, 0, wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Mode", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        _connectSizer.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        _modeComboBoxChoices = [ u"EXCLUSIVE", u"SHARED" ]
        self._modeComboBox = wx.ComboBox( self, wx.ID_ANY, u"SHARED", wx.DefaultPosition, wx.DefaultSize, _modeComboBoxChoices, wx.CB_READONLY )
        self._modeComboBox.SetSelection( 1 )
        _connectSizer.Add( self._modeComboBox, 0, wx.ALL, 5 )
        
        self._connectButton = wx.Button( self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
        _connectSizer.Add( self._connectButton, 0, wx.ALL, 5 )
        
        
        mainSizer.Add( _connectSizer, 0, wx.EXPAND, 5 )
        
        bSizer46 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_splitter2 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
        self.m_splitter2.SetSashGravity( 0.65 )
        self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )
        self.m_splitter2.SetMinimumPaneSize( 1 )
        
        self.m_panel14 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer47 = wx.BoxSizer( wx.VERTICAL )
        
        self._pagesNoteBook = wx.Notebook( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self._pagesNoteBook.SetMinSize( wx.Size( -1,300 ) )
        
        self._apduPagePanel = wx.Panel( self._pagesNoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        _apduPageSizer = wx.BoxSizer( wx.VERTICAL )
        
        _apduSizer = wx.BoxSizer( wx.VERTICAL )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._claTextCtrl = wx.TextCtrl( self._apduPagePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._claTextCtrl.SetMaxLength( 2 ) 
        bSizer4.Add( self._claTextCtrl, 0, wx.ALL, 5 )
        
        self._insTextCtrl = wx.TextCtrl( self._apduPagePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._insTextCtrl.SetMaxLength( 2 ) 
        bSizer4.Add( self._insTextCtrl, 0, wx.ALL, 5 )
        
        self._p1TextCtrl = wx.TextCtrl( self._apduPagePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._p1TextCtrl.SetMaxLength( 2 ) 
        bSizer4.Add( self._p1TextCtrl, 0, wx.ALL, 5 )
        
        self._p2TextCtrl = wx.TextCtrl( self._apduPagePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._p2TextCtrl.SetMaxLength( 2 ) 
        bSizer4.Add( self._p2TextCtrl, 0, wx.ALL, 5 )
        
        self._lcTextCtrl = wx.TextCtrl( self._apduPagePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.TE_READONLY )
        self._lcTextCtrl.SetMaxLength( 2 ) 
        bSizer4.Add( self._lcTextCtrl, 0, wx.ALL, 5 )
        
        self._dataTextCtrl = wx.TextCtrl( self._apduPagePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer4.Add( self._dataTextCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        self._leTextCtrl = wx.TextCtrl( self._apduPagePanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._leTextCtrl.SetMaxLength( 2 ) 
        bSizer4.Add( self._leTextCtrl, 0, wx.ALL, 5 )
        
        
        bSizer5.Add( bSizer4, 0, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._autoGetResponseCheckBox = wx.CheckBox( self._apduPagePanel, wx.ID_ANY, u"Auto GET RESPONSE", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self._autoGetResponseCheckBox, 0, wx.ALL, 5 )
        
        self._transmitButton = wx.Button( self._apduPagePanel, wx.ID_ANY, u"Transmit", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self._transmitButton, 0, wx.ALL, 5 )
        
        
        bSizer5.Add( bSizer6, 0, wx.EXPAND, 5 )
        
        
        _apduSizer.Add( bSizer5, 0, wx.EXPAND, 5 )
        
        
        _apduPageSizer.Add( _apduSizer, 0, wx.EXPAND, 5 )
        
        self._apduListCtrl = wx.ListCtrl( self._apduPagePanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( 820,-1 ), wx.LC_REPORT )
        _apduPageSizer.Add( self._apduListCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self._apduPagePanel.SetSizer( _apduPageSizer )
        self._apduPagePanel.Layout()
        _apduPageSizer.Fit( self._apduPagePanel )
        self._pagesNoteBook.AddPage( self._apduPagePanel, u"Basic APDU", True )
        self._gpPagePanel = wx.Panel( self._pagesNoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        _gpPageSizer = wx.BoxSizer( wx.VERTICAL )
        
        bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer52 = wx.BoxSizer( wx.VERTICAL )
        
        
        bSizer52.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        bSizer53 = wx.BoxSizer( wx.HORIZONTAL )
        
        _scpinfoMethodChoices = [ u"Auto Detect", u"User input" ]
        self._scpinfoMethod = wx.RadioBox( self._gpPagePanel, wx.ID_ANY, u"SCP informations", wx.DefaultPosition, wx.DefaultSize, _scpinfoMethodChoices, 1, wx.RA_SPECIFY_ROWS )
        self._scpinfoMethod.SetSelection( 0 )
        bSizer53.Add( self._scpinfoMethod, 0, wx.ALL, 5 )
        
        bSizer37 = wx.BoxSizer( wx.VERTICAL )
        
        
        bSizer37.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        bSizer36 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText11 = wx.StaticText( self._gpPagePanel, wx.ID_ANY, u"SCP", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        bSizer36.Add( self.m_staticText11, 0, wx.ALL, 5 )
        
        _scpChoiceChoices = [ u"1", u"2", u"3" ]
        self._scpChoice = wx.Choice( self._gpPagePanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _scpChoiceChoices, 0 )
        self._scpChoice.SetSelection( 1 )
        self._scpChoice.Enable( False )
        
        bSizer36.Add( self._scpChoice, 0, wx.ALL, 5 )
        
        
        bSizer36.AddSpacer( ( 10, 0), 0, 0, 5 )
        
        self.m_staticText12 = wx.StaticText( self._gpPagePanel, wx.ID_ANY, u"i", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        bSizer36.Add( self.m_staticText12, 0, wx.ALL, 5 )
        
        self._scpiTextCtrl = wx.TextCtrl( self._gpPagePanel, wx.ID_ANY, u"15", wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._scpiTextCtrl.SetMaxLength( 2 ) 
        self._scpiTextCtrl.Enable( False )
        
        bSizer36.Add( self._scpiTextCtrl, 0, wx.ALL, 5 )
        
        
        bSizer36.AddSpacer( ( 10, 0), 0, 0, 5 )
        
        
        bSizer36.AddSpacer( ( 0, 0), 0, 0, 5 )
        
        
        bSizer37.Add( bSizer36, 0, 0, 5 )
        
        
        bSizer37.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer53.Add( bSizer37, 0, wx.EXPAND, 5 )
        
        bSizer38 = wx.BoxSizer( wx.VERTICAL )
        
        
        bSizer38.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self._mutualAuthButton = wx.Button( self._gpPagePanel, wx.ID_ANY, u"Mutual Authentication", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer38.Add( self._mutualAuthButton, 0, wx.ALL, 5 )
        
        
        bSizer38.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer53.Add( bSizer38, 1, wx.EXPAND, 5 )
        
        
        bSizer52.Add( bSizer53, 0, wx.EXPAND, 5 )
        
        
        bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )
        
        
        _gpPageSizer.Add( bSizer41, 0, wx.EXPAND, 5 )
        
        self.m_notebook2 = wx.Notebook( self._gpPagePanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,500 ), wx.NB_TOP )
        self._contentManagerPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer231 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer30 = wx.BoxSizer( wx.VERTICAL )
        
        self._capFilePicker = wx.FilePickerCtrl( self._contentManagerPage, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.cap", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer30.Add( self._capFilePicker, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer231.Add( bSizer30, 0, wx.EXPAND, 5 )
        
        bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._capFileInformationTreeCtrl = wx.TreeCtrl( self._contentManagerPage, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TR_DEFAULT_STYLE )
        bSizer31.Add( self._capFileInformationTreeCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        bSizer50 = wx.BoxSizer( wx.VERTICAL )
        
        self._loadButton = wx.Button( self._contentManagerPage, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._loadButton.Enable( False )
        
        bSizer50.Add( self._loadButton, 0, wx.ALL, 5 )
        
        self._installButton = wx.Button( self._contentManagerPage, wx.ID_ANY, u"Install", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._installButton.Enable( False )
        
        bSizer50.Add( self._installButton, 0, wx.ALL, 5 )
        
        
        bSizer50.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer31.Add( bSizer50, 0, wx.EXPAND, 5 )
        
        
        bSizer231.Add( bSizer31, 1, wx.EXPAND, 5 )
        
        
        self._contentManagerPage.SetSizer( bSizer231 )
        self._contentManagerPage.Layout()
        bSizer231.Fit( self._contentManagerPage )
        self.m_notebook2.AddPage( self._contentManagerPage, u"Content Manager", True )
        self._contentViewerPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._contentTreeCtrl = wx.TreeCtrl( self._contentViewerPage, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TR_DEFAULT_STYLE )
        bSizer23.Add( self._contentTreeCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        bSizer26 = wx.BoxSizer( wx.VERTICAL )
        
        self._refreshCardContent = wx.Button( self._contentViewerPage, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer26.Add( self._refreshCardContent, 0, wx.ALL, 5 )
        
        self._installCardContent = wx.Button( self._contentViewerPage, wx.ID_ANY, u"Install", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._installCardContent.Enable( False )
        
        bSizer26.Add( self._installCardContent, 0, wx.ALL, 5 )
        
        self._selectCardContent = wx.Button( self._contentViewerPage, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._selectCardContent.Enable( False )
        
        bSizer26.Add( self._selectCardContent, 0, wx.ALL, 5 )
        
        self._deleteCardContent = wx.Button( self._contentViewerPage, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._deleteCardContent.Enable( False )
        
        bSizer26.Add( self._deleteCardContent, 0, wx.ALL, 5 )
        
        
        bSizer23.Add( bSizer26, 0, wx.EXPAND, 5 )
        
        
        self._contentViewerPage.SetSizer( bSizer23 )
        self._contentViewerPage.Layout()
        bSizer23.Fit( self._contentViewerPage )
        self.m_notebook2.AddPage( self._contentViewerPage, u"Content Viewer", False )
        self._keyManagerPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer342 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._keyDataListCtrl = wx.ListCtrl( self._keyManagerPage, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_REPORT )
        bSizer51.Add( self._keyDataListCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer34.Add( bSizer51, 1, wx.EXPAND, 5 )
        
        bSizer40 = wx.BoxSizer( wx.VERTICAL )
        
        self._getKeyTemplateInfoButton = wx.Button( self._keyManagerPage, wx.ID_ANY, u"Get Key Template Information", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer40.Add( self._getKeyTemplateInfoButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer28 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self._keyManagerPage, wx.ID_ANY, u"S-ENC", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer29.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self._keyLen1TextCtrl = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.TE_READONLY )
        bSizer29.Add( self._keyLen1TextCtrl, 0, wx.ALL, 5 )
        
        self._key1TextCtrl = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._key1TextCtrl.SetMinSize( wx.Size( 300,-1 ) )
        
        bSizer29.Add( self._key1TextCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer28.Add( bSizer29, 1, wx.EXPAND, 5 )
        
        bSizer301 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self._keyManagerPage, wx.ID_ANY, u"S-MAC", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer301.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        self._keyLen2TextCtrl = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.TE_READONLY )
        bSizer301.Add( self._keyLen2TextCtrl, 0, wx.ALL, 5 )
        
        self._key2TextCtrl = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._key2TextCtrl.SetMinSize( wx.Size( 300,-1 ) )
        
        bSizer301.Add( self._key2TextCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer28.Add( bSizer301, 1, wx.EXPAND, 5 )
        
        bSizer311 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self._keyManagerPage, wx.ID_ANY, u"    DEK", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer311.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self._keyLen3TextCtrl = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.TE_READONLY )
        bSizer311.Add( self._keyLen3TextCtrl, 0, wx.ALL, 5 )
        
        self._key3TextCtrl = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._key3TextCtrl.SetMinSize( wx.Size( 300,-1 ) )
        
        bSizer311.Add( self._key3TextCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer28.Add( bSizer311, 1, wx.EXPAND, 5 )
        
        
        bSizer40.Add( bSizer28, 0, wx.EXPAND, 5 )
        
        bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText10 = wx.StaticText( self._keyManagerPage, wx.ID_ANY, u"Old KVN", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        bSizer33.Add( self.m_staticText10, 0, wx.ALL, 5 )
        
        self._oldKVNTextCtrl = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._oldKVNTextCtrl.SetMaxLength( 2 ) 
        bSizer33.Add( self._oldKVNTextCtrl, 0, wx.ALL, 5 )
        
        self.m_staticText9 = wx.StaticText( self._keyManagerPage, wx.ID_ANY, u"NewKVN", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer33.Add( self.m_staticText9, 0, wx.ALL, 5 )
        
        self._newKVNTextCtrl = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._newKVNTextCtrl.SetMaxLength( 2 ) 
        bSizer33.Add( self._newKVNTextCtrl, 0, wx.ALL, 5 )
        
        self._putKeyButton = wx.Button( self._keyManagerPage, wx.ID_ANY, u"Put Key", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer33.Add( self._putKeyButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self._deleteKeyButton = wx.Button( self._keyManagerPage, wx.ID_ANY, u"Delete Key", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer33.Add( self._deleteKeyButton, 0, wx.ALL, 5 )
        
        self._resetKeyButton = wx.Button( self._keyManagerPage, wx.ID_ANY, u"Default", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer33.Add( self._resetKeyButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        bSizer40.Add( bSizer33, 0, wx.EXPAND, 5 )
        
        
        bSizer40.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer34.Add( bSizer40, 0, wx.EXPAND, 5 )
        
        
        bSizer342.Add( bSizer34, 1, wx.EXPAND, 5 )
        
        
        self._keyManagerPage.SetSizer( bSizer342 )
        self._keyManagerPage.Layout()
        bSizer342.Fit( self._keyManagerPage )
        self.m_notebook2.AddPage( self._keyManagerPage, u"Key Manager", False )
        
        _gpPageSizer.Add( self.m_notebook2, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self._gpPagePanel.SetSizer( _gpPageSizer )
        self._gpPagePanel.Layout()
        _gpPageSizer.Fit( self._gpPagePanel )
        self._pagesNoteBook.AddPage( self._gpPagePanel, u"GlobalPlatform", False )
        self._scriptPagePanel = wx.Panel( self._pagesNoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer44 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer45 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._scriptFilePicker = wx.FilePickerCtrl( self._scriptPagePanel, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 650,-1 ), wx.FLP_DEFAULT_STYLE )
        bSizer45.Add( self._scriptFilePicker, 1, wx.ALL, 5 )
        
        self._scriptRefreshButton = wx.Button( self._scriptPagePanel, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer45.Add( self._scriptRefreshButton, 0, wx.ALL, 5 )
        
        self.m_staticText4 = wx.StaticText( self._scriptPagePanel, wx.ID_ANY, u"Loop count:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer45.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self._scriptLoopCountTextCtrl = wx.TextCtrl( self._scriptPagePanel, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer45.Add( self._scriptLoopCountTextCtrl, 0, wx.ALL, 5 )
        
        self._scriptRunButton = wx.Button( self._scriptPagePanel, wx.ID_ANY, u"Run Script", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer45.Add( self._scriptRunButton, 0, wx.ALL, 5 )
        
        self._scriptClearResultButton = wx.Button( self._scriptPagePanel, wx.ID_ANY, u"Clear Result", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer45.Add( self._scriptClearResultButton, 0, wx.ALL, 5 )
        
        
        bSizer44.Add( bSizer45, 0, wx.EXPAND, 5 )
        
        self._scriptListCtrl = wx.ListCtrl( self._scriptPagePanel, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_REPORT )
        bSizer44.Add( self._scriptListCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self._scriptPagePanel.SetSizer( bSizer44 )
        self._scriptPagePanel.Layout()
        bSizer44.Fit( self._scriptPagePanel )
        self._pagesNoteBook.AddPage( self._scriptPagePanel, u"Script", False )
        self._aboutPagePanel = wx.Panel( self._pagesNoteBook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer331 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer331.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        bSizer43 = wx.BoxSizer( wx.VERTICAL )
        
        
        bSizer43.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        bSizer401 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer401.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText101 = wx.StaticText( self._aboutPagePanel, wx.ID_ANY, u"PyResMan v2.1", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText101.Wrap( -1 )
        bSizer401.Add( self.m_staticText101, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer401.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer43.Add( bSizer401, 0, wx.EXPAND, 5 )
        
        bSizer39 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer39.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_hyperlink1 = wx.HyperlinkCtrl( self._aboutPagePanel, wx.ID_ANY, u"JavaCardOS Technologies. All rights reserved.", u"http://www.javacardos.com", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_CENTRE|wx.HL_DEFAULT_STYLE )
        bSizer39.Add( self.m_hyperlink1, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer39.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer43.Add( bSizer39, 0, wx.EXPAND, 5 )
        
        bSizer381 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer381.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_hyperlink2 = wx.HyperlinkCtrl( self._aboutPagePanel, wx.ID_ANY, u"Website: http://www.javacardos.com/", u"http://www.javacardos.com", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_CENTRE|wx.HL_DEFAULT_STYLE )
        bSizer381.Add( self.m_hyperlink2, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer381.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer43.Add( bSizer381, 0, wx.EXPAND, 5 )
        
        bSizer371 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer371.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_hyperlink3 = wx.HyperlinkCtrl( self._aboutPagePanel, wx.ID_ANY, u"Discussion: http://www.javacardos.com/javacardforum/", u"http://www.javacardos.com/javacardforum/", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_CENTRE|wx.HL_DEFAULT_STYLE )
        bSizer371.Add( self.m_hyperlink3, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer371.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer43.Add( bSizer371, 0, wx.EXPAND, 5 )
        
        
        bSizer43.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer331.Add( bSizer43, 1, wx.EXPAND, 5 )
        
        
        bSizer331.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        self._aboutPagePanel.SetSizer( bSizer331 )
        self._aboutPagePanel.Layout()
        bSizer331.Fit( self._aboutPagePanel )
        self._pagesNoteBook.AddPage( self._aboutPagePanel, u"About", False )
        
        bSizer47.Add( self._pagesNoteBook, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel14.SetSizer( bSizer47 )
        self.m_panel14.Layout()
        bSizer47.Fit( self.m_panel14 )
        self.m_panel15 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer49 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._logTextCtrl = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2 )
        bSizer49.Add( self._logTextCtrl, 1, wx.ALL|wx.EXPAND, 5 )
        
        
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
        self._connectButton.Bind( wx.EVT_BUTTON, self._connectButtonOnButtonClick )
        self._claTextCtrl.Bind( wx.EVT_CHAR, self._claTextCtrlOnChar )
        self._insTextCtrl.Bind( wx.EVT_CHAR, self._insTextCtrlOnChar )
        self._p1TextCtrl.Bind( wx.EVT_CHAR, self._p1TextCtrlOnChar )
        self._p2TextCtrl.Bind( wx.EVT_CHAR, self._p2TextCtrlOnChar )
        self._dataTextCtrl.Bind( wx.EVT_CHAR, self._dataTextCtrlOnChar )
        self._dataTextCtrl.Bind( wx.EVT_TEXT, self._dataTextCtrlOnText )
        self._leTextCtrl.Bind( wx.EVT_CHAR, self._leTextCtrlOnChar )
        self._transmitButton.Bind( wx.EVT_BUTTON, self._transmitButtonOnButtonClick )
        self._scpinfoMethod.Bind( wx.EVT_RADIOBOX, self._scpinfoMethodOnRadioBox )
        self._scpiTextCtrl.Bind( wx.EVT_CHAR, self._scpiTextCtrlOnChar )
        self._mutualAuthButton.Bind( wx.EVT_BUTTON, self._mutualAuthButtonOnButtonClick )
        self._capFilePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self._capFilePickerOnFileChanged )
        self._capFileInformationTreeCtrl.Bind( wx.EVT_TREE_SEL_CHANGED, self._capFileInformationTreeCtrlOnTreeSelChanged )
        self._loadButton.Bind( wx.EVT_BUTTON, self._loadButtonOnButtonClick )
        self._installButton.Bind( wx.EVT_BUTTON, self._installButtonOnButtonClick )
        self._contentTreeCtrl.Bind( wx.EVT_TREE_SEL_CHANGED, self._contentTreeCtrlOnTreeSelChanged )
        self._refreshCardContent.Bind( wx.EVT_BUTTON, self._refreshCardContentOnButtonClick )
        self._installCardContent.Bind( wx.EVT_BUTTON, self._installCardContentOnButtonClick )
        self._selectCardContent.Bind( wx.EVT_BUTTON, self._selectCardContentOnButtonClick )
        self._deleteCardContent.Bind( wx.EVT_BUTTON, self._deleteCardContentOnButtonClick )
        self._keyDataListCtrl.Bind( wx.EVT_LIST_ITEM_SELECTED, self._keyDataListCtrlOnListItemSelected )
        self._getKeyTemplateInfoButton.Bind( wx.EVT_BUTTON, self._getKeyTemplateInfoButtonOnButtonClick )
        self._key1TextCtrl.Bind( wx.EVT_CHAR, self._key1TextCtrlOnChar )
        self._key1TextCtrl.Bind( wx.EVT_TEXT, self._key1TextCtrlOnText )
        self._key2TextCtrl.Bind( wx.EVT_CHAR, self._key2TextCtrlOnChar )
        self._key2TextCtrl.Bind( wx.EVT_TEXT, self._key2TextCtrlOnText )
        self._key3TextCtrl.Bind( wx.EVT_CHAR, self._key3TextCtrlOnChar )
        self._key3TextCtrl.Bind( wx.EVT_TEXT, self._key3TextCtrlOnText )
        self._oldKVNTextCtrl.Bind( wx.EVT_CHAR, self._oldKVNTextCtrlOnChar )
        self._oldKVNTextCtrl.Bind( wx.EVT_TEXT, self._oldKVNTextCtrlOnText )
        self._newKVNTextCtrl.Bind( wx.EVT_CHAR, self._newKVNTextCtrlOnChar )
        self._newKVNTextCtrl.Bind( wx.EVT_TEXT, self._newKVNTextCtrlOnText )
        self._putKeyButton.Bind( wx.EVT_BUTTON, self._putKeyButtonOnButtonClick )
        self._deleteKeyButton.Bind( wx.EVT_BUTTON, self._deleteKeyButtonOnButtonClick )
        self._resetKeyButton.Bind( wx.EVT_BUTTON, self._resetKeyButtonOnButtonClick )
        self._scriptFilePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self._scriptFilePickerOnFileChanged )
        self._scriptRefreshButton.Bind( wx.EVT_BUTTON, self._scriptRefreshButtonOnButtonClick )
        self._scriptLoopCountTextCtrl.Bind( wx.EVT_CHAR, self._scriptLoopCountTextCtrlOnChar )
        self._scriptRunButton.Bind( wx.EVT_BUTTON, self._scriptRunButtonOnButtonClick )
        self._scriptClearResultButton.Bind( wx.EVT_BUTTON, self._scriptClearResultButtonOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _connectButtonOnButtonClick( self, event ):
        event.Skip()
    
    def _claTextCtrlOnChar( self, event ):
        event.Skip()
    
    def _insTextCtrlOnChar( self, event ):
        event.Skip()
    
    def _p1TextCtrlOnChar( self, event ):
        event.Skip()
    
    def _p2TextCtrlOnChar( self, event ):
        event.Skip()
    
    def _dataTextCtrlOnChar( self, event ):
        event.Skip()
    
    def _dataTextCtrlOnText( self, event ):
        event.Skip()
    
    def _leTextCtrlOnChar( self, event ):
        event.Skip()
    
    def _transmitButtonOnButtonClick( self, event ):
        event.Skip()
    
    def _scpinfoMethodOnRadioBox( self, event ):
        event.Skip()
    
    def _scpiTextCtrlOnChar( self, event ):
        event.Skip()
    
    def _mutualAuthButtonOnButtonClick( self, event ):
        event.Skip()
    
    def _capFilePickerOnFileChanged( self, event ):
        event.Skip()
    
    def _capFileInformationTreeCtrlOnTreeSelChanged( self, event ):
        event.Skip()
    
    def _loadButtonOnButtonClick( self, event ):
        event.Skip()
    
    def _installButtonOnButtonClick( self, event ):
        event.Skip()
    
    def _contentTreeCtrlOnTreeSelChanged( self, event ):
        event.Skip()
    
    def _refreshCardContentOnButtonClick( self, event ):
        event.Skip()
    
    def _installCardContentOnButtonClick( self, event ):
        event.Skip()
    
    def _selectCardContentOnButtonClick( self, event ):
        event.Skip()
    
    def _deleteCardContentOnButtonClick( self, event ):
        event.Skip()
    
    def _keyDataListCtrlOnListItemSelected( self, event ):
        event.Skip()
    
    def _getKeyTemplateInfoButtonOnButtonClick( self, event ):
        event.Skip()
    
    def _key1TextCtrlOnChar( self, event ):
        event.Skip()
    
    def _key1TextCtrlOnText( self, event ):
        event.Skip()
    
    def _key2TextCtrlOnChar( self, event ):
        event.Skip()
    
    def _key2TextCtrlOnText( self, event ):
        event.Skip()
    
    def _key3TextCtrlOnChar( self, event ):
        event.Skip()
    
    def _key3TextCtrlOnText( self, event ):
        event.Skip()
    
    def _oldKVNTextCtrlOnChar( self, event ):
        event.Skip()
    
    def _oldKVNTextCtrlOnText( self, event ):
        event.Skip()
    
    def _newKVNTextCtrlOnChar( self, event ):
        event.Skip()
    
    def _newKVNTextCtrlOnText( self, event ):
        event.Skip()
    
    def _putKeyButtonOnButtonClick( self, event ):
        event.Skip()
    
    def _deleteKeyButtonOnButtonClick( self, event ):
        event.Skip()
    
    def _resetKeyButtonOnButtonClick( self, event ):
        event.Skip()
    
    def _scriptFilePickerOnFileChanged( self, event ):
        event.Skip()
    
    def _scriptRefreshButtonOnButtonClick( self, event ):
        event.Skip()
    
    def _scriptLoopCountTextCtrlOnChar( self, event ):
        event.Skip()
    
    def _scriptRunButtonOnButtonClick( self, event ):
        event.Skip()
    
    def _scriptClearResultButtonOnButtonClick( self, event ):
        event.Skip()
    
    def m_splitter2OnIdle( self, event ):
        self.m_splitter2.SetSashPosition( 0 )
        self.m_splitter2.Unbind( wx.EVT_IDLE )
    

