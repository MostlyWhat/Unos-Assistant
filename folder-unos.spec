# -*- mode: python ; coding: utf-8 -*-

import os
import platform
import sys

import PyInstaller

block_cipher = None

datas = []
datas.extend(PyInstaller.utils.hooks.collect_data_files('en_core_web_sm'))

a = Analysis(['unos.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=['en-core-web-sm'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='unos',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='unos')
