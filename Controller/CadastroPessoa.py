from PySide2.QtWidgets import QWidget

from Controller.CadastroPadrao import CadastroPadrao
from View.Ui_CadastroPessoa import Ui_CadastroPessoa


class CadastroPessoa(QWidget, CadastroPadrao, Ui_CadastroPessoa):

    def __init__(self, db, window_list, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.db = db
        self.window_list = window_list
        self.show()

    def carrega_dados(self):
        # pega os dados dos banco e popula a interface
        pass

    def formata_dados_e_salva(self):
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

        self.confirma(dados)

