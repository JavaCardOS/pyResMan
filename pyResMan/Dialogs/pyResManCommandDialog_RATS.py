# -*- coding: utf-8 -*-

'''
Modified on 2017-03-28

@author: javacardos@gmail.com
@organization: https://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from pyResMan.BaseDialogs.pyResManCommandDialogBase_RATS import CommandDialogBase_RATS
from pyResMan.Util import IDOK, IDCANCEL
from pyResMan.Util import Util, HexValidator

###########################################################################
## Class CommandDialog_RATS
###########################################################################

MODE_IDLE = 0
MODE_PARSING = 1
MODE_BUILDING = 2

class CommandDialog_RATS ( CommandDialogBase_RATS ):
    
    def __init__( self, parent ):
        CommandDialogBase_RATS.__init__ ( self, parent )
        self.__mode = MODE_IDLE
        self._textctrlHeader.SetMaxLength(1 * 2)
        self._textctrlCommandValue.SetMaxLength(2 * 2)
        # Set validator;
        self._textctrlHeader.SetValidator(HexValidator())
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
            
            try:
                commandValue = Util.s2vl(self._textctrlCommandValue.GetValue())
                self._textctrlHeader.SetValue('%02X' %(commandValue[0]))
                
                parameter = commandValue[1]
                self._choiceFSDI.SetSelection((parameter >> 4) & 0x0F)
                self._choiceCID.SetSelection(parameter & 0x0F)
            except:
                pass

            self.__mode = MODE_IDLE
        else:
            pass
    
    def buildCommandValue(self):
        if self.__mode == MODE_IDLE:
            self.__mode = MODE_BUILDING
            
            try:
                commandValue = []
                commandValue.append(Util.s2vl(self._textctrlHeader.GetValue())[0])
                commandValue.append((self._choiceFSDI.GetSelection() << 4) | self._choiceCID.GetSelection())
                self._textctrlCommandValue.SetValue(Util.vl2s(commandValue, ''))
            except:
                pass

            self.__mode = MODE_IDLE
        else:
            pass
        
    def _textctrlHeaderOnText(self, event):
        self.buildCommandValue()
    
    def _choiceCIDOnChoice(self, event):
        self.buildCommandValue()
    
    def _choiceFSDIOnChoice(self, event):
        self.buildCommandValue()
    
    def _textctrlCommandValueOnText(self, event):
        self.parseCommandValue()
    
