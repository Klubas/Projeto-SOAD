from PySide2.QtWidgets import QWidget

from Controller.SairDialog import SairDialog
from Controller.StatusDialog import StatusDialog
from View.Ui_CadastroPessoa import Ui_CadastroPessoa


class CadastroPessoa(QWidget, Ui_CadastroPessoa):

    def __init__(self, db, window_list, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.db = db
        self.window_list = window_list

    def cancela(self):
        # limpa a interface
        pass

    def carrega_dados(self):
        # pega os dados dos banco e popula a interface
        pass

    def formata_dados(self):
        # pega os dados da tela e popula um dicionario de dados
        dados = {
            "metodo": "prc_insert_pessoa",
            "params": {
                "nome": "pedro",
                "email": "email@email",
                "telefone": "42999823030",
                "documento": "987654321",
                "inscricao_estadual": "",
                "fantasia": ""
            }
        }
        return dados

    def confirma(self):
        # pega os dados tela e envia pro banco
        dados_formatados = self.formata_dados()
        self.salva_dados(dados_formatados)

    def salva_dados(self, dados):
        # envia dicionario de dados pro banco utilizando uma procedure
        prc = self.db.call_procedure('soad', 'prc_insert_pessoa', dados)
        if not prc[0]:
            dialog = StatusDialog()
            dialog.definir_mensagem("\nSQL executada:\n" + prc[2], str(prc[1]))
            dialog.exec()

    def __fechar(self):
        #verifica se tem alguma alteracao pendente e pergunta se deseja fechar
        dialog = SairDialog()
        dialog.definir_mensagem("Tem certeza que deseja fechar? Todas as alterações serão perdidas.")
        return dialog.exec()

    def closeEvent(self, event): #PySide2.QtGui.QCloseEvent
        if self.__fechar():
            self.window_list.remove(self)
            event.accept()
        else:
            event.ignore()

