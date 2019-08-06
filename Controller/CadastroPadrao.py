from Controller.SairDialog import SairDialog
from Controller.StatusDialog import StatusDialog


class CadastroPadrao():

    def __init__(self):
        self.dados_formatados = None
        self.db = None

    def cancela(self):
        # limpa a interface
        pass

    def carrega_dados(self):
        # popula a interface
        pass

    def formata_dados_e_salva(self):
        # formata os dados da interface
        pass

    def salva_dados(self, dados):
        # envia dicionario de dados pro banco utilizando uma procedure
        prc = self.db.call_procedure('soad', dados["metodo"], dados)
        if not prc[0]:
            dialog = StatusDialog(status='ERRO', mensagem='Não foi possível salvar os dados.', exception=prc[1])
            dialog.exec()

    def confirma(self, dados):
        # pega os dados tela e envia pro banco
        self.salva_dados(dados)


    def fechar(self):
        #verifica se tem alguma alteracao pendente e pergunta se deseja fechar
        dialog = SairDialog()
        dialog.definir_mensagem("Tem certeza que deseja fechar? Todas as alterações serão perdidas.")
        return dialog.exec()

    # Override PySide2.QtGui.QCloseEvent
    def closeEvent(self, event):
        if self.fechar():
            self.window_list.remove(self)
            self.close()
            event.accept()
        else:
            event.ignore()

