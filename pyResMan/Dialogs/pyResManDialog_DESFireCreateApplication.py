# -*- coding: utf-8 -*-

'''
Modified on 2017-03-28

@author: javacardos@gmail.com
@organization: https://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from pyResMan.BaseDialogs.pyResManDESFireDialogBase_CreateApplication import DESFireDialogBase_CreateApplication
from pyResMan.Util import IDOK, IDCANCEL
from pyResMan.Util import HexValidator
from wx._gdi_ import Colour_Red

###########################################################################
## Class DESFireDialog_CreateApplication
###########################################################################


class DESFireDialog_CreateApplication ( DESFireDialogBase_CreateApplication ):
    
    def __init__( self, parent ):
        DESFireDialogBase_CreateApplication.__init__ ( self, parent )
        
        self._textctrlAID.SetValidator(HexValidator())
        self._textctrlKeySettings.SetValidator(HexValidator())
        self._textctrlNumOfKeys.SetValidator(HexValidator())
    
    def _buttonOKOnButtonClick(self, event):
        if len(self._textctrlAID.GetValue()) != 6:
            self._textctrlAID.SetForegroundColour('#FF0000')
            return
        if len(self._textctrlKeySettings.GetValue()) != 2:
            self._textctrlKeySettings.SetForegroundColour('#FF0000')
            return
        if len(self._textctrlNumOfKeys.GetValue()) != 2:
            self._textctrlNumOfKeys.SetForegroundColour('#FF0000')
            return
        self.EndModal(IDOK)
    
    def _buttonCancelOnButtonClick(self, event):
        self.EndModal(IDCANCEL)
    
    def getAID(self):
        return int(self._textctrlAID.GetValue(), 0x10)
    
    def getKeySett(self):
        return int(self._textctrlKeySettings.GetValue(), 0x10)
    
    def getNumOfKeys(self):
        return int(self._textctrlNumOfKeys.GetValue(), 0x10)
    
    def _textctrlAIDOnText(self, event):
        self._textctrlAID.SetForegroundColour('#000000')
    
    def _textctrlKeySettingsOnText(self, event):
        self._textctrlKeySettings.SetForegroundColour('#000000')
    
    def _textctrlNumOfKeysOnText(self, event):
        self._textctrlNumOfKeys.SetForegroundColour('#000000')
    