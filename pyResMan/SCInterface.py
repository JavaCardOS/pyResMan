'''
Created on 2016-5-7

@author: zhenkui
'''

class SCInterface(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
    
    def connect(self, readername, protocol):
        pass
    
    def disconnect(self):
        pass
    
    def transmit(self, cmd):
        pass
    
    def listreaders(self):
        pass
    