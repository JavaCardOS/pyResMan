# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from pyResMan.BaseDialogs.pyResManCommandDialogBase_MifareBlockWrite import CommandDialogBase_MifareBlockWrite
from pyResMan.Util import IDOK, IDCANCEL
from pyResMan.Util import HexValidator, Util

###########################################################################
## Class CommandDialog_MifareBlockWrite
###########################################################################

MODE_IDLE = 0
MODE_PARSING = 1
MODE_BUILDING = 2

class CommandDialog_MifareBlockWrite ( CommandDialogBase_MifareBlockWrite ):
    def __init__( self, parent, bytesCount = 1 ):
        CommandDialogBase_MifareBlockWrite.__init__ ( self, parent )
        self.__mode = MODE_IDLE
        self._textctrlCommandValue.SetMaxLength(bytesCount * 2)
        # Set validator;
        self._textctrlCommandValue.SetValidator(HexValidator())
        
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
#             if commandValue[0] != 0xA0:
#                 pass
            self._choiceBlockNumber.SetSelection(commandValue[1])
            self._textctrlData.SetValue(Util.vl2s(commandValue[2 :], ''))
            
            self.__mode = MODE_IDLE
        else:
            pass
    
    def buildCommandValue(self):
        if self.__mode == MODE_IDLE:
            self.__mode = MODE_BUILDING
            
            commandValue = []
            # Command type;
            commandValue.append(0xA0)
            # Block number;
            commandValue.append(self._choiceBlockNumber.GetSelection())
            # Data;
            data = [0x00] * 16
            try:
                data = Util.s2vl(self._textctrlData.GetValue())
            except:
                pass
            for d in data:
                commandValue.append(d)
            # 
            self._textctrlCommandValue.SetValue(Util.vl2s(commandValue, ''))
            
            self.__mode = MODE_IDLE
        else:
            pass

    def _choiceBlockNumberOnChoice( self, event ):
        self.buildCommandValue()
    
    def _textctrlDataOnText( self, event ):
        self.buildCommandValue()
    
    def _textctrlCommandValueOnText( self, event ):
        self.parseCommandValue()
