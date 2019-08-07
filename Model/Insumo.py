from Model.Mercadoria import Mercadoria


class Insumo(Mercadoria):

    def __init__(self, quantidade_embalagem, id_unidade_medida):
        super(Mercadoria, self).__init__()
        self.quantidade_embalagem = quantidade_embalagem
        self.id_unidade_medida = id_unidade_medida

