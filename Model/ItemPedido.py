import logging

class ItemPedido:
    def __init__(self, tipo, quantidade, valor_unitario, codigo='', item_pedido_id=None, **kwargs):
        self.item_pedido_id = None if item_pedido_id is None else int(item_pedido_id)
        self.tipo = str(tipo)
        self.descricao = str(kwargs.get('descricao'))
        self.codigo = str(codigo)
        self.quantidade = int(float(quantidade))
        self.valor_unitario = float(valor_unitario)
        self.valor_total = float(quantidade) * float(valor_unitario)

        self.alerta = kwargs.get('alerta') if 'alerta' in kwargs else ''

        if tipo == 'MERCADORIA':
            self.mercadoria_id = int(kwargs.get('mercadoria_id'))
            self.unidade_medida = str(kwargs.get('unidade_medida'))
            self.unidade_medida_id = int(kwargs.get('unidade_medida_id'))
            self.mercadoria = str(kwargs.get('mercadoria'))

        if tipo == 'REMANUFATURA':
            self.casco_id = int(kwargs.get('casco_id'))
            self.insumo_id = int(kwargs.get('insumo_id'))
            self.nova_remanufatura = bool(kwargs.get('nova_remanufatura'))

    def to_dict(self):
        if self.tipo == 'MERCADORIA':
            return {
                "item_pedido_id": self.item_pedido_id
                , "tipo_item": self.tipo
                , "mercadoria_id": self.mercadoria_id
                , "quantidade": self.quantidade
                , "unidade_medida_id": self.unidade_medida_id
                , "valor_unitario": self.valor_unitario
                , "codigo": self.codigo
                #, "valor_total": self.valor_total
            }

        elif self.tipo == 'REMANUFATURA':
            return {
                "item_pedido_id": self.item_pedido_id
                , "tipo_item": self.tipo
                , "casco_id": self.casco_id
                , 'insumo_id': self.insumo_id
                , "quantidade": self.quantidade
                , "valor_unitario": self.valor_unitario
                , "nova_remanufatura": self.nova_remanufatura
                , "codigo": self.codigo
                #, "valor_total": self.valor_total
            }

    def to_item_dict(self):
        try:
            return {
                "item_pedido_id": self.item_pedido_id
                , "tipo_item": self.tipo
                , "descricao": self.descricao
                , "codigo" : self.codigo
                , "quantidade": self.quantidade
                , "valor_unitario": self.valor_unitario
                , "valor_total": self.valor_total
                , "alerta": self.alerta
            }
        except Exception as e:
            logging.debug(e)
            return None
