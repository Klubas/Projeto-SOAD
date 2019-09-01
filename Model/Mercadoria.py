
class Mercadoria:

    def __init__(self, descricao, marca, ativo=True, permite_venda=True, id_mercadoria=None):
        self.id_mercadoria = id_mercadoria
        self.descricao = descricao
        self.marca = marca
        self.ativo = ativo
        self.permite_venda = permite_venda

    def to_dict(self):
        pass