import os

import PyInstaller.__main__

#os.removedirs('.\\dist')
#os.removedirs('.\\build')
#os.remove('*.spec')

PyInstaller.__main__.run([
    '--name=%s' % "SOAD Sistema",
  # '--onefile',
    '--windowed',
    '--add-binary=%s;Resources\\database\\bin\\runtime' % os.path.join('Resources', 'database', 'bin', 'runtime'),
    '--add-binary=%s;Resources\\gtk-3.8.1' % os.path.join('Resources', 'gtk-3.8.1'),
    '--add-data=%s;Resources\\icons' % os.path.join('Resources', 'icons', '*.png'),
    '--add-data=%s;Resources\\Imagens' % os.path.join('Resources', 'Imagens', '*.png'),
    '--add-binary=%s;Resources\\Scripts\\SQL' % os.path.join('Resources', 'Scripts', 'SQL', '*.backup'),
    '--icon=%s' % os.path.join('soad.ico'),
    '--console',
    os.path.join('SOAD.py')
])
