# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/Componentes/LocalizarDialog.ui',
# licensing of 'Resources/UI/Componentes/LocalizarDialog.ui' applies.
#
# Created: Thu Sep  5 18:58:24 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_LocalizarDialog(object):
    def setupUi(self, LocalizarDialog):
        LocalizarDialog.setObjectName("LocalizarDialog")
        LocalizarDialog.setWindowModality(QtCore.Qt.WindowModal)
        LocalizarDialog.resize(600, 300)
        LocalizarDialog.setMinimumSize(QtCore.QSize(600, 300))
        LocalizarDialog.setSizeGripEnabled(True)
        LocalizarDialog.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(LocalizarDialog)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_valor = QtWidgets.QLineEdit(LocalizarDialog)
        self.lineEdit_valor.setObjectName("lineEdit_valor")
        self.gridLayout.addWidget(self.lineEdit_valor, 0, 1, 1, 1)
        self.comboBox_campo = QtWidgets.QComboBox(LocalizarDialog)
        self.comboBox_campo.setMinimumSize(QtCore.QSize(150, 0))
        self.comboBox_campo.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_campo.setObjectName("comboBox_campo")
        self.gridLayout.addWidget(self.comboBox_campo, 0, 0, 1, 1)
        self.pushButton_buscar = QtWidgets.QPushButton(LocalizarDialog)
        self.pushButton_buscar.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_buscar.setMaximumSize(QtCore.QSize(75, 23))
        self.pushButton_buscar.setDefault(True)
        self.pushButton_buscar.setObjectName("pushButton_buscar")
        self.gridLayout.addWidget(self.pushButton_buscar, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.tableWidget_linhas = QtWidgets.QTableWidget(LocalizarDialog)
        self.tableWidget_linhas.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.tableWidget_linhas.setTabKeyNavigation(True)
        self.tableWidget_linhas.setDragEnabled(False)
        self.tableWidget_linhas.setAlternatingRowColors(True)
        self.tableWidget_linhas.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_linhas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_linhas.setShowGrid(True)
        self.tableWidget_linhas.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_linhas.setWordWrap(False)
        self.tableWidget_linhas.setObjectName("tableWidget_linhas")
        self.tableWidget_linhas.setColumnCount(1)
        self.tableWidget_linhas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_linhas.setHorizontalHeaderItem(0, item)
        self.tableWidget_linhas.horizontalHeader().setVisible(True)
        self.tableWidget_linhas.horizontalHeader().setHighlightSections(False)
        self.tableWidget_linhas.verticalHeader().setVisible(False)
        self.tableWidget_linhas.verticalHeader().setHighlightSections(False)
        self.verticalLayout_2.addWidget(self.tableWidget_linhas)
        self.buttonBox = QtWidgets.QDialogButtonBox(LocalizarDialog)
        self.buttonBox.setSizeIncrement(QtCore.QSize(0, 1))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(LocalizarDialog)
        QtCore.QMetaObject.connectSlotsByName(LocalizarDialog)

    def retranslateUi(self, LocalizarDialog):
        LocalizarDialog.setWindowTitle(QtWidgets.QApplication.translate("LocalizarDialog", "Localizar", None, -1))
        self.pushButton_buscar.setText(QtWidgets.QApplication.translate("LocalizarDialog", "Buscar", None, -1))
        self.tableWidget_linhas.setSortingEnabled(True)
        self.tableWidget_linhas.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("LocalizarDialog", "ID", None, -1))

