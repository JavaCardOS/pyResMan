# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Util import Util
from wx import CHK_UNCHECKED, CHK_CHECKED

###########################################################################
## Class MyDialog1
###########################################################################

class BaseInstallDialog ( wx.Dialog ):
    
    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer30 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Package AID", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer31.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self._packageAIDTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        self._packageAIDTextCtrl.SetMinSize( wx.Size( 275,-1 ) )
        
        bSizer31.Add( self._packageAIDTextCtrl, 0, wx.ALL, 5 )
        
        
        bSizer30.Add( bSizer31, 1, wx.EXPAND, 5 )
        
        bSizer32 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Applet AID", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
        self.m_staticText8.Wrap( -1 )
        bSizer32.Add( self.m_staticText8, 0, wx.ALL, 5 )
        
        self._appletAIDTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        self._appletAIDTextCtrl.SetMinSize( wx.Size( 275,-1 ) )
        
        bSizer32.Add( self._appletAIDTextCtrl, 0, wx.ALL, 5 )
        
        
        bSizer30.Add( bSizer32, 1, wx.EXPAND, 5 )
        
        bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Instance AID", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer33.Add( self.m_staticText9, 0, wx.ALL, 5 )
        
        self._instanceAIDTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self._instanceAIDTextCtrl.SetMinSize( wx.Size( 275,-1 ) )
        
        bSizer33.Add( self._instanceAIDTextCtrl, 0, wx.ALL, 5 )
        
        
        bSizer30.Add( bSizer33, 1, wx.EXPAND, 5 )
        
        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer30.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
        
        bSizer39 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Parameters", wx.DefaultPosition, wx.Size( 75,-1 ), 0 )
        self.m_staticText10.Wrap( -1 )
        bSizer39.Add( self.m_staticText10, 0, wx.ALL, 5 )
        
        self._parametersTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 235,-1 ), 0 )
        self._parametersTextCtrl.SetMinSize( wx.Size( 275,-1 ) )
        
        bSizer39.Add( self._parametersTextCtrl, 0, wx.ALL, 5 )
        
        
        bSizer30.Add( bSizer39, 1, wx.EXPAND, 5 )
        
        bSizer34 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._privSecurityDomainCheckBox = wx.CheckBox( self, wx.ID_ANY, u"Security Domain", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer34.Add( self._privSecurityDomainCheckBox, 1, wx.ALL|wx.EXPAND, 5 )
        
        self._privDAPVerificationCheckBox = wx.CheckBox( self, wx.ID_ANY, u"DAP Verification", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer34.Add( self._privDAPVerificationCheckBox, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer30.Add( bSizer34, 1, wx.EXPAND, 5 )
        
        bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._privDelegatedManagementCheckBox = wx.CheckBox( self, wx.ID_ANY, u"Delegated Management", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer35.Add( self._privDelegatedManagementCheckBox, 1, wx.ALL|wx.EXPAND, 5 )
        
        self._privCardLockCheckBox = wx.CheckBox( self, wx.ID_ANY, u"Card Lock", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer35.Add( self._privCardLockCheckBox, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer30.Add( bSizer35, 1, wx.EXPAND, 5 )
        
        bSizer36 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._privCardTerminateCheckBox = wx.CheckBox( self, wx.ID_ANY, u"Card Terminate", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer36.Add( self._privCardTerminateCheckBox, 1, wx.ALL|wx.EXPAND, 5 )
        
        self._privCardResetCheckBox = wx.CheckBox( self, wx.ID_ANY, u"Card Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer36.Add( self._privCardResetCheckBox, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer30.Add( bSizer36, 1, wx.EXPAND, 5 )
        
        bSizer37 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._privCVMManagementCheckBox = wx.CheckBox( self, wx.ID_ANY, u"CVM Management", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer37.Add( self._privCVMManagementCheckBox, 1, wx.ALL|wx.EXPAND, 5 )
        
        self._privMandatedDAPVerificationCheckBox = wx.CheckBox( self, wx.ID_ANY, u"Mandated DAP Verification", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer37.Add( self._privMandatedDAPVerificationCheckBox, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer30.Add( bSizer37, 1, wx.EXPAND, 5 )
        
        self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer30.Add( self.m_staticline11, 0, wx.EXPAND |wx.ALL, 5 )
        
        bSizer38 = wx.BoxSizer( wx.HORIZONTAL )
        
        self._OKButton = wx.Button( self, wx.ID_OK, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer38.Add( self._OKButton, 1, wx.ALL|wx.EXPAND, 5 )
        
        self._cancelButton = wx.Button( self, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer38.Add( self._cancelButton, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer30.Add( bSizer38, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer30 )
        self.Layout()
        bSizer30.Fit( self )
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self._packageAIDTextCtrl.Bind( wx.EVT_CHAR, self._packageAIDTextCtrlOnChar )
        self._appletAIDTextCtrl.Bind( wx.EVT_CHAR, self._appletAIDTextCtrlOnChar )
        self._instanceAIDTextCtrl.Bind( wx.EVT_CHAR, self._instanceAIDTextCtrlOnChar )
        self._instanceAIDTextCtrl.Bind( wx.EVT_TEXT, self._instanceAIDTextCtrlOnText )
        self._parametersTextCtrl.Bind( wx.EVT_CHAR, self._parametersTextCtrlOnChar )
        self._parametersTextCtrl.Bind( wx.EVT_TEXT, self._parametersTextCtrlOnText )
        self._privSecurityDomainCheckBox.Bind( wx.EVT_CHECKBOX, self._privSecurityDomainCheckBoxOnCheckBox )
        self._privDAPVerificationCheckBox.Bind( wx.EVT_CHECKBOX, self._privDAPVerificationCheckBoxOnCheckBox )
        self._privDelegatedManagementCheckBox.Bind( wx.EVT_CHECKBOX, self._privDelegatedManagementCheckBoxOnCheckBox )
        self._privCardLockCheckBox.Bind( wx.EVT_CHECKBOX, self._privCardLockCheckBoxOnCheckBox )
        self._privCardTerminateCheckBox.Bind( wx.EVT_CHECKBOX, self._privCardTerminateCheckBoxOnCheckBox )
        self._privCardResetCheckBox.Bind( wx.EVT_CHECKBOX, self._privCardResetCheckBoxOnCheckBox )
        self._privCVMManagementCheckBox.Bind( wx.EVT_CHECKBOX, self._privCVMManagementCheckBoxOnCheckBox )
        self._privMandatedDAPVerificationCheckBox.Bind( wx.EVT_CHECKBOX, self._privMandatedDAPVerificationCheckBoxOnCheckBox )
        self._OKButton.Bind( wx.EVT_BUTTON, self._OKButtonOnButtonClick )
        self._cancelButton.Bind( wx.EVT_BUTTON, self._cancelButtonOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def _packageAIDTextCtrlOnChar( self, event ):
        event.Skip()
    
    def _appletAIDTextCtrlOnChar( self, event ):
        event.Skip()
    
    def _instanceAIDTextCtrlOnChar( self, event ):
        event.Skip()
    
    def _instanceAIDTextCtrlOnText( self, event ):
        event.Skip()
    
    def _parametersTextCtrlOnChar( self, event ):
        event.Skip()
    
    def _parametersTextCtrlOnText( self, event ):
        event.Skip()
    
    def _privSecurityDomainCheckBoxOnCheckBox( self, event ):
        event.Skip()
    
    def _privDAPVerificationCheckBoxOnCheckBox( self, event ):
        event.Skip()
    
    def _privDelegatedManagementCheckBoxOnCheckBox( self, event ):
        event.Skip()
    
    def _privCardLockCheckBoxOnCheckBox( self, event ):
        event.Skip()
    
    def _privCardTerminateCheckBoxOnCheckBox( self, event ):
        event.Skip()
    
    def _privCardResetCheckBoxOnCheckBox( self, event ):
        event.Skip()
    
    def _privCVMManagementCheckBoxOnCheckBox( self, event ):
        event.Skip()
    
    def _privMandatedDAPVerificationCheckBoxOnCheckBox( self, event ):
        event.Skip()
    
    def _OKButtonOnButtonClick( self, event ):
        event.Skip()
    
    def _cancelButtonOnButtonClick( self, event ):
        event.Skip()
    
    

class pyResMan_InstallDialog(BaseInstallDialog):
    def __init__(self, parent):
        BaseInstallDialog.__init__(self, parent)
        self.__packageAID = ''
        self.__appletAID = ''
    
    def setPackageAID(self, packageAID):
        self.__packageAID = packageAID
        self._packageAIDTextCtrl.SetValue("".join("%02X" %(ord(c)) for c in packageAID))
        
    def setAppletAID(self, appletAID):
        self.__appletAID = appletAID
        self._appletAIDTextCtrl.SetValue("".join("%02X" %(ord(c)) for c in appletAID))
    
    def setInstanceAID(self, instanceAID):
        self._instanceAIDTextCtrl.SetValue("".join("%02X" %(ord(c)) for c in instanceAID))

    def getPackageAID(self):
        return self.__packageAID
    
    def getAppletAID(self):
        return self.__appletAID
    
    def getInstanceAID(self):
        instanceAIDString = self._instanceAIDTextCtrl.GetValue()
        return Util.s2vs(instanceAIDString)

    def getPrivileges(self):
        pv = 0
        if self._privSecurityDomainCheckBox.IsChecked():
            pv |= 0x80
        if self._privDAPVerificationCheckBox.IsChecked():
            pv |= 0xC0
            pv &= ~(0x01)
        if self._privDelegatedManagementCheckBox.IsChecked():
            pv |= 0xA0
        if self._privCardLockCheckBox.IsChecked():
            pv |= 0x10
        if self._privCardTerminateCheckBox.IsChecked():
            pv |= 0x08
        if self._privCardResetCheckBox.IsChecked():
            pv |= 0x04
        if self._privCVMManagementCheckBox.IsChecked():
            pv |= 0x02
        if self._privMandatedDAPVerificationCheckBox.IsChecked():
            pv |= 0xC1
        return pv
        
    def getInstallParameters(self):
        parametersString = self._parametersTextCtrl.GetValue()
        return Util.s2vs(parametersString)

    def _packageAIDTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _moduleAIDTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()
    
    def _instanceAIDTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()

    def _instanceAIDTextCtrlOnText( self, event ):
        event.Skip()
        v = self._instanceAIDTextCtrl.GetValue()
        if len(v) & 0x01 != 0:
            self._instanceAIDTextCtrl.SetBackgroundColour('#FF6347')
        else:
            self._instanceAIDTextCtrl.SetBackgroundColour('WHITE')
        self._instanceAIDTextCtrl.Refresh()
    
    def _parametersTextCtrlOnChar( self, event ):
        keyCode = event.KeyCode
        if Util.ishexchar_kc(keyCode):
            event.Skip()

    def _parametersTextCtrlOnText( self, event ):
        event.Skip()
        v = self._parametersTextCtrl.GetValue()
        if len(v) & 0x01 != 0:
            self._parametersTextCtrl.SetBackgroundColour('#FF6347')
        else:
            self._parametersTextCtrl.SetBackgroundColour('WHITE')
        self._parametersTextCtrl.Refresh()
    
    def _privSecurityDomainCheckBoxOnCheckBox( self, event ):
        event.Skip()
        if not self._privSecurityDomainCheckBox.IsChecked():
            self._privDAPVerificationCheckBox.SetValue(CHK_UNCHECKED)
            self._privDelegatedManagementCheckBox.SetValue(CHK_UNCHECKED)
            self._privMandatedDAPVerificationCheckBox.SetValue(CHK_UNCHECKED)
        
    def _privDAPVerificationCheckBoxOnCheckBox( self, event ):
        event.Skip()
        if self._privDAPVerificationCheckBox.IsChecked():
            self._privSecurityDomainCheckBox.SetValue(CHK_CHECKED)
            self._privMandatedDAPVerificationCheckBox.SetValue(CHK_UNCHECKED)
    
    def _privDelegatedManagementCheckBoxOnCheckBox( self, event ):
        event.Skip()
        if self._privDelegatedManagementCheckBox.IsChecked():
            self._privSecurityDomainCheckBox.SetValue(CHK_CHECKED)
    
    def _privCardLockCheckBoxOnCheckBox( self, event ):
        event.Skip()
    
    def _privCardTerminateCheckBoxOnCheckBox( self, event ):
        event.Skip()
    
    def _privCardResetCheckBoxOnCheckBox( self, event ):
        event.Skip()
    
    def _privCVMManagementCheckBoxOnCheckBox( self, event ):
        event.Skip()
    
    def _privMandatedDAPVerificationCheckBoxOnCheckBox( self, event ):
        event.Skip()
        if self._privMandatedDAPVerificationCheckBox.IsChecked():
            self._privSecurityDomainCheckBox.SetValue(CHK_CHECKED)
            self._privDAPVerificationCheckBox.SetValue(CHK_UNCHECKED)
    
    def _OKButtonOnButtonClick( self, event ):
#         if len(self._packageAIDTextCtrl.GetValue()) % 2 != 0:
#             self._packageAIDTextCtrl.SetFocus()
#             pass
#         if len(self._appletAIDTextCtrl.GetValue()) % 2 != 0:
#             self._appletAIDTextCtrl.SetFocus()
#             pass
        if len(self._instanceAIDTextCtrl.GetValue()) % 2 != 0:
            self._instanceAIDTextCtrl.SetFocus()
            return
        if len(self._parametersTextCtrl.GetValue()) % 2 != 0:
            self._parametersAIDTextCtrl.SetFocus()
            return
        event.Skip()
    
    def _cancelButtonOnButtonClick( self, event ):
        event.Skip()
