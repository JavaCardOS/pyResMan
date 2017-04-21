# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class DESFireDialogBase_CreateApplication
###########################################################################

class DESFireDialogBase_CreateApplication ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"DESFire create application", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer167 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer168 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText95 = wx.StaticText( self, wx.ID_ANY, u"AID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText95.Wrap( -1 )
        bSizer168.Add( self.m_staticText95, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlAID = wx.TextCtrl( self, wx.ID_ANY, u"000001", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlAID.SetMaxLength( 6 ) 
        bSizer168.Add( self._textctrlAID, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer167.Add( bSizer168, 1, wx.EXPAND, 5 )
        
        bSizer169 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText96 = wx.StaticText( self, wx.ID_ANY, u"Key Sett.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText96.Wrap( -1 )
        bSizer169.Add( self.m_staticText96, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlKeySettings = wx.TextCtrl( self, wx.ID_ANY, u"0F", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlKeySettings.SetMaxLength( 2 ) 
        bSizer169.Add( self._textctrlKeySettings, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer167.Add( bSizer169, 0, wx.EXPAND, 5 )
        
        bSizer170 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText97 = wx.StaticText( self, wx.ID_ANY, u"Num Of Keys", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText97.Wrap( -1 )
        bSizer170.Add( self.m_staticText97, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlNumOfKeys = wx.TextCtrl( self, wx.ID_ANY, u"01", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlNumOfKeys.SetMaxLength( 2 ) 
        bSizer170.Add( self._textctrlNumOfKeys, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer167.Add( bSizer170, 1, wx.EXPAND, 5 )
        
        bSizer171 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonOK.SetDefault() 
        bSizer171.Add( self._buttonOK, 0, wx.ALL, 5 )
        
        self._buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer171.Add( self._buttonCancel, 0, wx.ALL, 5 )
        
        
        bSizer167.Add( bSizer171, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer167 )
        self.Layout()
        bSizer167.Fit( self )
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self._textctrlAID.Bind( wx.EVT_TEXT, self._textctrlAIDOnText )
        self._textctrlKeySettings.Bind( wx.EVT_TEXT, self._textctrlKeySettingsOnText )
        self._textctrlNumOfKeys.Bind( wx.EVT_TEXT, self._textctrlNumOfKeysOnText )
        self._buttonOK.Bind( wx.EVT_BUTTON, self._buttonOKOnButtonClick )
        self._buttonCancel.Bind( wx.EVT_BUTTON, self._buttonCancelOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _textctrlAIDOnText( self, event ):
        event.Skip()
    
    def _textctrlKeySettingsOnText( self, event ):
        event.Skip()
    
    def _textctrlNumOfKeysOnText( self, event ):
        event.Skip()
    
    def _buttonOKOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonCancelOnButtonClick( self, event ):
        event.Skip()
    

