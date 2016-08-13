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
## Class CommandDialogBase_AnticollisionSelect
###########################################################################

class CommandDialogBase_AnticollisionSelect ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ANTICOLLISION/SELECT", pos = wx.DefaultPosition, size = wx.Size( 359,176 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer48 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer49 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Level", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )
        self.m_staticText19.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
        
        bSizer49.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceLevelChoices = [ u"Level1", u"Level2", u"Level3" ]
        self._choiceLevel = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceLevelChoices, 0 )
        self._choiceLevel.SetSelection( 0 )
        bSizer49.Add( self._choiceLevel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer49.AddSpacer( ( 10, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Byte Count", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )
        bSizer49.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceByteCountChoices = [ u"2", u"3", u"4", u"5", u"6", u"7" ]
        self._choiceByteCount = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceByteCountChoices, 0 )
        self._choiceByteCount.SetSelection( 0 )
        bSizer49.Add( self._choiceByteCount, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer49.AddSpacer( ( 10, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Bit Count", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )
        bSizer49.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceBitCountChoices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7" ]
        self._choiceBitCount = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceBitCountChoices, 0 )
        self._choiceBitCount.SetSelection( 0 )
        bSizer49.Add( self._choiceBitCount, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer48.Add( bSizer49, 1, wx.EXPAND, 5 )
        
        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"UID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )
        bSizer51.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlUID = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlUID.SetMaxLength( 8 ) 
        bSizer51.Add( self._textctrlUID, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer48.Add( bSizer51, 1, wx.EXPAND, 5 )
        
        bSizer52 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextCommandName = wx.StaticText( self, wx.ID_ANY, u"Command Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextCommandName.Wrap( -1 )
        bSizer52.Add( self._statictextCommandName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlCommandValue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer52.Add( self._textctrlCommandValue, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer48.Add( bSizer52, 1, wx.EXPAND, 5 )
        
        bSizer491 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer491.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self._buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonOK.SetDefault() 
        bSizer491.Add( self._buttonOK, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer491.Add( self._buttonCancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer491.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer48.Add( bSizer491, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer48 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self._choiceLevel.Bind( wx.EVT_CHOICE, self._choiceLevelOnChoice )
        self._choiceByteCount.Bind( wx.EVT_CHOICE, self._choiceByteCountOnChoice )
        self._choiceBitCount.Bind( wx.EVT_CHOICE, self._choiceBitCountOnChoice )
        self._textctrlUID.Bind( wx.EVT_TEXT, self._textctrlUIDOnText )
        self._textctrlCommandValue.Bind( wx.EVT_TEXT, self._textctrlCommandValueOnText )
        self._buttonOK.Bind( wx.EVT_BUTTON, self._buttonOKOnButtonClick )
        self._buttonCancel.Bind( wx.EVT_BUTTON, self._buttonCancelOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _choiceLevelOnChoice( self, event ):
        event.Skip()
    
    def _choiceByteCountOnChoice( self, event ):
        event.Skip()
    
    def _choiceBitCountOnChoice( self, event ):
        event.Skip()
    
    def _textctrlUIDOnText( self, event ):
        event.Skip()
    
    def _textctrlCommandValueOnText( self, event ):
        event.Skip()
    
    def _buttonOKOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonCancelOnButtonClick( self, event ):
        event.Skip()
    

