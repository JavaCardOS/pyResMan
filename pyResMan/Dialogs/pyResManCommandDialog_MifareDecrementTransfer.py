# -*- coding: utf-8 -*-

'''
Modified on 2017-03-28

@author: javacardos@gmail.com
@organization: https://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from pyResMan.BaseDialogs.pyResManCommandDialogBase_MifareDecrementTransfer import CommandDialogBase_MifareDecrementTransfer
from pyResMan.Util import IDOK, IDCANCEL
from pyResMan.Util import HexValidator, Util

###########################################################################
## Class CommandDialog_MifareDecrementTransfer
###########################################################################

MODE_IDLE = 0
MODE_PARSING = 1
MODE_BUILDING = 2

class CommandDialog_MifareDecrementTransfer ( CommandDialogBase_MifareDecrementTransfer ):
    def __init__( self, parent, bytesCount = 1 ):
        CommandDialogBase_MifareDecrementTransfer.__init__ ( self, parent )
        self.__mode = MODE_IDLE
        self._textctrlCommandValue.SetMaxLength(bytesCount * 2)
        # Set validator;
        self._textctrlCommandValue.SetValidator(HexValidator())
        
        for bn in range(256):
            self._choiceBlockNumber.Append('%d' %(bn))
        self._choiceBlockNumber.SetSelection(0)
        self._textctrlValue.SetValidator(HexValidator())
    
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
#             if commandValue[0] != 0xXX:
#                 pass
            self._choiceBlockNumber.SetSelection(commandValue[1])
            self._textctrlValue.SetValue(Util.vl2s(commandValue[2 :], ''))
            
            self.__mode = MODE_IDLE
        else:
            pass
    
    def buildCommandValue(self):
        if self.__mode == MODE_IDLE:
            self.__mode = MODE_BUILDING
            
            commandValue = []
            # Command type;
            commandValue.append(0xC0)
            # Block Number;
            commandValue.append(self._choiceBlockNumber.GetSelection())
            # Operand;
            operand = [0x00, 0x00, 0x00, 0x00]
            try:
                operand = Util.s2vl(self._textctrlValue.GetValue())
            except:
                pass
            for o in operand:
                commandValue.append(o)
            # 
            self._textctrlCommandValue.SetValue(Util.vl2s(commandValue, ''))
            
            self.__mode = MODE_IDLE
        else:
            pass

    def _choiceBlockNumberOnChoice(self, event):
        self.buildCommandValue()
    
    def _textctrlValueOnText( self, event ):
        self.buildCommandValue()
    
    def _textctrlCommandValueOnText( self, event ):
        self.parseCommandValue()
