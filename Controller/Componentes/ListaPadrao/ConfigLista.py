
from datetime import datetime

from Controller.Componentes.StatusDialog import StatusDialog


class ConfigLista:
    """
    descricao::str
    tabela::str - Tabela onde serão pegos os dados
    colunas::list(dict()) - Lista com dicionários contendo {"nome_coluna": ("descricao", tipo)}
    data::list(dict()) - Lista de dicionários, onde cada item da lista é uma linha da tabelas
        e cada atributo do dicionário é referente a uma coluna (referenciado com a chave de colunas::list(dict()))
    interface::QWidget
    filtro::QDialog


    """
    def __init__(self):
        pass

    def get_tipo_relatorio(self, tipo):
        tipo = tipo.upper()

        relatorio = None
        if tipo == 'VENDA':

            from Controller.CadastroPedido import CadastroPedido

            relatorio = {
            "descricao": "Lista de pedidos de venda",
            "tabela": 'vw_pedido_venda',
            "colunas": {
                "id_pedido": ("Número", int),
                "situacao": ("Situação", str),
                "data_cadastro": ("Data do Pedido", datetime),
                "data_entrega": ("Data para Entrega", datetime),
                "valor_total_mercadorias": ("Total das mercadorias", float),
                "valor_total_remanufaturas": ("Total das remanufaturas", float),
                "pessoa": ("Cliente", str),
                "documento": ("Documento", str),
                "inscricao_estadual": ("Inscrição Estadual", str),
                "fantasia": ("Nome Fantasia", str),
                "email": ("Email", str),
                "telefone": ("Telefone", str),
                "observacao": ("Observações", str),
            }
            , "interface": CadastroPedido
            , "filtro": None
        }

        if tipo == 'COMPRA':

            from Controller.CadastroPedido import CadastroPedido

            relatorio = {
                "descricao": "Lista de pedidos de compra",
                "tabela": 'vw_pedido_compra'
                , "colunas": {
                        "id_pedido": ("Número", int),
                        "situacao": ("Situação", str),
                        "data_cadastro": ("Data do Pedido", datetime),
                        "data_entrega": ("Data para Entrega", datetime),
                        "valor_total_mercadorias": ("Valor Total", float),
                        "pessoa": ("Cliente", str),
                        "documento": ("Documento", str),
                        "inscricao_estadual": ("Inscrição Estadual", str),
                        "fantasia": ("Nome Fantasia", str),
                        "email": ("Email", str),
                        "telefone": ("Telefone", str),
                        "observacao": ("Observações", str),
                    }
                , "interface": CadastroPedido
                , "filtro": None
            }

        if tipo == 'ESTOQUE':

            from Controller.Componentes.ListaPadrao.Filtro.FiltrosLista.FiltroEstoque import FiltroEstoque

            relatorio = {
                "descricao": "Lista de itens em estoque",
                "tabela": 'vw_item_lote'
                , "colunas": {
                    "id_lote": ("Lote", int),
                    "id_item_lote": ("Item", int),
                    "valor_unitario": ("Valor unitário", float),
                    "quantidade_item": ("Quantidade", float),
                    "data_validade": ("Data validade", datetime),
                    "lote_fabricante": ("Lote do fabricante", str),
                    #"id_mercadoria": ("ID Mercadoria", int, False)
                    "codigo_mercadoria": ("Código mercadoria", str),
                    "descricao": ("Mercadoria", str),
                    "marca": ("Fabricante", str),
                    "tipo_mercadoria": ("Classificação", str),
                    "unidade_medida": ("Unidade Medida", str),
                    "data_cadastro": ("Data entrada", datetime),
                    "id_pedido_entrada": ("Número da Compra", int),
                    "nome_pessoa_entrada": ("Fornecedor", str),
                    "documento_pessoa_entrada": ("CNPJ Fornecedor", str),
                    "data_retirada": ("Data saída", datetime),
                    "id_pedido_saida": ("Número Venda", int),
                    "motivo_retirada": ("Motivo saída", str),
                    "aberto": ("Item aberto", bool),
                    "data_abertura": ("Data Abertura", datetime),
                    "motivo_abertura": ("Motivo Abertura", str),
                    "observacao": ("Observação", str)
                }
                , "interface": None
                , "filtro": FiltroEstoque
            }

        if tipo == 'REMANUFATURA':
            from Controller.RegistroRemanufatura import RegistroRemanufatura
            relatorio = {
                "descricao": "Lista de remanufaturas",
                "tabela": "vw_remanufatura"
                , "colunas": {
                    "id_remanufatura": ("Remanufatura", int),
                    "codigo": ("Código da remanufatura", str),
                    "data_cadastro": ("Data cadastro", datetime),
                    "situacao_remanufatura": ("Situação da remanufatura", str),
                    "casco": ("Casco", str),
                    "insumo": ("Insumo", str),
                    "id_item_lote": ("Item lote do insumo", int),
                    "colorido": ("Colorido", bool),
                    "valor_unitario": ("Valor", float),
                    "id_pedido": ("Pedido", int),
                    "situacao_pedido": ("Situação do pedido", str),
                    "pessoa": ("Cliente", str),
                    "documento": ("CPF/CNPJ Cliente", str)
                }
                , "interface": RegistroRemanufatura
                , "filtro": None
            }

        if tipo == 'MERCADORIA':

            from Controller.CadastroMercadoria import CadastroMercadoria

            relatorio = {
                "descricao": "Lista de mercadorias",
                "tabela": 'vw_mercadoria'
                , "colunas": {
                    "id_mercadoria": ("ID Mercadoria", int, False)
                    , "codigo": ("Código mercadoria", str)
                    , "tipo_mercadoria": ("Classificação", str)
                    , "descricao": ("Descrição", str)
                    , "marca": ("Fabricante", str)
                    , "data_cadastro": ("Data cadastro", datetime)
                    , "ativo": ("Ativo", bool)
                    , "permite_venda": ("Permite venda", bool)
                    , "valor_venda": ("Valor de venda", float)
                    , "quantidade_embalagem": ("Quantidade embalagem", float)
                    , "abreviacao": ("Unidade medida embalagem", str)
                    , "colorido": ("Colorido", bool)
                    , "quantidade_insumo":("Quantidade insumo", float)
                    , "unidade_medida_insumo": ("Unidade de medida casco", str)
                    , "insumo_casco": ("Insumo casco", str)
                }
                , "interface": CadastroMercadoria
                , "filtro": None
            }

        if tipo == 'CLIENTE':

            from Controller.CadastroPessoa import CadastroPessoa

            relatorio = {
                "descricao": "Lista de clientes",
                "tabela": "vw_pessoa_cliente"
                , "colunas": {
                    "id_pessoa": ("ID", int, False)
                    , "nome": ("Nome", str)
                    , "documento": ("CPF/CNPJ", str)
                    , "fantasia": ("Nome Fantasia", str)
                    , "email": ("Email", str)
                    , "telefone": ("Telefone", str)
                    , "inscricao_estadual": ("Inscrição Estadual", str)
                    , "municipio": ("Município", str)
                    , "sigla_uf": ("UF", str)
                    , "logradouro": ("Logradouro", str)
                    , "bairro": ("Bairro", str)
                    , "numero": ("Número", str)
                    , "cep": ("CEP", str)
                    , "complemento": ("Complemento", str)
                    , "tipo_endereco": ("Tipo de endereço", str)
                    , "pais": ("País", str)
                }
                , "interface": CadastroPessoa
                , "filtro": None
            }

        if tipo == 'FORNECEDOR':

            from Controller.CadastroPessoa import CadastroPessoa

            relatorio = {
                "descricao": "Lista de fornecedores",
                "tabela": "vw_pessoa_fornecedor"
                , "colunas": {
                    "id_pessoa": ("ID", int, False)
                    , "nome": ("Nome", str)
                    , "documento": ("CPF/CNPJ", str)
                    , "fantasia": ("Nome Fantasia", str)
                    , "email": ("Email", str)
                    , "telefone": ("Telefone", str)
                    , "inscricao_estadual": ("Inscrição Estadual", str)
                    , "municipio": ("Município", str)
                    , "sigla_uf": ("UF", str)
                    , "logradouro": ("Logradouro", str)
                    , "bairro": ("Bairro", str)
                    , "numero": ("Número", str)
                    , "cep": ("CEP", str)
                    , "complemento": ("Complemento", str)
                    , "tipo_endereco": ("Tipo de endereço", str)
                    , "pais": ("País", str)
                }
                , "interface": CadastroPessoa
                , "filtro": None
            }

        if not relatorio:
            dialog = StatusDialog(
                status='ERRO'
                , mensagem="O tipo de relatório " + tipo + " não é válido."
                , parent=self)
            dialog.exec()

        return relatorio
