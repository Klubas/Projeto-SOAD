import os
import subprocess
from pathlib import Path


class Builder:
    """"
    Classe para gerar as classes das janelas criadas com qtCreator.
    Apenas irá rodar a ferramenta pyside2-uic

    Ex: pyside2-uic.exe MyWindow.ui -o MyWindow.py

    O caminho da ferramenta pode ser informado no construtor da classe

    """
    def __init__(self, py_uic_path='pyside2-uic', view="View", resources="Resources"):
        self.py_uic_path = py_uic_path
        self.view = view
        self.resources = resources

    def build_files(self, file_list):
        for file in file_list:
            print(file)
            new_file_path = file.split(os.sep)
            new_file_name = new_file_path[len(new_file_path)-1].split('.')
            print(new_file_name)
            new_file_name[len(new_file_name)-1] = ".py"
            print(new_file_name)
            new_file_name = new_file_name[0] + new_file_name[1]
            print(new_file_name)
            self.build_py_file(file, os.path.join(self.view, new_file_name))

    def build_files_from_folder(self, folder_path):
        self.build_files(self.get_files_from_folder(folder_path))

    def get_files_from_folder(self, folder_path):
        file_list = []        
        # cant have spaces in file name
        pathlist = Path(folder_path).glob('**' + os.sep + '*.ui')
        for path in pathlist:
            file_list.append(str(path))
        return file_list

    def build_py_file(self, uifile, pyfile):
        cmd = self.py_uic_path + " " + uifile + " -o " + pyfile
        print("cmd=" + cmd)
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        p.wait()


if __name__ == '__main__':

    import platform

    if platform.system() == 'Linux':
        pyuic="/opt/anaconda/bin/pyuic5"
    elif platform.system() == 'Windows':
        pyuic="pyside2-uic"

    pyuic = "pyside2-uic"
    builder = Builder(py_uic_path=pyuic, view=os.path.join("..", "View"), resources=os.path.join("..", "Resources"))
    builder.build_files_from_folder(os.path.join("..", "Resources"))