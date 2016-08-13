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
## Class CommandDialogBase_PPS
###########################################################################

class CommandDialogBase_PPS ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"PPS", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer60 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer61 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"CID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText28.Wrap( -1 )
        bSizer61.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceCIDChoices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15" ]
        self._choiceCID = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceCIDChoices, 0 )
        self._choiceCID.SetSelection( 0 )
        bSizer61.Add( self._choiceCID, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer61.AddSpacer( ( 20, 0), 1, wx.EXPAND, 5 )
        
        self._checkboxPPS1 = wx.CheckBox( self, wx.ID_ANY, u"PPS1", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer61.Add( self._checkboxPPS1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"DSI", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText29.Wrap( -1 )
        bSizer61.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceDSIChoices = [ u"1", u"2", u"4", u"8" ]
        self._choiceDSI = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceDSIChoices, 0 )
        self._choiceDSI.SetSelection( 0 )
        bSizer61.Add( self._choiceDSI, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"DRI", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText30.Wrap( -1 )
        bSizer61.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceDRIChoices = [ u"1", u"2", u"4", u"8" ]
        self._choiceDRI = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceDRIChoices, 0 )
        self._choiceDRI.SetSelection( 0 )
        bSizer61.Add( self._choiceDRI, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer60.Add( bSizer61, 1, wx.EXPAND, 5 )
        
        bSizer62 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextCommandName = wx.StaticText( self, wx.ID_ANY, u"PPS", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextCommandName.Wrap( -1 )
        bSizer62.Add( self._statictextCommandName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlCommandValue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer62.Add( self._textctrlCommandValue, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer60.Add( bSizer62, 1, wx.EXPAND, 5 )
        
        bSizer63 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer63.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self._buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonOK.SetDefault() 
        bSizer63.Add( self._buttonOK, 0, wx.ALL, 5 )
        
        self._buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer63.Add( self._buttonCancel, 0, wx.ALL, 5 )
        
        
        bSizer63.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer60.Add( bSizer63, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer60 )
        self.Layout()
        bSizer60.Fit( self )
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self._choiceCID.Bind( wx.EVT_CHOICE, self._choiceCIDOnChoice )
        self._checkboxPPS1.Bind( wx.EVT_CHECKBOX, self._checkboxPPS1OnCheckBox )
        self._choiceDSI.Bind( wx.EVT_CHOICE, self._choiceDSIOnChoice )
        self._choiceDRI.Bind( wx.EVT_CHOICE, self._choiceDRIOnChoice )
        self._textctrlCommandValue.Bind( wx.EVT_TEXT, self._textctrlCommandValueOnText )
        self._buttonOK.Bind( wx.EVT_BUTTON, self._buttonOKOnButtonClick )
        self._buttonCancel.Bind( wx.EVT_BUTTON, self._buttonCancelOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _choiceCIDOnChoice( self, event ):
        event.Skip()
    
    def _checkboxPPS1OnCheckBox( self, event ):
        event.Skip()
    
    def _choiceDSIOnChoice( self, event ):
        event.Skip()
    
    def _choiceDRIOnChoice( self, event ):
        event.Skip()
    
    def _textctrlCommandValueOnText( self, event ):
        event.Skip()
    
    def _buttonOKOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonCancelOnButtonClick( self, event ):
        event.Skip()
    

