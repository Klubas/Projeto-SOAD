from PySide2.QtWidgets import QWidget

from Controller.CadastroPadrao import CadastroPadrao
from Model.Mercadoria import Mercadoria
from Model.Remanufatura import Remanufatura
from View.Ui_CadastroPedido import Ui_CadastroPedido


class CadastroPedido(QWidget, CadastroPadrao, Ui_CadastroPedido):

    def __init__(self, db=None, window_list=None, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.db = db
        self.window_list = window_list
        self.tipo_pedido = kwargs.get('tipo')
        self.show()

        # Componentes da interface
        # ...

    def carrega_dados(self):
        # pega os dados dos banco e popula a interface
        pass

    def formata_dados_e_salva(self):
        # pega os dados da tela e popula um dicionario de dados
        #https://stackoverflow.com/questions/10252010/serializing-class-instance-to-json

        #pedido = Pedido()
        item1 = Mercadoria()
        item2 = Mercadoria()
        item3 = Remanufatura()

        dados = {
            "metodo": "prc_cadastro_pedido",
            "params": {
                "tipo_pedido": 'COMPRA',
                "pessoa_id": 134,
                "observacao": 'teste observacao',
                "data_entrega": '',
                "itens ": [
                    {
                        "tipo_item": 'MERCADORIA',
                        "mercadoria_id": 24,
                        "quantidade": 5,
                        "valor_unitario": 25.00,
                        "unidade_medida": 276
                    },
                    {
                        "tipo_item": 'MERCADORIA',
                        "mercadoria_id": 25,
                        "quantidade": 3,
                        "valor_unitario": 30.00,
                        "unidade_medida": 276
                    },
                    {
                        "tipo_item": 'REMANUFATURA',
                        "casco_id": 2,
                        "insumo_id": 7,
                        "quantidade": 3,
                        "valor_unitario": 15.00,
                        "nova_remanufatura": False
                    }
                ]
            }
        }

        self.confirma(dados)


