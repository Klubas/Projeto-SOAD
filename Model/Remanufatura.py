class Remanufatura:

    def __init__(self, casco_id, insumo_id, codigo='', valor_unitario=0, situacao='CADASTRADA', remanufatura_id=None):
        self.remanufatura_id = int(remanufatura_id)
        self.codigo = str(codigo)
        self.casco_id = int(casco_id)
        self.insumo_id = int(insumo_id)
        self.valor_unitario = float(valor_unitario)
        self.situacao = str(situacao)

    def to_dict(self):
        return {
            "remanufatura_id": self.remanufatura_id
            , "codigo": self.codigo
            , "casco_id": self.casco_id
            , "insumo_id": self.insumo_id
            , "valor_unitario": self.valor_unitario
            , "situacao": self.situacao
            , "log": ''
        }
