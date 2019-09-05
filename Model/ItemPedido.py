
class ItemPedido:
    def __init__(self, tipo, quantidade, valor_unitario, valor_total=None, item_pedido_id=None, **kwargs):
        self.item_pedido_id = item_pedido_id
        self.tipo = tipo
        self.descricao = kwargs.get('descricao')
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.valor_total = float(quantidade) * float(valor_unitario)


        if tipo == 'MERCADORIA':
            self.mercadoria_id = kwargs.get('mercadoria_id')
            self.unidade_medida = kwargs.get('unidade_medida')
            self.unidade_medida_id = kwargs.get('unidade_medida_id')
            self.mercadoria = kwargs.get('mercadoria')

        if tipo == 'REMANUFATURA':
            self.casco_id = kwargs.get('casco_id')
            self.insumo_id = kwargs.get('insumo_id')
            self.nova_remanufatura = kwargs.get('nova_remanufatura')

    def to_dict(self):
        if self.tipo == 'MERCADORIA':
            return {
                "item_pedido_id": self.item_pedido_id
                , "tipo": self.tipo
                , "mercadoria_id": self.mercadoria_id
                , "quantidade": self.quantidade
                , "unidade_medida_id": self.unidade_medida_id
                , "valor_unitario": self.valor_unitario
                #, "valor_total": self.valor_total
            }

        elif self.tipo == 'REMANUFATURA':
            return {
                #"item_pedido_id": self.item_pedido_id
                "tipo_item": self.tipo
                , "casco_id": self.casco_id
                , 'insumo_id': self.insumo_id
                , "quantidade": self.quantidade
                , "valor_unitario": self.valor_unitario
                , "nova_remanufatura": self.nova_remanufatura
                #, "valor_total": self.valor_total
            }

    def to_item_dict(self):

        return {
            "item_pedido_id": self.item_pedido_id
            , "tipo": self.tipo
            , "descricao": self.descricao
            , "quantidade": self.quantidade
            , "valor_unitario": self.valor_unitario
            , "valor_total": self.valor_total
        }