from Controller.Componentes.ListaPadrao.Filtro.FiltroPadrao import FiltroPadrao

from View.Componentes import Ui_FiltroEstoque

class FiltroEstoque(FiltroPadrao, Ui_FiltroEstoque):
    def __init__(self, parent=None):
        super(FiltroEstoque, self).__init__(parent)
