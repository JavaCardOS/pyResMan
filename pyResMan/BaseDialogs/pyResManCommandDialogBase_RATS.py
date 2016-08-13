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
## Class CommandDialogBase_RATS
###########################################################################

class CommandDialogBase_RATS ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"RATS", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer56 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer57 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Header", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText24.Wrap( -1 )
        bSizer57.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlHeader = wx.TextCtrl( self, wx.ID_ANY, u"E0", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
        self._textctrlHeader.SetMaxLength( 2 ) 
        bSizer57.Add( self._textctrlHeader, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer57.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"FSDI", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText25.Wrap( -1 )
        bSizer57.Add( self.m_staticText25, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceFSDIChoices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8" ]
        self._choiceFSDI = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceFSDIChoices, 0 )
        self._choiceFSDI.SetSelection( 0 )
        bSizer57.Add( self._choiceFSDI, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer57.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"CID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText26.Wrap( -1 )
        bSizer57.Add( self.m_staticText26, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceCIDChoices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15" ]
        self._choiceCID = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceCIDChoices, 0 )
        self._choiceCID.SetSelection( 0 )
        bSizer57.Add( self._choiceCID, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer56.Add( bSizer57, 1, wx.EXPAND, 5 )
        
        bSizer58 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextCommandName = wx.StaticText( self, wx.ID_ANY, u"RATS", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextCommandName.Wrap( -1 )
        bSizer58.Add( self._statictextCommandName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlCommandValue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer58.Add( self._textctrlCommandValue, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer56.Add( bSizer58, 1, wx.EXPAND, 5 )
        
        bSizer59 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer59.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self._buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonOK.SetDefault() 
        bSizer59.Add( self._buttonOK, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer59.Add( self._buttonCancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer59.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer56.Add( bSizer59, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer56 )
        self.Layout()
        bSizer56.Fit( self )
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self._textctrlHeader.Bind( wx.EVT_TEXT, self._textctrlHeaderOnText )
        self._choiceFSDI.Bind( wx.EVT_CHOICE, self._choiceFSDIOnChoice )
        self._choiceCID.Bind( wx.EVT_CHOICE, self._choiceCIDOnChoice )
        self._textctrlCommandValue.Bind( wx.EVT_TEXT, self._textctrlCommandValueOnText )
        self._buttonOK.Bind( wx.EVT_BUTTON, self._buttonOKOnButtonClick )
        self._buttonCancel.Bind( wx.EVT_BUTTON, self._buttonCancelOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _textctrlHeaderOnText( self, event ):
        event.Skip()
    
    def _choiceFSDIOnChoice( self, event ):
        event.Skip()
    
    def _choiceCIDOnChoice( self, event ):
        event.Skip()
    
    def _textctrlCommandValueOnText( self, event ):
        event.Skip()
    
    def _buttonOKOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonCancelOnButtonClick( self, event ):
        event.Skip()
    

