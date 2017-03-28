# -*- coding: utf-8 -*-

'''
Modified on 2017-03-28

@author: javacardos@gmail.com
@organization: https://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from pyResMan.BaseDialogs.pyResManCommandDialogBase_AnticollisionSelect import CommandDialogBase_AnticollisionSelect
from pyResMan.Util import IDOK, IDCANCEL
from pyResMan.Util import Util, HexValidator

###########################################################################
## Class CommandDialog_AnticollisionSelect
###########################################################################

MODE_IDLE = 0
MODE_PARSING = 1
MODE_BUILDING = 2

class CommandDialog_AnticollisionSelect ( CommandDialogBase_AnticollisionSelect):
    
    def __init__( self, parent, select = False ):
        CommandDialogBase_AnticollisionSelect.__init__ ( self, parent )
        self.__mode = MODE_IDLE
        self._textctrlUID.Enable(select)
        self._textctrlUID.SetMaxLength(4 * 2)
        self._textctrlCommandValue.SetMaxLength((2 * 2) if not select else (6 * 2))
        
        if select:
            self._textctrlUID.SetValue('00000000')
        
        # Set validator;
        self._textctrlUID.SetValidator(HexValidator())
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
                
                # SEL;
                SEL = commandValue[0]
                if SEL == 0x93:
                    self._choiceLevel.SetSelection(0)
                elif SEL == 0x95:
                    self._choiceLevel.SetSelection(1)
                elif SEL == 0x97:
                    self._choiceLevel.SetSelection(2)
                else:
                    self._choiceLevel.SetSelection(0)
                # NVB;
                NVB = commandValue[1]
                self._choiceByteCount.SetSelection(((NVB >> 4) & 0x07) - 2)
                self._choiceBitCount.SetSelection(NVB & 0x07)
                # UID;
                if len(commandValue) > 2:
                    self._textctrlUID.SetValue(Util.vl2s(commandValue[2 : ], ''))
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
                # SEL;
                SELIndex = self._choiceLevel.GetSelection()
                commandValue.append(0x93 + 2 * SELIndex)
                # NVB;
                commandValue.append((((self._choiceByteCount.GetSelection() + 2) << 4) & 0xF0) | (self._choiceBitCount.GetSelection() & 0x0F))
                # UID;
                uidString = self._textctrlUID.GetValue()
                commandValue += Util.s2vl(uidString)
                
                self._textctrlCommandValue.SetValue(Util.vl2s(commandValue, ''))
            except:
                pass

            self.__mode = MODE_IDLE
        else:
            pass
    
    def _choiceBitCountOnChoice(self, event):
        self.buildCommandValue()
    
    def _choiceByteCountOnChoice(self, event):
        self.buildCommandValue()

    def _choiceLevelOnChoice(self, event):
        self.buildCommandValue()
    
    def _textctrlUIDOnText(self, event):
        self.buildCommandValue()
    
    def _textctrlCommandValueOnText(self, event):
        self.parseCommandValue()
