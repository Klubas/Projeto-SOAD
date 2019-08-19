from Controller.Componentes.LocalizarDialog import LocalizarDialog
from Controller.Componentes.SairDialog import SairDialog
from Controller.Componentes.StatusDialog import StatusDialog


class CadastroPadrao:

    def __init__(self):
        self.dados_formatados = None
        self.db = None
        self.window_list = None

        # Configuracoes
        self.localizar_campos = None
        self.dados = None
        self.modo_edicao = False
        self.view_busca = None
        self.colunas_busca = None

        # QFrame
        self.frame_menu = None
        self.frame_buttons = None

        # QWidget
        self.widget = None

    # Reimplementar chamando super
    def cadastrar(self):
        if self.modo_edicao:
            dialog = StatusDialog(
                status='ERRO'
                , mensagem='A interface está em modo de edição!'
            )
            return dialog.exec()
        else:
            self.frame_menu.setDisabled(True)
            self.frame_buttons.setDisabled(False)
            self.widget.setDisabled(False)
            self.modo_edicao = True

    # Reimplementar chamando super
    def editar(self):
        if self.modo_edicao:
            dialog = StatusDialog(
                status='ERRO'
                , mensagem='A interface está em modo de edição!'
            )
            return dialog.exec()
        else:
            self.frame_menu.setDisabled(True)
            self.frame_buttons.setDisabled(False)
            self.widget.setDisabled(False)
            self.modo_edicao = True

    # Reimplementar chamando super
    def excluir(self):
        if self.modo_edicao:
            dialog = StatusDialog(
                status='ERRO'
                , mensagem='A interface está em modo de edição!'
            )
            return dialog.exec()
        else:
            self.frame_menu.setDisabled(False)
            self.widget.setDisabled(True)
            self.frame_buttons.setDisabled(True)

    # todo: implementar botão localizar
    def localizar(self):
        # abre modal para informar ID do pedido
        localizar = LocalizarDialog(
            db=self.db
            , campos=self.localizar_campos
            , tabela=self.view_busca
            , colunas=self.colunas_busca
        )

        if localizar.exec() != 0:
            # posiciona dados na interface
            pass
        else:
            # Não faz nada
            pass


    # Reimplementar chamando super
    def limpar_dados(self):
        # limpa todos os campos
        self.frame_menu.setDisabled(False)
        self.widget.setDisabled(True)
        self.frame_buttons.setDisabled(True)

    # Reimplementar chamando super e limpar_dados
    def cancela(self):
        if not self.modo_edicao:
            dialog = StatusDialog(
                status='ERRO'
                , mensagem='A interface não está em modo de edição!'
            )
            return dialog.exec()
        else:
            self.limpar_dados()
            self.modo_edicao = False
            pass

    # Reimplementar chamando super
    def valida_obrigatorios(self):
        # Validar campos obrigatórios da interface
        pass

    # Reimplementar chamando super
    def confirma(self):
        if not self.modo_edicao:
            dialog = StatusDialog(
                status='ERRO'
                , mensagem='A interface não está em modo de edição!'
            )
            return dialog.exec()
        else:

            # verifica campos obrigatórios
            if not self.valida_obrigatorios():
                dialog = StatusDialog(
                    status='ALERTA',
                    mensagem='Por favor preencha todos os campos obrigatórios.'
                )
                return dialog.exec()

            # pega os dados tela e envia pro banco
            prc = self.db.call_procedure(self.db.schema, self.dados)

            if prc[0]:
                dialog = StatusDialog(
                    status='OK'
                    , mensagem='Cadastro realizado com sucesso!'
                )
                self.modo_edicao = False
            else:
                dialog = StatusDialog(
                    status='ERRO'
                    , mensagem='Não foi possível salvar os dados.'
                    , exception=str(prc[1]) + ' ' + str(prc[2])
                )
                self.modo_edicao = True

            dialog.exec()

            return prc[0]

    # Não precisa ser reimplementado na tela
    def fechar(self):
        #verifica se tem alguma alteracao pendente e pergunta se deseja fechar
        fechar = True
        if self.modo_edicao:
            dialog = SairDialog()
            dialog.definir_mensagem("Tem certeza que deseja fechar? Todas as alterações serão perdidas.")
            fechar = dialog.exec()

        return fechar

    def verifica_modo_edicao(self):
        pass

