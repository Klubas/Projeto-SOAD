from PySide2.QtWidgets import QWidget
from View.Ui_CadastroPessoa import Ui_CadastroPessoa

from Controller.StatusDialog import StatusDialog


class CadastroPessoa(QWidget, Ui_CadastroPessoa):

    def __init__(self, db, window_list):
        super().__init__()
        self.setupUi(self)
        self.db = db
        self.window_list = window_list

    def confirma(self):
        # pega os dados tela e envia pro banco
        dados_formatados = self.formata_dados()
        self.salva_dados(dados_formatados)

    def cancela(self):
        # limpa a interface
        pass

    def carrega_dados(self):
        # pega os dados dos banco e popula a interface
        pass

    def formata_dados(self):
        # pega os dados da tela e popula um dicionario de dados
        dados = {
            "nome": "pedro",
            "email": "email@email",
            "telefone": "42999823030",
            "documento": "12345678901",
            "inscricao_estadual": "",
            "fantasia": ""
        }
        return dados

    def salva_dados(self, dados):
        # envia dicionario de dados pro banco utilizando uma procedure
        prc = self.db.call_procedure('prc_insert_pessoa', dados)
        print(prc[1])

    def __fechar(self):
        #verifica se tem alguma alteracao pendente e pergunta se deseja fechar
        return True

    def closeEvent(self, event): #PySide2.QtGui.QCloseEvent
        if self.__fechar():
            self.window_list.remove(self)
            event.accept()
        else:
            event.ignore()

