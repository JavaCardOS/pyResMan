'''
Created on 2016-05-14

@author: javacardos@gmail.com
@organization: http://www.javacardos.com/
@copyright: JavaCardOS Technologies. All rights reserved.
'''

from GPInterface import GPInterface
from GPInterface import SCARD_PROTOCOL_T1
from R502SpyLibrary import R502SpyLibrary

if __name__ == '__main__':
    gpInterface = GPInterface()
    readers = gpInterface.listreaders()
    for reader in readers:
        if reader.find('R502 SPY') != -1:
            break
    gpInterface.connect(reader, SCARD_PROTOCOL_T1)
    
    scDebugger = R502SpyLibrary(gpInterface)
    scDebugger.init()
    scDebugger.rfManaul()
    scDebugger.rfOn()
    
    ret, rsp = scDebugger.claWUPA('\x52')
    print str(ret) + ' > ' + ''.join('%02X ' %(ord(b)) for b in rsp)
    
    ret, rsp = scDebugger.claAnticollision('\x93\x20')
    print str(ret) + ' > ' +  ''.join('%02X ' %(ord(b)) for b in rsp)
    uid = rsp

    ret, rsp = scDebugger.claSelect('\x93\x70' + uid)
    print str(ret) + ' > ' +  ''.join('%02X ' %(ord(b)) for b in rsp)

    ret, rsp = scDebugger.claAnticollision('\x95\x20')
    print str(ret) + ' > ' +  ''.join('%02X ' %(ord(b)) for b in rsp)

    ret, rsp = scDebugger.claSelect('\x95\x70\x0A\x38\x30\x80')
    print str(ret) + ' > ' +  ''.join('%02X ' %(ord(b)) for b in rsp)
    
    ret, rsp = scDebugger.claRATS('\xE0\x80')
    print str(ret) + ' > ' +  ''.join('%02X ' %(ord(b)) for b in rsp)
    
    ret, rsp = scDebugger.claPPS('\xD0\x11\x0F')
    print str(ret) + ' > ' +  ''.join('%02X ' %(ord(b)) for b in rsp)
    
    ret, rsp = scDebugger.claHLTA('\x50\x00')
    print str(ret) + ' > ' +  ''.join('%02X ' %(ord(b)) for b in rsp)

    gpInterface.disconnect()
    