# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources\UI\CadastroPedido.ui',
# licensing of 'Resources\UI\CadastroPedido.ui' applies.
#
# Created: Mon Sep  2 00:43:48 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CadastroPedido(object):
    def setupUi(self, CadastroPedido):
        CadastroPedido.setObjectName("CadastroPedido")
        CadastroPedido.setWindowModality(QtCore.Qt.NonModal)
        CadastroPedido.resize(830, 570)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CadastroPedido.sizePolicy().hasHeightForWidth())
        CadastroPedido.setSizePolicy(sizePolicy)
        CadastroPedido.setMinimumSize(QtCore.QSize(830, 570))
        self.gridLayout = QtWidgets.QGridLayout(CadastroPedido)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_menu = QtWidgets.QWidget(CadastroPedido)
        self.frame_menu.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_menu.setObjectName("frame_menu")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_menu)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout.addWidget(self.frame_menu)
        self.frame_contents = QtWidgets.QFrame(CadastroPedido)
        self.frame_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contents.setObjectName("frame_contents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_contents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_identificacao = QtWidgets.QGroupBox(self.frame_contents)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.groupBox_identificacao.setFont(font)
        self.groupBox_identificacao.setObjectName("groupBox_identificacao")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_identificacao)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formGroupBox_pessoa = QtWidgets.QGroupBox(self.groupBox_identificacao)
        self.formGroupBox_pessoa.setObjectName("formGroupBox_pessoa")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox_pessoa)
        self.formLayout.setObjectName("formLayout")
        self.label_documento = QtWidgets.QLabel(self.formGroupBox_pessoa)
        self.label_documento.setObjectName("label_documento")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_documento)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_documento = QtWidgets.QLineEdit(self.formGroupBox_pessoa)
        self.lineEdit_documento.setMaximumSize(QtCore.QSize(120, 16777215))
        self.lineEdit_documento.setObjectName("lineEdit_documento")
        self.horizontalLayout_2.addWidget(self.lineEdit_documento)
        self.lineEdit_nome_pessoa = QtWidgets.QLineEdit(self.formGroupBox_pessoa)
        self.lineEdit_nome_pessoa.setEnabled(False)
        self.lineEdit_nome_pessoa.setObjectName("lineEdit_nome_pessoa")
        self.horizontalLayout_2.addWidget(self.lineEdit_nome_pessoa)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_data = QtWidgets.QLabel(self.formGroupBox_pessoa)
        self.label_data.setObjectName("label_data")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_data)
        self.dateEdit_entrega = QtWidgets.QDateEdit(self.formGroupBox_pessoa)
        self.dateEdit_entrega.setMaximumSize(QtCore.QSize(120, 16777215))
        self.dateEdit_entrega.setWrapping(False)
        self.dateEdit_entrega.setFrame(True)
        self.dateEdit_entrega.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_entrega.setAccelerated(False)
        self.dateEdit_entrega.setProperty("showGroupSeparator", True)
        self.dateEdit_entrega.setCalendarPopup(True)
        self.dateEdit_entrega.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit_entrega.setObjectName("dateEdit_entrega")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit_entrega)
        self.gridLayout_2.addWidget(self.formGroupBox_pessoa, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_identificacao, 0, 0, 1, 1)
        self.groupBox_items = QtWidgets.QGroupBox(self.frame_contents)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.groupBox_items.setFont(font)
        self.groupBox_items.setFlat(False)
        self.groupBox_items.setCheckable(False)
        self.groupBox_items.setChecked(False)
        self.groupBox_items.setObjectName("groupBox_items")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_items)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_items)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.East)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_campos = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_campos.sizePolicy().hasHeightForWidth())
        self.tab_campos.setSizePolicy(sizePolicy)
        self.tab_campos.setMinimumSize(QtCore.QSize(746, 265))
        self.tab_campos.setMaximumSize(QtCore.QSize(746, 265))
        self.tab_campos.setObjectName("tab_campos")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_campos)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.tab_campos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_items = QtWidgets.QFrame(self.frame)
        self.frame_items.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_items.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_items.setObjectName("frame_items")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_items)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalFrame_tipo_item = QtWidgets.QFrame(self.frame_items)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame_tipo_item.sizePolicy().hasHeightForWidth())
        self.horizontalFrame_tipo_item.setSizePolicy(sizePolicy)
        self.horizontalFrame_tipo_item.setMinimumSize(QtCore.QSize(0, 40))
        self.horizontalFrame_tipo_item.setMaximumSize(QtCore.QSize(16777215, 40))
        self.horizontalFrame_tipo_item.setObjectName("horizontalFrame_tipo_item")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalFrame_tipo_item)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setContentsMargins(10, -1, 10, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.radioButton_mercadoria = QtWidgets.QRadioButton(self.horizontalFrame_tipo_item)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_mercadoria.sizePolicy().hasHeightForWidth())
        self.radioButton_mercadoria.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.radioButton_mercadoria.setFont(font)
        self.radioButton_mercadoria.setChecked(True)
        self.radioButton_mercadoria.setObjectName("radioButton_mercadoria")
        self.horizontalLayout_8.addWidget(self.radioButton_mercadoria)
        self.radioButton_remanufatura = QtWidgets.QRadioButton(self.horizontalFrame_tipo_item)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_remanufatura.sizePolicy().hasHeightForWidth())
        self.radioButton_remanufatura.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.radioButton_remanufatura.setFont(font)
        self.radioButton_remanufatura.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_remanufatura.setObjectName("radioButton_remanufatura")
        self.horizontalLayout_8.addWidget(self.radioButton_remanufatura)
        self.verticalLayout_3.addWidget(self.horizontalFrame_tipo_item)
        self.stackedWidget_item = QtWidgets.QStackedWidget(self.frame_items)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_item.sizePolicy().hasHeightForWidth())
        self.stackedWidget_item.setSizePolicy(sizePolicy)
        self.stackedWidget_item.setMaximumSize(QtCore.QSize(16777215, 100))
        self.stackedWidget_item.setLineWidth(1)
        self.stackedWidget_item.setObjectName("stackedWidget_item")
        self.page_mercadoria = QtWidgets.QWidget()
        self.page_mercadoria.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.page_mercadoria.setObjectName("page_mercadoria")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_mercadoria)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setHorizontalSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frameFormLayout_mercadoria = QtWidgets.QFrame(self.page_mercadoria)
        self.frameFormLayout_mercadoria.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFormLayout_mercadoria.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameFormLayout_mercadoria.setObjectName("frameFormLayout_mercadoria")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frameFormLayout_mercadoria)
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_mercadoria = QtWidgets.QLabel(self.frameFormLayout_mercadoria)
        self.label_mercadoria.setObjectName("label_mercadoria")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_mercadoria)
        self.horizontalLayout_mercadoria = QtWidgets.QHBoxLayout()
        self.horizontalLayout_mercadoria.setObjectName("horizontalLayout_mercadoria")
        self.lineEdit_mercadoria_id = QtWidgets.QLineEdit(self.frameFormLayout_mercadoria)
        self.lineEdit_mercadoria_id.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_mercadoria_id.setObjectName("lineEdit_mercadoria_id")
        self.horizontalLayout_mercadoria.addWidget(self.lineEdit_mercadoria_id)
        self.lineEdit_mercadoria = QtWidgets.QLineEdit(self.frameFormLayout_mercadoria)
        self.lineEdit_mercadoria.setEnabled(False)
        self.lineEdit_mercadoria.setObjectName("lineEdit_mercadoria")
        self.horizontalLayout_mercadoria.addWidget(self.lineEdit_mercadoria)
        self.formLayout_4.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_mercadoria)
        self.gridLayout_8.addWidget(self.frameFormLayout_mercadoria, 0, 0, 1, 1)
        self.stackedWidget_item.addWidget(self.page_mercadoria)
        self.page_remanufatura = QtWidgets.QWidget()
        self.page_remanufatura.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.page_remanufatura.setObjectName("page_remanufatura")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_remanufatura)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frameFormLayout_remanufatura = QtWidgets.QFrame(self.page_remanufatura)
        self.frameFormLayout_remanufatura.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frameFormLayout_remanufatura.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFormLayout_remanufatura.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameFormLayout_remanufatura.setObjectName("frameFormLayout_remanufatura")
        self.formLayout_5 = QtWidgets.QFormLayout(self.frameFormLayout_remanufatura)
        self.formLayout_5.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_5.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_casco = QtWidgets.QLabel(self.frameFormLayout_remanufatura)
        self.label_casco.setObjectName("label_casco")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_casco)
        self.horizontalLayout_casco = QtWidgets.QHBoxLayout()
        self.horizontalLayout_casco.setObjectName("horizontalLayout_casco")
        self.lineEdit_casco_id = QtWidgets.QLineEdit(self.frameFormLayout_remanufatura)
        self.lineEdit_casco_id.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_casco_id.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_casco_id.setInputMask("")
        self.lineEdit_casco_id.setObjectName("lineEdit_casco_id")
        self.horizontalLayout_casco.addWidget(self.lineEdit_casco_id)
        self.lineEdit_casco = QtWidgets.QLineEdit(self.frameFormLayout_remanufatura)
        self.lineEdit_casco.setEnabled(False)
        self.lineEdit_casco.setObjectName("lineEdit_casco")
        self.horizontalLayout_casco.addWidget(self.lineEdit_casco)
        self.formLayout_5.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_casco)
        self.label_insumo = QtWidgets.QLabel(self.frameFormLayout_remanufatura)
        self.label_insumo.setObjectName("label_insumo")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_insumo)
        self.horizontalLayout_insumo = QtWidgets.QHBoxLayout()
        self.horizontalLayout_insumo.setObjectName("horizontalLayout_insumo")
        self.lineEdit_insumo_id = QtWidgets.QLineEdit(self.frameFormLayout_remanufatura)
        self.lineEdit_insumo_id.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_insumo_id.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_insumo_id.setInputMask("")
        self.lineEdit_insumo_id.setObjectName("lineEdit_insumo_id")
        self.horizontalLayout_insumo.addWidget(self.lineEdit_insumo_id)
        self.lineEdit_insumo = QtWidgets.QLineEdit(self.frameFormLayout_remanufatura)
        self.lineEdit_insumo.setEnabled(False)
        self.lineEdit_insumo.setObjectName("lineEdit_insumo")
        self.horizontalLayout_insumo.addWidget(self.lineEdit_insumo)
        self.formLayout_5.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_insumo)
        self.horizontalLayout_check_casco = QtWidgets.QHBoxLayout()
        self.horizontalLayout_check_casco.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_check_casco.setObjectName("horizontalLayout_check_casco")
        self.checkBox_reutilizar_casco = QtWidgets.QCheckBox(self.frameFormLayout_remanufatura)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.checkBox_reutilizar_casco.setFont(font)
        self.checkBox_reutilizar_casco.setToolTipDuration(5)
        self.checkBox_reutilizar_casco.setStatusTip("")
        self.checkBox_reutilizar_casco.setText("")
        self.checkBox_reutilizar_casco.setObjectName("checkBox_reutilizar_casco")
        self.horizontalLayout_check_casco.addWidget(self.checkBox_reutilizar_casco)
        self.formLayout_5.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_check_casco)
        self.label_reutilizar_casco = QtWidgets.QLabel(self.frameFormLayout_remanufatura)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_reutilizar_casco.setFont(font)
        self.label_reutilizar_casco.setToolTipDuration(5)
        self.label_reutilizar_casco.setObjectName("label_reutilizar_casco")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_reutilizar_casco)
        self.gridLayout_9.addWidget(self.frameFormLayout_remanufatura, 0, 0, 1, 1)
        self.stackedWidget_item.addWidget(self.page_remanufatura)
        self.verticalLayout_3.addWidget(self.stackedWidget_item)
        self.formLayout_quantidades = QtWidgets.QFormLayout()
        self.formLayout_quantidades.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_quantidades.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_quantidades.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_quantidades.setContentsMargins(9, 6, 9, 6)
        self.formLayout_quantidades.setObjectName("formLayout_quantidades")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_quantidade = QtWidgets.QLabel(self.frame_items)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.label_quantidade.setFont(font)
        self.label_quantidade.setWordWrap(False)
        self.label_quantidade.setObjectName("label_quantidade")
        self.horizontalLayout_9.addWidget(self.label_quantidade)
        self.label_UNIDADE_MEDIDA = QtWidgets.QLabel(self.frame_items)
        self.label_UNIDADE_MEDIDA.setText("")
        self.label_UNIDADE_MEDIDA.setObjectName("label_UNIDADE_MEDIDA")
        self.horizontalLayout_9.addWidget(self.label_UNIDADE_MEDIDA)
        self.formLayout_quantidades.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_9)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setContentsMargins(6, -1, -1, -1)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.lineEdit_quantidade = QtWidgets.QLineEdit(self.frame_items)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_quantidade.sizePolicy().hasHeightForWidth())
        self.lineEdit_quantidade.setSizePolicy(sizePolicy)
        self.lineEdit_quantidade.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_quantidade.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_quantidade.setInputMask("")
        self.lineEdit_quantidade.setText("")
        self.lineEdit_quantidade.setFrame(True)
        self.lineEdit_quantidade.setCursorPosition(0)
        self.lineEdit_quantidade.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_quantidade.setReadOnly(False)
        self.lineEdit_quantidade.setObjectName("lineEdit_quantidade")
        self.horizontalLayout_12.addWidget(self.lineEdit_quantidade)
        self.label_valor_unitario = QtWidgets.QLabel(self.frame_items)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_valor_unitario.sizePolicy().hasHeightForWidth())
        self.label_valor_unitario.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(50)
        font.setBold(False)
        self.label_valor_unitario.setFont(font)
        self.label_valor_unitario.setObjectName("label_valor_unitario")
        self.horizontalLayout_12.addWidget(self.label_valor_unitario)
        self.lineEdit_valor_unitario = QtWidgets.QLineEdit(self.frame_items)
        self.lineEdit_valor_unitario.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_valor_unitario.setInputMask("")
        self.lineEdit_valor_unitario.setText("")
        self.lineEdit_valor_unitario.setMaxLength(32767)
        self.lineEdit_valor_unitario.setCursorPosition(0)
        self.lineEdit_valor_unitario.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_valor_unitario.setObjectName("lineEdit_valor_unitario")
        self.horizontalLayout_12.addWidget(self.lineEdit_valor_unitario)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.frame_items)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        self.lineEdit_valor_total_item = QtWidgets.QLineEdit(self.frame_items)
        self.lineEdit_valor_total_item.setEnabled(False)
        self.lineEdit_valor_total_item.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_valor_total_item.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lineEdit_valor_total_item.setFont(font)
        self.lineEdit_valor_total_item.setInputMask("")
        self.lineEdit_valor_total_item.setText("")
        self.lineEdit_valor_total_item.setFrame(False)
        self.lineEdit_valor_total_item.setCursorPosition(0)
        self.lineEdit_valor_total_item.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_valor_total_item.setObjectName("lineEdit_valor_total_item")
        self.horizontalLayout_12.addWidget(self.lineEdit_valor_total_item)
        self.formLayout_quantidades.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_12)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setContentsMargins(6, 9, -1, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.label_valor_total_pedido = QtWidgets.QLabel(self.frame_items)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_valor_total_pedido.setFont(font)
        self.label_valor_total_pedido.setObjectName("label_valor_total_pedido")
        self.horizontalLayout_15.addWidget(self.label_valor_total_pedido)
        self.lineEdit_valor_total_pedido = QtWidgets.QLineEdit(self.frame_items)
        self.lineEdit_valor_total_pedido.setEnabled(False)
        self.lineEdit_valor_total_pedido.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.lineEdit_valor_total_pedido.setFont(font)
        self.lineEdit_valor_total_pedido.setInputMask("")
        self.lineEdit_valor_total_pedido.setText("")
        self.lineEdit_valor_total_pedido.setFrame(False)
        self.lineEdit_valor_total_pedido.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_valor_total_pedido.setObjectName("lineEdit_valor_total_pedido")
        self.horizontalLayout_15.addWidget(self.lineEdit_valor_total_pedido)
        self.formLayout_quantidades.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_15)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout_quantidades.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.formLayout_quantidades)
        self.horizontalLayout_7.addWidget(self.frame_items)
        self.frame_item_buttons = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_item_buttons.sizePolicy().hasHeightForWidth())
        self.frame_item_buttons.setSizePolicy(sizePolicy)
        self.frame_item_buttons.setMinimumSize(QtCore.QSize(110, 0))
        self.frame_item_buttons.setMaximumSize(QtCore.QSize(150, 16777215))
        self.frame_item_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_item_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_item_buttons.setObjectName("frame_item_buttons")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_item_buttons)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.buttonBox_item = QtWidgets.QDialogButtonBox(self.frame_item_buttons)
        self.buttonBox_item.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox_item.sizePolicy().hasHeightForWidth())
        self.buttonBox_item.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.buttonBox_item.setFont(font)
        self.buttonBox_item.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox_item.setAutoFillBackground(False)
        self.buttonBox_item.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox_item.setStandardButtons(QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Reset|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox_item.setCenterButtons(False)
        self.buttonBox_item.setObjectName("buttonBox_item")
        self.gridLayout_6.addWidget(self.buttonBox_item, 1, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.frame_item_buttons)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_campos, "")
        self.tab_tabela = QtWidgets.QWidget()
        self.tab_tabela.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_tabela.sizePolicy().hasHeightForWidth())
        self.tab_tabela.setSizePolicy(sizePolicy)
        self.tab_tabela.setMaximumSize(QtCore.QSize(746, 265))
        self.tab_tabela.setObjectName("tab_tabela")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_tabela)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_tabela = QtWidgets.QWidget(self.tab_tabela)
        self.widget_tabela.setAutoFillBackground(False)
        self.widget_tabela.setObjectName("widget_tabela")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_tabela)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tableWidget_items = QtWidgets.QTableWidget(self.widget_tabela)
        self.tableWidget_items.setAutoScrollMargin(17)
        self.tableWidget_items.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_items.setProperty("showDropIndicator", False)
        self.tableWidget_items.setAlternatingRowColors(True)
        self.tableWidget_items.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_items.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_items.setShowGrid(True)
        self.tableWidget_items.setWordWrap(False)
        self.tableWidget_items.setObjectName("tableWidget_items")
        self.tableWidget_items.setColumnCount(1)
        self.tableWidget_items.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_items.setHorizontalHeaderItem(0, item)
        self.tableWidget_items.horizontalHeader().setVisible(False)
        self.tableWidget_items.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_items.horizontalHeader().setHighlightSections(False)
        self.tableWidget_items.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_items.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_items.verticalHeader().setVisible(False)
        self.tableWidget_items.verticalHeader().setHighlightSections(False)
        self.gridLayout_5.addWidget(self.tableWidget_items, 0, 0, 1, 1)
        self.horizontalLayout_5.addWidget(self.widget_tabela)
        self.tabWidget.addTab(self.tab_tabela, "")
        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_items, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_contents)
        self.frame_buttons = QtWidgets.QFrame(CadastroPedido)
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
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(CadastroPedido)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_item.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(CadastroPedido)

    def retranslateUi(self, CadastroPedido):
        CadastroPedido.setWindowTitle(QtWidgets.QApplication.translate("CadastroPedido", "Cadastrar Pedido", None, -1))
        self.pushButton_cadastrar.setText(QtWidgets.QApplication.translate("CadastroPedido", "Cadastrar", None, -1))
        self.pushButton_editar.setText(QtWidgets.QApplication.translate("CadastroPedido", "Editar", None, -1))
        self.pushButton_excluir.setText(QtWidgets.QApplication.translate("CadastroPedido", "Excluir", None, -1))
        self.pushButton_localizar.setText(QtWidgets.QApplication.translate("CadastroPedido", "Localizar", None, -1))
        self.groupBox_identificacao.setTitle(QtWidgets.QApplication.translate("CadastroPedido", "Identificação", None, -1))
        self.formGroupBox_pessoa.setTitle(QtWidgets.QApplication.translate("CadastroPedido", "Pessoa", None, -1))
        self.label_documento.setText(QtWidgets.QApplication.translate("CadastroPedido", "CPF/CNPJ", None, -1))
        self.label_data.setText(QtWidgets.QApplication.translate("CadastroPedido", "Data Entrega", None, -1))
        self.groupBox_items.setTitle(QtWidgets.QApplication.translate("CadastroPedido", "Itens", None, -1))
        self.radioButton_mercadoria.setText(QtWidgets.QApplication.translate("CadastroPedido", "Mercadoria", None, -1))
        self.radioButton_remanufatura.setText(QtWidgets.QApplication.translate("CadastroPedido", "Remanufatura", None, -1))
        self.label_mercadoria.setText(QtWidgets.QApplication.translate("CadastroPedido", "Mercadoria", None, -1))
        self.label_casco.setText(QtWidgets.QApplication.translate("CadastroPedido", "Casco", None, -1))
        self.label_insumo.setText(QtWidgets.QApplication.translate("CadastroPedido", "Insumo", None, -1))
        self.checkBox_reutilizar_casco.setToolTip(QtWidgets.QApplication.translate("CadastroPedido", "Define se irá utilizar remanufaturas que já foram realizadas ou será registrada uma nova remanufatura", None, -1))
        self.label_reutilizar_casco.setToolTip(QtWidgets.QApplication.translate("CadastroPedido", "Define se irá utilizar remanufaturas que já foram realizadas ou será registrada uma nova remanufatura", None, -1))
        self.label_reutilizar_casco.setText(QtWidgets.QApplication.translate("CadastroPedido", "Não reutilizar remanufaturas ", None, -1))
        self.label_quantidade.setText(QtWidgets.QApplication.translate("CadastroPedido", "Quantidade (Un)", None, -1))
        self.lineEdit_quantidade.setPlaceholderText(QtWidgets.QApplication.translate("CadastroPedido", "0", None, -1))
        self.label_valor_unitario.setText(QtWidgets.QApplication.translate("CadastroPedido", "Valor Unitário (R$)", None, -1))
        self.lineEdit_valor_unitario.setPlaceholderText(QtWidgets.QApplication.translate("CadastroPedido", "0,00", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("CadastroPedido", "Total Item (R$)", None, -1))
        self.lineEdit_valor_total_item.setPlaceholderText(QtWidgets.QApplication.translate("CadastroPedido", "0,00", None, -1))
        self.label_valor_total_pedido.setText(QtWidgets.QApplication.translate("CadastroPedido", "Total Pedido (R$)", None, -1))
        self.lineEdit_valor_total_pedido.setPlaceholderText(QtWidgets.QApplication.translate("CadastroPedido", "0,00", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_campos), QtWidgets.QApplication.translate("CadastroPedido", "Campos", None, -1))
        self.tableWidget_items.setSortingEnabled(True)
        self.tableWidget_items.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("CadastroPedido", "ID", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tabela), QtWidgets.QApplication.translate("CadastroPedido", "Linhas", None, -1))

