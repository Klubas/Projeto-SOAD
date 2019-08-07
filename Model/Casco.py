from Model.Mercadoria import Mercadoria


class Casco(Mercadoria):

    def __init__(self, quantidade_insumo):
        super(Mercadoria, self).__init__()
        self.quantidade_insumo = quantidade_insumo

