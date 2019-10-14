from View.Ui_EstornoPedido import Ui_EstornoPedido


class EstornoPedido(Ui_EstornoPedido):

    def __init__(self, db=None, window_list=None, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.db = db
        self.window_list = window_list

        self.show()