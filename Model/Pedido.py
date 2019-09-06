import logging

from Model.Mercadoria import Mercadoria
from Model.Remanufatura import Remanufatura


class Pedido:

    def __init__(self, tipo_pedido, pessoa_id=None, data_entrega=None, situacao='CADASTRADO', data_cadastro=None, observacao=None, pedido_id=None):

        self.pedido_id = None if pedido_id is None else int(pedido_id)
        self.pessoa_id = None if pessoa_id is None else int(pessoa_id)
        self.tipo_pedido = str(tipo_pedido)
        self.situacao = str(situacao)
        self.data_entrega = data_entrega
        self.observacao = str(observacao)
        self.data_cadastro = data_cadastro

        self.itens = [] #ItemPedido
        self.mercadorias = []
        self.remanufaturas = []

    def adicionar_item(self, *items):
        for item in items:

            if type(item) is Mercadoria:
                self.mercadorias.append(item)

            elif type(item) is Remanufatura:
                self.remanufaturas.append(item)

            else:
                logging.debug("Tipo {", type(item).__name__, ":", str(item), "} inválido.")

    def remover_item(self, item):
        if type(item) is Mercadoria:
            self.mercadorias.remove(item)

        elif type(item) is Remanufatura:
            self.remanufaturas.remove(item)

        else:
            logging.debug("Tipo {", type(item).__name__, ":", str(item), "} inválido.")

    def to_dict(self):
        itens = list(dict())
        if self.itens is not None:
            for i in self.itens:
                itens.append(i.to_dict())

        return {
            "pedido_id": self.pedido_id
            , "pessoa_id": self.pessoa_id
            , "tipo_pedido": self.tipo_pedido
            #, "situacao": self.situacao
            , "data_entrega": self.data_entrega
            , "observacao": self.observacao
            , "data_cadastro": self.data_cadastro
            , "itens": itens
        }

