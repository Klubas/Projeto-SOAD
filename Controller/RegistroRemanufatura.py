from PySide2.QtWidgets import QWidget

from View.Ui_RegistroRemanufatura import Ui_RegistroRemanufatura


class RegistroRemanufatura(QWidget, Ui_RegistroRemanufatura):

    def __init__(self, db=None, window_list=None, **kwargs):
        #super(CadastroPadrao, self).__init__()
        super(RegistroRemanufatura, self).__init__()
        ### Padrão
        self.parent_window = self
        self.setupUi(self)

        self.db = db
        self.window_list = window_list
        self.modo_edicao = False

        # Conectar botões

        self.show()

    def buscar_mercadoria(self):
        # Busca insumo e casco e preenche os campos
        # insumo
        # casco
        pass

    def gerar_remanufaturas(self):
        # Chamado pelo botão ok
        # Grava remanufatura no banco
        # Posiciona na lista o(s) retornos(s)
        pass

    def limpar_formulario(self):
        # limpa os campos de cadastro da remanufatura
        pass

    def limpar_lista(self):
        # remove todas as remanufaturas da lista (excluir do banco)
        pass

    def realizar_remanufaturas(self):
        # chama o procedimento de realizar remanufatura para
        # todas as remanufaturas selecionadas na lista
        pass

    def selecionar_todas(self):
        # seleciona todas as remanufaturas com situacao == 'CADASTRADA'
        pass

    def esvaziar_embalagem(self):
        # Marca lote sendo utilizado para recargas como vazio e busca o próximo
        pass