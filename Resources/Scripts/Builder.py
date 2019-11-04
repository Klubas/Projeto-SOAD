import os
import platform
import subprocess
import sys
from pathlib import Path


class Builder:

    """"
    Classe para gerar as classes das janelas criadas com qtCreator.
    Apenas irá rodar a ferramenta pyside2-uic

    Ex: pyside2-uic.exe MyWindow.ui -o MyWindow.py

    O caminho da ferramenta pode ser informado no constructor
    """

    def __init__(self, pyuic_path='pyside2-uic', py_folder="View", ui_folder="Resources"):
        self.py_uic_path = pyuic_path
        self.view = py_folder
        self.resources = ui_folder

        if platform.system() == 'Window':
            self.rm = 'del'
        else:
            self.rm = 'rm'

    def build_files(self, file_list):
        for file in file_list:
            new_file_path = file.split(os.sep)
            new_file_name = new_file_path[len(new_file_path)-1].split('.')
            new_file_name[len(new_file_name)-1] = ".py"
            new_file_name = "Ui_" + new_file_name[0] + new_file_name[1]
            self.build_py_file(file, self.view + os.sep + new_file_name)

    def build_files_from_folder(self, folder_path):
        cmd = self.rm + ' ' + self.view + os.sep + '*.py'
        print("Removendo aquivos .py")
        print(cmd)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.build_files(self.get_files_from_folder(folder_path))

    def get_files_from_folder(self, folder_path):
        file_list = []        
        # cant have spaces in file name
        pathlist = Path(folder_path).glob('.' + os.sep + '*.ui')
        for path in pathlist:
            file_list.append(str(path))
        return file_list

    def build_py_file(self, uifile, pyfile):
        cmd = self.py_uic_path + " " + uifile + " -o " + pyfile
        print(cmd)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.wait()


# Ordem dos argumento está errada não sei que bagunça eu fiz
# Builder pyuic ui_folder py_folder
if __name__ == '__main__':
    print(str(sys.argv))
    builder = Builder(
        pyuic_path=sys.argv[1],
        ui_folder=sys.argv[3],
        py_folder=sys.argv[2]
    )
    builder.build_files_from_folder(sys.argv[2])
