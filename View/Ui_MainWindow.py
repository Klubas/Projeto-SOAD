# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\MainWindow.ui'
#
# Created: Mon Jul 15 20:58:42 2019
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1220, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(2560, 1080))
        MainWindow.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1211, 711))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gridLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 23))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1220, 21))
        self.menubar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menubar.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.menubar.setDefaultUp(False)
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
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionSair.setShortcutVisibleInContextMenu(True)
        self.actionSair.setObjectName("actionSair")
        self.actionPessoa = QtWidgets.QAction(MainWindow)
        self.actionPessoa.setObjectName("actionPessoa")
        self.actionProduto = QtWidgets.QAction(MainWindow)
        self.actionProduto.setObjectName("actionProduto")
        self.actionInsumo = QtWidgets.QAction(MainWindow)
        self.actionInsumo.setObjectName("actionInsumo")
        self.actionToners = QtWidgets.QAction(MainWindow)
        self.actionToners.setObjectName("actionToners")
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
        self.menuArquivo.addAction(self.actionSair)
        self.menuCadastros.addAction(self.actionPessoa)
        self.menuCadastros.addAction(self.actionProduto)
        self.menuCadastros.addAction(self.actionInsumo)
        self.menuCadastros.addAction(self.actionToners)
        self.menuVendas.addAction(self.actionNova_Venda)
        self.menuVendas.addAction(self.actionDevolucao)
        self.menuEstoque.addAction(self.actionRegistrar_compra)
        self.menuEstoque.addAction(self.actionDescarte_de_Material)
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
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
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
        self.actionProduto.setText(QtWidgets.QApplication.translate("MainWindow", "Produto", None, -1))
        self.actionProduto.setStatusTip(QtWidgets.QApplication.translate("MainWindow", "Cadastrar Produtos", None, -1))
        self.actionInsumo.setText(QtWidgets.QApplication.translate("MainWindow", "Insumo", None, -1))
        self.actionToners.setText(QtWidgets.QApplication.translate("MainWindow", "Toners", None, -1))
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

