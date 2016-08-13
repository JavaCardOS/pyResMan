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
## Class CommandDialogBase_IBlock
###########################################################################

class CommandDialogBase_IBlock ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"I-BLOCK", pos = wx.DefaultPosition, size = wx.Size( 534,303 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer45 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer90 = wx.BoxSizer( wx.VERTICAL )
        
        _boxsizerIBlockData = wx.BoxSizer( wx.HORIZONTAL )
        
        self._checkboxChaining = wx.CheckBox( self, wx.ID_ANY, u"Chaining", wx.DefaultPosition, wx.DefaultSize, 0 )
        _boxsizerIBlockData.Add( self._checkboxChaining, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer90.Add( _boxsizerIBlockData, 1, wx.EXPAND, 5 )
        
        bSizer92 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._checkboxCIDFollowing = wx.CheckBox( self, wx.ID_ANY, u"CID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._checkboxCIDFollowing.SetValue(True) 
        bSizer92.Add( self._checkboxCIDFollowing, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceCIDChoices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14", u"15" ]
        self._choiceCID = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceCIDChoices, 0 )
        self._choiceCID.SetSelection( 0 )
        bSizer92.Add( self._choiceCID, 0, wx.ALL, 5 )
        
        
        bSizer90.Add( bSizer92, 1, wx.EXPAND, 5 )
        
        bSizer93 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._checkboxNADFollowing = wx.CheckBox( self, wx.ID_ANY, u"NAD", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._checkboxNADFollowing.SetValue(True) 
        bSizer93.Add( self._checkboxNADFollowing, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlNAD = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlNAD.SetMaxLength( 2 ) 
        bSizer93.Add( self._textctrlNAD, 0, wx.ALL, 5 )
        
        
        bSizer90.Add( bSizer93, 1, wx.EXPAND, 5 )
        
        bSizer96 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._checkboxBlockNumber = wx.CheckBox( self, wx.ID_ANY, u"Block Number", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._checkboxBlockNumber.SetValue(True) 
        bSizer96.Add( self._checkboxBlockNumber, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer90.Add( bSizer96, 1, wx.EXPAND, 5 )
        
        bSizer97 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText62 = wx.StaticText( self, wx.ID_ANY, u"INF", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText62.Wrap( -1 )
        bSizer97.Add( self.m_staticText62, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlINF = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer97.Add( self._textctrlINF, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer90.Add( bSizer97, 1, wx.EXPAND, 5 )
        
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
        self._checkboxChaining.Bind( wx.EVT_CHECKBOX, self._checkboxChainingOnCheckBox )
        self._checkboxCIDFollowing.Bind( wx.EVT_CHECKBOX, self._checkboxCIDFollowingOnCheckBox )
        self._choiceCID.Bind( wx.EVT_CHOICE, self._choiceCIDOnChoice )
        self._checkboxNADFollowing.Bind( wx.EVT_CHECKBOX, self._checkboxNADFollowingOnCheckBox )
        self._textctrlNAD.Bind( wx.EVT_TEXT, self._textctrlNADOnText )
        self._checkboxBlockNumber.Bind( wx.EVT_CHECKBOX, self._checkboxBlockNumberOnCheckBox )
        self._textctrlINF.Bind( wx.EVT_TEXT, self._textctrlINFOnText )
        self._textctrlEDC.Bind( wx.EVT_TEXT, self._textctrlEDCOnText )
        self._textctrlCommandValue.Bind( wx.EVT_TEXT, self._textctrlCommandValueOnText )
        self._buttonOK.Bind( wx.EVT_BUTTON, self._buttonOKOnButtonClick )
        self._buttonCancel.Bind( wx.EVT_BUTTON, self._buttonCancelOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _checkboxChainingOnCheckBox( self, event ):
        event.Skip()
    
    def _checkboxCIDFollowingOnCheckBox( self, event ):
        event.Skip()
    
    def _choiceCIDOnChoice( self, event ):
        event.Skip()
    
    def _checkboxNADFollowingOnCheckBox( self, event ):
        event.Skip()
    
    def _textctrlNADOnText( self, event ):
        event.Skip()
    
    def _checkboxBlockNumberOnCheckBox( self, event ):
        event.Skip()
    
    def _textctrlINFOnText( self, event ):
        event.Skip()
    
    def _textctrlEDCOnText( self, event ):
        event.Skip()
    
    def _textctrlCommandValueOnText( self, event ):
        event.Skip()
    
    def _buttonOKOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonCancelOnButtonClick( self, event ):
        event.Skip()
    

