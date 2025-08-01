# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:\\党培祥\\tkinter教程\\腾讯一天一个游戏\\跑酷\\方块跑酷游戏.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='方块跑酷游戏',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['D:\\党培祥\\tkinter教程\\腾讯一天一个游戏\\跑酷\\running_man_13424.ico'],
)
