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
## Class CommandDialogBase_REQBWUPB
###########################################################################

class CommandDialogBase_REQBWUPB ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"REQB/WUPB", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer64 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer65 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Apf", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText32.Wrap( -1 )
        bSizer65.Add( self.m_staticText32, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlApf = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
        bSizer65.Add( self._textctrlApf, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer65.AddSpacer( ( 15, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"AFI", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText33.Wrap( -1 )
        bSizer65.Add( self.m_staticText33, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlAFI = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
        bSizer65.Add( self._textctrlAFI, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer65.AddSpacer( ( 15, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Command", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText34.Wrap( -1 )
        bSizer65.Add( self.m_staticText34, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceCommandTypeChoices = [ u"REQB", u"WUPB" ]
        self._choiceCommandType = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceCommandTypeChoices, 0 )
        self._choiceCommandType.SetSelection( 0 )
        bSizer65.Add( self._choiceCommandType, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer65.AddSpacer( ( 15, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Number of slots", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText35.Wrap( -1 )
        bSizer65.Add( self.m_staticText35, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceNumberOfSlotsChoices = [ u"1", u"2", u"4", u"5", u"8", u"16" ]
        self._choiceNumberOfSlots = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceNumberOfSlotsChoices, 0 )
        self._choiceNumberOfSlots.SetSelection( 0 )
        bSizer65.Add( self._choiceNumberOfSlots, 0, wx.ALL, 5 )
        
        
        bSizer64.Add( bSizer65, 1, wx.EXPAND, 5 )
        
        bSizer66 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextCommandName = wx.StaticText( self, wx.ID_ANY, u"Command Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextCommandName.Wrap( -1 )
        bSizer66.Add( self._statictextCommandName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlCommandValue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
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
        self._textctrlApf.Bind( wx.EVT_TEXT, self._textctrlApfOnText )
        self._textctrlAFI.Bind( wx.EVT_TEXT, self._textctrlAFIOnText )
        self._choiceCommandType.Bind( wx.EVT_CHOICE, self._choiceCommandTypeOnChoice )
        self._choiceNumberOfSlots.Bind( wx.EVT_CHOICE, self._choiceNumberOfSlotsOnChoice )
        self._textctrlCommandValue.Bind( wx.EVT_TEXT, self._textctrlCommandValueOnText )
        self._buttonOK.Bind( wx.EVT_BUTTON, self._buttonOKOnButtonClick )
        self._buttonCancel.Bind( wx.EVT_BUTTON, self._buttonCancelOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _textctrlApfOnText( self, event ):
        event.Skip()
    
    def _textctrlAFIOnText( self, event ):
        event.Skip()
    
    def _choiceCommandTypeOnChoice( self, event ):
        event.Skip()
    
    def _choiceNumberOfSlotsOnChoice( self, event ):
        event.Skip()
    
    def _textctrlCommandValueOnText( self, event ):
        event.Skip()
    
    def _buttonOKOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonCancelOnButtonClick( self, event ):
        event.Skip()
    

