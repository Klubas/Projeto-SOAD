# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\CadastroPessoa.ui'
#
# Created: Sat Jul 13 03:29:00 2019
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CadastroPessoa(object):
    def setupUi(self, CadastroPessoa):
        CadastroPessoa.setObjectName("CadastroPessoa")
        CadastroPessoa.setWindowModality(QtCore.Qt.NonModal)
        CadastroPessoa.resize(578, 560)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CadastroPessoa.sizePolicy().hasHeightForWidth())
        CadastroPessoa.setSizePolicy(sizePolicy)
        CadastroPessoa.setMinimumSize(QtCore.QSize(568, 559))
        self.horizontalLayoutWidget = QtWidgets.QWidget(CadastroPessoa)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 571, 561))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(0, 5, 5, 5)
        self.formLayout.setSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_modalidade = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_modalidade.setObjectName("label_modalidade")
        self.horizontalLayout_2.addWidget(self.label_modalidade)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setAutoRepeat(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton.setChecked(False)
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_nome = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_nome.setObjectName("label_nome")
        self.horizontalLayout_3.addWidget(self.label_nome)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.formLayout)

        self.retranslateUi(CadastroPessoa)
        QtCore.QMetaObject.connectSlotsByName(CadastroPessoa)

    def retranslateUi(self, CadastroPessoa):
        CadastroPessoa.setWindowTitle(QtWidgets.QApplication.translate("CadastroPessoa", "Cadastrar Pessoa", None, -1))
        self.label_modalidade.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Tipo", None, -1))
        self.radioButton_2.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Jurídica", None, -1))
        self.radioButton.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Física", None, -1))
        self.label_nome.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Nome", None, -1))

