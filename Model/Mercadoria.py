
class Mercadoria:

    def __init__(self, descricao=None, marca=None, valor_unitario=None, ativo=True, permite_venda=True, id_mercadoria=None, **kwargs):
        self.id_mercadoria = id_mercadoria
        self.descricao = descricao
        self.marca = marca
        self.ativo = ativo
        self.permite_venda = permite_venda
        self.valor_unitario = valor_unitario
        self.tipo = kwargs.get('tipo_mercadoria')

        if self.tipo == 'MERCADORIA':
            pass

        elif self.tipo == 'INSUMO':
            pass

        elif self.tipo == 'CASCO':
            pass

    def to_dict(self):
        pass