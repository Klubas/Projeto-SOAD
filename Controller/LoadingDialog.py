from PySide2.QtWidgets import QDialog

from View.Componentes.Ui_LoadingDialog import Ui_LoadingDialog


class LoadingDialog(QDialog, Ui_LoadingDialog):

    def __init__(self, parent=None):
        super(LoadingDialog, self).__init__(parent)
        self.setupUi(self)

        num = 10000
        aux = num
        for i in range(num):
            print(i)
            self.progressBar.setValue(i)
            if self.progressBar.value() == num-1:
                self.progressBar.setInvertedAppearance(not self.progressBar.invertedAppearance())
                aux = 0
                i = 0

