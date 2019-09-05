
class Mercadoria:

    def __init__(self, descricao=None, marca=None, valor_unitario=None, ativo=True, permite_venda=True, id_mercadoria=None):
        self.id_mercadoria = id_mercadoria
        self.descricao = descricao
        self.marca = marca
        self.ativo = ativo
        self.permite_venda = permite_venda
        self.valor_unitario = valor_unitario

    def to_dict(self):
        pass