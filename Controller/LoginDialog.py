import logging
import os
import sys

from PySide2.QtGui import QCloseEvent, QImage, QPixmap
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from Controller.Componentes.StatusDialog import StatusDialog
from Controller.MainWindow import MainWindow
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

        # carrega e redimensiona a imagem
        logo = QImage(os.path.join("Resources", "Imagens", "logo.png")).smoothScaled(165, 165)

        self.label_logo.setPixmap(QPixmap.fromImage(logo))

        #dsv
        self.load_configs()
        self.lineEdit_usuario.setText('soadmin')
        self.lineEdit_senha.setText('soad2019')

    def __setup_db_connection__(self):
        try:
            servidor = self.comboBox_servidor.currentText().split(':')

            db = DataBase(
                username=self.lineEdit_usuario.text()
                , password=self.lineEdit_senha.text()
                , host=servidor[0]
                , port=int(servidor[1])
            )

            db.abrir_conexao()

            return db

        except Exception as e:
            logging.debug('[LoginDialog] ' + str(e))
            dialog = StatusDialog(
                status='ALERTA'
                , mensagem="Usuário ou senha inválidos."
                , exception=e
                , parent=self)
            print(e.__cause__)
            dialog.exec()
            return False

    def load_configs(self):
        logging.info('[LoginDialog] Implementar forma de carregar usuário e ambiente de um arquivo de texto.')

    def login(self):

        if len(self.lineEdit_usuario.text()) == 0 \
                or len(self.lineEdit_senha.text()) == 0:

            dialog = StatusDialog(mensagem="Por favor informe seu usuário e senha."
                                  , parent=self)
            dialog.exec()

        else:

            db = self.__setup_db_connection__()

            #db = True

            try:
                if db:
                    db.definir_schema('soad')
                    w = MainWindow(db)
                    w.showNormal()
                    self.hide()

            except Exception as e:
                logging.debug('[LoginDialog] ' + str(e))
                dialog = StatusDialog(status='ERRO'
                                      , mensagem="Erro ao abrir o sistema."
                                      , exception=e
                                      , parent=self)
                dialog.exec()

        return "Ok"

    def status_botao(self):
        self.buttonBox.button(QDialogButtonBox.Ok).setDisabled(
            (len(self.lineEdit_usuario.text()) == 0)
            or (len(self.lineEdit_senha.text()) == 0)
        )

    def cancelar(self):
        self.closeEvent(event=QCloseEvent())

    def closeEvent(self, event):
        event.accept()
        sys.exit()
