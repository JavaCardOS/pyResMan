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
## Class CommandDialogBase_MifareLoadKey
###########################################################################

class CommandDialogBase_MifareLoadKey ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Mifare Load Key", pos = wx.DefaultPosition, size = wx.Size( 374,162 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer45 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer117 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText65 = wx.StaticText( self, wx.ID_ANY, u"Mode", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText65.Wrap( -1 )
        bSizer117.Add( self.m_staticText65, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceModeChoices = [ u"Key A", u"Key B" ]
        self._choiceMode = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceModeChoices, 0 )
        self._choiceMode.SetSelection( 0 )
        bSizer117.Add( self._choiceMode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText66 = wx.StaticText( self, wx.ID_ANY, u"Sector Number", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText66.Wrap( -1 )
        bSizer117.Add( self.m_staticText66, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceSectorNumberChoices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15" ]
        self._choiceSectorNumber = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceSectorNumberChoices, 0 )
        self._choiceSectorNumber.SetSelection( 0 )
        bSizer117.Add( self._choiceSectorNumber, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer45.Add( bSizer117, 1, wx.EXPAND, 5 )
        
        bSizer118 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText67 = wx.StaticText( self, wx.ID_ANY, u"Key", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText67.Wrap( -1 )
        bSizer118.Add( self.m_staticText67, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlKey = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlKey.SetMaxLength( 12 ) 
        bSizer118.Add( self._textctrlKey, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer45.Add( bSizer118, 1, wx.EXPAND, 5 )
        
        
        bSizer45.AddSpacer( ( 0, 20), 1, wx.EXPAND, 5 )
        
        bSizer46 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextCommandName = wx.StaticText( self, wx.ID_ANY, u"Load Key", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextCommandName.Wrap( -1 )
        bSizer46.Add( self._statictextCommandName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlCommandValue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlCommandValue.SetExtraStyle( wx.WS_EX_VALIDATE_RECURSIVELY )
        
        bSizer46.Add( self._textctrlCommandValue, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer45.Add( bSizer46, 0, wx.EXPAND, 5 )
        
        bSizer47 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer47.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self._buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonOK.SetDefault() 
        bSizer47.Add( self._buttonOK, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer47.Add( self._buttonCancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer47.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer45.Add( bSizer47, 0, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer45 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self._choiceMode.Bind( wx.EVT_CHOICE, self._choiceModeOnChoice )
        self._choiceSectorNumber.Bind( wx.EVT_CHOICE, self._choiceSectorNumberOnChoice )
        self._textctrlKey.Bind( wx.EVT_TEXT, self._textctrlKeyOnText )
        self._textctrlCommandValue.Bind( wx.EVT_TEXT, self._textctrlCommandValueOnText )
        self._buttonOK.Bind( wx.EVT_BUTTON, self._buttonOKOnButtonClick )
        self._buttonCancel.Bind( wx.EVT_BUTTON, self._buttonCancelOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _choiceModeOnChoice( self, event ):
        event.Skip()
    
    def _choiceSectorNumberOnChoice( self, event ):
        event.Skip()
    
    def _textctrlKeyOnText( self, event ):
        event.Skip()
    
    def _textctrlCommandValueOnText( self, event ):
        event.Skip()
    
    def _buttonOKOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonCancelOnButtonClick( self, event ):
        event.Skip()
    

