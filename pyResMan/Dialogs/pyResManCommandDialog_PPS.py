# -*- coding: utf-8 -*-

'''
Modified on 2017-03-28

@author: javacardos@gmail.com
@organization: https://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from pyResMan.BaseDialogs.pyResManCommandDialogBase_PPS import CommandDialogBase_PPS
from pyResMan.Util import IDOK, IDCANCEL
from pyResMan.Util import Util, HexValidator

###########################################################################
## Class CommandDialog_PPS
###########################################################################

MODE_IDLE = 0
MODE_PARSING = 1
MODE_BUILDING = 2

class CommandDialog_PPS ( CommandDialogBase_PPS ):
    
    def __init__( self, parent ):
        CommandDialogBase_PPS.__init__ ( self, parent )
        self.__mode = MODE_IDLE
        self._textctrlCommandValue.SetMaxLength(3 * 2)
        # Set validator;
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
                commandValueString = self._textctrlCommandValue.GetValue()
                commandValue = Util.s2vl(commandValueString)
                # Start byte;
                self._choiceCID.SetSelection(commandValue[0] & 0x0F)
                # Parameter 0;
                self._checkboxPPS1.SetValue(True if (commandValue[1] & 0x10) else False)
                # Parameter 1;
                parameter1 = commandValue[2]
                #     DSI;
                self._choiceDSI.SetSelection((parameter1 >> 2) & 0x03)
                #     DRI;
                self._choiceDSI.SetSelection(parameter1 & 0x03)
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
                
                commandValue.append(0b11010000 | self._choiceCID.GetSelection())
                if self._checkboxPPS1.GetValue():
                    commandValue.append(0x11)
                    commandValue.append(0b0000 | ((self._choiceDSI.GetSelection() & 0x03) << 2) | (self._choiceDSI.GetSelection() & 0x03))
                else:
                    commandValue.append(0x01)
                
                self._textctrlCommandValue.SetValue(Util.vl2s(commandValue, ''))
            except:
                pass

            self.__mode = MODE_IDLE
        else:
            pass

    def _choiceCIDOnChoice(self, event):
        self.buildCommandValue()
    
    def _choiceDSIOnChoice(self, event):
        self.buildCommandValue()
    
    def _choiceDRIOnChoice(self, event):
        self.buildCommandValue()
    
    def _checkboxPPS1OnCheckBox(self, event):
        self.buildCommandValue()
    
    def _textctrlCommandValueOnText(self, event):
        self.parseCommandValue()
    
