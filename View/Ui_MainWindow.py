# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\MainWindow.ui'
#
# Created: Wed Jul 24 02:19:23 2019
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1418, 768)
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
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(0, 10, 1401, 770))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridWidget_2 = QtWidgets.QWidget(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget_2.sizePolicy().hasHeightForWidth())
        self.gridWidget_2.setSizePolicy(sizePolicy)
        self.gridWidget_2.setMinimumSize(QtCore.QSize(1024, 768))
        self.gridWidget_2.setAutoFillBackground(False)
        self.gridWidget_2.setObjectName("gridWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget_2)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.gridWidget_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(400, 0))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridWidget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(350, 0))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_5.addWidget(self.pushButton_4)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalWidget = QtWidgets.QWidget(self.gridWidget_2)
        self.verticalWidget.setMinimumSize(QtCore.QSize(0, 350))
        self.verticalWidget.setMaximumSize(QtCore.QSize(16777215, 350))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        self.calendarWidget.setMinimumSize(QtCore.QSize(100, 100))
        self.calendarWidget.setMaximumSize(QtCore.QSize(300, 200))
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.gridLayout.addWidget(self.verticalWidget, 0, 5, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.gridWidget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(400, 0))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridWidget_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(350, 0))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.gridWidget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1418, 21))
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
        self.actionReconectar = QtWidgets.QAction(MainWindow)
        self.actionReconectar.setObjectName("actionReconectar")
        self.menuArquivo.addAction(self.actionSair)
        self.menuArquivo.addAction(self.actionReconectar)
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
        self.pushButton_3.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("MainWindow", "PushButton", None, -1))
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
        self.actionReconectar.setText(QtWidgets.QApplication.translate("MainWindow", "Reconectar", None, -1))

