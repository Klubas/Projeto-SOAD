from Controller.SairDialog import SairDialog
from Controller.StatusDialog import StatusDialog


class CadastroPadrao:

    def __init__(self):
        self.dados_formatados = None
        self.db = None
        self.window_list = None

    def cancela(self):
        # limpa a interface
        pass

    def carrega_dados(self):
        # popula a interface
        pass

    def formata_dados_e_salva(self):
        # formata os dados da interface
        pass

    def confirma(self, dados):
        # pega os dados tela e envia pro banco
        prc = self.db.call_procedure('soad', dados["metodo"], dados)

        if prc[0]:
            dialog = StatusDialog(
                status='OK'
                , mensagem='Cadastro realizado com sucesso!'
            )

        else:
            dialog = StatusDialog(
                status='ERRO'
                , mensagem='Não foi possível salvar os dados.'
                , exception=str(prc[1]) + ' ' + str(prc[2])
            )

        dialog.exec()

        return prc[0]



    def fechar(self):
        #verifica se tem alguma alteracao pendente e pergunta se deseja fechar
        dialog = SairDialog()
        dialog.definir_mensagem("Tem certeza que deseja fechar? Todas as alterações serão perdidas.")
        fechar = dialog.exec()
        return fechar


