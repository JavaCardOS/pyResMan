# -*- coding: utf-8 -*-

'''
Modified on 2017-03-28

@author: javacardos@gmail.com
@organization: https://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from pyResMan.BaseDialogs.pyResManCommandDialogBase_MifareAuthentication import CommandDialogBase_MifareAuthentication
from pyResMan.Util import IDOK, IDCANCEL
from pyResMan.Util import HexValidator, Util

###########################################################################
## Class CommandDialog_MifareAuthentication
###########################################################################

MODE_IDLE = 0
MODE_PARSING = 1
MODE_BUILDING = 2

class CommandDialog_MifareAuthentication ( CommandDialogBase_MifareAuthentication ):
    def __init__( self, parent, bytesCount = 1 ):
        CommandDialogBase_MifareAuthentication.__init__ ( self, parent )
        self.__mode = MODE_IDLE
        self._textctrlCommandValue.SetMaxLength(bytesCount * 2)
        # Set validator;
        self._textctrlCommandValue.SetValidator(HexValidator())
        
        self._textctrlUID.SetValue('00000000')
        
        for i in range(256):
            self._choiceBlockNumber.Append('%d' %(i))
    
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
            
            commandValue = Util.s2vl(self._textctrlCommandValue.GetValue())
            
            self._choiceMode.SetSelection(0 if commandValue[0] == 0x60 else 1)
            self._choiceBlockNumber.SetSelection(commandValue[1])
            self._textctrlKey.SetValue(Util.vl2s(commandValue[2 : 8], ''))
            if len(commandValue) >= 12:
                self._textctrlUID.SetValue(Util.vl2s(commandValue[8 : ], ''))
        
            self.__mode = MODE_IDLE
        else:
            pass
    
    def buildCommandValue(self):
        if self.__mode == MODE_IDLE:
            self.__mode = MODE_BUILDING
            
            commandValue = []
            # Mode;
            commandValue.append(0x60 if (self._choiceMode.GetSelection() == 0) else 0x61)
            # Sector number;
            commandValue.append(self._choiceBlockNumber.GetSelection())
            # Key data;
            keyData= [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
            try:
                keyData = Util.s2vl(self._textctrlKey.GetValue())
            except:
                pass
            for kd in keyData:
                commandValue.append(kd)
            # UID;
            UID = [0x65, 0xE0, 0x5E, 0x1E]
            try:
                UID = Util.s2vl(self._textctrlUID.GetValue())
            except:
                pass
            for id in UID:
                commandValue.append(id)
            # 
            self._textctrlCommandValue.SetValue(Util.vl2s(commandValue, ''))
            
            self.__mode = MODE_IDLE
        else:
            pass
        
    def _choiceModeOnChoice( self, event ):
        self.buildCommandValue()
    
    def _choiceBlockNumberOnChoice(self, event):
        self.buildCommandValue()
    
    def _textctrlKeyOnText( self, event ):
        self.buildCommandValue()
    
    def _textctrlUIDOnText(self, event):
        self.buildCommandValue()
    
    def _textctrlCommandValueOnText( self, event ):
        self.parseCommandValue()
