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
## Class DESFireDialogBase_CreateFile
###########################################################################

class DESFireDialogBase_CreateFile ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"DESFire Create File", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer182 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer183 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextFileNo = wx.StaticText( self, wx.ID_ANY, u"File No.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextFileNo.Wrap( -1 )
        bSizer183.Add( self._statictextFileNo, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlFileNo = wx.TextCtrl( self, wx.ID_ANY, u"00", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlFileNo.SetMaxLength( 2 ) 
        bSizer183.Add( self._textctrlFileNo, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer182.Add( bSizer183, 1, wx.EXPAND, 5 )
        
        bSizer185 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextComSet = wx.StaticText( self, wx.ID_ANY, u"Com. Set.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextComSet.Wrap( -1 )
        bSizer185.Add( self._statictextComSet, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlComSet = wx.TextCtrl( self, wx.ID_ANY, u"00", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlComSet.SetMaxLength( 2 ) 
        bSizer185.Add( self._textctrlComSet, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer182.Add( bSizer185, 1, wx.EXPAND, 5 )
        
        bSizer186 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextAccessRights = wx.StaticText( self, wx.ID_ANY, u"Access Rights", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextAccessRights.Wrap( -1 )
        bSizer186.Add( self._statictextAccessRights, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlAccessRights = wx.TextCtrl( self, wx.ID_ANY, u"EEEE", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlAccessRights.SetMaxLength( 4 ) 
        bSizer186.Add( self._textctrlAccessRights, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer182.Add( bSizer186, 1, wx.EXPAND, 5 )
        
        bSizer187 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextFileSize = wx.StaticText( self, wx.ID_ANY, u"File Size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextFileSize.Wrap( -1 )
        bSizer187.Add( self._statictextFileSize, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlFileSize = wx.TextCtrl( self, wx.ID_ANY, u"000001", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlFileSize.SetMaxLength( 6 ) 
        bSizer187.Add( self._textctrlFileSize, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer182.Add( bSizer187, 1, wx.EXPAND, 5 )
        
        bSizer188 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextLowerLimit = wx.StaticText( self, wx.ID_ANY, u"Lower Limit", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextLowerLimit.Wrap( -1 )
        bSizer188.Add( self._statictextLowerLimit, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlLowerLimit = wx.TextCtrl( self, wx.ID_ANY, u"00000000", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlLowerLimit.SetMaxLength( 8 ) 
        bSizer188.Add( self._textctrlLowerLimit, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer182.Add( bSizer188, 1, wx.EXPAND, 5 )
        
        bSizer189 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextUpperLimit = wx.StaticText( self, wx.ID_ANY, u"Upper Limit", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextUpperLimit.Wrap( -1 )
        bSizer189.Add( self._statictextUpperLimit, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlUpperLimit = wx.TextCtrl( self, wx.ID_ANY, u"FFFFFFFF", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlUpperLimit.SetMaxLength( 8 ) 
        bSizer189.Add( self._textctrlUpperLimit, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer182.Add( bSizer189, 1, wx.EXPAND, 5 )
        
        bSizer190 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextValue = wx.StaticText( self, wx.ID_ANY, u"Value", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextValue.Wrap( -1 )
        bSizer190.Add( self._statictextValue, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlValue = wx.TextCtrl( self, wx.ID_ANY, u"11111111", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlValue.SetMaxLength( 8 ) 
        bSizer190.Add( self._textctrlValue, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer182.Add( bSizer190, 1, wx.EXPAND, 5 )
        
        bSizer193 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._checkboxLimitedCreditEnabled = wx.CheckBox( self, wx.ID_ANY, u"Limited Credit Enabled", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._checkboxLimitedCreditEnabled.SetValue(True) 
        bSizer193.Add( self._checkboxLimitedCreditEnabled, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer182.Add( bSizer193, 1, wx.EXPAND, 5 )
        
        bSizer191 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextRecordSize = wx.StaticText( self, wx.ID_ANY, u"Record Size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextRecordSize.Wrap( -1 )
        bSizer191.Add( self._statictextRecordSize, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlRecordSize = wx.TextCtrl( self, wx.ID_ANY, u"000010", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlRecordSize.SetMaxLength( 6 ) 
        bSizer191.Add( self._textctrlRecordSize, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer182.Add( bSizer191, 1, wx.EXPAND, 5 )
        
        bSizer192 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._statictextMaxNumOfRecords = wx.StaticText( self, wx.ID_ANY, u"Max Num. Of Records", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._statictextMaxNumOfRecords.Wrap( -1 )
        bSizer192.Add( self._statictextMaxNumOfRecords, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._textctrlMaxNumOfRecords = wx.TextCtrl( self, wx.ID_ANY, u"000020", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._textctrlMaxNumOfRecords.SetMaxLength( 6 ) 
        bSizer192.Add( self._textctrlMaxNumOfRecords, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer182.Add( bSizer192, 1, wx.EXPAND, 5 )
        
        bSizer194 = wx.BoxSizer( wx.HORIZONTAL )
        
        
        bSizer194.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        self._buttonOK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        self._buttonOK.SetDefault() 
        bSizer194.Add( self._buttonOK, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self._buttonCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer194.Add( self._buttonCancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer194.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
        
        
        bSizer182.Add( bSizer194, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        self.SetSizer( bSizer182 )
        self.Layout()
        bSizer182.Fit( self )
        
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
    

