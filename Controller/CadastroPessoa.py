from PySide2.QtWidgets import QWidget
from View.Ui_CadastroPessoa import Ui_CadastroPessoa


class CadastroPessoa(QWidget, Ui_CadastroPessoa):

    def __init__(self, db, window_list):
        super().__init__()
        self.setupUi(self)
        self.db = db
        self.window_list = window_list
        self.confirma()

    def carrega_dados(self):
        pass

    def formata_dados(self):
        dados = {
            "nome": "pedro",
            "email": "email@email",
            "telefone": "42999823030"
        }
        return dados

    def salva_dados(self, dados):
        i = self.db.insert('pessoa', dados)
        print(i)

    def confirma(self):
        dados_formatados = self.formata_dados()
        self.salva_dados(dados_formatados)

    def cancela(self):
        pass

    def __fechar(self):
        #verifica se tem alguma alteracao pendente e pergunta se deseja fechar
        return True

    def closeEvent(self, event): #PySide2.QtGui.QCloseEvent
        if self.__fechar():
            self.window_list.remove(self)
            event.accept()
        else:
            event.ignore()

