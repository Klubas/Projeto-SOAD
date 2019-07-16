import sys

from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from Controller.MainWindow import MainWindow
from Controller.StatusDialog import StatusDialog
from Model.DataBase import DataBase
from View.Ui_LoginDialog import Ui_LoginDialog


class LoginDialog(QDialog, Ui_LoginDialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox_servidor.addItem("localhost:5432")
        self.buttonBox.button(QDialogButtonBox.Ok).setDisabled(True)

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.login)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancelar)

        self.lineEdit_usuario.textChanged[str].connect(self.status_botao)
        self.lineEdit_senha.textChanged[str].connect(self.status_botao)

        if self.comboBox_servidor.count() == 1:
            self.verticalWidget_servidor.setVisible(False)


    def __setup_db_connection__(self):
        try:
            servidor = self.comboBox_servidor.currentText().split(':')

            return DataBase(
                username=self.lineEdit_usuario.text()
                , password=self.lineEdit_senha.text()
                , host=servidor[0]
                , port=int(servidor[1])
            )

        except Exception as e:
            dialog = StatusDialog()
            dialog.definir_mensagem("Não foi possível se conectar ao banco de dados.", e)
            dialog.exec()
            return False

    def login(self):

        if len(self.lineEdit_usuario.text()) == 0 \
                or len(self.lineEdit_senha.text()) == 0:

            dialog = StatusDialog()
            dialog.definir_mensagem("Por favor informe seu usuário e senha.")
            dialog.exec()

        else:

            try:
                db = self.__setup_db_connection__()

                if db:
                    w = MainWindow(db)
                    w.showMaximized()
                    self.close()
            except Exception as e:
                dialog = StatusDialog()
                dialog.definir_mensagem("Não foi possível se conectar ao banco de dados,", e)
                dialog.exec()

    def user_vazio(self):
        self.status_botao()

    def pass_vazio(self):
        self.status_botao()

    def status_botao(self):
        self.buttonBox.button(QDialogButtonBox.Ok).setDisabled(
            (len(self.lineEdit_usuario.text()) == 0) or (len(self.lineEdit_senha.text()) == 0)
        )

    def cancelar(self):
        self.closeEvent(event=QCloseEvent())

    def closeEvent(self, event):
        event.accept()
        sys.exit()
