# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources\UI\MainWindow.ui',
# licensing of 'Resources\UI\MainWindow.ui' applies.
#
# Created: Sun Sep 15 19:04:15 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1420, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1420, 768))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setFocusPolicy(QtCore.Qt.TabFocus)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame_venda = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_venda.sizePolicy().hasHeightForWidth())
        self.frame_venda.setSizePolicy(sizePolicy)
        self.frame_venda.setObjectName("frame_venda")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_venda)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_venda = QtWidgets.QPushButton(self.frame_venda)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_venda.sizePolicy().hasHeightForWidth())
        self.pushButton_venda.setSizePolicy(sizePolicy)
        self.pushButton_venda.setMaximumSize(QtCore.QSize(693, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_venda.setFont(font)
        self.pushButton_venda.setAutoRepeatDelay(298)
        self.pushButton_venda.setFlat(True)
        self.pushButton_venda.setObjectName("pushButton_venda")
        self.verticalLayout.addWidget(self.pushButton_venda)
        self.pushButton_lista_vendas = QtWidgets.QPushButton(self.frame_venda)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_lista_vendas.setFont(font)
        self.pushButton_lista_vendas.setAutoDefault(True)
        self.pushButton_lista_vendas.setDefault(False)
        self.pushButton_lista_vendas.setFlat(True)
        self.pushButton_lista_vendas.setObjectName("pushButton_lista_vendas")
        self.verticalLayout.addWidget(self.pushButton_lista_vendas)
        self.gridLayout.addWidget(self.frame_venda, 0, 0, 1, 1)
        self.frame_compra = QtWidgets.QFrame(self.centralwidget)
        self.frame_compra.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_compra.sizePolicy().hasHeightForWidth())
        self.frame_compra.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 203, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 203, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 203, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 203, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frame_compra.setPalette(palette)
        self.frame_compra.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_compra.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_compra.setObjectName("frame_compra")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_compra)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_compra = QtWidgets.QPushButton(self.frame_compra)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_compra.sizePolicy().hasHeightForWidth())
        self.pushButton_compra.setSizePolicy(sizePolicy)
        self.pushButton_compra.setMaximumSize(QtCore.QSize(693, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_compra.setFont(font)
        self.pushButton_compra.setAutoRepeatDelay(298)
        self.pushButton_compra.setFlat(True)
        self.pushButton_compra.setObjectName("pushButton_compra")
        self.verticalLayout_5.addWidget(self.pushButton_compra)
        self.pushButton_lista_compras = QtWidgets.QPushButton(self.frame_compra)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_lista_compras.setFont(font)
        self.pushButton_lista_compras.setAutoDefault(True)
        self.pushButton_lista_compras.setDefault(False)
        self.pushButton_lista_compras.setFlat(True)
        self.pushButton_lista_compras.setObjectName("pushButton_lista_compras")
        self.verticalLayout_5.addWidget(self.pushButton_lista_compras)
        self.pushButton_remanufatura = QtWidgets.QPushButton(self.frame_compra)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_remanufatura.setFont(font)
        self.pushButton_remanufatura.setAutoDefault(True)
        self.pushButton_remanufatura.setDefault(False)
        self.pushButton_remanufatura.setFlat(True)
        self.pushButton_remanufatura.setObjectName("pushButton_remanufatura")
        self.verticalLayout_5.addWidget(self.pushButton_remanufatura)
        self.gridLayout.addWidget(self.frame_compra, 0, 1, 1, 1)
        self.frame_mercadoria = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_mercadoria.sizePolicy().hasHeightForWidth())
        self.frame_mercadoria.setSizePolicy(sizePolicy)
        self.frame_mercadoria.setObjectName("frame_mercadoria")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_mercadoria)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_mercadoria = QtWidgets.QPushButton(self.frame_mercadoria)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_mercadoria.sizePolicy().hasHeightForWidth())
        self.pushButton_mercadoria.setSizePolicy(sizePolicy)
        self.pushButton_mercadoria.setMaximumSize(QtCore.QSize(693, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_mercadoria.setFont(font)
        self.pushButton_mercadoria.setAutoRepeatDelay(298)
        self.pushButton_mercadoria.setFlat(True)
        self.pushButton_mercadoria.setObjectName("pushButton_mercadoria")
        self.verticalLayout_4.addWidget(self.pushButton_mercadoria)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_mercadoria)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setAutoDefault(True)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_mercadoria)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoDefault(True)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.gridLayout.addWidget(self.frame_mercadoria, 1, 1, 1, 1)
        self.frame_pessoa = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_pessoa.sizePolicy().hasHeightForWidth())
        self.frame_pessoa.setSizePolicy(sizePolicy)
        self.frame_pessoa.setObjectName("frame_pessoa")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_pessoa)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_pessoa = QtWidgets.QPushButton(self.frame_pessoa)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_pessoa.sizePolicy().hasHeightForWidth())
        self.pushButton_pessoa.setSizePolicy(sizePolicy)
        self.pushButton_pessoa.setMaximumSize(QtCore.QSize(693, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_pessoa.setFont(font)
        self.pushButton_pessoa.setAutoRepeatDelay(298)
        self.pushButton_pessoa.setFlat(True)
        self.pushButton_pessoa.setObjectName("pushButton_pessoa")
        self.verticalLayout_3.addWidget(self.pushButton_pessoa)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_pessoa)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setAutoDefault(True)
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_pessoa)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoDefault(True)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.gridLayout.addWidget(self.frame_pessoa, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label_background = QtWidgets.QLabel(self.centralwidget)
        self.label_background.setObjectName("label_background")
        self.verticalLayout_2.addWidget(self.label_background)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1420, 21))
        self.menubar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menubar.setInputMethodHints(QtCore.Qt.ImhPreferLatin|QtCore.Qt.ImhPreferUppercase)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setInputMethodHints(QtCore.Qt.ImhNone)
        self.menuArquivo.setSeparatorsCollapsible(False)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuCadastros = QtWidgets.QMenu(self.menubar)
        self.menuCadastros.setObjectName("menuCadastros")
        self.menuVendas = QtWidgets.QMenu(self.menubar)
        self.menuVendas.setObjectName("menuVendas")
        self.menuEstoque = QtWidgets.QMenu(self.menubar)
        self.menuEstoque.setObjectName("menuEstoque")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        self.menuRelat_rios = QtWidgets.QMenu(self.menubar)
        self.menuRelat_rios.setObjectName("menuRelat_rios")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.statusbar.setFont(font)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionSair.setShortcutVisibleInContextMenu(True)
        self.actionSair.setObjectName("actionSair")
        self.actionPessoa = QtWidgets.QAction(MainWindow)
        self.actionPessoa.setObjectName("actionPessoa")
        self.actionMercadoria = QtWidgets.QAction(MainWindow)
        self.actionMercadoria.setObjectName("actionMercadoria")
        self.actionInsumo = QtWidgets.QAction(MainWindow)
        self.actionInsumo.setObjectName("actionInsumo")
        self.actionCasco = QtWidgets.QAction(MainWindow)
        self.actionCasco.setObjectName("actionCasco")
        self.actionSobre = QtWidgets.QAction(MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.actionNova_Venda = QtWidgets.QAction(MainWindow)
        self.actionNova_Venda.setObjectName("actionNova_Venda")
        self.actionCancelar_venda = QtWidgets.QAction(MainWindow)
        self.actionCancelar_venda.setObjectName("actionCancelar_venda")
        self.actionRegistrar_compra = QtWidgets.QAction(MainWindow)
        self.actionRegistrar_compra.setObjectName("actionRegistrar_compra")
        self.actionCancelar_compra = QtWidgets.QAction(MainWindow)
        self.actionCancelar_compra.setObjectName("actionCancelar_compra")
        self.actionDescarte_de_Material = QtWidgets.QAction(MainWindow)
        self.actionDescarte_de_Material.setObjectName("actionDescarte_de_Material")
        self.actionDevolucao = QtWidgets.QAction(MainWindow)
        self.actionDevolucao.setObjectName("actionDevolucao")
        self.actionProdutos_em_Estoque = QtWidgets.QAction(MainWindow)
        self.actionProdutos_em_Estoque.setObjectName("actionProdutos_em_Estoque")
        self.actionVendas = QtWidgets.QAction(MainWindow)
        self.actionVendas.setObjectName("actionVendas")
        self.actionCompras = QtWidgets.QAction(MainWindow)
        self.actionCompras.setObjectName("actionCompras")
        self.actionDescartes = QtWidgets.QAction(MainWindow)
        self.actionDescartes.setObjectName("actionDescartes")
        self.actionReconectar = QtWidgets.QAction(MainWindow)
        self.actionReconectar.setObjectName("actionReconectar")
        self.actionNova_Remanufatura = QtWidgets.QAction(MainWindow)
        self.actionNova_Remanufatura.setCheckable(True)
        self.actionNova_Remanufatura.setEnabled(False)
        self.actionNova_Remanufatura.setVisible(False)
        self.actionNova_Remanufatura.setObjectName("actionNova_Remanufatura")
        self.actionRegistrar_Remanufaturas = QtWidgets.QAction(MainWindow)
        self.actionRegistrar_Remanufaturas.setObjectName("actionRegistrar_Remanufaturas")
        self.menuArquivo.addAction(self.actionSair)
        self.menuArquivo.addAction(self.actionReconectar)
        self.menuCadastros.addAction(self.actionPessoa)
        self.menuCadastros.addAction(self.actionMercadoria)
        self.menuCadastros.addAction(self.actionInsumo)
        self.menuCadastros.addAction(self.actionCasco)
        self.menuVendas.addAction(self.actionNova_Venda)
        self.menuVendas.addAction(self.actionDevolucao)
        self.menuEstoque.addAction(self.actionRegistrar_compra)
        self.menuEstoque.addAction(self.actionDescarte_de_Material)
        self.menuEstoque.addAction(self.actionNova_Remanufatura)
        self.menuEstoque.addAction(self.actionRegistrar_Remanufaturas)
        self.menuAjuda.addAction(self.actionSobre)
        self.menuRelat_rios.addAction(self.actionProdutos_em_Estoque)
        self.menuRelat_rios.addAction(self.actionVendas)
        self.menuRelat_rios.addAction(self.actionCompras)
        self.menuRelat_rios.addAction(self.actionDescartes)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuCadastros.menuAction())
        self.menubar.addAction(self.menuVendas.menuAction())
        self.menubar.addAction(self.menuEstoque.menuAction())
        self.menubar.addAction(self.menuRelat_rios.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "SOAD ", None, -1))
        self.pushButton_venda.setText(QtWidgets.QApplication.translate("MainWindow", "Registro de Venda", None, -1))
        self.pushButton_lista_vendas.setText(QtWidgets.QApplication.translate("MainWindow", "Lista de Vendas", None, -1))
        self.pushButton_compra.setText(QtWidgets.QApplication.translate("MainWindow", "Registro de Compras", None, -1))
        self.pushButton_lista_compras.setText(QtWidgets.QApplication.translate("MainWindow", "Lista de Compras", None, -1))
        self.pushButton_remanufatura.setText(QtWidgets.QApplication.translate("MainWindow", "Realizar Remanufatura", None, -1))
        self.pushButton_mercadoria.setText(QtWidgets.QApplication.translate("MainWindow", "Cadastro de Mercadoria", None, -1))
        self.pushButton_6.setText(QtWidgets.QApplication.translate("MainWindow", "Lista de Mercadorias", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "Estoque", None, -1))
        self.pushButton_pessoa.setText(QtWidgets.QApplication.translate("MainWindow", "Cadastro de Pessoa", None, -1))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("MainWindow", "Lista de Cliente", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "Lista de Fornecedores", None, -1))
        self.label_background.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))
        self.menuArquivo.setTitle(QtWidgets.QApplication.translate("MainWindow", "Arquivo", None, -1))
        self.menuCadastros.setTitle(QtWidgets.QApplication.translate("MainWindow", "Cadastros", None, -1))
        self.menuVendas.setTitle(QtWidgets.QApplication.translate("MainWindow", "Vendas", None, -1))
        self.menuEstoque.setTitle(QtWidgets.QApplication.translate("MainWindow", "Estoque", None, -1))
        self.menuAjuda.setTitle(QtWidgets.QApplication.translate("MainWindow", "Ajuda", None, -1))
        self.menuRelat_rios.setTitle(QtWidgets.QApplication.translate("MainWindow", "Relatórios", None, -1))
        self.actionSair.setText(QtWidgets.QApplication.translate("MainWindow", "Sair", None, -1))
        self.actionSair.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Sair do sistema", None, -1))
        self.actionSair.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.actionPessoa.setText(QtWidgets.QApplication.translate("MainWindow", "Pessoa", None, -1))
        self.actionPessoa.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Cadastrar Pessoas", None, -1))
        self.actionMercadoria.setText(QtWidgets.QApplication.translate("MainWindow", "Mercadoria", None, -1))
        self.actionMercadoria.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Cadastrar Produtos", None, -1))
        self.actionInsumo.setText(QtWidgets.QApplication.translate("MainWindow", "Insumo", None, -1))
        self.actionCasco.setText(QtWidgets.QApplication.translate("MainWindow", "Casco", None, -1))
        self.actionSobre.setText(QtWidgets.QApplication.translate("MainWindow", "Sobre", None, -1))
        self.actionSobre.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Sobre o sistema", None, -1))
        self.actionNova_Venda.setText(QtWidgets.QApplication.translate("MainWindow", "Nova Venda", None, -1))
        self.actionNova_Venda.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Cadastrar Novas Vendas", None, -1))
        self.actionCancelar_venda.setText(QtWidgets.QApplication.translate("MainWindow", "Cancelar venda", None, -1))
        self.actionRegistrar_compra.setText(QtWidgets.QApplication.translate("MainWindow", "Registrar compra", None, -1))
        self.actionRegistrar_compra.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Registrar uma compra no estoque", None, -1))
        self.actionCancelar_compra.setText(QtWidgets.QApplication.translate("MainWindow", "Cancelar compra", None, -1))
        self.actionDescarte_de_Material.setText(QtWidgets.QApplication.translate("MainWindow", "Descarte de Material", None, -1))
        self.actionDescarte_de_Material.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Descartar materiais", None, -1))
        self.actionDevolucao.setText(QtWidgets.QApplication.translate("MainWindow", "Devolução", None, -1))
        self.actionDevolucao.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Realizar uma devolução", None, -1))
        self.actionProdutos_em_Estoque.setText(QtWidgets.QApplication.translate("MainWindow", "Produtos em Estoque", None, -1))
        self.actionVendas.setText(QtWidgets.QApplication.translate("MainWindow", "Vendas", None, -1))
        self.actionCompras.setText(QtWidgets.QApplication.translate("MainWindow", "Compras", None, -1))
        self.actionDescartes.setText(QtWidgets.QApplication.translate("MainWindow", "Descartes", None, -1))
        self.actionReconectar.setText(QtWidgets.QApplication.translate("MainWindow", "Reconectar", None, -1))
        self.actionNova_Remanufatura.setText(QtWidgets.QApplication.translate("MainWindow", "Nova Remanufatura", None, -1))
        self.actionRegistrar_Remanufaturas.setText(QtWidgets.QApplication.translate("MainWindow", "Registrar Remanufaturas", None, -1))

