# -*- mode: python -*-

block_cipher = None


a = Analysis(['c:\\Users\\Michael Akinosho\\github\\Capstone-Project-Ideas\\python_gui\\CustomStyles\\src\\main\\python\\main.py'],
             pathex=['c:\\Users\\Michael Akinosho\\github\\Capstone-Project-Ideas\\python_gui\\CustomStyles\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['c:\\virtual-envs\\venv-gui\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\MICHAE~1\\AppData\\Local\\Temp\\tmpzbmtjtkh\\fbs_pyinstaller_hook.py'],
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
          name='Painter Text Editor',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='c:\\Users\\Michael Akinosho\\github\\Capstone-Project-Ideas\\python_gui\\CustomStyles\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='Painter Text Editor')
