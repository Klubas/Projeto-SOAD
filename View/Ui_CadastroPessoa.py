# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\CadastroPessoa.ui',
# licensing of 'C:\Users\Lucas\PycharmProjects\Projeto-SOAD\Resources\UI\CadastroPessoa.ui' applies.
#
# Created: Thu Aug  8 00:08:21 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtWidgets

class Ui_CadastroPessoa(object):
    def setupUi(self, CadastroPessoa):
        CadastroPessoa.setObjectName("CadastroPessoa")
        CadastroPessoa.setWindowModality(QtCore.Qt.NonModal)
        CadastroPessoa.resize(1099, 598)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CadastroPessoa.sizePolicy().hasHeightForWidth())
        CadastroPessoa.setSizePolicy(sizePolicy)
        CadastroPessoa.setMinimumSize(QtCore.QSize(568, 559))
        self.gridLayout_2 = QtWidgets.QGridLayout(CadastroPessoa)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_2 = QtWidgets.QWidget(CadastroPessoa)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_menu = QtWidgets.QFrame(self.widget_2)
        self.frame_menu.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_menu)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_cadastrar = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_cadastrar.setCheckable(False)
        self.pushButton_cadastrar.setDefault(False)
        self.pushButton_cadastrar.setFlat(True)
        self.pushButton_cadastrar.setObjectName("pushButton_cadastrar")
        self.horizontalLayout_3.addWidget(self.pushButton_cadastrar)
        self.pushButton_editar = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_editar.setCheckable(False)
        self.pushButton_editar.setDefault(False)
        self.pushButton_editar.setFlat(True)
        self.pushButton_editar.setObjectName("pushButton_editar")
        self.horizontalLayout_3.addWidget(self.pushButton_editar)
        self.pushButton_excluir = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_excluir.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_excluir.setCheckable(False)
        self.pushButton_excluir.setDefault(False)
        self.pushButton_excluir.setFlat(True)
        self.pushButton_excluir.setObjectName("pushButton_excluir")
        self.horizontalLayout_3.addWidget(self.pushButton_excluir)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.frame_menu)
        self.frame_contents = QtWidgets.QFrame(self.widget_2)
        self.frame_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contents.setObjectName("frame_contents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_contents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.widget = QtWidgets.QWidget(self.frame_contents)
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.dados_pessoa = QtWidgets.QGridLayout()
        self.dados_pessoa.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.dados_pessoa.setContentsMargins(20, 20, 20, 20)
        self.dados_pessoa.setObjectName("dados_pessoa")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setContentsMargins(0, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setObjectName("formLayout")
        self.label_tipo_pessoa = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_tipo_pessoa.sizePolicy().hasHeightForWidth())
        self.label_tipo_pessoa.setSizePolicy(sizePolicy)
        self.label_tipo_pessoa.setMaximumSize(QtCore.QSize(16777214, 17))
        self.label_tipo_pessoa.setObjectName("label_tipo_pessoa")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_tipo_pessoa)
        self.widget_tipo_pessoa = QtWidgets.QWidget(self.widget)
        self.widget_tipo_pessoa.setEnabled(False)
        self.widget_tipo_pessoa.setObjectName("widget_tipo_pessoa")
        self.horizontalLayout_tipo_pessoa = QtWidgets.QHBoxLayout(self.widget_tipo_pessoa)
        self.horizontalLayout_tipo_pessoa.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_tipo_pessoa.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_tipo_pessoa.setObjectName("horizontalLayout_tipo_pessoa")
        self.radioButton_pj = QtWidgets.QRadioButton(self.widget_tipo_pessoa)
        self.radioButton_pj.setMaximumSize(QtCore.QSize(16777215, 17))
        self.radioButton_pj.setChecked(True)
        self.radioButton_pj.setAutoRepeat(False)
        self.radioButton_pj.setObjectName("radioButton_pj")
        self.horizontalLayout_tipo_pessoa.addWidget(self.radioButton_pj)
        self.radioButton_pf = QtWidgets.QRadioButton(self.widget_tipo_pessoa)
        self.radioButton_pf.setMaximumSize(QtCore.QSize(16777215, 17))
        self.radioButton_pf.setChecked(False)
        self.radioButton_pf.setAutoRepeat(False)
        self.radioButton_pf.setObjectName("radioButton_pf")
        self.horizontalLayout_tipo_pessoa.addWidget(self.radioButton_pf)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.widget_tipo_pessoa)
        self.label_nome = QtWidgets.QLabel(self.widget)
        self.label_nome.setObjectName("label_nome")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_nome)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nome)
        self.label_fantasia = QtWidgets.QLabel(self.widget)
        self.label_fantasia.setObjectName("label_fantasia")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_fantasia)
        self.lineEdit_fantasia = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_fantasia.setObjectName("lineEdit_fantasia")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fantasia)
        self.label_documento = QtWidgets.QLabel(self.widget)
        self.label_documento.setObjectName("label_documento")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_documento)
        self.lineEdit_documento = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_documento.setObjectName("lineEdit_documento")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_documento)
        self.label_email = QtWidgets.QLabel(self.widget)
        self.label_email.setObjectName("label_email")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_email)
        self.lineEdit_email = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_email)
        self.label_telefone = QtWidgets.QLabel(self.widget)
        self.label_telefone.setObjectName("label_telefone")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_telefone)
        self.lineEdit_telefone = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_telefone.setObjectName("lineEdit_telefone")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_telefone)
        self.label_IE = QtWidgets.QLabel(self.widget)
        self.label_IE.setObjectName("label_IE")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_IE)
        self.horizontalLayout_IE = QtWidgets.QHBoxLayout()
        self.horizontalLayout_IE.setObjectName("horizontalLayout_IE")
        self.lineEdit_IE = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_IE.setEnabled(False)
        self.lineEdit_IE.setObjectName("lineEdit_IE")
        self.horizontalLayout_IE.addWidget(self.lineEdit_IE)
        self.checkBox_isento = QtWidgets.QCheckBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_isento.sizePolicy().hasHeightForWidth())
        self.checkBox_isento.setSizePolicy(sizePolicy)
        self.checkBox_isento.setChecked(True)
        self.checkBox_isento.setObjectName("checkBox_isento")
        self.horizontalLayout_IE.addWidget(self.checkBox_isento)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_IE)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.dados_pessoa.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.dados_pessoa, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.widget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_contents)
        self.frame_buttons = QtWidgets.QFrame(self.widget_2)
        self.frame_buttons.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_buttons)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame_buttons)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.frame_buttons)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)

        self.retranslateUi(CadastroPessoa)
        QtCore.QMetaObject.connectSlotsByName(CadastroPessoa)

    def retranslateUi(self, CadastroPessoa):
        CadastroPessoa.setWindowTitle(QtWidgets.QApplication.translate("CadastroPessoa", "Cadastrar Pessoa", None, -1))
        self.pushButton_cadastrar.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Cadastrar", None, -1))
        self.pushButton_editar.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Editar", None, -1))
        self.pushButton_excluir.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Excluir", None, -1))
        self.label_tipo_pessoa.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Tipo:", None, -1))
        self.radioButton_pj.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Jurídica", None, -1))
        self.radioButton_pf.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Física", None, -1))
        self.label_nome.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Nome:", None, -1))
        self.label_fantasia.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Nome Fantasia", None, -1))
        self.label_documento.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Documento:", None, -1))
        self.label_email.setText(QtWidgets.QApplication.translate("CadastroPessoa", "e-Mail:", None, -1))
        self.label_telefone.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Telefone:", None, -1))
        self.label_IE.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Inscrição Estadual:", None, -1))
        self.checkBox_isento.setText(QtWidgets.QApplication.translate("CadastroPessoa", "ISENTO", None, -1))

