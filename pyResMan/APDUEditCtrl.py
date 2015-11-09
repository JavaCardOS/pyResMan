# -*- coding:utf8 -*-

'''
Created on 2015-11-4

@author: javacardos@gmail.com
@organization: http://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

import wx
from wx.lib.masked.textctrl import BaseMaskedTextCtrl

class APDUByteEditCtrl(BaseMaskedTextCtrl):
    '''
    Edit ctrl for apdu one byte (CLA, INS, P1, P2, LC, LE);
    '''

    def __init__(self, parent, id=-1, value = '',
                  pos = wx.DefaultPosition,
                  size = wx.DefaultSize,
                  style = wx.TE_PROCESS_TAB,
                  validator = wx.DefaultValidator,
                  name = 'IpAddrCtrl',
                  setupEventHandling = True,        ## setup event handling by default
                  bytesCount = 1,
                  **kwargs):
        '''
        Constructor
        '''
        kwargs['mask'] = "XX" * bytesCount
        kwargs['excludeChars'] = 'ghijklmnopqrstuvwxyzGHIJKLMNOPQRSTUVWXYZ'
        BaseMaskedTextCtrl.__init__(
                self, parent, id=id, value = value,
                pos=pos, size=size,
                style = style,
                validator = validator,
                name = name,
                setupEventHandling = setupEventHandling,
                **kwargs)
