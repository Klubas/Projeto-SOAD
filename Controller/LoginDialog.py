import json
import logging
import os
import sys

from PySide2.QtGui import QCloseEvent, QImage, QPixmap, QIcon
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from Controller.Componentes.StatusDialog import StatusDialog
from Controller.MainWindow import MainWindow
from Model.DataBase import DataBase
from SOAD import resource_path
from View.Ui_LoginDialog import Ui_LoginDialog


class LoginDialog(QDialog, Ui_LoginDialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox_servidor.addItem("localhost:5432")
        self.comboBox_servidor.addItem("10.0.2.2:5432")
        self.buttonBox.button(QDialogButtonBox.Ok).setDisabled(True)
        self.main = None
        self.restored = False

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.login)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancelar)

        self.lineEdit_usuario.textChanged[str].connect(self.status_botao)
        self.lineEdit_senha.textChanged[str].connect(self.status_botao)

        if self.comboBox_servidor.count() == 1:
            self.verticalGroupBox_servidor.setVisible(False)

        icon_path = os.path.join("Resources", "Imagens", "soad.png")
        icon_image = QImage(resource_path(icon_path)).smoothScaled(135, 135)
        self.icon = QIcon(resource_path(icon_path))
        self.setWindowIcon(self.icon)

        self.label_logo.setPixmap(QPixmap.fromImage(icon_image))

        self.saved_config(action='load')

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

    def saved_config(self, action):
        action = action.upper()
        if action == 'SAVE':

            data = {
                "hostname": self.comboBox_servidor.currentText()
                , "username": self.lineEdit_usuario.text()
                , "password": self.lineEdit_senha.text()
                , "restored": "1"
            }

            try:
                with open('.credencial.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
            except Exception as e:
                logging.debug('[LoginDialog] Não foi possível salvar o arquivo de configuração.')

                logging.debug('Exception> ' + str(e))

        elif action == 'LOAD':
            try:
                with open('.credencial.json') as json_file:
                    data = json.load(json_file)
                    self.comboBox_servidor.setCurrentText(data['hostname'])
                    self.lineEdit_usuario.setText(data['username'])
                    self.lineEdit_senha.setText(data['password'])
                    self.restored = data['restored']

            except Exception as e:
                logging.debug('[LoginDialog] Não foi possível abrir o arquivo de configuração.')
                from Resources.Scripts.Installer import Installer
                #installer = Installer("Resources\database\\bin\\runtime",
                #                      "Resources\\Scripts\\SQL\\dump.backup",
                #                      "soad2019")
                installer = Installer("/usr/bin",
                                      "Resources/Scripts/SQL/dump.backup",
                                      "soad2019")
                installer.create_database()
                logging.debug('Exception> ' + str(e))

    def login(self):

        if len(self.lineEdit_usuario.text()) == 0 \
                or len(self.lineEdit_senha.text()) == 0:

            dialog = StatusDialog(mensagem="Por favor informe seu usuário e senha."
                                  , parent=self)
            dialog.exec()

        else:

            db = self.__setup_db_connection__()

            try:
                if db:
                    if self.main is None:
                        db.definir_schema('soad')
                        self.main = MainWindow(db, self)
                        self.main.setWindowIcon(self.icon)
                    self.main.showMaximized()
                    self.saved_config(action='save')
                    self.hide()

            except Exception as e:
                logging.debug('[LoginDialog] ' + str(e))
                self.saved_config(action='save')
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
