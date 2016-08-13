# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from BaseDialogs.pyResManCommandDialogBase_MifareRestore import CommandDialogBase_MifareRestore
from Util import IDOK, IDCANCEL
from Util import HexValidator, Util

###########################################################################
## Class CommandDialog_MifareRestore
###########################################################################

MODE_IDLE = 0
MODE_PARSING = 1
MODE_BUILDING = 2

class CommandDialog_MifareRestore ( CommandDialogBase_MifareRestore ):
    def __init__( self, parent, bytesCount = 1 ):
        CommandDialogBase_MifareRestore.__init__ ( self, parent )
        self.__mode = MODE_IDLE
        self._textctrlCommandValue.SetMaxLength(bytesCount * 2)
        # Set validator;
        self._textctrlCommandValue.SetValidator(HexValidator())
        self._textctrlCommandValue.Disable()
        
        for bn in range(256):
            self._choiceBlockNumber.Append('%d' %(bn))
        self._choiceBlockNumber.SetSelection(0)
    
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
#             # Check command type;
#             if commandValue[0] != 0xC2:
#                 pass
            self._choiceBlockNumber.SetSelection(commandValue[1])
            
            self.__mode = MODE_IDLE
        else:
            pass
    
    def buildCommandValue(self):
        if self.__mode == MODE_IDLE:
            self.__mode = MODE_BUILDING
            
            commandValue = []
            # Command type;
            commandValue.append(0xC2)
            # Block Number;
            commandValue.append(self._choiceBlockNumber.GetSelection())
            # 
            self._textctrlCommandValue.SetValue(Util.vl2s(commandValue, ''))
            
            self.__mode = MODE_IDLE
        else:
            pass

    def _choiceBlockNumberOnChoice(self, event):
        self.buildCommandValue()
    
    def _textctrlCommandValueOnText( self, event ):
        self.parseCommandValue()
