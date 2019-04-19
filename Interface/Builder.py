import subprocess
from pathlib import Path

""""
Classe para gerar as classes das janelas criadas com qtCreator.
Apenas irá rodar a ferramenta pyside2-uic

Ex: pyside2-uic.exe MyWindow.ui -o MyWindow.py

O caminho da ferramenta pode ser informado no construtor da classe

"""

class Builder:
    def __init__(self, py_uic_path='pyside2-uic'):
        #super.__init__(self)
        self.py_uic_path = py_uic_path

    def build_files(self, file_list=None):
        if not file_list:
            return

        for file in file_list:
            self.build_py_file(file, file+".py")

    def build_files_from_folder(self, folder_path):
        self.build_files(self.get_files_from_folder(folder_path))

    def get_files_from_folder(self, folder_path):
        file_list = []
        pathlist = Path(folder_path).glob('**/*.ui')
        for path in pathlist:
            file_list.append(str(path))
        return file_list

    def build_py_file(self, uifile, pyfile):
        cmd = self.py_uic_path + " " + uifile + " -o " + pyfile
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.wait()
