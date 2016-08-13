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
## Class CommandDialogBase_SBlock
###########################################################################

class CommandDialogBase_SBlock ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"S-BLOCK", pos = wx.DefaultPosition, size = wx.Size( 534,240 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer45 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer90 = wx.BoxSizer( wx.VERTICAL )
        
        _boxsizerSBlockData = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText61.Wrap( -1 )
        _boxsizerSBlockData.Add( self.m_staticText61, 0, wx.ALL, 5 )
        
        _choiceTypeChoices = [ u"DESELECT", u"WTX" ]
        self._choiceType = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceTypeChoices, 0 )
        self._choiceType.SetSelection( 1 )
        _boxsizerSBlockData.Add( self._choiceType, 0, wx.ALL, 5 )
        
        
        bSizer90.Add( _boxsizerSBlockData, 1, wx.EXPAND, 5 )
        
        bSizer92 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._checkboxCIDFollowing = wx.CheckBox( self, wx.ID_ANY, u"CID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._checkboxCIDFollowing.SetValue(True) 
        bSizer92.Add( self._checkboxCIDFollowing, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceCIDChoices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15" ]
        self._choiceCID = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceCIDChoices, 0 )
        self._choiceCID.SetSelection( 0 )
        bSizer92.Add( self._choiceCID, 0, wx.ALL, 5 )
        
        
        bSizer90.Add( bSizer92, 1, wx.EXPAND, 5 )
        
        bSizer971 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText621 = wx.StaticText( self, wx.ID_ANY, u"INF", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText621.Wrap( -1 )
        bSizer971.Add( self.m_staticText621, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText631 = wx.StaticText( self, wx.ID_ANY, u"Power level", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText631.Wrap( -1 )
        bSizer971.Add( self.m_staticText631, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choicePowerLevelChoices = [ u"0", u"1", u"2", u"3" ]
        self._choicePowerLevel = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choicePowerLevelChoices, 0 )
        self._choicePowerLevel.SetSelection( 0 )
        bSizer971.Add( self._choicePowerLevel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText64 = wx.StaticText( self, wx.ID_ANY, u"WTXM", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText64.Wrap( -1 )
        bSizer971.Add( self.m_staticText64, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlWTXM = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlWTXM.SetMaxLength( 2 ) 
        bSizer971.Add( self._textctrlWTXM, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer90.Add( bSizer971, 1, wx.EXPAND, 5 )
        
        bSizer98 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText63 = wx.StaticText( self, wx.ID_ANY, u"EDC", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText63.Wrap( -1 )
        bSizer98.Add( self.m_staticText63, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlEDC = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlEDC.SetMaxLength( 4 ) 
        bSizer98.Add( self._textctrlEDC, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer90.Add( bSizer98, 1, wx.EXPAND, 5 )
        
        
        bSizer45.Add( bSizer90, 0, wx.EXPAND, 5 )
        
        
        bSizer45.AddSpacer( ( 0, 10), 1, wx.EXPAND, 5 )
        
        bSizer46 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextCommandName = wx.StaticText( self, wx.ID_ANY, u"Command Name", wx.DefaultPosition, wx.DefaultSize, 0 )
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
        self._choiceType.Bind( wx.EVT_CHOICE, self._choiceTypeOnChoice )
        self._checkboxCIDFollowing.Bind( wx.EVT_CHECKBOX, self._checkboxCIDFollowingOnCheckBox )
        self._choiceCID.Bind( wx.EVT_CHOICE, self._choiceCIDOnChoice )
        self._choicePowerLevel.Bind( wx.EVT_CHOICE, self._choicePowerLevelOnChoice )
        self._textctrlWTXM.Bind( wx.EVT_TEXT, self._textctrlWTXMOnText )
        self._textctrlEDC.Bind( wx.EVT_TEXT, self._textctrlEDCOnText )
        self._textctrlCommandValue.Bind( wx.EVT_TEXT, self._textctrlCommandValueOnText )
        self._buttonOK.Bind( wx.EVT_BUTTON, self._buttonOKOnButtonClick )
        self._buttonCancel.Bind( wx.EVT_BUTTON, self._buttonCancelOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _choiceTypeOnChoice( self, event ):
        event.Skip()
    
    def _checkboxCIDFollowingOnCheckBox( self, event ):
        event.Skip()
    
    def _choiceCIDOnChoice( self, event ):
        event.Skip()
    
    def _choicePowerLevelOnChoice( self, event ):
        event.Skip()
    
    def _textctrlWTXMOnText( self, event ):
        event.Skip()
    
    def _textctrlEDCOnText( self, event ):
        event.Skip()
    
    def _textctrlCommandValueOnText( self, event ):
        event.Skip()
    
    def _buttonOKOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonCancelOnButtonClick( self, event ):
        event.Skip()
    

