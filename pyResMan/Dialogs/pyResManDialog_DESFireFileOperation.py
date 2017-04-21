'''
Created on 2017/04/19

@author: zhenkui
'''
from pyResMan.BaseDialogs.pyResManDESFireDialogBase_FileOperation import DESFireDialogBase_FileOperation
from pyResMan.Util import IDOK, IDCANCEL, Util
from pyResMan.DESFireEx import READ_DATA, WRITE_DATA, CREDIT, DEBIT,\
    LIMITED_CREDIT, WRITE_RECORD, READ_RECORDS

class DESFireDialog_FileOperation(DESFireDialogBase_FileOperation):
    '''
    '''


    def __init__(self, parent, command_type, file_id):
        '''
        Constructor
        '''
        DESFireDialogBase_FileOperation.__init__(self, parent)
        
        self.__hideAllControls()
        
        if command_type == READ_DATA:
            self._statictextFileNo.Show()
            self._statictextOffset.Show()
            self._statictextLength.Show()
            self._textctrlFileNo.Show()
            self._textctrlOffset.Show()
            self._textctrlLength.Show()
        elif command_type == WRITE_DATA:
            self._statictextFileNo.Show()
            self._statictextOffset.Show()
            self._statictextData.Show()
            self._textctrlFileNo.Show()
            self._textctrlOffset.Show()
            self._textctrlData.Show()
        elif command_type == CREDIT:
            self._statictextFileNo.Show()
            self._statictextValue.Show()
            self._textctrlFileNo.Show()
            self._textctrlValue.Show()
        elif command_type == DEBIT:
            self._statictextFileNo.Show()
            self._statictextValue.Show()
            self._textctrlFileNo.Show()
            self._textctrlValue.Show()
        elif command_type == LIMITED_CREDIT:
            self._statictextFileNo.Show()
            self._statictextValue.Show()
            self._textctrlFileNo.Show()
            self._textctrlValue.Show()
        elif command_type == WRITE_RECORD:
            self._statictextFileNo.Show()
            self._statictextOffset.Show()
            self._statictextData.Show()
            self._textctrlFileNo.Show()
            self._textctrlOffset.Show()
            self._textctrlData.Show()
        elif command_type == READ_RECORDS:
            self._statictextFileNo.Show()
            self._statictextOffset.Show()
            self._statictextLength.Show()
            self._textctrlFileNo.Show()
            self._textctrlOffset.Show()
            self._textctrlLength.Show()
        else:
            pass
        
        self._textctrlFileNo.SetValue('%02X' %(file_id))
        
        self.DoLayoutAdaptation()
        
    def __hideAllControls(self):
        self._statictextFileNo.Hide()
        self._statictextOffset.Hide()
        self._statictextLength.Hide()
        self._statictextValue.Hide()
        self._statictextData.Hide()
        
        self._textctrlFileNo.Hide()
        self._textctrlOffset.Hide()
        self._textctrlLength.Hide()
        self._textctrlValue.Hide()
        self._textctrlData.Hide()

    def _buttonOKOnButtonClick(self, event):
        self.EndModal(IDOK)
    
    def _buttonCancelOnButtonClick(self, event):
        self.EndModal(IDCANCEL)
    
    def getFileNo(self):
        return int(self._textctrlFileNo.GetValue(), 0x10)
    
    def getOffset(self):
        return int(self._textctrlOffset.GetValue(), 0x10)
    
    def getLength(self):
        return int(self._textctrlLength.GetValue(), 0x10)
    
    def getValue(self):
        return int(self._textctrlValue.GetValue(), 0x10)

    def getData(self):
        return Util.s2vl(self._textctrlData.GetValue())
    