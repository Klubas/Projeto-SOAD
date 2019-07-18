import json

from PySide2.QtWidgets import QWidget

from Controller.SairDialog import SairDialog
from Controller.StatusDialog import StatusDialog
from Model.Mercadoria import Mercadoria
from Model.Pedido import Pedido
from Model.Remanufatura import Remanufatura
from View.Ui_CadastroPedido import Ui_CadastroPedido


class CadastroPedido(QWidget, Ui_CadastroPedido):

    def __init__(self, db, window_list):
        super().__init__()
        self.setupUi(self)
        self.db = db
        self.window_list = window_list

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

        pedido = Pedido()
        item1 = Mercadoria()
        item2 = Mercadoria()
        item3 = Remanufatura()

        dados = {
            "tipo_pedido": "COMPRA",
            "pessoa_id": "",
            "observacao": "",
            "data_entrega": "",
            "Item": {
                "Mercadoria": {
                    "mercadoria_id": "",
                    "quantidade": "",
                    "valor_unitario": ""
                },
                "Remanufatura": {
                    "mercadoria_id": "",
                    "quantidade": "",
                    "valor_unitario": ""
                }
            }
        }
        return json.dumps(dados)

    def confirma(self):
        # pega os dados tela e envia pro banco
        dados_formatados = self.formata_dados()
        self.salva_dados(dados_formatados)

    def salva_dados(self, dados):
        # envia dicionario de dados pro banco utilizando uma procedure
        prc = self.db.call_procedure('prc_insert_pessoa', dados)
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
            event.accept()
        else:
            event.ignore()

