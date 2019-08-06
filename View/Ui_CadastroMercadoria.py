# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\CadastroMercadoria.ui',
# licensing of 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\CadastroMercadoria.ui' applies.
#
# Created: Tue Aug  6 00:11:04 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_CadastroMercadoria(object):
    def setupUi(self, CadastroMercadoria):
        CadastroMercadoria.setObjectName("CadastroMercadoria")
        CadastroMercadoria.setWindowModality(QtCore.Qt.NonModal)
        CadastroMercadoria.resize(578, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CadastroMercadoria.sizePolicy().hasHeightForWidth())
        CadastroMercadoria.setSizePolicy(sizePolicy)
        CadastroMercadoria.setMinimumSize(QtCore.QSize(568, 559))
        self.horizontalLayoutWidget = QtWidgets.QWidget(CadastroMercadoria)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 571, 561))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.retranslateUi(CadastroMercadoria)
        QtCore.QMetaObject.connectSlotsByName(CadastroMercadoria)

    def retranslateUi(self, CadastroMercadoria):
        CadastroMercadoria.setWindowTitle(QtWidgets.QApplication.translate("CadastroMercadoria", "Cadastrar Produto", None, -1))

