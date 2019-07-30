# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\CadastroPadrao.ui'
#
# Created: Sun Jul 28 22:46:04 2019
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_CadastroPadrao(object):
    def setupUi(self, CadastroPadrao):
        CadastroPadrao.setObjectName("CadastroPadrao")
        CadastroPadrao.setWindowModality(QtCore.Qt.WindowModal)
        CadastroPadrao.setEnabled(True)
        CadastroPadrao.resize(614, 562)
        CadastroPadrao.setCursor(QtCore.Qt.ArrowCursor)
        self.verticalLayoutWidget = QtWidgets.QWidget(CadastroPadrao)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 611, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(-1, 20, 20, 20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 10))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.salvar_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.salvar_button.setObjectName("salvar_button")
        self.horizontalLayout.addWidget(self.salvar_button)
        self.cancelar_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancelar_button.setObjectName("cancelar_button")
        self.horizontalLayout.addWidget(self.cancelar_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(CadastroPadrao)
        QtCore.QMetaObject.connectSlotsByName(CadastroPadrao)

    def retranslateUi(self, CadastroPadrao):
        CadastroPadrao.setWindowTitle(QtWidgets.QApplication.translate("CadastroPadrao", "Cadastro - ", None, -1))
        self.salvar_button.setText(QtWidgets.QApplication.translate("CadastroPadrao", "Salvar", None, -1))
        self.cancelar_button.setText(QtWidgets.QApplication.translate("CadastroPadrao", "Cancelar", None, -1))

