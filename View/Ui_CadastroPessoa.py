# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources\UI\CadastroPessoa.ui',
# licensing of 'Resources\UI\CadastroPessoa.ui' applies.
#
# Created: Mon Sep  2 00:43:48 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CadastroPessoa(object):
    def setupUi(self, CadastroPessoa):
        CadastroPessoa.setObjectName("CadastroPessoa")
        CadastroPessoa.setWindowModality(QtCore.Qt.NonModal)
        CadastroPessoa.resize(830, 520)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CadastroPessoa.sizePolicy().hasHeightForWidth())
        CadastroPessoa.setSizePolicy(sizePolicy)
        CadastroPessoa.setMinimumSize(QtCore.QSize(830, 520))
        self.gridLayout_2 = QtWidgets.QGridLayout(CadastroPessoa)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_menu = QtWidgets.QWidget(CadastroPessoa)
        self.frame_menu.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_menu.setObjectName("frame_menu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_menu)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_cadastrar = QtWidgets.QPushButton(self.frame_menu)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_cadastrar.setFont(font)
        self.pushButton_cadastrar.setCheckable(False)
        self.pushButton_cadastrar.setDefault(False)
        self.pushButton_cadastrar.setFlat(True)
        self.pushButton_cadastrar.setObjectName("pushButton_cadastrar")
        self.horizontalLayout_3.addWidget(self.pushButton_cadastrar)
        self.pushButton_editar = QtWidgets.QPushButton(self.frame_menu)
        self.pushButton_editar.setEnabled(False)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_editar.setFont(font)
        self.pushButton_editar.setCheckable(False)
        self.pushButton_editar.setDefault(False)
        self.pushButton_editar.setFlat(True)
        self.pushButton_editar.setObjectName("pushButton_editar")
        self.horizontalLayout_3.addWidget(self.pushButton_editar)
        self.pushButton_excluir = QtWidgets.QPushButton(self.frame_menu)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_excluir.setFont(font)
        self.pushButton_excluir.setCheckable(False)
        self.pushButton_excluir.setDefault(False)
        self.pushButton_excluir.setFlat(True)
        self.pushButton_excluir.setObjectName("pushButton_excluir")
        self.horizontalLayout_3.addWidget(self.pushButton_excluir)
        self.pushButton_localizar = QtWidgets.QPushButton(self.frame_menu)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_localizar.setFont(font)
        self.pushButton_localizar.setCheckable(False)
        self.pushButton_localizar.setDefault(False)
        self.pushButton_localizar.setFlat(True)
        self.pushButton_localizar.setObjectName("pushButton_localizar")
        self.horizontalLayout_3.addWidget(self.pushButton_localizar)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.frame_menu)
        self.frame_contents = QtWidgets.QFrame(CadastroPessoa)
        self.frame_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contents.setObjectName("frame_contents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_contents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_endereco = QtWidgets.QGroupBox(self.frame_contents)
        self.groupBox_endereco.setObjectName("groupBox_endereco")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_endereco)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.formLayout_enderco = QtWidgets.QFormLayout()
        self.formLayout_enderco.setContentsMargins(0, -1, -1, -1)
        self.formLayout_enderco.setObjectName("formLayout_enderco")
        self.label_cep = QtWidgets.QLabel(self.groupBox_endereco)
        self.label_cep.setObjectName("label_cep")
        self.formLayout_enderco.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_cep)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_cep = QtWidgets.QLineEdit(self.groupBox_endereco)
        self.lineEdit_cep.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_cep.setMaxLength(9)
        self.lineEdit_cep.setObjectName("lineEdit_cep")
        self.horizontalLayout_11.addWidget(self.lineEdit_cep)
        self.label_endereco_id = QtWidgets.QLabel(self.groupBox_endereco)
        self.label_endereco_id.setText("")
        self.label_endereco_id.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_endereco_id.setObjectName("label_endereco_id")
        self.horizontalLayout_11.addWidget(self.label_endereco_id)
        self.formLayout_enderco.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_11)
        self.label_uf = QtWidgets.QLabel(self.groupBox_endereco)
        self.label_uf.setObjectName("label_uf")
        self.formLayout_enderco.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_uf)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.comboBox_uf = QtWidgets.QComboBox(self.groupBox_endereco)
        self.comboBox_uf.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox_uf.setFont(font)
        self.comboBox_uf.setObjectName("comboBox_uf")
        self.horizontalLayout_9.addWidget(self.comboBox_uf)
        self.label_municipio = QtWidgets.QLabel(self.groupBox_endereco)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_municipio.sizePolicy().hasHeightForWidth())
        self.label_municipio.setSizePolicy(sizePolicy)
        self.label_municipio.setObjectName("label_municipio")
        self.horizontalLayout_9.addWidget(self.label_municipio)
        self.comboBox_municipio = QtWidgets.QComboBox(self.groupBox_endereco)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_municipio.sizePolicy().hasHeightForWidth())
        self.comboBox_municipio.setSizePolicy(sizePolicy)
        self.comboBox_municipio.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_municipio.setFrame(True)
        self.comboBox_municipio.setObjectName("comboBox_municipio")
        self.horizontalLayout_9.addWidget(self.comboBox_municipio)
        self.formLayout_enderco.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_9)
        self.label_logradouro = QtWidgets.QLabel(self.groupBox_endereco)
        self.label_logradouro.setObjectName("label_logradouro")
        self.formLayout_enderco.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_logradouro)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_logradouro = QtWidgets.QLineEdit(self.groupBox_endereco)
        self.lineEdit_logradouro.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_logradouro.setInputMask("")
        self.lineEdit_logradouro.setMaxLength(80)
        self.lineEdit_logradouro.setObjectName("lineEdit_logradouro")
        self.horizontalLayout_7.addWidget(self.lineEdit_logradouro)
        self.label_numero = QtWidgets.QLabel(self.groupBox_endereco)
        self.label_numero.setObjectName("label_numero")
        self.horizontalLayout_7.addWidget(self.label_numero)
        self.lineEdit_numero = QtWidgets.QLineEdit(self.groupBox_endereco)
        self.lineEdit_numero.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_numero.setMaxLength(5)
        self.lineEdit_numero.setObjectName("lineEdit_numero")
        self.horizontalLayout_7.addWidget(self.lineEdit_numero)
        self.label_bairro = QtWidgets.QLabel(self.groupBox_endereco)
        self.label_bairro.setObjectName("label_bairro")
        self.horizontalLayout_7.addWidget(self.label_bairro)
        self.lineEdit_bairro = QtWidgets.QLineEdit(self.groupBox_endereco)
        self.lineEdit_bairro.setInputMask("")
        self.lineEdit_bairro.setMaxLength(80)
        self.lineEdit_bairro.setObjectName("lineEdit_bairro")
        self.horizontalLayout_7.addWidget(self.lineEdit_bairro)
        self.formLayout_enderco.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.label_complemento = QtWidgets.QLabel(self.groupBox_endereco)
        self.label_complemento.setObjectName("label_complemento")
        self.formLayout_enderco.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_complemento)
        self.lineEdit_complemento = QtWidgets.QLineEdit(self.groupBox_endereco)
        self.lineEdit_complemento.setInputMask("")
        self.lineEdit_complemento.setText("")
        self.lineEdit_complemento.setMaxLength(100)
        self.lineEdit_complemento.setObjectName("lineEdit_complemento")
        self.formLayout_enderco.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_complemento)
        self.horizontalLayout_6.addLayout(self.formLayout_enderco)
        self.gridLayout_7.addWidget(self.groupBox_endereco, 2, 0, 1, 1)
        self.groupBox_identificacao_modalidade = QtWidgets.QGroupBox(self.frame_contents)
        self.groupBox_identificacao_modalidade.setMaximumSize(QtCore.QSize(16777215, 250))
        self.groupBox_identificacao_modalidade.setObjectName("groupBox_identificacao_modalidade")
        self.horizontalLayout_identificacao = QtWidgets.QHBoxLayout(self.groupBox_identificacao_modalidade)
        self.horizontalLayout_identificacao.setObjectName("horizontalLayout_identificacao")
        self.frame_identificacao = QtWidgets.QFrame(self.groupBox_identificacao_modalidade)
        self.frame_identificacao.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_identificacao.setObjectName("frame_identificacao")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_identificacao)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_identificacao = QtWidgets.QWidget(self.frame_identificacao)
        self.widget_identificacao.setMinimumSize(QtCore.QSize(500, 0))
        self.widget_identificacao.setObjectName("widget_identificacao")
        self.formLayout_identificacao = QtWidgets.QFormLayout(self.widget_identificacao)
        self.formLayout_identificacao.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout_identificacao.setContentsMargins(0, 0, 0, 0)
        self.formLayout_identificacao.setObjectName("formLayout_identificacao")
        self.label_nome = QtWidgets.QLabel(self.widget_identificacao)
        self.label_nome.setObjectName("label_nome")
        self.formLayout_identificacao.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_nome)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.widget_identificacao)
        self.lineEdit_nome.setInputMask("")
        self.lineEdit_nome.setMaxLength(100)
        self.lineEdit_nome.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_nome.setClearButtonEnabled(False)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.formLayout_identificacao.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nome)
        self.label_fantasia = QtWidgets.QLabel(self.widget_identificacao)
        self.label_fantasia.setObjectName("label_fantasia")
        self.formLayout_identificacao.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_fantasia)
        self.lineEdit_fantasia = QtWidgets.QLineEdit(self.widget_identificacao)
        self.lineEdit_fantasia.setInputMask("")
        self.lineEdit_fantasia.setMaxLength(100)
        self.lineEdit_fantasia.setObjectName("lineEdit_fantasia")
        self.formLayout_identificacao.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fantasia)
        self.label = QtWidgets.QLabel(self.widget_identificacao)
        self.label.setObjectName("label")
        self.formLayout_identificacao.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_email = QtWidgets.QLineEdit(self.widget_identificacao)
        self.lineEdit_email.setInputMask("")
        self.lineEdit_email.setText("")
        self.lineEdit_email.setMaxLength(100)
        self.lineEdit_email.setDragEnabled(False)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.horizontalLayout_5.addWidget(self.lineEdit_email)
        self.label_3 = QtWidgets.QLabel(self.widget_identificacao)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit_telefone = QtWidgets.QLineEdit(self.widget_identificacao)
        self.lineEdit_telefone.setInputMask("")
        self.lineEdit_telefone.setText("")
        self.lineEdit_telefone.setMaxLength(32767)
        self.lineEdit_telefone.setObjectName("lineEdit_telefone")
        self.horizontalLayout_5.addWidget(self.lineEdit_telefone)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)
        self.formLayout_identificacao.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_IE = QtWidgets.QLabel(self.widget_identificacao)
        self.label_IE.setObjectName("label_IE")
        self.formLayout_identificacao.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_IE)
        self.horizontalLayout_IE = QtWidgets.QHBoxLayout()
        self.horizontalLayout_IE.setObjectName("horizontalLayout_IE")
        self.lineEdit_IE = QtWidgets.QLineEdit(self.widget_identificacao)
        self.lineEdit_IE.setEnabled(False)
        self.lineEdit_IE.setMaxLength(15)
        self.lineEdit_IE.setObjectName("lineEdit_IE")
        self.horizontalLayout_IE.addWidget(self.lineEdit_IE)
        self.checkBox_isento = QtWidgets.QCheckBox(self.widget_identificacao)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_isento.sizePolicy().hasHeightForWidth())
        self.checkBox_isento.setSizePolicy(sizePolicy)
        self.checkBox_isento.setChecked(True)
        self.checkBox_isento.setObjectName("checkBox_isento")
        self.horizontalLayout_IE.addWidget(self.checkBox_isento)
        self.formLayout_identificacao.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_IE)
        self.label_documento = QtWidgets.QLabel(self.widget_identificacao)
        self.label_documento.setObjectName("label_documento")
        self.formLayout_identificacao.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_documento)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.widget_tipo_pessoa = QtWidgets.QWidget(self.widget_identificacao)
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
        self.horizontalLayout_10.addWidget(self.widget_tipo_pessoa)
        self.lineEdit_documento = QtWidgets.QLineEdit(self.widget_identificacao)
        self.lineEdit_documento.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEdit_documento.setMaxLength(14)
        self.lineEdit_documento.setObjectName("lineEdit_documento")
        self.horizontalLayout_10.addWidget(self.lineEdit_documento)
        self.formLayout_identificacao.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.gridLayout_3.addWidget(self.widget_identificacao, 0, 0, 1, 1)
        self.horizontalLayout_identificacao.addWidget(self.frame_identificacao)
        self.groupBox_modalidade = QtWidgets.QGroupBox(self.groupBox_identificacao_modalidade)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_modalidade.sizePolicy().hasHeightForWidth())
        self.groupBox_modalidade.setSizePolicy(sizePolicy)
        self.groupBox_modalidade.setMaximumSize(QtCore.QSize(200, 200))
        self.groupBox_modalidade.setObjectName("groupBox_modalidade")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_modalidade)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget_modalidade = QtWidgets.QListWidget(self.groupBox_modalidade)
        self.listWidget_modalidade.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget_modalidade.setTabKeyNavigation(True)
        self.listWidget_modalidade.setProperty("showDropIndicator", False)
        self.listWidget_modalidade.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_modalidade.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget_modalidade.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget_modalidade.setObjectName("listWidget_modalidade")
        self.gridLayout.addWidget(self.listWidget_modalidade, 0, 0, 1, 1)
        self.horizontalLayout_identificacao.addWidget(self.groupBox_modalidade)
        self.gridLayout_7.addWidget(self.groupBox_identificacao_modalidade, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_contents)
        self.frame_buttons = QtWidgets.QFrame(CadastroPessoa)
        self.frame_buttons.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_buttons)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_id = QtWidgets.QLabel(self.frame_buttons)
        self.label_id.setText("")
        self.label_id.setObjectName("label_id")
        self.horizontalLayout.addWidget(self.label_id)
        self.lineEdit_id = QtWidgets.QLineEdit(self.frame_buttons)
        self.lineEdit_id.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_id.sizePolicy().hasHeightForWidth())
        self.lineEdit_id.setSizePolicy(sizePolicy)
        self.lineEdit_id.setAutoFillBackground(False)
        self.lineEdit_id.setFrame(False)
        self.lineEdit_id.setDragEnabled(False)
        self.lineEdit_id.setReadOnly(False)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.horizontalLayout.addWidget(self.lineEdit_id)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame_buttons)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.frame_buttons)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(CadastroPessoa)
        QtCore.QMetaObject.connectSlotsByName(CadastroPessoa)

    def retranslateUi(self, CadastroPessoa):
        CadastroPessoa.setWindowTitle(QtWidgets.QApplication.translate("CadastroPessoa", "Cadastrar Pessoa", None, -1))
        self.pushButton_cadastrar.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Cadastrar", None, -1))
        self.pushButton_editar.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Editar", None, -1))
        self.pushButton_excluir.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Excluir", None, -1))
        self.pushButton_localizar.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Localizar", None, -1))
        self.groupBox_endereco.setTitle(QtWidgets.QApplication.translate("CadastroPessoa", "Endereco", None, -1))
        self.label_cep.setText(QtWidgets.QApplication.translate("CadastroPessoa", "CEP", None, -1))
        self.lineEdit_cep.setInputMask(QtWidgets.QApplication.translate("CadastroPessoa", "99999-999", None, -1))
        self.label_uf.setText(QtWidgets.QApplication.translate("CadastroPessoa", "UF", None, -1))
        self.label_municipio.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Município", None, -1))
        self.label_logradouro.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Logradouro", None, -1))
        self.label_numero.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Número", None, -1))
        self.lineEdit_numero.setInputMask(QtWidgets.QApplication.translate("CadastroPessoa", "00000", None, -1))
        self.label_bairro.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Bairro", None, -1))
        self.label_complemento.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Complemento", None, -1))
        self.groupBox_identificacao_modalidade.setTitle(QtWidgets.QApplication.translate("CadastroPessoa", "Identificação", None, -1))
        self.label_nome.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Nome:", None, -1))
        self.label_fantasia.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Nome Fantasia:", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Email:", None, -1))
        self.lineEdit_email.setPlaceholderText(QtWidgets.QApplication.translate("CadastroPessoa", "email@dominio.com", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Tel:", None, -1))
        self.lineEdit_telefone.setPlaceholderText(QtWidgets.QApplication.translate("CadastroPessoa", "+55 (042) 99999999", None, -1))
        self.label_IE.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Inscrição Estadual:", None, -1))
        self.checkBox_isento.setText(QtWidgets.QApplication.translate("CadastroPessoa", "ISENTO", None, -1))
        self.label_documento.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Documento:", None, -1))
        self.radioButton_pj.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Pessoa Jurídica", None, -1))
        self.radioButton_pf.setText(QtWidgets.QApplication.translate("CadastroPessoa", "Pessoa Física", None, -1))
        self.lineEdit_documento.setInputMask(QtWidgets.QApplication.translate("CadastroPessoa", "999.999.999-99", None, -1))
        self.lineEdit_documento.setText(QtWidgets.QApplication.translate("CadastroPessoa", "000.000.000-00", None, -1))
        self.groupBox_modalidade.setTitle(QtWidgets.QApplication.translate("CadastroPessoa", "Modalidades", None, -1))

