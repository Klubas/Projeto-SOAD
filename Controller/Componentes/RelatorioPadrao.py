from PySide2.QtWidgets import QWidget

from View.Componentes.Ui_RelatorioPadrao import Ui_RelatorioPadrao


class RelatorioPadrao(QWidget, Ui_RelatorioPadrao):
    """

    Classe para criar dinamicamente um relatório com base em uma tabela/view e as colunas desejadas

    Parametros:
    tabela::str - Tabela onde serão pegos os dados
    colunas::list(dict()) - Lista com dicionários contendo {"nome_coluna": "descricao"}


    """
    def __init__(self, db, window_list, parent, **kwargs):
        super(RelatorioPadrao, self).__init__()
        self.parent_window = self
        self.setupUi(self)
        self.window_list = window_list
        self.db = db

    def get_column_by_name(self, column):
        pass

    def select_all_rows(self):
        pass

    def set_columns(self):
        pass

    def set_data(self):
        pass

    def filter(self):
        pass