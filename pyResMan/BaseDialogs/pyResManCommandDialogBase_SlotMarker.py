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
## Class CommandDialogBase_SlotMarker
###########################################################################

class CommandDialogBase_SlotMarker ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Slot-Marker", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer64 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer65 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText34.Wrap( -1 )
        bSizer65.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceCommandTypeChoices = [ u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15", u"16", wx.EmptyString ]
        self._choiceCommandType = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceCommandTypeChoices, 0 )
        self._choiceCommandType.SetSelection( 0 )
        bSizer65.Add( self._choiceCommandType, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer65.AddSpacer( ( 15, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer64.Add( bSizer65, 1, wx.EXPAND, 5 )
        
        bSizer66 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextCommandName = wx.StaticText( self, wx.ID_ANY, u"Slot Marker", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextCommandName.Wrap( -1 )
        bSizer66.Add( self._statictextCommandName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlCommandValue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( 30,-1 ), 0 )
        bSizer66.Add( self._textctrlCommandValue, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer64.Add( bSizer66, 1, wx.EXPAND, 5 )
        
        bSizer67 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer67.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self._buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonOK.SetDefault() 
        bSizer67.Add( self._buttonOK, 0, wx.ALL, 5 )
        
        self._buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer67.Add( self._buttonCancel, 0, wx.ALL, 5 )
        
        
        bSizer67.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer64.Add( bSizer67, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer64 )
        self.Layout()
        bSizer64.Fit( self )
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self._choiceCommandType.Bind( wx.EVT_CHOICE, self._choiceCommandTypeOnChoice )
        self._textctrlCommandValue.Bind( wx.EVT_TEXT, self._textctrlCommandValueOnText )
        self._buttonOK.Bind( wx.EVT_BUTTON, self._buttonOKOnButtonClick )
        self._buttonCancel.Bind( wx.EVT_BUTTON, self._buttonCancelOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _choiceCommandTypeOnChoice( self, event ):
        event.Skip()
    
    def _textctrlCommandValueOnText( self, event ):
        event.Skip()
    
    def _buttonOKOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonCancelOnButtonClick( self, event ):
        event.Skip()
    

