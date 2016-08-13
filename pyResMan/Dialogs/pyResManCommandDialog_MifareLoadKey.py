# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from BaseDialogs.pyResManCommandDialogBase_MifareLoadKey import CommandDialogBase_MifareLoadKey
from Util import IDOK, IDCANCEL
from Util import HexValidator, Util

###########################################################################
## Class CommandDialog_MifareLoadKey
###########################################################################

MODE_IDLE = 0
MODE_PARSING = 1
MODE_BUILDING = 2

class CommandDialog_MifareLoadKey ( CommandDialogBase_MifareLoadKey ):
    def __init__( self, parent, bytesCount = 1 ):
        CommandDialogBase_MifareLoadKey.__init__ ( self, parent )
        self.__mode = MODE_IDLE
        self._textctrlCommandValue.SetMaxLength(bytesCount * 2)
        # Set validator;
        self._textctrlCommandValue.SetValidator(HexValidator())
        self._textctrlCommandValue.Disable()
    
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

            commandValue= Util.s2vl(self._textctrlCommandValue.GetValue())
            
            self.__mode = MODE_IDLE
        else:
            pass
    
    def buildCommandValue(self):
        if self.__mode == MODE_IDLE:
            self.__mode = MODE_BUILDING
            
            commandValue = []
            self._textctrlCommandValue.SetValue(Util.vl2s(commandValue, ''))
            
            self.__mode = MODE_IDLE
        else:
            pass

    def _choiceModeOnChoice( self, event ):
        self.buildCommandValue()
    
    def _choiceSectorNumberOnChoice( self, event ):
        self.buildCommandValue()
    
    def _textctrlKeyOnText( self, event ):
        self.buildCommandValue()
    
    def _textctrlCommandValueOnText( self, event ):
        self.parseCommandValue()
