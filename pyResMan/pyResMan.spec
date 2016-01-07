# -*- mode: python -*-

block_cipher = None

print dir()
basepath = os.path.abspath(os.path.curdir)

a = Analysis(['Main.py'],
             pathex=[basepath],
             binaries=[('GPPcScConnectionPlugin.dll', '.')],
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
          console=True , version='version.txt')
