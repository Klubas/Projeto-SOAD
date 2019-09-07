import logging

from Controller.Componentes.ConfirmDialog import ConfirmDialog
from Controller.Componentes.LocalizarDialog import LocalizarDialog
from Controller.Componentes.StatusDialog import StatusDialog


class CadastroPadrao:
    """
    Classe padrão para cadastros
    Alguns métodos devem ser reimplementados chamando super(ClasseFilha, self).metodo()

    Métodos:

    void cadastrar()
    void editar()
    void excluir()
    int localizar()
    void limpar_dados()
    void receber_dados(dict())
    void cancela()
    str/int valida_obrigatorios()
    bool confirma()
    bool fechar
    bool nao_esta_em_modo_edicao()
    bool esta_em_modo_edicao()
    void entrar_modo_edicao()
    void sair_modo_edicao()
    void define_permite_editar()

    """

    def __init__(self):
        self.dados_formatados = None
        self.db = None
        self.window_list = None

        # Configuracoes
        self.localizar_campos = None
        self.dados = None
        self.modo_edicao = False
        self.novo_cadastro = True
        self.view_busca = None
        self.colunas_busca = None
        self.campos_obrigatorios = dict()

        # QFrame
        self.frame_menu = None
        self.frame_buttons = None

        self.lineEdit_id = None
        self.pushButton_editar = None
        self.pushButton_excluir = None

        # QWidget
        self.frame_contents = None
        self.parent_window = None

    # Reimplementar chamando super
    def cadastrar(self):
        self.entrar_modo_edicao()
        self.novo_cadastro = True
        self.lineEdit_id.setText('')

    # Reimplementar chamando super
    def editar(self):
        self.entrar_modo_edicao()
        self.novo_cadastro = False

    # Reimplementar chamando super
    def excluir(self):
        if self.nao_esta_em_modo_edicao():
            return self.db.call_procedure(self.db.schema, self.dados)[0]
        else:
            return False

    def localizar(self, parent=None):

        localizar = LocalizarDialog(
            db=self.db
            , campos=self.localizar_campos
            , tabela=self.view_busca
            , colunas=self.colunas_busca
            , parent=parent
        )

        localizar.retorno_dados.connect(self.receber_dados)
        modal = localizar.exec()

        return modal

    # Reimplementar chamando super
    def limpar_dados(self):
        # limpa todos os campos
        #self.frame_menu.setDisabled(True)
        #self.frame_contents.setDisabled(False)
        #self.frame_buttons.setDisabled(False)
        self.lineEdit_id.setText('')

    def receber_dados(self, dados):
        self.dados = dados

    # Reimplementar chamando super e limpar_dados
    def cancela(self):
        if self.modo_edicao:
            dialog = ConfirmDialog()
            dialog.definir_mensagem("Tem certeza que deseja cancelar? Todas as alterações serão perdidas.")
            cancelar = dialog.exec()

        else:
            return False

        if cancelar:
            self.sair_modo_edicao()

        return cancelar

    # Reimplementar chamando super
    def valida_obrigatorios(self):
        if len(self.campos_obrigatorios) > 0:
            for campo, valor in self.campos_obrigatorios.items():
                try:
                    if valor.text() == '':
                        dialog = StatusDialog(
                            status='ALERTA'
                            , mensagem='O campo ' + campo + ' é obrigatório.'
                            , parent=self.parent_window
                        )
                        return dialog.exec()
                except AttributeError as attr:
                    if valor.currentText() == '':
                        dialog = StatusDialog(
                            status='ALERTA'
                            , mensagem='O campo ' + campo + ' é obrigatório.'
                            , parent=self.parent_window
                        )
                        return dialog.exec()
                except Exception as e:
                    dialog = StatusDialog(
                        status='ERRO'
                        , mensagem='Erro ao verificar campos obrigatórios.'
                        , exception=e
                        , parent=self.parent_window
                    )
                    return dialog.exec()

        return 'OK'

    # Reimplementar chamando super
    def confirma(self):
        if self.esta_em_modo_edicao():

            if self.valida_obrigatorios() != 'OK':
                return False

            # pega os dados tela e envia pro banco
            prc = self.db.call_procedure(self.db.schema, self.dados)

            if prc[0]:

                if self.novo_cadastro:
                    acao = 'realizado'
                else:
                    acao = 'atualizado'

                dialog = StatusDialog(
                    status='OK'
                    , mensagem='Cadastro ' + acao + ' com sucesso!'
                    , parent=self.parent_window
                )

                self.sair_modo_edicao()

            else:
                dialog = StatusDialog(
                    status='ERRO'
                    , mensagem='Não foi possível salvar os dados.'
                    , exception=str(prc[1]) + ' ' + str(prc[2])
                    , parent=self.parent_window
                )
                self.modo_edicao = True

            # Finaliza e retorna
            dialog.exec()
            logging.debug('prc=' + str(prc[1][0]))
            return prc[0], prc[1][0]

    # Não precisa ser reimplementado na tela
    #verifica se tem alguma alteracao pendente e pergunta se deseja fechar
    def fechar(self):
        if self.modo_edicao:
            dialog = ConfirmDialog()
            dialog.definir_mensagem("Tem certeza que deseja fechar? Todas as alterações serão perdidas.")
            fechar = dialog.exec()
        else:
            fechar = True

        return fechar

    def nao_esta_em_modo_edicao(self):
        if self.modo_edicao:
            dialog = StatusDialog(
                status='ERRO'
                , mensagem='A interface está em modo de edição!'
                , parent=self.parent_window
            )
            return dialog.exec()
        else:
            logging.info('Não está em modo de edição.')
            return True

    def esta_em_modo_edicao(self):
        if not self.modo_edicao:
            dialog = StatusDialog(
                status='ERRO'
                , mensagem='A interface não está em modo de edição!'
                , parent=self.parent_window
            )
            return dialog.exec()
        else:
            logging.info('Está em modo de edição.')
            return True

    def entrar_modo_edicao(self):
        if self.nao_esta_em_modo_edicao():
            self.modo_edicao = True
            self.frame_menu.setDisabled(True)
            self.frame_buttons.setDisabled(False)
            self.frame_contents.setDisabled(False)
            logging.info('Entrando em modo edição')


    def sair_modo_edicao(self):
        if self.esta_em_modo_edicao():
            self.modo_edicao = False
            self.frame_menu.setDisabled(False)
            self.frame_buttons.setDisabled(True)
            self.frame_contents.setDisabled(True)
            logging.info('Saindo do modo edição')

    def define_permite_editar(self):
        logging.info('Editar: ' + str(self.lineEdit_id.text() == ''))
        self.pushButton_editar.setDisabled(self.lineEdit_id.text() == '')
        self.pushButton_excluir.setDisabled(self.lineEdit_id.text() == '')
