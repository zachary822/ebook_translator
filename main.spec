# -*- mode: python -*-

block_cipher = None

a = Analysis(['main.py'],
             pathex=['/Users/zacharyjuang/PycharmProjects/ebook_translator'],
             binaries=[],
             datas=[('/Users/zacharyjuang/PycharmProjects/chinese_converter/chinese_converter/bigram.json',
                     'chinese_converter'),
                    ('/Users/zacharyjuang/PycharmProjects/chinese_converter/chinese_converter/monogram.json',
                     'chinese_converter'),
                    ('/Users/zacharyjuang/PycharmProjects/chinese_converter/chinese_converter/simplified.txt',
                     'chinese_converter'),
                    ('/Users/zacharyjuang/PycharmProjects/chinese_converter/chinese_converter/traditional.txt',
                     'chinese_converter')],
             hiddenimports=[],
             hookspath=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False)
app = BUNDLE(exe,
             name='ebook_converter.app',
             icon=None,
             bundle_identifier=None,
             info_plist={
                 'NSHighResolutionCapable': 'True',
                 'NSRequiresAquaSystemAppearance': 'False'
             })
