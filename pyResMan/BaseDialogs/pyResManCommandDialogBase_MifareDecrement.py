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
## Class CommandDialogBase_MifareDecrement
###########################################################################

class CommandDialogBase_MifareDecrement ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Mifare Decrement", pos = wx.DefaultPosition, size = wx.Size( 374,171 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer45 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer117 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText65 = wx.StaticText( self, wx.ID_ANY, u"Block Number", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText65.Wrap( -1 )
        bSizer117.Add( self.m_staticText65, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceBlockNumberChoices = []
        self._choiceBlockNumber = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceBlockNumberChoices, 0 )
        self._choiceBlockNumber.SetSelection( 0 )
        bSizer117.Add( self._choiceBlockNumber, 0, wx.ALL, 5 )
        
        
        bSizer45.Add( bSizer117, 1, wx.EXPAND, 5 )
        
        bSizer146 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText86 = wx.StaticText( self, wx.ID_ANY, u"Operand", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText86.Wrap( -1 )
        bSizer146.Add( self.m_staticText86, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlValue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlValue.SetMaxLength( 8 ) 
        bSizer146.Add( self._textctrlValue, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer45.Add( bSizer146, 0, wx.EXPAND, 5 )
        
        
        bSizer45.AddSpacer( ( 0, 20), 1, wx.EXPAND, 5 )
        
        bSizer46 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextCommandName = wx.StaticText( self, wx.ID_ANY, u"Mifare Decrement", wx.DefaultPosition, wx.DefaultSize, 0 )
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
        self._choiceBlockNumber.Bind( wx.EVT_CHOICE, self._choiceBlockNumberOnChoice )
        self._textctrlValue.Bind( wx.EVT_TEXT, self._textctrlValueOnText )
        self._textctrlCommandValue.Bind( wx.EVT_TEXT, self._textctrlCommandValueOnText )
        self._buttonOK.Bind( wx.EVT_BUTTON, self._buttonOKOnButtonClick )
        self._buttonCancel.Bind( wx.EVT_BUTTON, self._buttonCancelOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _choiceBlockNumberOnChoice( self, event ):
        event.Skip()
    
    def _textctrlValueOnText( self, event ):
        event.Skip()
    
    def _textctrlCommandValueOnText( self, event ):
        event.Skip()
    
    def _buttonOKOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonCancelOnButtonClick( self, event ):
        event.Skip()
    

