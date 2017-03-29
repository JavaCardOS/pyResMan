# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class pyResManDialogBase
###########################################################################

class pyResManDialogBase ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"pyResMan", pos = wx.DefaultPosition, size = wx.Size( 1028,687 ), style = wx.DEFAULT_DIALOG_STYLE|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        
        mainSizer = wx.BoxSizer( wx.VERTICAL )
        
        _connectSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"ReaderName", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        _connectSizer.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _comboReaderNameChoices = []
        self._comboReaderName = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), _comboReaderNameChoices, wx.CB_READONLY )
        self._comboReaderName.SetSelection( 0 )
        _connectSizer.Add( self._comboReaderName, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Protocol", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        _connectSizer.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _comboProtocolChoices = [ u"T0", u"T1", u"T0/T1" ]
        self._comboProtocol = wx.ComboBox( self, wx.ID_ANY, u"T0/T1", wx.DefaultPosition, wx.Size( 75,-1 ), _comboProtocolChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
        self._comboProtocol.SetSelection( 2 )
        _connectSizer.Add( self._comboProtocol, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Mode", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        _connectSizer.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _comboModeChoices = [ u"EXCLUSIVE", u"SHARED" ]
        self._comboMode = wx.ComboBox( self, wx.ID_ANY, u"SHARED", wx.DefaultPosition, wx.DefaultSize, _comboModeChoices, wx.CB_READONLY )
        self._comboMode.SetSelection( 1 )
        _connectSizer.Add( self._comboMode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonConnect = wx.Button( self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
        _connectSizer.Add( self._buttonConnect, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        mainSizer.Add( _connectSizer, 0, wx.EXPAND, 5 )
        
        bSizer46 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_splitter2 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
        self.m_splitter2.SetSashGravity( 0.72 )
        self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )
        self.m_splitter2.SetMinimumPaneSize( 1 )
        
        self.m_panel14 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer47 = wx.BoxSizer( wx.VERTICAL )
        
        self._notebookPages = wx.Notebook( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self._notebookPages.SetMinSize( wx.Size( -1,300 ) )
        
        self._panelApdu = wx.Panel( self._notebookPages, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        _apduPageSizer = wx.BoxSizer( wx.VERTICAL )
        
        _apduSizer = wx.BoxSizer( wx.VERTICAL )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._textctrlCLA = wx.TextCtrl( self._panelApdu, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._textctrlCLA.SetMaxLength( 2 ) 
        bSizer4.Add( self._textctrlCLA, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlINS = wx.TextCtrl( self._panelApdu, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._textctrlINS.SetMaxLength( 2 ) 
        bSizer4.Add( self._textctrlINS, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlP1 = wx.TextCtrl( self._panelApdu, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._textctrlP1.SetMaxLength( 2 ) 
        bSizer4.Add( self._textctrlP1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlP2 = wx.TextCtrl( self._panelApdu, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._textctrlP2.SetMaxLength( 2 ) 
        bSizer4.Add( self._textctrlP2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlLc = wx.TextCtrl( self._panelApdu, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.TE_READONLY )
        self._textctrlLc.SetMaxLength( 2 ) 
        bSizer4.Add( self._textctrlLc, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlData = wx.TextCtrl( self._panelApdu, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer4.Add( self._textctrlData, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlLe = wx.TextCtrl( self._panelApdu, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._textctrlLe.SetMaxLength( 2 ) 
        bSizer4.Add( self._textctrlLe, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer5.Add( bSizer4, 0, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._checkboxAutoGetResponse = wx.CheckBox( self._panelApdu, wx.ID_ANY, u"Auto GET RESPONSE", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self._checkboxAutoGetResponse, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonTransmit = wx.Button( self._panelApdu, wx.ID_ANY, u"Transmit", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self._buttonTransmit, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer5.Add( bSizer6, 0, wx.EXPAND, 5 )
        
        
        _apduSizer.Add( bSizer5, 0, wx.EXPAND, 5 )
        
        
        _apduPageSizer.Add( _apduSizer, 0, wx.EXPAND, 5 )
        
        self._listctrlApduList = wx.ListCtrl( self._panelApdu, wx.ID_ANY, wx.DefaultPosition, wx.Size( 820,-1 ), wx.LC_REPORT )
        _apduPageSizer.Add( self._listctrlApduList, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self._panelApdu.SetSizer( _apduPageSizer )
        self._panelApdu.Layout()
        _apduPageSizer.Fit( self._panelApdu )
        self._notebookPages.AddPage( self._panelApdu, u"Basic APDU", True )
        self._panelGP = wx.Panel( self._notebookPages, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        _gpPageSizer = wx.BoxSizer( wx.VERTICAL )
        
        bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer52 = wx.BoxSizer( wx.VERTICAL )
        
        
        bSizer52.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        bSizer53 = wx.BoxSizer( wx.HORIZONTAL )
        
        _radioSCPInfoMethodChoices = [ u"Auto Detect", u"User input" ]
        self._radioSCPInfoMethod = wx.RadioBox( self._panelGP, wx.ID_ANY, u"SCP informations", wx.DefaultPosition, wx.DefaultSize, _radioSCPInfoMethodChoices, 1, wx.RA_SPECIFY_ROWS )
        self._radioSCPInfoMethod.SetSelection( 0 )
        bSizer53.Add( self._radioSCPInfoMethod, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        bSizer37 = wx.BoxSizer( wx.VERTICAL )
        
        
        bSizer37.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        bSizer36 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText11 = wx.StaticText( self._panelGP, wx.ID_ANY, u"SCP", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        bSizer36.Add( self.m_staticText11, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceSCPChoices = [ u"1", u"2", u"3" ]
        self._choiceSCP = wx.Choice( self._panelGP, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceSCPChoices, 0 )
        self._choiceSCP.SetSelection( 1 )
        self._choiceSCP.Enable( False )
        
        bSizer36.Add( self._choiceSCP, 0, wx.ALL, 5 )
        
        
        bSizer36.AddSpacer( ( 10, 0), 0, 0, 5 )
        
        self.m_staticText12 = wx.StaticText( self._panelGP, wx.ID_ANY, u"i", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        bSizer36.Add( self.m_staticText12, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlSCPi = wx.TextCtrl( self._panelGP, wx.ID_ANY, u"15", wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._textctrlSCPi.SetMaxLength( 2 ) 
        self._textctrlSCPi.Enable( False )
        
        bSizer36.Add( self._textctrlSCPi, 0, wx.ALL, 5 )
        
        
        bSizer36.AddSpacer( ( 10, 0), 0, 0, 5 )
        
        
        bSizer36.AddSpacer( ( 0, 0), 0, 0, 5 )
        
        
        bSizer37.Add( bSizer36, 0, 0, 5 )
        
        
        bSizer37.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer53.Add( bSizer37, 0, wx.EXPAND, 5 )
        
        bSizer38 = wx.BoxSizer( wx.VERTICAL )
        
        
        bSizer38.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self._buttonMutualAuth = wx.Button( self._panelGP, wx.ID_ANY, u"Mutual Authentication", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer38.Add( self._buttonMutualAuth, 0, wx.ALL, 5 )
        
        
        bSizer38.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer53.Add( bSizer38, 1, wx.EXPAND, 5 )
        
        
        bSizer52.Add( bSizer53, 0, wx.EXPAND, 5 )
        
        
        bSizer41.Add( bSizer52, 1, wx.EXPAND, 5 )
        
        
        _gpPageSizer.Add( bSizer41, 0, wx.EXPAND, 5 )
        
        self.m_notebook2 = wx.Notebook( self._panelGP, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,500 ), wx.NB_TOP )
        self._contentManagerPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer231 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer30 = wx.BoxSizer( wx.VERTICAL )
        
        self._filepickerCapFile = wx.FilePickerCtrl( self._contentManagerPage, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.cap", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        bSizer30.Add( self._filepickerCapFile, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer231.Add( bSizer30, 0, wx.EXPAND, 5 )
        
        bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._treectrlCapFileInformation = wx.TreeCtrl( self._contentManagerPage, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TR_DEFAULT_STYLE )
        bSizer31.Add( self._treectrlCapFileInformation, 1, wx.ALL|wx.EXPAND, 5 )
        
        bSizer50 = wx.BoxSizer( wx.VERTICAL )
        
        self._buttonLoad = wx.Button( self._contentManagerPage, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonLoad.Enable( False )
        
        bSizer50.Add( self._buttonLoad, 0, wx.ALL, 5 )
        
        self._buttonInstall = wx.Button( self._contentManagerPage, wx.ID_ANY, u"Install", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonInstall.Enable( False )
        
        bSizer50.Add( self._buttonInstall, 0, wx.ALL, 5 )
        
        
        bSizer50.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer31.Add( bSizer50, 0, wx.EXPAND, 5 )
        
        
        bSizer231.Add( bSizer31, 1, wx.EXPAND, 5 )
        
        
        self._contentManagerPage.SetSizer( bSizer231 )
        self._contentManagerPage.Layout()
        bSizer231.Fit( self._contentManagerPage )
        self.m_notebook2.AddPage( self._contentManagerPage, u"Content Manager", False )
        self._contentViewerPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer23 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._treectrlCardContent = wx.TreeCtrl( self._contentViewerPage, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TR_DEFAULT_STYLE )
        bSizer23.Add( self._treectrlCardContent, 1, wx.ALL|wx.EXPAND, 5 )
        
        bSizer26 = wx.BoxSizer( wx.VERTICAL )
        
        self._buttonRefreshCardContent = wx.Button( self._contentViewerPage, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer26.Add( self._buttonRefreshCardContent, 0, wx.ALL, 5 )
        
        self._buttonInstallCardContent = wx.Button( self._contentViewerPage, wx.ID_ANY, u"Install", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonInstallCardContent.Enable( False )
        
        bSizer26.Add( self._buttonInstallCardContent, 0, wx.ALL, 5 )
        
        self._buttonSelectCardContent = wx.Button( self._contentViewerPage, wx.ID_ANY, u"Select", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonSelectCardContent.Enable( False )
        
        bSizer26.Add( self._buttonSelectCardContent, 0, wx.ALL, 5 )
        
        self._buttonDeleteCardContent = wx.Button( self._contentViewerPage, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonDeleteCardContent.Enable( False )
        
        bSizer26.Add( self._buttonDeleteCardContent, 0, wx.ALL, 5 )
        
        
        bSizer23.Add( bSizer26, 0, wx.EXPAND, 5 )
        
        
        self._contentViewerPage.SetSizer( bSizer23 )
        self._contentViewerPage.Layout()
        bSizer23.Fit( self._contentViewerPage )
        self.m_notebook2.AddPage( self._contentViewerPage, u"Content Viewer", False )
        self._keyManagerPage = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer342 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._listctrlKeyData = wx.ListCtrl( self._keyManagerPage, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), wx.LC_REPORT )
        bSizer51.Add( self._listctrlKeyData, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer34.Add( bSizer51, 1, wx.EXPAND, 5 )
        
        bSizer40 = wx.BoxSizer( wx.VERTICAL )
        
        self._buttonGetKeyTemplateInfo = wx.Button( self._keyManagerPage, wx.ID_ANY, u"Get Key Template Information", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer40.Add( self._buttonGetKeyTemplateInfo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer28 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer29 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self._keyManagerPage, wx.ID_ANY, u"S-ENC", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer29.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlKey1Length = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.TE_READONLY )
        bSizer29.Add( self._textctrlKey1Length, 0, wx.ALL, 5 )
        
        self._textctrlKey1 = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlKey1.SetMinSize( wx.Size( 300,-1 ) )
        
        bSizer29.Add( self._textctrlKey1, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer28.Add( bSizer29, 1, wx.EXPAND, 5 )
        
        bSizer301 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self._keyManagerPage, wx.ID_ANY, u"S-MAC", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer301.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlKey2Length = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.TE_READONLY )
        bSizer301.Add( self._textctrlKey2Length, 0, wx.ALL, 5 )
        
        self._textctrlKey2 = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlKey2.SetMinSize( wx.Size( 300,-1 ) )
        
        bSizer301.Add( self._textctrlKey2, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer28.Add( bSizer301, 1, wx.EXPAND, 5 )
        
        bSizer311 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self._keyManagerPage, wx.ID_ANY, u"    DEK", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer311.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlKey3Length = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), wx.TE_READONLY )
        bSizer311.Add( self._textctrlKey3Length, 0, wx.ALL, 5 )
        
        self._textctrlKey3 = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlKey3.SetMinSize( wx.Size( 300,-1 ) )
        
        bSizer311.Add( self._textctrlKey3, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer28.Add( bSizer311, 1, wx.EXPAND, 5 )
        
        
        bSizer40.Add( bSizer28, 0, wx.EXPAND, 5 )
        
        bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText10 = wx.StaticText( self._keyManagerPage, wx.ID_ANY, u"Old KVN", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        bSizer33.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlOldKVN = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._textctrlOldKVN.SetMaxLength( 2 ) 
        bSizer33.Add( self._textctrlOldKVN, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText9 = wx.StaticText( self._keyManagerPage, wx.ID_ANY, u"NewKVN", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer33.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlNewKVN = wx.TextCtrl( self._keyManagerPage, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 25,-1 ), 0 )
        self._textctrlNewKVN.SetMaxLength( 2 ) 
        bSizer33.Add( self._textctrlNewKVN, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonPutKey = wx.Button( self._keyManagerPage, wx.ID_ANY, u"Put Key", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer33.Add( self._buttonPutKey, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonDeleteKey = wx.Button( self._keyManagerPage, wx.ID_ANY, u"Delete Key", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer33.Add( self._buttonDeleteKey, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonKeyDefault = wx.Button( self._keyManagerPage, wx.ID_ANY, u"Default", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        bSizer33.Add( self._buttonKeyDefault, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer40.Add( bSizer33, 0, wx.EXPAND, 5 )
        
        
        bSizer40.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer34.Add( bSizer40, 0, wx.EXPAND, 5 )
        
        
        bSizer342.Add( bSizer34, 1, wx.EXPAND, 5 )
        
        
        self._keyManagerPage.SetSizer( bSizer342 )
        self._keyManagerPage.Layout()
        bSizer342.Fit( self._keyManagerPage )
        self.m_notebook2.AddPage( self._keyManagerPage, u"Key Manager", True )
        
        _gpPageSizer.Add( self.m_notebook2, 0, wx.EXPAND |wx.ALL, 5 )
        
        
        self._panelGP.SetSizer( _gpPageSizer )
        self._panelGP.Layout()
        _gpPageSizer.Fit( self._panelGP )
        self._notebookPages.AddPage( self._panelGP, u"GlobalPlatform", False )
        self._panelScript = wx.Panel( self._notebookPages, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer44 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer45 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._filepickerScriptFile = wx.FilePickerCtrl( self._panelScript, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.Size( 650,-1 ), wx.FLP_DEFAULT_STYLE )
        bSizer45.Add( self._filepickerScriptFile, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonScriptRefresh = wx.Button( self._panelScript, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer45.Add( self._buttonScriptRefresh, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText4 = wx.StaticText( self._panelScript, wx.ID_ANY, u"Loop count:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer45.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlScriptLoopCount = wx.TextCtrl( self._panelScript, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
        bSizer45.Add( self._textctrlScriptLoopCount, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonScriptRun = wx.Button( self._panelScript, wx.ID_ANY, u"Run Script", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer45.Add( self._buttonScriptRun, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonScriptClearResult = wx.Button( self._panelScript, wx.ID_ANY, u"Clear Result", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer45.Add( self._buttonScriptClearResult, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer44.Add( bSizer45, 0, wx.EXPAND, 5 )
        
        self._listctrlScriptList = wx.ListCtrl( self._panelScript, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LC_REPORT )
        bSizer44.Add( self._listctrlScriptList, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self._panelScript.SetSizer( bSizer44 )
        self._panelScript.Layout()
        bSizer44.Fit( self._panelScript )
        self._notebookPages.AddPage( self._panelScript, u"Script", False )
        self._panelSCDebugger = wx.Panel( self._notebookPages, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer411 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel13 = wx.Panel( self._panelSCDebugger, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer451 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._textctrlDebuggerScriptFilePathName = wx.TextCtrl( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        bSizer451.Add( self._textctrlDebuggerScriptFilePathName, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonDebuggerScriptLoadFile = wx.Button( self.m_panel13, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonDebuggerScriptLoadFile.SetMaxSize( wx.Size( 50,-1 ) )
        
        bSizer451.Add( self._buttonDebuggerScriptLoadFile, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonDebuggerScriptSaveFile = wx.Button( self.m_panel13, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonDebuggerScriptSaveFile.SetMaxSize( wx.Size( 50,-1 ) )
        
        bSizer451.Add( self._buttonDebuggerScriptSaveFile, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText13 = wx.StaticText( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
        self.m_staticText13.Wrap( -1 )
        bSizer451.Add( self.m_staticText13, 0, wx.ALL, 5 )
        
        self._buttonDebuggerScriptItemUp = wx.Button( self.m_panel13, wx.ID_ANY, u"Up", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonDebuggerScriptItemUp.SetMaxSize( wx.Size( 50,-1 ) )
        
        bSizer451.Add( self._buttonDebuggerScriptItemUp, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonDebuggerScriptItemDown = wx.Button( self.m_panel13, wx.ID_ANY, u"Down", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonDebuggerScriptItemDown.SetMaxSize( wx.Size( 50,-1 ) )
        
        bSizer451.Add( self._buttonDebuggerScriptItemDown, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonDebuggerScriptItemDelete = wx.Button( self.m_panel13, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonDebuggerScriptItemDelete.SetMaxSize( wx.Size( 50,-1 ) )
        
        bSizer451.Add( self._buttonDebuggerScriptItemDelete, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText131 = wx.StaticText( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
        self.m_staticText131.Wrap( -1 )
        bSizer451.Add( self.m_staticText131, 0, wx.ALL, 5 )
        
        self._buttonDebuggerScriptRun = wx.Button( self.m_panel13, wx.ID_ANY, u"Play", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonDebuggerScriptRun.SetMaxSize( wx.Size( 50,-1 ) )
        
        bSizer451.Add( self._buttonDebuggerScriptRun, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonDebuggerScriptStep = wx.Button( self.m_panel13, wx.ID_ANY, u"Step", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonDebuggerScriptStep.SetMaxSize( wx.Size( 50,-1 ) )
        
        bSizer451.Add( self._buttonDebuggerScriptStep, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonDebuggerScriptStop = wx.Button( self.m_panel13, wx.ID_ANY, u"Stop", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonDebuggerScriptStop.SetMaxSize( wx.Size( 50,-1 ) )
        
        bSizer451.Add( self._buttonDebuggerScriptStop, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        self.m_panel13.SetSizer( bSizer451 )
        self.m_panel13.Layout()
        bSizer451.Fit( self.m_panel13 )
        bSizer411.Add( self.m_panel13, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_splitter21 = wx.SplitterWindow( self._panelSCDebugger, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
        self.m_splitter21.SetSashGravity( 0.2 )
        self.m_splitter21.Bind( wx.EVT_IDLE, self.m_splitter21OnIdle )
        
        self.m_panel11 = wx.Panel( self.m_splitter21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer42 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._treectrlDebuggerCommands = wx.TreeCtrl( self.m_panel11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        bSizer42.Add( self._treectrlDebuggerCommands, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel11.SetSizer( bSizer42 )
        self.m_panel11.Layout()
        bSizer42.Fit( self.m_panel11 )
        self.m_panel12 = wx.Panel( self.m_splitter21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer441 = wx.BoxSizer( wx.VERTICAL )
        
        self._listctrlDebuggerScriptCommand = wx.grid.Grid( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        
        # Grid
        self._listctrlDebuggerScriptCommand.CreateGrid( 0, 0 )
        self._listctrlDebuggerScriptCommand.EnableEditing( False )
        self._listctrlDebuggerScriptCommand.EnableGridLines( True )
        self._listctrlDebuggerScriptCommand.EnableDragGridSize( False )
        self._listctrlDebuggerScriptCommand.SetMargins( 0, 0 )
        
        # Columns
        self._listctrlDebuggerScriptCommand.AutoSizeColumns()
        self._listctrlDebuggerScriptCommand.EnableDragColMove( False )
        self._listctrlDebuggerScriptCommand.EnableDragColSize( True )
        self._listctrlDebuggerScriptCommand.SetColLabelSize( 0 )
        self._listctrlDebuggerScriptCommand.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        
        # Rows
        self._listctrlDebuggerScriptCommand.EnableDragRowSize( True )
        self._listctrlDebuggerScriptCommand.SetRowLabelSize( 0 )
        self._listctrlDebuggerScriptCommand.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        
        # Label Appearance
        
        # Cell Defaults
        self._listctrlDebuggerScriptCommand.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer441.Add( self._listctrlDebuggerScriptCommand, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel12.SetSizer( bSizer441 )
        self.m_panel12.Layout()
        bSizer441.Fit( self.m_panel12 )
        self.m_splitter21.SplitVertically( self.m_panel11, self.m_panel12, 0 )
        bSizer411.Add( self.m_splitter21, 1, wx.EXPAND, 5 )
        
        
        self._panelSCDebugger.SetSizer( bSizer411 )
        self._panelSCDebugger.Layout()
        bSizer411.Fit( self._panelSCDebugger )
        self._notebookPages.AddPage( self._panelSCDebugger, u"SmartCard Debugger", False )
        self._panelMifare = wx.Panel( self._notebookPages, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer155 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer161 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText92 = wx.StaticText( self._panelMifare, wx.ID_ANY, u"This function is only available for the online store product: ", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        self.m_staticText92.Wrap( -1 )
        self.m_staticText92.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
        
        bSizer161.Add( self.m_staticText92, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        self.m_hyperlink4 = wx.HyperlinkCtrl( self._panelMifare, wx.ID_ANY, u"Mifare Clone 1K", u"https://javacardos.com/store/mifare-clone-1k.php", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_LEFT|wx.HL_DEFAULT_STYLE )
        bSizer161.Add( self.m_hyperlink4, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )
        
        
        bSizer155.Add( bSizer161, 1, wx.ALIGN_CENTER, 5 )
        
        bSizer157 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._gridCardData = wx.grid.Grid( self._panelMifare, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        
        # Grid
        self._gridCardData.CreateGrid( 64, 16 )
        self._gridCardData.EnableEditing( True )
        self._gridCardData.EnableGridLines( True )
        self._gridCardData.EnableDragGridSize( False )
        self._gridCardData.SetMargins( 0, 0 )
        
        # Columns
        self._gridCardData.AutoSizeColumns()
        self._gridCardData.EnableDragColMove( False )
        self._gridCardData.EnableDragColSize( True )
        self._gridCardData.SetColLabelSize( 30 )
        self._gridCardData.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        
        # Rows
        self._gridCardData.EnableDragRowSize( True )
        self._gridCardData.SetRowLabelSize( 80 )
        self._gridCardData.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        
        # Label Appearance
        
        # Cell Defaults
        self._gridCardData.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
        bSizer157.Add( self._gridCardData, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticline3 = wx.StaticLine( self._panelMifare, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        bSizer157.Add( self.m_staticline3, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        bSizer158 = wx.BoxSizer( wx.VERTICAL )
        
        self._buttonLoadCardData = wx.Button( self._panelMifare, wx.ID_ANY, u"Load Data From File ...", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer158.Add( self._buttonLoadCardData, 0, wx.ALL|wx.EXPAND, 5 )
        
        self._buttonSaveCardData = wx.Button( self._panelMifare, wx.ID_ANY, u"Save Data To File ...", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer158.Add( self._buttonSaveCardData, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
        
        self.m_staticline4 = wx.StaticLine( self._panelMifare, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LI_VERTICAL )
        bSizer158.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
        
        bSizer160 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText91 = wx.StaticText( self._panelMifare, wx.ID_ANY, u"KeyA:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText91.Wrap( -1 )
        bSizer160.Add( self.m_staticText91, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlKeyA = wx.TextCtrl( self._panelMifare, wx.ID_ANY, u"FFFFFFFFFFFF", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlKeyA.SetMaxLength( 12 ) 
        bSizer160.Add( self._textctrlKeyA, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer158.Add( bSizer160, 0, wx.EXPAND, 5 )
        
        self._buttonDumpCard = wx.Button( self._panelMifare, wx.ID_ANY, u"Dump Card", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer158.Add( self._buttonDumpCard, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
        
        self._buttonCloneCard = wx.Button( self._panelMifare, wx.ID_ANY, u"Clone Card", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer158.Add( self._buttonCloneCard, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticline2 = wx.StaticLine( self._panelMifare, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LI_VERTICAL )
        bSizer158.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
        
        bSizer159 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText90 = wx.StaticText( self._panelMifare, wx.ID_ANY, u"UID:", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
        self.m_staticText90.Wrap( -1 )
        bSizer159.Add( self.m_staticText90, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlUID = wx.TextCtrl( self._panelMifare, wx.ID_ANY, u"00000000", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlUID.SetMaxLength( 8 ) 
        bSizer159.Add( self._textctrlUID, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer158.Add( bSizer159, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self._buttonChangeUID = wx.Button( self._panelMifare, wx.ID_ANY, u"Change UID", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer158.Add( self._buttonChangeUID, 0, wx.ALL|wx.EXPAND, 5 )
        
        self._buttonUnblockCard = wx.Button( self._panelMifare, wx.ID_ANY, u"UnblockCard", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer158.Add( self._buttonUnblockCard, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticline21 = wx.StaticLine( self._panelMifare, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.LI_VERTICAL )
        bSizer158.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
        
        self._buttonClearCardData = wx.Button( self._panelMifare, wx.ID_ANY, u"Clear Data", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer158.Add( self._buttonClearCardData, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer157.Add( bSizer158, 0, wx.EXPAND, 5 )
        
        
        bSizer155.Add( bSizer157, 1, wx.EXPAND, 5 )
        
        
        self._panelMifare.SetSizer( bSizer155 )
        self._panelMifare.Layout()
        bSizer155.Fit( self._panelMifare )
        self._notebookPages.AddPage( self._panelMifare, u"Mifare", False )
        self._panelAbout = wx.Panel( self._notebookPages, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer331 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer331.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        bSizer43 = wx.BoxSizer( wx.VERTICAL )
        
        
        bSizer43.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        bSizer401 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer401.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText101 = wx.StaticText( self._panelAbout, wx.ID_ANY, u"PyResMan v4.0", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText101.Wrap( -1 )
        bSizer401.Add( self.m_staticText101, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer401.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer43.Add( bSizer401, 0, wx.EXPAND, 5 )
        
        bSizer39 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer39.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText94 = wx.StaticText( self._panelAbout, wx.ID_ANY, u"JavaCardOS Technologies. All rights reserved.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText94.Wrap( -1 )
        bSizer39.Add( self.m_staticText94, 0, wx.ALL, 5 )
        
        
        bSizer39.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer43.Add( bSizer39, 0, wx.EXPAND, 5 )
        
        bSizer381 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer381.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_hyperlink2 = wx.HyperlinkCtrl( self._panelAbout, wx.ID_ANY, u"Site: https://www.javacardos.com/", u"https://www.javacardos.com/?s=pyresman", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_CENTRE|wx.HL_DEFAULT_STYLE )
        bSizer381.Add( self.m_hyperlink2, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer381.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer43.Add( bSizer381, 0, wx.EXPAND, 5 )
        
        bSizer371 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer371.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_hyperlink3 = wx.HyperlinkCtrl( self._panelAbout, wx.ID_ANY, u"Forum: https://www.javacardos.com/javacardforum/", u"https://www.javacardos.com/javacardforum//?s=pyresman", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_CENTRE|wx.HL_DEFAULT_STYLE )
        bSizer371.Add( self.m_hyperlink3, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer371.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer43.Add( bSizer371, 0, wx.EXPAND, 5 )
        
        
        bSizer43.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer331.Add( bSizer43, 1, wx.EXPAND, 5 )
        
        
        bSizer331.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        self._panelAbout.SetSizer( bSizer331 )
        self._panelAbout.Layout()
        bSizer331.Fit( self._panelAbout )
        self._notebookPages.AddPage( self._panelAbout, u"About", False )
        
        bSizer47.Add( self._notebookPages, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel14.SetSizer( bSizer47 )
        self.m_panel14.Layout()
        bSizer47.Fit( self.m_panel14 )
        self.m_panel15 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer49 = wx.BoxSizer( wx.VERTICAL )
        
        self._textctrlLog = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_RICH2 )
        bSizer49.Add( self._textctrlLog, 1, wx.ALL|wx.EXPAND, 5 )
        
        bSizer154 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer154.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText93 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"JavaCardOS Technologies. All rights reserved.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText93.Wrap( -1 )
        bSizer154.Add( self.m_staticText93, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticline5 = wx.StaticLine( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        bSizer154.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_hyperlink21 = wx.HyperlinkCtrl( self.m_panel15, wx.ID_ANY, u"Site: https://www.javacardos.com/", u"https://www.javacardos.com/?s=pyresman", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_CENTRE|wx.HL_DEFAULT_STYLE )
        bSizer154.Add( self.m_hyperlink21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticline6 = wx.StaticLine( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
        bSizer154.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_hyperlink31 = wx.HyperlinkCtrl( self.m_panel15, wx.ID_ANY, u"Forum: https://www.javacardos.com/javacardforum/", u"https://www.javacardos.com/javacardforum//?s=pyresman", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_CENTRE|wx.HL_DEFAULT_STYLE )
        bSizer154.Add( self.m_hyperlink31, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer154.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self._buttonClearLog = wx.Button( self.m_panel15, wx.ID_ANY, u"Clear Log", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer154.Add( self._buttonClearLog, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
        
        
        bSizer154.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer49.Add( bSizer154, 0, wx.EXPAND, 5 )
        
        
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
        self._buttonConnect.Bind( wx.EVT_BUTTON, self._buttonConnectOnButtonClick )
        self._textctrlCLA.Bind( wx.EVT_CHAR, self._textctrlCLAOnChar )
        self._textctrlINS.Bind( wx.EVT_CHAR, self._textctrlINSOnChar )
        self._textctrlP1.Bind( wx.EVT_CHAR, self._textctrlP1OnChar )
        self._textctrlP2.Bind( wx.EVT_CHAR, self._textctrlP2OnChar )
        self._textctrlData.Bind( wx.EVT_CHAR, self._textctrlDataOnChar )
        self._textctrlData.Bind( wx.EVT_TEXT, self._textctrlDataOnText )
        self._textctrlLe.Bind( wx.EVT_CHAR, self._textctrlLeOnChar )
        self._buttonTransmit.Bind( wx.EVT_BUTTON, self._buttonTransmitOnButtonClick )
        self._radioSCPInfoMethod.Bind( wx.EVT_RADIOBOX, self._radioSCPInfoMethodOnRadioBox )
        self._textctrlSCPi.Bind( wx.EVT_CHAR, self._textctrlSCPiOnChar )
        self._buttonMutualAuth.Bind( wx.EVT_BUTTON, self._buttonMutualAuthOnButtonClick )
        self._filepickerCapFile.Bind( wx.EVT_FILEPICKER_CHANGED, self._filepickerCapFileOnFileChanged )
        self._treectrlCapFileInformation.Bind( wx.EVT_TREE_SEL_CHANGED, self._treectrlCapFileInformationOnTreeSelChanged )
        self._buttonLoad.Bind( wx.EVT_BUTTON, self._buttonLoadOnButtonClick )
        self._buttonInstall.Bind( wx.EVT_BUTTON, self._buttonInstallOnButtonClick )
        self._treectrlCardContent.Bind( wx.EVT_TREE_SEL_CHANGED, self._treectrlCardContentOnTreeSelChanged )
        self._buttonRefreshCardContent.Bind( wx.EVT_BUTTON, self._buttonRefreshCardContentOnButtonClick )
        self._buttonInstallCardContent.Bind( wx.EVT_BUTTON, self._buttonInstallCardContentOnButtonClick )
        self._buttonSelectCardContent.Bind( wx.EVT_BUTTON, self._buttonSelectCardContentOnButtonClick )
        self._buttonDeleteCardContent.Bind( wx.EVT_BUTTON, self._buttonDeleteCardContentOnButtonClick )
        self._listctrlKeyData.Bind( wx.EVT_LIST_ITEM_SELECTED, self._listctrlKeyDataOnListItemSelected )
        self._buttonGetKeyTemplateInfo.Bind( wx.EVT_BUTTON, self._buttonGetKeyTemplateInfoOnButtonClick )
        self._textctrlKey1.Bind( wx.EVT_CHAR, self._textctrlKey1OnChar )
        self._textctrlKey1.Bind( wx.EVT_TEXT, self._textctrlKey1OnText )
        self._textctrlKey2.Bind( wx.EVT_CHAR, self._textctrlKey2OnChar )
        self._textctrlKey2.Bind( wx.EVT_TEXT, self._textctrlKey2OnText )
        self._textctrlKey3.Bind( wx.EVT_CHAR, self._textctrlKey3OnChar )
        self._textctrlKey3.Bind( wx.EVT_TEXT, self._textctrlKey3OnText )
        self._textctrlOldKVN.Bind( wx.EVT_CHAR, self._oldKVNTextCtrlOnChar )
        self._textctrlOldKVN.Bind( wx.EVT_TEXT, self._oldKVNTextCtrlOnText )
        self._textctrlNewKVN.Bind( wx.EVT_CHAR, self._newKVNTextCtrlOnChar )
        self._textctrlNewKVN.Bind( wx.EVT_TEXT, self._newKVNTextCtrlOnText )
        self._buttonPutKey.Bind( wx.EVT_BUTTON, self._buttonPutKeyOnButtonClick )
        self._buttonDeleteKey.Bind( wx.EVT_BUTTON, self._buttonDeleteKeyOnButtonClick )
        self._buttonKeyDefault.Bind( wx.EVT_BUTTON, self._buttonKeyDefaultOnButtonClick )
        self._filepickerScriptFile.Bind( wx.EVT_FILEPICKER_CHANGED, self._filepickerScriptFileOnFileChanged )
        self._buttonScriptRefresh.Bind( wx.EVT_BUTTON, self._buttonScriptRefreshOnButtonClick )
        self._textctrlScriptLoopCount.Bind( wx.EVT_CHAR, self._textctrlScriptLoopCountOnChar )
        self._buttonScriptRun.Bind( wx.EVT_BUTTON, self._buttonScriptRunOnButtonClick )
        self._buttonScriptClearResult.Bind( wx.EVT_BUTTON, self._buttonScriptClearResultOnButtonClick )
        self._buttonDebuggerScriptLoadFile.Bind( wx.EVT_BUTTON, self._buttonDebuggerScriptLoadFileOnButtonClick )
        self._buttonDebuggerScriptSaveFile.Bind( wx.EVT_BUTTON, self._buttonDebuggerScriptSaveFileOnButtonClick )
        self._buttonDebuggerScriptItemUp.Bind( wx.EVT_BUTTON, self._buttonDebuggerScriptItemUpOnButtonClick )
        self._buttonDebuggerScriptItemDown.Bind( wx.EVT_BUTTON, self._buttonDebuggerScriptItemDownOnButtonClick )
        self._buttonDebuggerScriptItemDelete.Bind( wx.EVT_BUTTON, self._buttonDebuggerScriptItemDeleteOnButtonClick )
        self._buttonDebuggerScriptRun.Bind( wx.EVT_BUTTON, self._buttonDebuggerScriptRunOnButtonClick )
        self._buttonDebuggerScriptStep.Bind( wx.EVT_BUTTON, self._buttonDebuggerScriptStepOnButtonClick )
        self._buttonDebuggerScriptStop.Bind( wx.EVT_BUTTON, self._buttonDebuggerScriptStopOnButtonClick )
        self._treectrlDebuggerCommands.Bind( wx.EVT_LEFT_DCLICK, self._treectrlDebuggerCommandsOnLeftDClick )
        self._listctrlDebuggerScriptCommand.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self._listctrlDebuggerScriptCommandOnGridCellLeftDClick )
        self._buttonLoadCardData.Bind( wx.EVT_BUTTON, self._buttonLoadCardDataOnButtonClick )
        self._buttonSaveCardData.Bind( wx.EVT_BUTTON, self._buttonSaveCardDataOnButtonClick )
        self._buttonDumpCard.Bind( wx.EVT_BUTTON, self._buttonDumpCardOnButtonClick )
        self._buttonCloneCard.Bind( wx.EVT_BUTTON, self._buttonCloneCardOnButtonClick )
        self._buttonChangeUID.Bind( wx.EVT_BUTTON, self._buttonChangeUIDOnButtonClick )
        self._buttonUnblockCard.Bind( wx.EVT_BUTTON, self._buttonUnblockCardOnButtonClick )
        self._buttonClearCardData.Bind( wx.EVT_BUTTON, self._buttonClearCardDataOnButtonClick )
        self._buttonClearLog.Bind( wx.EVT_BUTTON, self._buttonClearLogOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _buttonConnectOnButtonClick( self, event ):
        event.Skip()
    
    def _textctrlCLAOnChar( self, event ):
        event.Skip()
    
    def _textctrlINSOnChar( self, event ):
        event.Skip()
    
    def _textctrlP1OnChar( self, event ):
        event.Skip()
    
    def _textctrlP2OnChar( self, event ):
        event.Skip()
    
    def _textctrlDataOnChar( self, event ):
        event.Skip()
    
    def _textctrlDataOnText( self, event ):
        event.Skip()
    
    def _textctrlLeOnChar( self, event ):
        event.Skip()
    
    def _buttonTransmitOnButtonClick( self, event ):
        event.Skip()
    
    def _radioSCPInfoMethodOnRadioBox( self, event ):
        event.Skip()
    
    def _textctrlSCPiOnChar( self, event ):
        event.Skip()
    
    def _buttonMutualAuthOnButtonClick( self, event ):
        event.Skip()
    
    def _filepickerCapFileOnFileChanged( self, event ):
        event.Skip()
    
    def _treectrlCapFileInformationOnTreeSelChanged( self, event ):
        event.Skip()
    
    def _buttonLoadOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonInstallOnButtonClick( self, event ):
        event.Skip()
    
    def _treectrlCardContentOnTreeSelChanged( self, event ):
        event.Skip()
    
    def _buttonRefreshCardContentOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonInstallCardContentOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonSelectCardContentOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonDeleteCardContentOnButtonClick( self, event ):
        event.Skip()
    
    def _listctrlKeyDataOnListItemSelected( self, event ):
        event.Skip()
    
    def _buttonGetKeyTemplateInfoOnButtonClick( self, event ):
        event.Skip()
    
    def _textctrlKey1OnChar( self, event ):
        event.Skip()
    
    def _textctrlKey1OnText( self, event ):
        event.Skip()
    
    def _textctrlKey2OnChar( self, event ):
        event.Skip()
    
    def _textctrlKey2OnText( self, event ):
        event.Skip()
    
    def _textctrlKey3OnChar( self, event ):
        event.Skip()
    
    def _textctrlKey3OnText( self, event ):
        event.Skip()
    
    def _oldKVNTextCtrlOnChar( self, event ):
        event.Skip()
    
    def _oldKVNTextCtrlOnText( self, event ):
        event.Skip()
    
    def _newKVNTextCtrlOnChar( self, event ):
        event.Skip()
    
    def _newKVNTextCtrlOnText( self, event ):
        event.Skip()
    
    def _buttonPutKeyOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonDeleteKeyOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonKeyDefaultOnButtonClick( self, event ):
        event.Skip()
    
    def _filepickerScriptFileOnFileChanged( self, event ):
        event.Skip()
    
    def _buttonScriptRefreshOnButtonClick( self, event ):
        event.Skip()
    
    def _textctrlScriptLoopCountOnChar( self, event ):
        event.Skip()
    
    def _buttonScriptRunOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonScriptClearResultOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonDebuggerScriptLoadFileOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonDebuggerScriptSaveFileOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonDebuggerScriptItemUpOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonDebuggerScriptItemDownOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonDebuggerScriptItemDeleteOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonDebuggerScriptRunOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonDebuggerScriptStepOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonDebuggerScriptStopOnButtonClick( self, event ):
        event.Skip()
    
    def _treectrlDebuggerCommandsOnLeftDClick( self, event ):
        event.Skip()
    
    def _listctrlDebuggerScriptCommandOnGridCellLeftDClick( self, event ):
        event.Skip()
    
    def _buttonLoadCardDataOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonSaveCardDataOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonDumpCardOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonCloneCardOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonChangeUIDOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonUnblockCardOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonClearCardDataOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonClearLogOnButtonClick( self, event ):
        event.Skip()
    
    def m_splitter2OnIdle( self, event ):
        self.m_splitter2.SetSashPosition( 0 )
        self.m_splitter2.Unbind( wx.EVT_IDLE )
    
    def m_splitter21OnIdle( self, event ):
        self.m_splitter21.SetSashPosition( 0 )
        self.m_splitter21.Unbind( wx.EVT_IDLE )
    

