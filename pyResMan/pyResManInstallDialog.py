# -*- coding: utf-8 -*- 


'''
Created on 2015-12-01

@author: javacardos@gmail.com
@organization: http://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from Util import Util
from wx import CHK_UNCHECKED, CHK_CHECKED
from pyResManInstallDialogBase import pyResManInstallDialogBase


class pyResManInstallDialog(pyResManInstallDialogBase):
    def __init__(self, parent):
        pyResManInstallDialogBase.__init__(self, parent)
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
