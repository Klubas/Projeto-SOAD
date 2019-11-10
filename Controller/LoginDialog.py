import json
import logging
import os
import sys

from PySide2.QtGui import QCloseEvent, QImage, QPixmap, QIcon
from PySide2.QtWidgets import QDialog, QDialogButtonBox

from Controller.Componentes.StatusDialog import StatusDialog
from Controller.MainWindow import MainWindow
from Model.DataBase import DataBase
from View.Ui_LoginDialog import Ui_LoginDialog


class LoginDialog(QDialog, Ui_LoginDialog):

    def __init__(self):
        super(LoginDialog, self).__init__()
        self.setupUi(self)

        self.comboBox_servidor.setEditable(True)
        self.buttonBox.button(QDialogButtonBox.Ok).setDisabled(True)
        self.buttonBox.button(QDialogButtonBox.Save).setDisabled(True)

        from pathlib import Path
        self.home_dir = str(Path.home())

        self.main = None
        self.restored = False

        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.login)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancelar)
        self.buttonBox.button(QDialogButtonBox.Save).clicked.connect(lambda: self.saved_config('RESTORE'))

        self.buttonBox.button(QDialogButtonBox.Save).setVisible(False)
        self.buttonBox.button(QDialogButtonBox.Save).setText('Config DB')

        self.lineEdit_usuario.textChanged[str].connect(self.status_botao)
        self.lineEdit_senha.textChanged[str].connect(self.status_botao)

        icon_path = os.path.join("Resources", "Imagens", "soad.png")
        icon_image = QImage(icon_path).smoothScaled(115, 115)
        self.icon = QIcon(icon_path)

        self.setWindowIcon(self.icon)

        self.label_logo.setPixmap(QPixmap.fromImage(icon_image))

        self.translate_ui()

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
        file_path = os.path.join(self.home_dir, '.credencial.json')
        if action == 'SAVE':

            data = {
                "hostname": self.comboBox_servidor.currentText()
                , "username": self.lineEdit_usuario.text()
                #, "password": self.lineEdit_senha.text()
                , "restored": "1"
            }

            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
            except Exception as e:
                logging.debug('[LoginDialog] Não foi possível salvar o arquivo de configuração.')

                logging.debug('Exception> ' + str(e))

        elif action == 'RESTORE':

            import platform
            from Resources.Scripts.Installer import Installer

            self.lineEdit_usuario.setText('soadmin')
            self.lineEdit_usuario.setDisabled(True)

            servidor = self.comboBox_servidor.currentText().split(':')

            logging.info('[LoginDialog] Restaurando banco de dados...')

            installer = Installer(
                postgresfolder=os.path.join("Resources", "database", "bin", "runtime")
                , dump_file=os.path.join("Resources", "Scripts", "SQL", "dump_schema.backup")
                , username=self.lineEdit_usuario.text()
                , password=self.lineEdit_senha.text()
                , host=servidor[0]
                , port=int(servidor[1])
                , _os=platform.system()
                , override_pg_path=True
            )
            installer.create_database()

            self.lineEdit_usuario.setDisabled(False)
            self.buttonBox.button(QDialogButtonBox.Save).setDisabled(True)

        elif action == 'LOAD':
            try:
                with open(file_path) as json_file:
                    try:
                        data = json.load(json_file)
                        self.comboBox_servidor.setCurrentText(data['hostname'])
                        self.lineEdit_usuario.setText(data['username'])
                        #self.lineEdit_senha.setText(data['password'])
                        self.restored = data['restored']
                        self.verticalGroupBox_servidor.setVisible(False)
                    except Exception:
                        logging.debug('[LoginDialog] Não foi possível ler o arquivo de configuração...')

            except FileNotFoundError as e:
                logging.debug('[LoginDialog] Não foi possível abrir o arquivo de configuração...')
                logging.debug('Exception> ' + str(e))
                self.buttonBox.button(QDialogButtonBox.Save).setVisible(True)
                self.comboBox_servidor.addItem("localhost:5432")
                self.comboBox_servidor.addItem("localhost:5433")
                self.comboBox_servidor.addItem("10.0.2.2:5432")
                self.comboBox_servidor.addItem("10.0.2.2:5433")

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

        ativar = (len(self.lineEdit_usuario.text()) == 0) \
                 or (len(self.lineEdit_senha.text()) == 0)

        self.buttonBox.button(QDialogButtonBox.Ok).setDisabled(ativar)
        self.buttonBox.button(QDialogButtonBox.Save).setDisabled(ativar)

    def cancelar(self):
        self.closeEvent(event=QCloseEvent())

    def closeEvent(self, event):
        event.accept()
        sys.exit()

    def translate_ui(self):
        self.buttonBox.button(QDialogButtonBox.Ok).setText('Login')
        self.buttonBox.button(QDialogButtonBox.Cancel).setText('Cancelar')
