import logging
import os

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QWidget

from Controller.Componentes.ConfirmDialog import ConfirmDialog
from Controller.Componentes.LocalizarDialog import LocalizarDialog
from Controller.Componentes.StatusDialog import StatusDialog


class CadastroPadrao(QWidget):
    """
    Classe padrão para cadastros
    Alguns métodos devem ser reimplementados chamando super(ClasseFilha, self).metodo()

    Métodos:

    void cadastrar()
    void editar()
    void excluir()
    int localizar()
    void limpar_dados()
    void receber_dados(dict())
    void cancela()
    str', 'int valida_obrigatorios()
    bool confirma()
    bool fechar
    bool nao_esta_em_modo_edicao()
    bool esta_em_modo_edicao()
    void entrar_modo_edicao()
    void sair_modo_edicao()
    void define_permite_editar()

    """

    def __init__(self, parent=None, **kwargs):
        super(CadastroPadrao, self).__init__(parent)

        self.dados_formatados = None
        self.db = None
        self.window_list = None

        self.dialog = kwargs.get('dialog')

        if self.dialog:
            self.setWindowFlags(Qt.Dialog)
        else:
            self.setWindowFlags(Qt.Window)

        # Configuracoes
        self.localizar_campos = None
        self.dados = None
        self.modo_edicao = False
        self.novo_cadastro = True
        self.view_busca = None
        self.colunas_busca = None
        self.filtro_adicional = None
        self.campos_obrigatorios = dict()

        # QFrame
        self.frame_menu = None
        self.frame_buttons = None

        self.lineEdit_id = None
        self.pushButton_cadastrar = None
        self.pushButton_editar = None
        self.pushButton_excluir = None
        self.pushButton_localizar = None

        # QWidget
        self.frame_contents = None
        self.parent_window = None

        self.icone_insert = None
        self.icone_update = None
        self.icone_delete = None
        self.icone_find = None

        #self.define_icones()

    def define_icones(self):
        self.icone_insert = QIcon(os.path.join('Resources', 'icons', 'insert.png'))
        self.icone_update = QIcon(os.path.join('Resources', 'icons', 'update.png'))
        self.icone_delete = QIcon(os.path.join('Resources', 'icons', 'delete.png'))
        self.icone_find = QIcon(os.path.join('Resources', 'icons', 'find.png'))

        self.pushButton_cadastrar.setIcon(self.icone_insert)
        self.pushButton_editar.setIcon(self.icone_update)
        self.pushButton_excluir.setIcon(self.icone_delete)
        self.pushButton_localizar.setIcon(self.icone_find)

    # Reimplementar chamando super
    def cadastrar(self):
        self.entrar_modo_edicao()
        self.novo_cadastro = True
        self.lineEdit_id.setText('')

    # Reimplementar chamando super
    def editar(self):
        self.entrar_modo_edicao()
        self.novo_cadastro = False

    # Reimplementar chamando super
    def excluir(self, validar=True):
        if self.nao_esta_em_modo_edicao():

            if validar:
                dialog = ConfirmDialog()
                dialog.definir_mensagem("Tem certeza que deseja realizar a exclusão desse registro?")
                cancelar = dialog.exec()
            else:
                cancelar = True

            return self.db.call_procedure(self.db.schema, self.dados) if cancelar else False
        else:
            return False

    def localizar(self, parent=None):

        localizar = LocalizarDialog(
            db=self.db
            , campos=self.localizar_campos
            , tabela=self.view_busca
            , colunas=self.colunas_busca
            , filtro=self.filtro_adicional
            , parent=parent
        )

        localizar.retorno_dados.connect(self.receber_dados)
        modal = localizar.exec()

        return modal if modal > 0 else None

    # Reimplementar chamando super
    def limpar_dados(self):
        # limpa todos os campos
        self.lineEdit_id.setText('')

    def receber_dados(self, dados):
        self.dados = dados

    # Reimplementar chamando super e limpar_dados
    def cancela(self):
        if self.modo_edicao:
            dialog = ConfirmDialog()
            dialog.definir_mensagem("Tem certeza que deseja cancelar? Todas as alterações serão perdidas.")
            cancelar = dialog.exec()

            if cancelar:
                self.sair_modo_edicao()
                return True

        return False

    # Reimplementar chamando super
    def valida_obrigatorios(self):
        if len(self.campos_obrigatorios) > 0:
            vermelho = "247, 192, 188"
            style = "background: rgb({});".format(vermelho)
            print(style)
            for campo, valor in self.campos_obrigatorios.items():
                valor.setStyleSheet(
                    "QLineEdit { background: white; }"
                )
                try:
                    if valor.text() == '':
                        valor.setStyleSheet(style)
                        dialog = StatusDialog(
                            status='ALERTA'
                            , mensagem='O campo ' + campo + ' é obrigatório.'
                            , parent=self.parent_window
                        )
                        #return dialog.exec()
                        return False
                except AttributeError as attr:
                    if valor.currentText() == '':
                        valor.setStyleSheet(style)
                        dialog = StatusDialog(
                            status='ALERTA'
                            , mensagem='O campo ' + campo + ' é obrigatório.'
                            , parent=self.parent_window
                        )
                        #return dialog.exec()
                        return False
                except Exception as e:
                    dialog = StatusDialog(
                        status='ERRO'
                        , mensagem='Erro ao verificar campos obrigatórios.'
                        , exception=e
                        , parent=self.parent_window
                    )
                    return dialog.exec()

        return 'OK'

    def marca_obrigatorios(self):
        if len(self.campos_obrigatorios) > 0:
            for campo, valor in self.campos_obrigatorios.items():
                valor.setStyleSheet("border: 0.5px solid red")

    def limpa_obrigatorios(self):
        if len(self.campos_obrigatorios) > 0:
            for campo, valor in self.campos_obrigatorios.items():
                valor.setStyleSheet("border: 0px solid black")
                valor.setStyleSheet("QLineEdit { background: white; }")

    # Reimplementar chamando super
    def confirma(self):
        if self.esta_em_modo_edicao():

            if self.valida_obrigatorios() != 'OK':
                return False

            # pega os dados tela e envia pro banco
            prc = self.db.call_procedure(self.db.schema, self.dados)

            if prc[0]:

                if self.novo_cadastro:
                    acao = 'realizado'
                else:
                    acao = 'atualizado'

                dialog = StatusDialog(
                    status='OK'
                    , mensagem='Cadastro ' + acao + ' com sucesso!'
                    , parent=self.parent_window
                )
                self.sair_modo_edicao()

            else:
                dialog = StatusDialog(
                    status='ALERTA'
                    , mensagem='Não foi possível salvar os dados.'
                    , exception=prc
                    , parent=self.parent_window
                )
                self.modo_edicao = True

            dialog.exec()
            return prc[0], prc[1][0]

    # Não deve ser reimplementado na tela
    #verifica se tem alguma alteracao pendente e pergunta se deseja fechar
    def fechar(self):
        if self.modo_edicao:
            dialog = ConfirmDialog()
            dialog.definir_mensagem("Tem certeza que deseja fechar? Todas as alterações serão perdidas.")
            fechar = dialog.exec()
        else:
            fechar = True

        return fechar

    def nao_esta_em_modo_edicao(self):
        if self.modo_edicao:
            dialog = StatusDialog(
                status='ERRO'
                , mensagem='A interface está em modo de edição!'
                , parent=self.parent_window
            )
            return dialog.exec()
        else:
            logging.info('[CadastroPadrao] Não está em modo de edição.')
            return True

    def esta_em_modo_edicao(self):
        if not self.modo_edicao:
            dialog = StatusDialog(
                status='ERRO'
                , mensagem='A interface não está em modo de edição!'
                , parent=self.parent_window
            )
            return dialog.exec()
        else:
            logging.info('[CadastroPadrao] Está em modo de edição.')
            return True

    def entrar_modo_edicao(self):
        if self.nao_esta_em_modo_edicao():
            self.modo_edicao = True
            self.frame_menu.setDisabled(True)
            self.frame_buttons.setDisabled(False)
            self.frame_contents.setDisabled(False)
            self.marca_obrigatorios()
            logging.info('[CadastroPadrao] Entrando em modo edição')

    def sair_modo_edicao(self):
        if self.esta_em_modo_edicao():
            self.modo_edicao = False
            self.frame_menu.setDisabled(False)
            self.frame_buttons.setDisabled(True)
            self.frame_contents.setDisabled(True)
            self.limpa_obrigatorios()
            self.define_permite_editar()
            logging.info('[CadastroPadrao] Saindo do modo edição')

    def entrar_modo_visualizacao(self):
        if self.nao_esta_em_modo_edicao():
            self.modo_edicao = False
            self.frame_menu.setDisabled(False)
            self.frame_buttons.setDisabled(True)
            self.frame_contents.setDisabled(False)

    def define_permite_editar(self):
        logging.info('[CadastroPadrao] Editar: ' + str(self.lineEdit_id.text() != ''))
        self.pushButton_editar.setDisabled(self.lineEdit_id.text() == '')
        self.pushButton_excluir.setDisabled(self.lineEdit_id.text() == '')

    def formatar_numero(self, numero):
        numero = str(numero)
        if len(numero.split(',')) > 0:
            return numero.replace(',', '.')
        elif len(numero.split('.')) > 0:
            return numero.replace('.', ',')

    # Override PySide2.QtGui.QCloseEvent
    def closeEvent(self, event):
        if self.fechar():
            if not self.dialog:
                self.window_list.remove(self)
            event.accept()
        else:
            event.ignore()

