# -*- coding:utf8 -*-

'''
Created on 2015-10-30

@author: javacardos@gmail.com
@organization: https://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

IDOK = 1
IDCANCEL = 2

class Util(object):
    '''
    Util functions;
    '''
    
    HEXCHARS = '0123456789ABCDEFabcdef'
    
    @staticmethod
    def removespace(s):
        s = s.replace(' ', '')
        s = s.replace('\t', '')
        s = s.replace('\r', '')
        s = s.replace('\n', '')
        return s
    
    @staticmethod
    def c2v(c):
        """Get value of one char; Argument c is the input char;"""
        cv = ord(c)
        if ((cv >= ord('0')) and (cv <= ord('9'))):
            return cv - ord('0')
        elif ((cv >= ord('A')) and (cv <= ord('F'))):
            return cv - ord('A') + 10
        elif ((cv >= ord('a')) and (cv <= ord('f'))):
            return cv - ord('a') + 10
        else:
            raise ValueError
    
    @staticmethod
    def s2vl(s):
        """Convert string to value list; Argument s is the input string; ("00A4040000" => {0x00, 0xA4, 0x04, 0x00, 0x00})"""
        s = Util.removespace(s)
        if (len(s) & 1) != 0:
            raise ValueError()
        for c in s:
            if c not in Util.HEXCHARS:
                raise ValueError()
        vl = []
        for i in xrange(0, len(s) / 2):
            vl.append(Util.c2v(s[i * 2]) << 4 | Util.c2v(s[i * 2 + 1]))
        return vl

    @staticmethod
    def s2vs(s):
        s = Util.removespace(s)
        if (len(s) & 1) != 0:
            raise ValueError()
        for c in s:
            if c not in Util.HEXCHARS:
                raise ValueError()
        vs = ''
        for i in xrange(0, len(s) / 2):
            vs += chr(Util.c2v(s[i * 2]) << 4 | Util.c2v(s[i * 2 + 1]))
        return vs
    
    @staticmethod
    def vl2s(vl, pad=''):
        """Convert value list to string; ({0x00, 0xA4, 0x04, 0x00, 0x00} => "00A4040000")"""
        return pad.join("%02X" %(v) for v in vl)

    @staticmethod
    def vs2s(vs, pad=''):
        """Convert value list to string; ('\x00\xA4\x04\x00\x00' => "00A4040000")"""
        return pad.join("%02X" %(ord(v)) for v in vs)

    @staticmethod
    def getTimeStr(tv):
        """Get time string to display; tv is the time value;"""
        if tv < 0:
            timeStr = '< 0'
        elif tv < 0.000001:
            timeStr = '%3.3fns' %(tv * (10 ** 9))
        elif tv < 0.001:
            timeStr = '%3.3fus' %(tv * (10 ** 6))
        elif tv < 1.0:
            timeStr = '%3.3fms' %(tv * (10 ** 3))
        else:
            timeStr = '%3.3fs' %(tv * (10 ** 0))
        return timeStr

    @staticmethod
    def isprint_keycode(kc): return kc >= 32 and kc <= 126

    @staticmethod
    def isprint_char(c): return ord(c) >= 32 and ord(c) <= 126

    @staticmethod
    def ishexchar_kc(kc):
        isHexChar = False
        if Util.isprint_keycode(kc):
            if kc >= ord('0') and kc <= ord('9'):
                isHexChar = True
            elif kc >= ord('a') and kc <= ord('f'):
                isHexChar = True
            elif kc >= ord('A') and kc <= ord('F'):
                isHexChar = True
        else:
            isHexChar = True
        return isHexChar

    @staticmethod
    def ishexchar_c(c):
        isHexChar = False
        if Util.isprint_char(c):
            if c >= '0' and c <= '9':
                isHexChar = True
            elif c >= 'a' and c <= 'f':
                isHexChar = True
            elif c >= 'A' and c <= 'F':
                isHexChar = True
        return isHexChar

    @staticmethod
    def isnumchar_kc(kc):
        isNumChar = False
        if Util.isprint_keycode(kc):
            if kc >= ord('0') and kc <= ord('9'):
                isNumChar = True
        else:
            isNumChar = True
        return isNumChar

    @staticmethod
    def isnumchar_c(c):
        isNumChar = False
        if Util.isprint_char(c):
            if c >= '0' and c <= '9':
                isNumChar = True
        else:
            isNumChar = True
        return isNumChar
    
    @staticmethod
    def ishexstr(s):
        s = Util.removespace(s)
        ishexstr = True
        for c in s:
            if not Util.ishexchar_c(c):
                ishexstr = False
                break
        return ishexstr


import wx

class HexValidator(wx.PyValidator):
    """Validate Hex strings"""
    def __init__(self):
        """Initialize the validator

        """
        super(HexValidator, self).__init__()

        # Event Handlers
        self.Bind(wx.EVT_CHAR, self.OnChar)

    def Clone(self):
        """Clones the current validator
        @return: clone of this object

        """
        return HexValidator()

#     def Validate(self, win):
#         """Validate an window value
#         @param win: window to validate
# 
#         """
#         for char in val:
#             if char not in Util.HEXCHARS:
#                 return False
#         else:
#             return True

    def OnChar(self, event):
        """Process values as they are entered into the control
        @param event: event that called this handler

        """
        key = event.GetKeyCode()
        if event.CmdDown() or key < wx.WXK_SPACE or key == wx.WXK_DELETE or \
           key > 255 or chr(key) in Util.HEXCHARS:
            event.Skip()
            return

        if not wx.Validator_IsSilent():
            wx.Bell()

        return
    
    def TransferFromWindow(self, *args, **kwargs):
        return True
    
    def TransferToWindow(self, *args, **kwargs):
        return True

