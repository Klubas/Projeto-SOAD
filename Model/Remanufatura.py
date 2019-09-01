class Remanufatura:

    def __init__(self, casco_id, insumo_id, valor_unitario=0, situacao='CADASTRADA', remanufatura_id=None):
        self.remanufatura_id = remanufatura_id
        self.casco_id = casco_id
        self.insumo_id = insumo_id
        self.valor_unitario = valor_unitario
        self.situacao = situacao

    def to_dict(self):
        pass