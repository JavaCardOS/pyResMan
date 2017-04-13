# -*- coding: utf-8 -*-

'''
Modified on 2017-03-28

@author: javacardos@gmail.com
@organization: https://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from pyResMan.BaseDialogs.pyResManDESFireDialogBase_CreateFile import DESFireDialogBase_CreateFile
from pyResMan.Util import IDOK, IDCANCEL
from pyResMan.Util import HexValidator
from pyResMan.DESFireEx import DESFireEx, CREATE_STDDATAFILE,\
    CREATE_BACKUPDATAFILE, CREATE_VALUE_FILE, CREATE_LINEAR_RECORD_FILE,\
    CREATE_CYCLIC_RECORD_FILE

###########################################################################
## Class DESFireDialog_CreateFile
###########################################################################

class DESFireDialog_CreateFile ( DESFireDialogBase_CreateFile ):
    
    def __init__( self, parent, file_type ):
        DESFireDialogBase_CreateFile.__init__ ( self, parent )
        
        self._textctrlFileNo.SetValidator(HexValidator())
        self._textctrlComSet.SetValidator(HexValidator())
        self._textctrlAccessRights.SetValidator(HexValidator())
        self._textctrlFileSize.SetValidator(HexValidator())
        self._textctrlLowerLimit.SetValidator(HexValidator())
        self._textctrlUpperLimit.SetValidator(HexValidator())
        self._textctrlValue.SetValidator(HexValidator())
        self._textctrlRecordSize.SetValidator(HexValidator())
        self._textctrlMaxNumOfRecords.SetValidator(HexValidator())
        
        self._textctrlFileSize.Hide()
        self._textctrlLowerLimit.Hide()
        self._textctrlUpperLimit.Hide()
        self._textctrlValue.Hide()
        self._checkboxLimitedCreditEnabled.Hide()
        self._textctrlRecordSize.Hide()
        self._textctrlMaxNumOfRecords.Hide()

        self._statictextFileSize.Hide()
        self._statictextLowerLimit.Hide()
        self._statictextUpperLimit.Hide()
        self._statictextValue.Hide()
        self._statictextRecordSize.Hide()
        self._statictextMaxNumOfRecords.Hide()
        
        if (file_type == CREATE_STDDATAFILE) or (file_type == CREATE_BACKUPDATAFILE):
            self._statictextFileSize.Show()
            self._textctrlFileSize.Show()
        elif (file_type == CREATE_VALUE_FILE):
            self._textctrlLowerLimit.Show()
            self._textctrlUpperLimit.Show()
            self._textctrlValue.Show()
            self._checkboxLimitedCreditEnabled.Show()
            self._statictextLowerLimit.Show()
            self._statictextUpperLimit.Show()
            self._statictextValue.Show()
        elif (file_type == CREATE_LINEAR_RECORD_FILE) or (file_type == CREATE_CYCLIC_RECORD_FILE):
            self._textctrlRecordSize.Show()
            self._textctrlMaxNumOfRecords.Show()
            self._statictextRecordSize.Show()
            self._statictextMaxNumOfRecords.Show()
        else:
            pass
        
        self.DoLayoutAdaptation()
    
    def _buttonOKOnButtonClick(self, event):
        self.EndModal(IDOK)
    
    def _buttonCancelOnButtonClick(self, event):
        self.EndModal(IDCANCEL)

    def getFileNo(self):
        return int(self._textctrlFileNo.GetValue(), 0x10)
    
    def getComSet(self):
        return int(self._textctrlComSet.GetValue(), 0x10)

    def getAccessRights(self):
        return int(self._textctrlAccessRights.GetValue(), 0x10)
    
    def getFileSize(self):
        return int(self._textctrlFileSize.GetValue(), 0x10)
    
    def getLowerLimit(self):
        return int(self._textctrlLowerLimit.GetValue(), 0x10)
    
    def getUpperLimit(self):
        return int(self._textctrlUpperLimit.GetValue(), 0x10)
    
    def getValue(self):
        return int(self._textctrlValue.GetValue(), 0x10)
    
    def isLimitDebitEnabled(self):
        return self._checkboxLimitedCreditEnabled.IsChecked()
    
    def getRecordSize(self):
        return int(self._textctrlRecordSize.GetValue(), 0x10)
    
    def getMaxNumOfRecords(self):
        return int(self._textctrlMaxNumOfRecords.GetValue(), 0x10)
    