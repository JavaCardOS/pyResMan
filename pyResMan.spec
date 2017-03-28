# -*- mode: python -*-

import os
import sys

block_cipher = None

basepath = os.path.abspath(os.path.curdir)

addlibpath = 'GpPcscConnectionPlugin.dll'
if sys.platform.startswith('linux'):
    addlibpath = "/usr/lib/libgppcscconnectionplugin.so.1"

a = Analysis(['pyResMan/Main.py'],
             pathex=[basepath],
             binaries=[(addlibpath, '.')],
             datas=None,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pyResMan',
          debug=False,
          strip=None,
          upx=False,
          console=True , version='version.txt')
