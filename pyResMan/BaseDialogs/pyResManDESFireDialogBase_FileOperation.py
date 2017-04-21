# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class DESFireDialogBase_FileOperation
###########################################################################

class DESFireDialogBase_FileOperation ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"DESFire File Operation", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer193 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer194 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextFileNo = wx.StaticText( self, wx.ID_ANY, u"File No", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ALIGN_CENTRE )
        self._statictextFileNo.Wrap( -1 )
        self._statictextFileNo.SetMinSize( wx.Size( 45,-1 ) )
        self._statictextFileNo.SetMaxSize( wx.Size( 45,-1 ) )
        
        bSizer194.Add( self._statictextFileNo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlFileNo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlFileNo.SetMaxLength( 2 ) 
        self._textctrlFileNo.Enable( False )
        
        bSizer194.Add( self._textctrlFileNo, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer193.Add( bSizer194, 1, wx.EXPAND, 5 )
        
        bSizer195 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextOffset = wx.StaticText( self, wx.ID_ANY, u"Offset", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ALIGN_CENTRE )
        self._statictextOffset.Wrap( -1 )
        self._statictextOffset.SetMinSize( wx.Size( 45,-1 ) )
        self._statictextOffset.SetMaxSize( wx.Size( 45,-1 ) )
        
        bSizer195.Add( self._statictextOffset, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlOffset = wx.TextCtrl( self, wx.ID_ANY, u"000000", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlOffset.SetMaxLength( 6 ) 
        bSizer195.Add( self._textctrlOffset, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer193.Add( bSizer195, 1, wx.EXPAND, 5 )
        
        bSizer196 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextLength = wx.StaticText( self, wx.ID_ANY, u"Length", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ALIGN_CENTRE )
        self._statictextLength.Wrap( -1 )
        self._statictextLength.SetMinSize( wx.Size( 45,-1 ) )
        self._statictextLength.SetMaxSize( wx.Size( 45,-1 ) )
        
        bSizer196.Add( self._statictextLength, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlLength = wx.TextCtrl( self, wx.ID_ANY, u"000000", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlLength.SetMaxLength( 6 ) 
        bSizer196.Add( self._textctrlLength, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer193.Add( bSizer196, 1, wx.EXPAND, 5 )
        
        bSizer197 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextData = wx.StaticText( self, wx.ID_ANY, u"DATA", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ALIGN_CENTRE )
        self._statictextData.Wrap( -1 )
        self._statictextData.SetMinSize( wx.Size( 45,-1 ) )
        self._statictextData.SetMaxSize( wx.Size( 45,-1 ) )
        
        bSizer197.Add( self._statictextData, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlData = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlData.SetMaxLength( 222 ) 
        bSizer197.Add( self._textctrlData, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer193.Add( bSizer197, 1, wx.EXPAND, 5 )
        
        bSizer199 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextValue = wx.StaticText( self, wx.ID_ANY, u"Value", wx.DefaultPosition, wx.Size( 45,-1 ), wx.ALIGN_CENTRE )
        self._statictextValue.Wrap( -1 )
        self._statictextValue.SetMinSize( wx.Size( 45,-1 ) )
        self._statictextValue.SetMaxSize( wx.Size( 45,-1 ) )
        
        bSizer199.Add( self._statictextValue, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlValue = wx.TextCtrl( self, wx.ID_ANY, u"00000000", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlValue.SetMaxLength( 8 ) 
        bSizer199.Add( self._textctrlValue, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer193.Add( bSizer199, 1, wx.EXPAND, 5 )
        
        bSizer198 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer198.Add( self._buttonOK, 0, wx.ALL, 5 )
        
        self._buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer198.Add( self._buttonCancel, 0, wx.ALL, 5 )
        
        
        bSizer193.Add( bSizer198, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer193 )
        self.Layout()
        bSizer193.Fit( self )
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self._buttonOK.Bind( wx.EVT_BUTTON, self._buttonOKOnButtonClick )
        self._buttonCancel.Bind( wx.EVT_BUTTON, self._buttonCancelOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _buttonOKOnButtonClick( self, event ):
        event.Skip()
    
    def _buttonCancelOnButtonClick( self, event ):
        event.Skip()
    

