# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from BaseDialogs.pyResManCommandDialogBase_SBlock import CommandDialogBase_SBlock
from Util import IDOK, IDCANCEL
from Util import HexValidator, Util

###########################################################################
## Class CommandDialog_Basic
###########################################################################

MODE_IDLE = 0
MODE_PARSING = 1
MODE_BUILDING = 2

class CommandDialog_SBlock ( CommandDialogBase_SBlock ):
    def __init__( self, parent ):
        CommandDialogBase_SBlock.__init__ ( self, parent )
        
        self.__mode = MODE_IDLE

        self._textctrlEDC.SetMaxLength(2 * 2)
#         self._textctrlINF.SetMaxLength()
#         self._textctrlCommandValue.SetMaxLength()

        # Set validator;
        self._textctrlCommandValue.SetValidator(HexValidator())
        self._textctrlEDC.SetValidator(HexValidator())
        self._textctrlWTXM.SetValidator(HexValidator())
    
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
#             if commandTypeIndex == 3:
#                 pass
            self._choiceType.SetSelection(1 if (PCD & 0b00110000) else 0)
            commandValueIndex += 1
            
            # Parse CID byte;
            if PCD & 0b00001000:
                self._checkboxCIDFollowing.SetValue(True)
                CID = commandValue[commandValueIndex]
                self._choiceCID.SetSelection(CID & 0x0F)
                commandValueIndex += 1
            else:
                self._checkboxCIDFollowing.SetValue(False)
            
            # Parse INF byte;
            INF= commandValue[commandValueIndex]
            self._choicePowerLevel.SetSelection((INF >> 6) & 3)
            self._textctrlWTXM.SetValue('%02X' %(INF & 0b00111111))
            
            self.__mode = MODE_IDLE
        else:
            pass
    
    def buildCommandValue(self):
        if self.__mode == MODE_IDLE:
            self.__mode = MODE_BUILDING

            commandValue = []
            # PCD byte;
            PCD = 0b11000010
            if self._choiceType.GetSelection() != 0:
                PCD |= 0b00110000
            if self._checkboxCIDFollowing.IsChecked():
                PCD |= 0b00001000
            commandValue.append(PCD)
            
            # CID byte;
            if self._checkboxCIDFollowing.IsChecked():
                CID = self._choiceCID.GetSelection()
                commandValue.append(CID)

            # Build INF field;
            WTXM = 0
            try:
                WTXM = Util.s2vl(self._textctrlWTXM.GetValue())[0] & 0b00111111
            except:
                pass
            
            commandValue.append(self._choicePowerLevel.GetSelection() | WTXM)
            
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
    
    def _textctrlEDCOnText( self, event ):
        self.buildCommandValue()
    
    def _textctrlWTXMOnText( self, event ):
        self.buildCommandValue()
    
    def _textctrlCommandValueOnText( self, event ):
        self.parseCommandValue()
