# -*- coding:utf8 -*-

'''
Created on 2016-7-19

@author: javacardos@gmail.com
@organization: http://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from pyResMan.Util import Util


class DebuggerScriptFile(object):
    '''
    classdocs
    '''
    
    __DEBUGGER_COMMANDS1 = [
      "RF_ON"
    , "RF_OFF"
    , "RF_AUTO"
    , "RF_MANUAL"
    ]
    
    __DEBUGGER_COMMANDS2 = [
#       "%UID%"
      "REQA"
    , "WUPA"
    , "ANTICOLLISION"
    , "SELECT"
    , "RATS"
    , "HLTA"
    , "PPS"
    , "REQB"
    , "WUPB"
    , "SLOT-MARKER"
    , "ATTRIB"
    , "HLTB"
    , "I-BLOCK"
    , "R-BLOCK"
    , "S-BLOCK"
    , "AUTHENTICATION"
    , "READ_BLOCK"
    , "WRITE_BLOCK"
    , "INCREMENT"
    , "DECREMENT"
    , "RESTORE"
    , "TRANSFER"
    ]

    def __init__(self, scriptPath):
        '''
        Constructor
        '''
        self.__scriptPath = scriptPath
    
    def parse(self):
        ret = True
        error = ''
        
        scriptLines = []
        with open(self.__scriptPath, 'r') as scriptFile:
            scriptLines = scriptFile.readlines()
        
        commandsInfo = []
        for scriptLine in scriptLines:
            scriptLine = scriptLine.strip()
            lineTokens = scriptLine.split()

            error = 'Invalid script line format. %s' %(scriptLine)
            
            if (len(lineTokens) < 1):
                ret = False
                break
            
            commandName = lineTokens[0].upper()

            if commandName in DebuggerScriptFile.__DEBUGGER_COMMANDS1:
                commandsInfo.append((commandName, ''))
                continue
            elif commandName in DebuggerScriptFile.__DEBUGGER_COMMANDS2:
                if (len(lineTokens) < 2):
                    ret = False
                    break
                commandValue = lineTokens[1]
                if not Util.ishexstr(commandValue):
                    ret = False
                    break
                commandsInfo.append((commandName, commandValue))
                continue
            else:
                ret = False
                break
        
        if ret:
            return ret, commandsInfo
        return ret, error
    
    def save(self, commandsInfo):
        with open(self.__scriptPath, 'w') as scriptFile:
            for commandInfo in commandsInfo:
                scriptFile.write(commandInfo[0] + ' ' + commandInfo[1] + '\n')
            scriptFile.flush()