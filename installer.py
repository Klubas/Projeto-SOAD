import os

import PyInstaller.__main__

PyInstaller.__main__.run([
    '--name=%s' % "SOAD Sistema",
   # '--onefile',
    '--windowed',
    '--add-binary=%s;Resources\\database\\bin\\runtime' % os.path.join('Resources', 'database', 'bin', 'runtime'),
    '--add-data=%s;Resources\\icons' % os.path.join('Resources', 'icons', '*.png'),
    '--add-data=%s;Resources\\Imagens' % os.path.join('Resources', 'Imagens', '*.png'),
    '--add-binary=%s;Resources\\Scripts\\SQL' % os.path.join('Resources', 'Scripts', 'SQL', '*.backup'),
    '--icon=%s' % os.path.join('soad.ico'),
    os.path.join('SOAD.py'),
])