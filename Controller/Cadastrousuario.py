import logging

from PySide2.QtWidgets import QDialogButtonBox

from Controller.Componentes.CadastroPadrao import CadastroPadrao
from Controller.Componentes.StatusDialog import StatusDialog
from View.Ui_CadastroUsuario import Ui_CadastroUsuario


class CadastroUsuario(CadastroPadrao, Ui_CadastroUsuario):

    def __init__(self, db, window_list=None, parent=None, **kwargs):
        super(CadastroUsuario, self).__init__(parent, **kwargs)
        self.setupUi(self)
        self.db = db
        self.window_list = window_list

        self.pushButton_cadastrar.clicked.connect(self.novo_usuario)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.confirmar)
        self.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(self.cancelar)
        self.buttonBox.button(QDialogButtonBox.Cancel).setVisible(False)

        self.lineEdit_username.textChanged[str].connect(self.status_botao)
        self.lineEdit_password.textChanged[str].connect(self.status_botao)

        self.checkBox_ativo.setVisible(False)
        self.pushButton_localizar.setVisible(False)

        self.define_icones()
        self.posicionar_usuario(self.db.username)
        self.show()

    def posicionar_usuario(self, username):
        self.frame_username.setDisabled(True)
        self.lineEdit_username.setText(username)

    def novo_usuario(self):
        self.frame_menu.setDisabled(True)
        self.frame_username.setDisabled(False)
        self.lineEdit_username.clear()
        self.lineEdit_password.clear()

    def confirmar(self):
        if self.frame_username.isEnabled():
            self.cadastrar_usuario()
        else:
            self.alterar_senha()
        self.frame_menu.setDisabled(False)
        self.posicionar_usuario(self.lineEdit_username.text())

    def cancelar(self):
        self.close()

    def alterar_senha(self):
        sql = '''ALTER ROLE {username} PASSWORD '{password}';'''\
            .format(username=self.lineEdit_username.text()
                    , password=self.lineEdit_password.text())

        retorno = self.db.execute_sql(sql, as_dict=False)

        if retorno[0]:
            dialog = StatusDialog(
                status='OK'
                , mensagem='Senha alterada com sucesso!'
            )
        else:
            dialog = StatusDialog(
                status='ALERTA'
                , mensagem='Não foi possível editar o usuário.'
                , exception=str(retorno)
            )

        logging.debug('[CadastroUsuario] Retorno alteração senha: ' + str(retorno))
        dialog.exec()

    def cadastrar_usuario(self):

        sql = '''
CREATE ROLE {username} WITH
    LOGIN
    SUPERUSER
    NOCREATEDB
    NOCREATEROLE
    INHERIT
    NOREPLICATION
    CONNECTION LIMIT -1
    PASSWORD '{password}';

GRANT "NORMAL_USER" TO {username};
        '''.format(password=self.lineEdit_password.text(), username=self.lineEdit_username.text())

        retorno = self.db.execute_sql(sql, as_dict=False)

        if retorno[0]:
            dialog = StatusDialog(
                status='OK'
                , mensagem='Usuário cadastrado com sucesso!'
            )
        else:
            dialog = StatusDialog(
                status='ALERTA'
                , mensagem='Não foi possível cadastrar o usuário.'
                , exception=str(retorno)
            )
        logging.debug('[CadastroUsuario] Retorno cadastro: ' + str(retorno))
        dialog.exec()

    def status_botao(self):
        ativar = (len(self.lineEdit_username.text()) == 0) \
                 or (len(self.lineEdit_password.text()) == 0)
        self.buttonBox.button(QDialogButtonBox.Ok).setDisabled(ativar)
