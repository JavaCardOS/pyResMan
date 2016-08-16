# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from pyResMan.Util import IDOK, IDCANCEL
from pyResMan.BaseDialogs.pyResManCommandDialogBase_ATTRIB import CommandDialogBase_ATTRIB
from pyResMan.Util import HexValidator

###########################################################################
## Class CommandDialog_Basic
###########################################################################

MODE_IDLE = 0
MODE_PARSING = 1
MODE_BUILDING = 2

class CommandDialog_ATTRIB ( CommandDialogBase_ATTRIB ):
    
    def __init__( self, parent ):
        CommandDialogBase_ATTRIB.__init__ ( self, parent )
        self.__mode = MODE_IDLE
        self._textctrlCommandHeader.SetMaxLength(1 * 2)
#         self._textctrlHigherLayerINF.SetMaxLength()
        self._textctrlIdentifier.SetMaxLength(4 * 2)
#         self._textctrlCommandValue.SetMaxLength()

        # Set validator;
        self._textctrlCommandHeader.SetValidator(HexValidator())
        self._textctrlHigherLayerINF.SetValidator(HexValidator())
        self._textctrlIdentifier.SetValidator(HexValidator())
        self._textctrlCommandValue.SetValidator(HexValidator())

    
    def _buttonOKOnButtonClick(self, event):
        self.EndModal(IDOK)
    
    def _buttonCancelOnButtonClick(self, event):
        self.EndModal(IDCANCEL)
    
    def getCommandName(self):
        return self._statictextCommandName.GetLabelText()
    
    def getCommandValue(self):
        return self._textctrlCommandValue.GetValue()
        
    def setCommandName(self, name):
        self._statictextCommandName.SetLabelText(name)
        self.SetTitle(name)
    
    def setCommandValue(self, value):
        self._textctrlCommandValue.SetValue(value)
        self.parseCommandValue()
    
    def parseCommandValue(self):
        if self.__mode == MODE_IDLE:
            self.__mode = MODE_PARSING
            self.__mode = MODE_IDLE
        else:
            pass
    
    def buildCommandValue(self):
        if self.__mode == MODE_IDLE:
            self.__mode = MODE_BUILDING
            self.__mode = MODE_IDLE
        else:
            pass
