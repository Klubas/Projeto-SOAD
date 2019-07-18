import logging

from Model.Mercadoria import Mercadoria
from Model.Remanufatura import Remanufatura


class Pedido:

    def __init__(self, pessoa, tipo_pedido, data_entrega=None, situacao='CADASTRADO', data_cadastro=None, observacao=None):

        self.pessoa = pessoa
        self.tipo_pedido = tipo_pedido
        self.situacao = situacao
        self.data_entrega = data_entrega
        self.observacao = observacao
        self.data_cadastro = data_cadastro

        self.items = []

    def adicionar_item(self, item):
        if type(item) is Mercadoria or type(item) is Remanufatura:
            self.items.append(item)
        else:
            logging.debug("Tipo {", type(item).__name__, "} inválido.")

    def remover_item(self, item):
        self.items.remove(item)


