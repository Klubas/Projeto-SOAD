import logging

class Mercadoria:

    def __init__(self, codigo, descricao=None, fabricante=None, valor_venda=None, ativo=True, permite_venda=True, mercadoria_id=None, **kwargs):
        self.mercadoria_id = '' if mercadoria_id is '' or mercadoria_id is None else int(mercadoria_id)
        self.codigo = str(codigo).upper()
        self.descricao = str(descricao)
        self.fabricante = str(fabricante).upper()
        self.ativo = bool(ativo)
        self.permite_venda = bool(permite_venda)
        self.valor_venda = float(valor_venda)
        self.tipo = str(kwargs.get('tipo_mercadoria'))

        if self.tipo == 'MERCADORIA':
            pass

        elif self.tipo == 'INSUMO':
            self.quantidade_embalagem = float(kwargs.get('quantidade_embalagem'))
            self.unidade_medida_id = int(kwargs.get('unidade_medida_id'))

        elif self.tipo == 'CASCO':
            self.insumo_id = int(kwargs.get('insumo_id'))
            self.quantidade_insumo = float(kwargs.get('quantidade_insumo'))
            self.unidade_medida_id = int(kwargs.get('unidade_medida_id'))

        else:
            logging.debug('[Mercadoria] Informado tipo de mercadoria inválido: ' + str(self.tipo))
            return

    def to_dict(self):
        mercadoria = dict()

        mercadoria['mercadoria_id'] = self.mercadoria_id
        mercadoria['codigo'] = self.codigo
        mercadoria['descricao'] = self.descricao
        mercadoria['marca'] = self.fabricante
        mercadoria['ativo'] = self.ativo
        mercadoria['permite_venda'] = self.permite_venda
        mercadoria['valor_venda'] = self.valor_venda
        mercadoria['tipo'] = self.tipo

        if self.tipo == 'INSUMO':
            mercadoria['quantidade'] = self.quantidade_embalagem
            mercadoria['unidade_medida_id'] = self.unidade_medida_id

        elif self.tipo == 'CASCO':
            mercadoria['insumo_id'] = self.insumo_id
            mercadoria['quantidade'] = self.quantidade_insumo
            mercadoria['unidade_medida_id'] = self.unidade_medida_id

        return mercadoria
