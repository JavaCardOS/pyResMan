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
## Class CommandDialogBase_ATTRIB
###########################################################################

class CommandDialogBase_ATTRIB ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"ATTRIB", pos = wx.DefaultPosition, size = wx.Size( 513,331 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer45 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText54 = wx.StaticText( self, wx.ID_ANY, u"CommandHeader", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText54.Wrap( -1 )
        bSizer91.Add( self.m_staticText54, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlCommandHeader = wx.TextCtrl( self, wx.ID_ANY, u"1D", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
        self._textctrlCommandHeader.SetMaxLength( 2 ) 
        bSizer91.Add( self._textctrlCommandHeader, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer45.Add( bSizer91, 0, 0, 5 )
        
        bSizer92 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"Identifier", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText55.Wrap( -1 )
        bSizer92.Add( self.m_staticText55, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlIdentifier = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlIdentifier.SetMaxLength( 8 ) 
        bSizer92.Add( self._textctrlIdentifier, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer45.Add( bSizer92, 0, wx.EXPAND, 5 )
        
        bSizer93 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText56 = wx.StaticText( self, wx.ID_ANY, u"Minimum TR0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText56.Wrap( -1 )
        bSizer93.Add( self.m_staticText56, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceMinTR0Choices = [ u"default value", u"48/fs", u"16/fs", u"RFU" ]
        self._choiceMinTR0 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceMinTR0Choices, 0 )
        self._choiceMinTR0.SetSelection( 0 )
        bSizer93.Add( self._choiceMinTR0, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText57 = wx.StaticText( self, wx.ID_ANY, u"Minimum TR1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText57.Wrap( -1 )
        bSizer93.Add( self.m_staticText57, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceMinTR1Choices = [ u"default value", u"48/fs", u"16/fs", u"RFU" ]
        self._choiceMinTR1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceMinTR1Choices, 0 )
        self._choiceMinTR1.SetSelection( 0 )
        bSizer93.Add( self._choiceMinTR1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._checkboxEOF = wx.CheckBox( self, wx.ID_ANY, u"EOF", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer93.Add( self._checkboxEOF, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._checkboxSOF = wx.CheckBox( self, wx.ID_ANY, u"SOF", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer93.Add( self._checkboxSOF, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer45.Add( bSizer93, 0, wx.EXPAND, 5 )
        
        bSizer94 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText58 = wx.StaticText( self, wx.ID_ANY, u"Maximum Frame Size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText58.Wrap( -1 )
        bSizer94.Add( self.m_staticText58, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceMaxFrameSizeChoices = [ u"16", u"24", u"32", u"40", u"48", u"64", u"96", u"128", u"256" ]
        self._choiceMaxFrameSize = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceMaxFrameSizeChoices, 0 )
        self._choiceMaxFrameSize.SetSelection( 0 )
        bSizer94.Add( self._choiceMaxFrameSize, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText59 = wx.StaticText( self, wx.ID_ANY, u"Bit rate PCD->PICC", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText59.Wrap( -1 )
        bSizer94.Add( self.m_staticText59, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceBitRatePCD2PICCChoices = [ u"106", u"212", u"424", u"847" ]
        self._choiceBitRatePCD2PICC = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceBitRatePCD2PICCChoices, 0 )
        self._choiceBitRatePCD2PICC.SetSelection( 0 )
        bSizer94.Add( self._choiceBitRatePCD2PICC, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.m_staticText60 = wx.StaticText( self, wx.ID_ANY, u"PICC->PCD", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText60.Wrap( -1 )
        bSizer94.Add( self.m_staticText60, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceBitRatePICC2PCDChoices = [ u"106", u"212", u"424", u"847" ]
        self._choiceBitRatePICC2PCD = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceBitRatePICC2PCDChoices, 0 )
        self._choiceBitRatePICC2PCD.SetSelection( 0 )
        bSizer94.Add( self._choiceBitRatePICC2PCD, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer45.Add( bSizer94, 0, wx.EXPAND, 5 )
        
        bSizer95 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText61 = wx.StaticText( self, wx.ID_ANY, u"Protocol Type", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText61.Wrap( -1 )
        bSizer95.Add( self.m_staticText61, 0, wx.ALL, 5 )
        
        self._checkboxProtocolType = wx.CheckBox( self, wx.ID_ANY, u"PICC compliant with ISO/IEC 14443-4", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer95.Add( self._checkboxProtocolType, 0, wx.ALL, 5 )
        
        
        bSizer45.Add( bSizer95, 0, wx.EXPAND, 5 )
        
        bSizer96 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText62 = wx.StaticText( self, wx.ID_ANY, u"CID", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText62.Wrap( -1 )
        bSizer96.Add( self.m_staticText62, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        _choiceCIDChoices = [ u"0", u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8", u"9", u"10", u"11", u"12", u"13", u"14" ]
        self._choiceCID = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _choiceCIDChoices, 0 )
        self._choiceCID.SetSelection( 0 )
        bSizer96.Add( self._choiceCID, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer45.Add( bSizer96, 0, wx.EXPAND, 5 )
        
        bSizer97 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText63 = wx.StaticText( self, wx.ID_ANY, u"Higher layer INF", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText63.Wrap( -1 )
        bSizer97.Add( self.m_staticText63, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlHigherLayerINF = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer97.Add( self._textctrlHigherLayerINF, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer45.Add( bSizer97, 0, wx.EXPAND, 5 )
        
        bSizer46 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextCommandName = wx.StaticText( self, wx.ID_ANY, u"Command Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextCommandName.Wrap( -1 )
        bSizer46.Add( self._statictextCommandName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlCommandValue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
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
        self._textctrlCommandHeader.Bind( wx.EVT_TEXT, self._textctrlCommandHeaderOnText )
        self._textctrlIdentifier.Bind( wx.EVT_TEXT, self._textctrlIdentifierOnText )
        self._choiceMinTR0.Bind( wx.EVT_CHOICE, self._choiceMinTR0OnChoice )
        self._choiceMinTR1.Bind( wx.EVT_CHOICE, self._choiceMinTR1OnChoice )
        self._checkboxEOF.Bind( wx.EVT_CHECKBOX, self._checkboxEOFOnCheckBox )
        self._checkboxSOF.Bind( wx.EVT_CHECKBOX, self._checkboxSOFOnCheckBox )
        self._choiceMaxFrameSize.Bind( wx.EVT_CHOICE, self._choiceMaxFrameSizeOnChoice )
        self._choiceBitRatePCD2PICC.Bind( wx.EVT_CHOICE, self._choiceBitRatePCD2PICCOnChoice )
        self._choiceBitRatePICC2PCD.Bind( wx.EVT_CHOICE, self._choiceBitRatePICC2PCDOnChoice )
        self._checkboxProtocolType.Bind( wx.EVT_CHECKBOX, self._checkboxProtocolTypeOnCheckBox )
        self._choiceCID.Bind( wx.EVT_CHOICE, self._choiceCIDOnChoice )
        self._textctrlHigherLayerINF.Bind( wx.EVT_TEXT, self._textctrlHigherLayerINFOnText )
        self._textctrlCommandValue.Bind( wx.EVT_TEXT, self._textctrlCommandValueOnText )
        self._buttonOK.Bind( wx.EVT_BUTTON, self._buttonOKOnButtonClick )
        self._buttonCancel.Bind( wx.EVT_BUTTON, self._buttonCancelOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _textctrlCommandHeaderOnText( self, event ):
        event.Skip()
    
    def _textctrlIdentifierOnText( self, event ):
        event.Skip()
    
    def _choiceMinTR0OnChoice( self, event ):
        event.Skip()
    
    def _choiceMinTR1OnChoice( self, event ):
        event.Skip()
    
    def _checkboxEOFOnCheckBox( self, event ):
        event.Skip()
    
    def _checkboxSOFOnCheckBox( self, event ):
        event.Skip()
    
    def _choiceMaxFrameSizeOnChoice( self, event ):
        event.Skip()
    
    def _choiceBitRatePCD2PICCOnChoice( self, event ):
        event.Skip()
    
    def _choiceBitRatePICC2PCDOnChoice( self, event ):
        event.Skip()
    
    def _checkboxProtocolTypeOnCheckBox( self, event ):
        event.Skip()
    
    def _choiceCIDOnChoice( self, event ):
        event.Skip()
    
    def _textctrlHigherLayerINFOnText( self, event ):
        event.Skip()
    
    def _textctrlCommandValueOnText( self, event ):
        event.Skip()
    
    def _buttonOKOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonCancelOnButtonClick( self, event ):
        event.Skip()
    

