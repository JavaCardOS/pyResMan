# -*- mode: python -*-
import sys

block_cipher = None

entry = ['pyResMan\\Main.py']
if sys.platform != 'win32':
    entry = ['pyResMan/Main.py']
    
a = Analysis(entry,
             pathex=['E:\\opensource\\pyResMan'],
             binaries=None,
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
          upx=True,
          console=True )
