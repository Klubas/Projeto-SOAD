# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/Componentes/ListaPadrao.ui',
# licensing of 'Resources/UI/Componentes/ListaPadrao.ui' applies.
#
# Created: Sun Nov 10 15:19:49 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ListaPadrao(object):
    def setupUi(self, ListaPadrao):
        ListaPadrao.setObjectName("ListaPadrao")
        ListaPadrao.resize(1200, 600)
        ListaPadrao.setMinimumSize(QtCore.QSize(1200, 600))
        self.gridLayout = QtWidgets.QGridLayout(ListaPadrao)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_menu = QtWidgets.QWidget(ListaPadrao)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menu.sizePolicy().hasHeightForWidth())
        self.frame_menu.setSizePolicy(sizePolicy)
        self.frame_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_menu.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_menu.setObjectName("frame_menu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_menu)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame = QtWidgets.QFrame(self.frame_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_filtro = QtWidgets.QPushButton(self.frame)
        self.pushButton_filtro.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_filtro.sizePolicy().hasHeightForWidth())
        self.pushButton_filtro.setSizePolicy(sizePolicy)
        self.pushButton_filtro.setMinimumSize(QtCore.QSize(120, 0))
        self.pushButton_filtro.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_filtro.setFont(font)
        self.pushButton_filtro.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_filtro.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_filtro.setCheckable(False)
        self.pushButton_filtro.setDefault(False)
        self.pushButton_filtro.setFlat(True)
        self.pushButton_filtro.setObjectName("pushButton_filtro")
        self.horizontalLayout_3.addWidget(self.pushButton_filtro)
        self.pushButton_atualizar = QtWidgets.QPushButton(self.frame)
        self.pushButton_atualizar.setMinimumSize(QtCore.QSize(120, 0))
        self.pushButton_atualizar.setMaximumSize(QtCore.QSize(140, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_atualizar.setFont(font)
        self.pushButton_atualizar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_atualizar.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_atualizar.setCheckable(False)
        self.pushButton_atualizar.setDefault(False)
        self.pushButton_atualizar.setFlat(True)
        self.pushButton_atualizar.setObjectName("pushButton_atualizar")
        self.horizontalLayout_3.addWidget(self.pushButton_atualizar)
        self.pushButton_relatorio = QtWidgets.QPushButton(self.frame)
        self.pushButton_relatorio.setMinimumSize(QtCore.QSize(120, 0))
        self.pushButton_relatorio.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_relatorio.setFont(font)
        self.pushButton_relatorio.setToolTipDuration(10000)
        self.pushButton_relatorio.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_relatorio.setFlat(True)
        self.pushButton_relatorio.setObjectName("pushButton_relatorio")
        self.horizontalLayout_3.addWidget(self.pushButton_relatorio)
        self.pushButton_acao = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_acao.sizePolicy().hasHeightForWidth())
        self.pushButton_acao.setSizePolicy(sizePolicy)
        self.pushButton_acao.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_acao.setFont(font)
        self.pushButton_acao.setFlat(True)
        self.pushButton_acao.setObjectName("pushButton_acao")
        self.horizontalLayout_3.addWidget(self.pushButton_acao)
        self.horizontalLayout_4.addWidget(self.frame)
        self.stackedWidget_filtros = QtWidgets.QStackedWidget(self.frame_menu)
        self.stackedWidget_filtros.setObjectName("stackedWidget_filtros")
        self.stackedWidget_filtrosPage1 = QtWidgets.QWidget()
        self.stackedWidget_filtrosPage1.setObjectName("stackedWidget_filtrosPage1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.stackedWidget_filtrosPage1)
        self.gridLayout_2.setContentsMargins(5, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_data = QtWidgets.QCheckBox(self.stackedWidget_filtrosPage1)
        self.checkBox_data.setEnabled(True)
        self.checkBox_data.setText("")
        self.checkBox_data.setObjectName("checkBox_data")
        self.gridLayout_2.addWidget(self.checkBox_data, 0, 1, 1, 1)
        self.horizontalWidget_data = QtWidgets.QWidget(self.stackedWidget_filtrosPage1)
        self.horizontalWidget_data.setEnabled(False)
        self.horizontalWidget_data.setObjectName("horizontalWidget_data")
        self.horizontalLayout_data = QtWidgets.QHBoxLayout(self.horizontalWidget_data)
        self.horizontalLayout_data.setSpacing(5)
        self.horizontalLayout_data.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_data.setObjectName("horizontalLayout_data")
        self.label = QtWidgets.QLabel(self.horizontalWidget_data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_data.addWidget(self.label)
        self.dateEdit = QtWidgets.QDateEdit(self.horizontalWidget_data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_data.addWidget(self.dateEdit)
        self.label_2 = QtWidgets.QLabel(self.horizontalWidget_data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_data.addWidget(self.label_2)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.horizontalWidget_data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_2.sizePolicy().hasHeightForWidth())
        self.dateEdit_2.setSizePolicy(sizePolicy)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_data.addWidget(self.dateEdit_2)
        self.gridLayout_2.addWidget(self.horizontalWidget_data, 0, 2, 1, 1)
        self.checkBox_filtro = QtWidgets.QCheckBox(self.stackedWidget_filtrosPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_filtro.sizePolicy().hasHeightForWidth())
        self.checkBox_filtro.setSizePolicy(sizePolicy)
        self.checkBox_filtro.setObjectName("checkBox_filtro")
        self.gridLayout_2.addWidget(self.checkBox_filtro, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 4, 1, 1)
        self.stackedWidget_filtros.addWidget(self.stackedWidget_filtrosPage1)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(723, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.stackedWidget_filtros.addWidget(self.page)
        self.horizontalLayout_4.addWidget(self.stackedWidget_filtros)
        self.verticalLayout.addWidget(self.frame_menu)
        self.frame_contents = QtWidgets.QFrame(ListaPadrao)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_contents.sizePolicy().hasHeightForWidth())
        self.frame_contents.setSizePolicy(sizePolicy)
        self.frame_contents.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_contents.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_contents.setObjectName("frame_contents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_contents)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame1 = QtWidgets.QFrame(self.frame_contents)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.frame1.setFont(font)
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setObjectName("frame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame1)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget_tabela = QtWidgets.QTableWidget(self.frame1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.tableWidget_tabela.setFont(font)
        self.tableWidget_tabela.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget_tabela.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget_tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_tabela.setAlternatingRowColors(True)
        self.tableWidget_tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_tabela.setObjectName("tableWidget_tabela")
        self.tableWidget_tabela.setColumnCount(0)
        self.tableWidget_tabela.setRowCount(0)
        self.tableWidget_tabela.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_tabela.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_tabela.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_tabela.verticalHeader().setVisible(False)
        self.tableWidget_tabela.verticalHeader().setHighlightSections(False)
        self.horizontalLayout_2.addWidget(self.tableWidget_tabela)
        self.horizontalLayout.addWidget(self.frame1)
        self.verticalLayout.addWidget(self.frame_contents)
        self.frame_buttons = QtWidgets.QFrame(ListaPadrao)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_buttons.sizePolicy().hasHeightForWidth())
        self.frame_buttons.setSizePolicy(sizePolicy)
        self.frame_buttons.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_buttons.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_buttons.setObjectName("frame_buttons")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_buttons)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(ListaPadrao)
        self.stackedWidget_filtros.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ListaPadrao)

    def retranslateUi(self, ListaPadrao):
        ListaPadrao.setWindowTitle(QtWidgets.QApplication.translate("ListaPadrao", "Form", None, -1))
        self.pushButton_filtro.setText(QtWidgets.QApplication.translate("ListaPadrao", "Filtrar", None, -1))
        self.pushButton_filtro.setShortcut(QtWidgets.QApplication.translate("ListaPadrao", "Ctrl+P", None, -1))
        self.pushButton_atualizar.setText(QtWidgets.QApplication.translate("ListaPadrao", "Atualizar", None, -1))
        self.pushButton_atualizar.setShortcut(QtWidgets.QApplication.translate("ListaPadrao", "Ctrl+P", None, -1))
        self.pushButton_relatorio.setToolTip(QtWidgets.QApplication.translate("ListaPadrao", "Realizar impressão em formato de relatório.", None, -1))
        self.pushButton_relatorio.setText(QtWidgets.QApplication.translate("ListaPadrao", "Relatório", None, -1))
        self.pushButton_relatorio.setShortcut(QtWidgets.QApplication.translate("ListaPadrao", "Ctrl+Shift+P", None, -1))
        self.pushButton_acao.setText(QtWidgets.QApplication.translate("ListaPadrao", "<ação>", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ListaPadrao", "Data", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("ListaPadrao", "até", None, -1))
        self.checkBox_filtro.setText(QtWidgets.QApplication.translate("ListaPadrao", "Apenas X", None, -1))
        self.tableWidget_tabela.setSortingEnabled(True)

