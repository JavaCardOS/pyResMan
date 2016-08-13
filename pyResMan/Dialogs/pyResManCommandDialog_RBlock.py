# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from BaseDialogs.pyResManCommandDialogBase_RBlock import CommandDialogBase_RBlock
from Util import IDOK, IDCANCEL
from Util import HexValidator, Util

###########################################################################
## Class CommandDialog_Basic
###########################################################################

MODE_IDLE = 0
MODE_PARSING = 1
MODE_BUILDING = 2

class CommandDialog_RBlock ( CommandDialogBase_RBlock ):
    def __init__( self, parent ):
        CommandDialogBase_RBlock.__init__ ( self, parent )
        
        self.__mode = MODE_IDLE

        self._textctrlEDC.SetMaxLength(2 * 2)
#         self._textctrlINF.SetMaxLength()
#         self._textctrlCommandValue.SetMaxLength()

        # Set validator;
        self._textctrlCommandValue.SetValidator(HexValidator())
        self._textctrlEDC.SetValidator(HexValidator())
        self._textctrlINF.SetValidator(HexValidator())
    
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
            
            commandValueString = self._textctrlCommandValue.GetValue()
            try:
                commandValue = Util.s2vl(commandValueString)
            except:
                return
            
            commandValueIndex = 0
            
            # Parse PCD byte;
            PCD = commandValue[commandValueIndex]
#             commandTypeIndex = ((PCD >> 6) & 0x03)
#             if commandTypeIndex == 2:
#                 pass
            self._choiceType.SetSelection(0 if not (PCD & 0b00010000) else 1)
            commandValueIndex += 1
            
            # Parse CID byte;
            if PCD & 0b00001000:
                self._checkboxCIDFollowing.SetValue(True)
                CID = commandValue[commandValueIndex]
                self._choiceCID.SetSelection(CID & 0x0F)
                commandValueIndex += 1
            else:
                self._checkboxCIDFollowing.SetValue(False)
            
            # Block Number Flag;
            self._checkboxBlockNumber.SetValue(True if (PCD & 0b00000001) else False)
            
            # Parse INF byte;
            INF = commandValue[commandValueIndex : ]
            self._textctrlINF.SetValue(Util.vl2s(INF, ''))
            
            self.__mode = MODE_IDLE
        else:
            pass
    
    def buildCommandValue(self):
        if self.__mode == MODE_IDLE:
            self.__mode = MODE_BUILDING

            commandValue = []
            # PCD byte;
            PCD = 0b10100010
            PCD |= (self._choiceType.GetSelection() << 4) & 0x10
            if self._checkboxCIDFollowing.IsChecked():
                PCD |= 0b00001000
            if self._checkboxBlockNumber.IsChecked():
                PCD |= 0b00000001
            commandValue.append(PCD)
            
            # CID byte;
            if self._checkboxCIDFollowing.IsChecked():
                CID = self._choiceCID.GetSelection()
                commandValue.append(CID)
            
            # Build INF field;
            try:
                INF = Util.s2vl(self._textctrlINF.GetValue())
                for infByte in INF:
                    commandValue.append(infByte)
            except:
                pass
            
#             # EDC bytes;
#             EDC = [ 0x00, 0x00 ]
#             try:
#                 EDC = Util.s2vl(self._textctrlEDC.GetValue())[ : 2]
#             except:
#                 pass
#             try:
#                 commandValue.append(EDC[0])
#             except:
#                 commandValue.append(0)
#             try:
#                 commandValue.append(EDC[1])
#             except:
#                 commandValue.append(0)
            
            self._textctrlCommandValue.SetValue(Util.vl2s(commandValue, ''))
            
            self.__mode = MODE_IDLE
        else:
            pass
    
    def _choiceTypeOnChoice( self, event ):
        self.buildCommandValue()
    
    def _checkboxCIDFollowingOnCheckBox( self, event ):
        if self._checkboxCIDFollowing.IsChecked():
            self._choiceCID.Enable()
        else:
            self._choiceCID.Disable()
        
        self.buildCommandValue()
    
    def _choicePowerLevelOnChoice( self, event ):
        self.buildCommandValue()
    
    def _choiceCIDOnChoice( self, event ):
        self.buildCommandValue()

    def _checkboxBlockNumberOnCheckBox( self, event ):
        self.buildCommandValue()
    
    def _textctrlINFOnText( self, event ):
        self.buildCommandValue()
    
    def _textctrlEDCOnText( self, event ):
        self.buildCommandValue()
    
    def _textctrlCommandValueOnText( self, event ):
        self.parseCommandValue()
