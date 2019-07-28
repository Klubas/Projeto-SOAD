from PySide2.QtWidgets import QWidget

from Controller.SairDialog import SairDialog
from Controller.StatusDialog import StatusDialog
from Model.Mercadoria import Mercadoria
from Model.Remanufatura import Remanufatura
from View.Ui_CadastroPedido import Ui_CadastroPedido


class CadastroPedido(QWidget, Ui_CadastroPedido):

    def __init__(self, db=None, window_list=None, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.db = db
        self.window_list = window_list
        self.tipo_pedido = kwargs.get('tipo_pedido')

        # Componentes da interface
        # ...

    def cancela(self):
        # limpa a interface
        pass

    def carrega_dados(self):
        # pega os dados dos banco e popula a interface
        pass

    def formata_dados(self):
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

        return dados

    def confirma(self):
        # pega os dados tela e envia pro banco
        try:
            dados_formatados = self.formata_dados()
            self.salva_dados(dados_formatados)
        except Exception as e:
            dialog = StatusDialog()
            dialog.definir_mensagem("Não foi possível salvar o pedido.", e)
            dialog.exec()

    def salva_dados(self, dados):
        # envia dicionario de dados pro banco utilizando uma procedure
        prc = self.db.call_procedure('soad', dados["metodo"], dados)
        if not prc[0]:
            dialog = StatusDialog()
            dialog.definir_mensagem("\nSQL executada:\n" + prc[2], str(prc[1]))
            dialog.exec()

    def __fechar__(self):
        #verifica se tem alguma alteracao pendente e pergunta se deseja fechar
        dialog = SairDialog()
        dialog.definir_mensagem("Tem certeza que deseja fechar? Todas as alterações serão perdidas.")
        return dialog.exec()

    # Override PySide2.QtGui.QCloseEvent
    def closeEvent(self, event):
        if self.__fechar__():
            self.window_list.remove(self)
            self.close()
            event.accept()
        else:
            event.ignore()

