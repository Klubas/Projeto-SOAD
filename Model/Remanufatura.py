class Remanufatura:

    def __init__(self, casco, insumo, valor_unitario=0, situacao='CADASTRADA', id_remanufatura=None):
        self.id_remanufatura = id_remanufatura
        self.casco = casco
        self.insumo = insumo
        self.valor_unitario = valor_unitario
        self.situacao = situacao
