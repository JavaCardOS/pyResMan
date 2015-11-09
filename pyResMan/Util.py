# -*- coding:utf8 -*-

'''
Created on 2015-10-30

@author: javacardos@gmail.com
@organization: http://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

class Util(object):
    '''
    Util functions;
    '''
    
    HEXCHARS = '0123456789ABCDEFabcdef'
    
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
        s = s.replace(' ', '')
        s = s.replace('\t', '')
        s = s.replace('\r', '')
        s = s.replace('\n', '')
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
    def vl2s(vl, pad):
        """Convert value list to string; ({0x00, 0xA4, 0x04, 0x00, 0x00} => "00A4040000")"""
        return pad.join("%02X" %(v) for v in vl)

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
