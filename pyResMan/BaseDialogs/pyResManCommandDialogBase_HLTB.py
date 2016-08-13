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
## Class CommandDialogBase_HLTB
###########################################################################

class CommandDialogBase_HLTB ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"HLTB", pos = wx.DefaultPosition, size = wx.Size( 425,184 ), style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer45 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer104 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText66 = wx.StaticText( self, wx.ID_ANY, u"Command Header", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText66.Wrap( -1 )
        bSizer104.Add( self.m_staticText66, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlCommandHeader = wx.TextCtrl( self, wx.ID_ANY, u"50", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
        self._textctrlCommandHeader.SetMaxLength( 2 ) 
        bSizer104.Add( self._textctrlCommandHeader, 0, wx.ALL, 5 )
        
        
        bSizer45.Add( bSizer104, 0, wx.EXPAND, 5 )
        
        bSizer105 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText67 = wx.StaticText( self, wx.ID_ANY, u"Identifier", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText67.Wrap( -1 )
        bSizer105.Add( self.m_staticText67, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.textctrlIdentifier = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.textctrlIdentifier.SetMaxLength( 8 ) 
        bSizer105.Add( self.textctrlIdentifier, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer45.Add( bSizer105, 0, wx.EXPAND, 5 )
        
        bSizer46 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextCommandName = wx.StaticText( self, wx.ID_ANY, u"Command Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextCommandName.Wrap( -1 )
        bSizer46.Add( self._statictextCommandName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlCommandValue = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlCommandValue.SetMaxLength( 10 ) 
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
        self.textctrlIdentifier.Bind( wx.EVT_TEXT, self.textctrlIdentifierOnText )
        self._textctrlCommandValue.Bind( wx.EVT_TEXT, self._textctrlCommandValueOnText )
        self._buttonOK.Bind( wx.EVT_BUTTON, self._buttonOKOnButtonClick )
        self._buttonCancel.Bind( wx.EVT_BUTTON, self._buttonCancelOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _textctrlCommandHeaderOnText( self, event ):
        event.Skip()
    
    def textctrlIdentifierOnText( self, event ):
        event.Skip()
    
    def _textctrlCommandValueOnText( self, event ):
        event.Skip()
    
    def _buttonOKOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonCancelOnButtonClick( self, event ):
        event.Skip()
    

