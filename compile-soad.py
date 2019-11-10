import os

import PyInstaller.__main__
from PyInstaller.utils.hooks import collect_data_files

#os.removedirs('.\\dist')
#os.removedirs('.\\build')
#os.remove('*.spec')

# Tem um bug do PyInstaller que não está pegando a DLL do shiboken2
# Precisa copiar ela da pasta do shiboken e colar na pasta do PySide2

PyInstaller.__main__.run([
    '--name=%s' % "SOAD-Sistema",
  # '--onefile',
    '--windowed',
    # binaries
    '--add-binary=%s;Resources\\Scripts\\SQL' % os.path.join('Resources', 'Scripts', 'SQL', '*.backup'),
    '--add-binary=%s;Resources\\database\\bin\\runtime' % os.path.join('Resources', 'database', 'bin', 'runtime'),
    '--add-binary=%s;Resources\\mingw32\\bin' % os.path.join('Resources', 'mingw32', 'bin'),
    # libs
    '--add-data=%s;tinycss2' % os.path.dirname(collect_data_files('tinycss2')[0][0]),
    '--add-data=%s;.' % os.path.dirname(collect_data_files('weasyprint')[0][0]),
    '--add-data=%s;cairocffi' % os.path.dirname(collect_data_files('cairocffi')[0][0]),
    '--add-data=%s;pyphen\\dictionaries' % os.path.dirname(collect_data_files('pyphen')[0][0]),
    # images
    '--add-data=%s;Resources\\icons' % os.path.join('Resources', 'icons', '*.png'),
    '--add-data=%s;Resources\\Imagens' % os.path.join('Resources', 'Imagens', '*.png'),
    # text
    '--add-data=%s;Resources\\styles' % os.path.join('Resources', 'styles', '*.css'),
    '--add-data=%s;Resources\\html' %  os.path.join('Resources', 'html', '*.html'),
    '--add-data=%s;Resources\\html\\RelatorioPadrao' % os.path.join('Resources', 'html', 'RelatorioPadrao', '*.html'),
    '--add-data=%s;Resources\\misc' % os.path.join('Resources', 'misc'),
    '--icon=%s' % os.path.join('soad.ico'),
    '--console',
    os.path.join('SOAD.py')
])
