# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources\UI\CadastroMercadoria.ui',
# licensing of 'Resources\UI\CadastroMercadoria.ui' applies.
#
# Created: Thu Oct 17 01:09:27 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_CadastroMercadoria(object):
    def setupUi(self, CadastroMercadoria):
        CadastroMercadoria.setObjectName("CadastroMercadoria")
        CadastroMercadoria.setWindowModality(QtCore.Qt.NonModal)
        CadastroMercadoria.resize(640, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CadastroMercadoria.sizePolicy().hasHeightForWidth())
        CadastroMercadoria.setSizePolicy(sizePolicy)
        CadastroMercadoria.setMinimumSize(QtCore.QSize(640, 300))
        CadastroMercadoria.setMaximumSize(QtCore.QSize(640, 400))
        self.gridLayout = QtWidgets.QGridLayout(CadastroMercadoria)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_menu = QtWidgets.QWidget(CadastroMercadoria)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menu.sizePolicy().hasHeightForWidth())
        self.frame_menu.setSizePolicy(sizePolicy)
        self.frame_menu.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_menu.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_menu.setObjectName("frame_menu")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_menu)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame = QtWidgets.QFrame(self.frame_menu)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_cadastrar = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_cadastrar.setFont(font)
        self.pushButton_cadastrar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_cadastrar.setCheckable(False)
        self.pushButton_cadastrar.setDefault(False)
        self.pushButton_cadastrar.setFlat(True)
        self.pushButton_cadastrar.setObjectName("pushButton_cadastrar")
        self.horizontalLayout_3.addWidget(self.pushButton_cadastrar)
        self.pushButton_editar = QtWidgets.QPushButton(self.frame)
        self.pushButton_editar.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_editar.setFont(font)
        self.pushButton_editar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_editar.setCheckable(False)
        self.pushButton_editar.setDefault(False)
        self.pushButton_editar.setFlat(True)
        self.pushButton_editar.setObjectName("pushButton_editar")
        self.horizontalLayout_3.addWidget(self.pushButton_editar)
        self.pushButton_excluir = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_excluir.setFont(font)
        self.pushButton_excluir.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_excluir.setCheckable(False)
        self.pushButton_excluir.setDefault(False)
        self.pushButton_excluir.setFlat(True)
        self.pushButton_excluir.setObjectName("pushButton_excluir")
        self.horizontalLayout_3.addWidget(self.pushButton_excluir)
        self.pushButton_localizar = QtWidgets.QPushButton(self.frame)
        self.pushButton_localizar.setBaseSize(QtCore.QSize(1, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_localizar.setFont(font)
        self.pushButton_localizar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_localizar.setCheckable(False)
        self.pushButton_localizar.setDefault(False)
        self.pushButton_localizar.setFlat(True)
        self.pushButton_localizar.setObjectName("pushButton_localizar")
        self.horizontalLayout_3.addWidget(self.pushButton_localizar)
        self.horizontalLayout_4.addWidget(self.frame)
        self.verticalLayout.addWidget(self.frame_menu)
        self.frame_contents = QtWidgets.QFrame(CadastroMercadoria)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_contents.sizePolicy().hasHeightForWidth())
        self.frame_contents.setSizePolicy(sizePolicy)
        self.frame_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contents.setObjectName("frame_contents")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_contents)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox_mercadoria = QtWidgets.QGroupBox(self.frame_contents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_mercadoria.sizePolicy().hasHeightForWidth())
        self.groupBox_mercadoria.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_mercadoria.setFont(font)
        self.groupBox_mercadoria.setObjectName("groupBox_mercadoria")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_mercadoria)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox_mercadoria)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setSizeIncrement(QtCore.QSize(0, 3))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_casco = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_casco.sizePolicy().hasHeightForWidth())
        self.page_casco.setSizePolicy(sizePolicy)
        self.page_casco.setObjectName("page_casco")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_casco)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_casco = QtWidgets.QFrame(self.page_casco)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_casco.sizePolicy().hasHeightForWidth())
        self.frame_casco.setSizePolicy(sizePolicy)
        self.frame_casco.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.frame_casco.setFont(font)
        self.frame_casco.setObjectName("frame_casco")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_casco)
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_3.setHorizontalSpacing(10)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_insumo = QtWidgets.QLabel(self.frame_casco)
        self.label_insumo.setMinimumSize(QtCore.QSize(0, 0))
        self.label_insumo.setObjectName("label_insumo")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_insumo)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit_insumo_id = QtWidgets.QLineEdit(self.frame_casco)
        self.lineEdit_insumo_id.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_insumo_id.setObjectName("lineEdit_insumo_id")
        self.horizontalLayout_7.addWidget(self.lineEdit_insumo_id)
        self.lineEdit_insumo = QtWidgets.QLineEdit(self.frame_casco)
        self.lineEdit_insumo.setEnabled(False)
        self.lineEdit_insumo.setObjectName("lineEdit_insumo")
        self.horizontalLayout_7.addWidget(self.lineEdit_insumo)
        self.lineEdit_insumo_fabricante = QtWidgets.QLineEdit(self.frame_casco)
        self.lineEdit_insumo_fabricante.setEnabled(False)
        self.lineEdit_insumo_fabricante.setObjectName("lineEdit_insumo_fabricante")
        self.horizontalLayout_7.addWidget(self.lineEdit_insumo_fabricante)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.label_quantidade = QtWidgets.QLabel(self.frame_casco)
        self.label_quantidade.setObjectName("label_quantidade")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_quantidade)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_quantidade_insumo = QtWidgets.QLineEdit(self.frame_casco)
        self.lineEdit_quantidade_insumo.setMinimumSize(QtCore.QSize(50, 0))
        self.lineEdit_quantidade_insumo.setMaximumSize(QtCore.QSize(90, 16777215))
        self.lineEdit_quantidade_insumo.setText("")
        self.lineEdit_quantidade_insumo.setObjectName("lineEdit_quantidade_insumo")
        self.horizontalLayout_10.addWidget(self.lineEdit_quantidade_insumo)
        self.label = QtWidgets.QLabel(self.frame_casco)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.comboBox_unidade_medida_insumo = QtWidgets.QComboBox(self.frame_casco)
        self.comboBox_unidade_medida_insumo.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_unidade_medida_insumo.setMaximumSize(QtCore.QSize(130, 16777215))
        self.comboBox_unidade_medida_insumo.setObjectName("comboBox_unidade_medida_insumo")
        self.horizontalLayout_10.addWidget(self.comboBox_unidade_medida_insumo)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.horizontalLayout_5.addWidget(self.frame_casco)
        self.stackedWidget.addWidget(self.page_casco)
        self.page_insumo = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_insumo.sizePolicy().hasHeightForWidth())
        self.page_insumo.setSizePolicy(sizePolicy)
        self.page_insumo.setObjectName("page_insumo")
        self._2 = QtWidgets.QVBoxLayout(self.page_insumo)
        self._2.setSpacing(0)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setObjectName("_2")
        self.frame_insumo = QtWidgets.QFrame(self.page_insumo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_insumo.sizePolicy().hasHeightForWidth())
        self.frame_insumo.setSizePolicy(sizePolicy)
        self.frame_insumo.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.frame_insumo.setFont(font)
        self.frame_insumo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_insumo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_insumo.setObjectName("frame_insumo")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_insumo)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_insumo)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.radioButton_pb = QtWidgets.QRadioButton(self.frame_insumo)
        self.radioButton_pb.setChecked(True)
        self.radioButton_pb.setObjectName("radioButton_pb")
        self.horizontalLayout_13.addWidget(self.radioButton_pb)
        self.radioButton_cor = QtWidgets.QRadioButton(self.frame_insumo)
        self.radioButton_cor.setObjectName("radioButton_cor")
        self.horizontalLayout_13.addWidget(self.radioButton_cor)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_13)
        self.label_quantidade_embalagem = QtWidgets.QLabel(self.frame_insumo)
        self.label_quantidade_embalagem.setObjectName("label_quantidade_embalagem")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_quantidade_embalagem)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_quantidade_embalagem = QtWidgets.QLineEdit(self.frame_insumo)
        self.lineEdit_quantidade_embalagem.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_quantidade_embalagem.setObjectName("lineEdit_quantidade_embalagem")
        self.horizontalLayout_6.addWidget(self.lineEdit_quantidade_embalagem)
        self.label_un_medida = QtWidgets.QLabel(self.frame_insumo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_un_medida.sizePolicy().hasHeightForWidth())
        self.label_un_medida.setSizePolicy(sizePolicy)
        self.label_un_medida.setObjectName("label_un_medida")
        self.horizontalLayout_6.addWidget(self.label_un_medida)
        self.comboBox_unidade_medida_embalagem = QtWidgets.QComboBox(self.frame_insumo)
        self.comboBox_unidade_medida_embalagem.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_unidade_medida_embalagem.setObjectName("comboBox_unidade_medida_embalagem")
        self.horizontalLayout_6.addWidget(self.comboBox_unidade_medida_embalagem)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self._2.addWidget(self.frame_insumo)
        self.stackedWidget.addWidget(self.page_insumo)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.formFrame = QtWidgets.QFrame(self.groupBox_mercadoria)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formFrame.sizePolicy().hasHeightForWidth())
        self.formFrame.setSizePolicy(sizePolicy)
        self.formFrame.setMinimumSize(QtCore.QSize(115, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.formFrame.setFont(font)
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(10, -1, 10, -1)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(9)
        self.formLayout.setObjectName("formLayout")
        self.label_codigo = QtWidgets.QLabel(self.formFrame)
        self.label_codigo.setObjectName("label_codigo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_codigo)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setContentsMargins(-1, -1, 9, -1)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lineEdit_codigo = QtWidgets.QLineEdit(self.formFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_codigo.sizePolicy().hasHeightForWidth())
        self.lineEdit_codigo.setSizePolicy(sizePolicy)
        self.lineEdit_codigo.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEdit_codigo.setMaximumSize(QtCore.QSize(120, 16777215))
        self.lineEdit_codigo.setText("")
        self.lineEdit_codigo.setMaxLength(15)
        self.lineEdit_codigo.setObjectName("lineEdit_codigo")
        self.horizontalLayout_11.addWidget(self.lineEdit_codigo)
        self.checkBox_permite_venda = QtWidgets.QCheckBox(self.formFrame)
        self.checkBox_permite_venda.setObjectName("checkBox_permite_venda")
        self.horizontalLayout_11.addWidget(self.checkBox_permite_venda)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.label_tipo = QtWidgets.QLabel(self.formFrame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_tipo.setFont(font)
        self.label_tipo.setObjectName("label_tipo")
        self.horizontalLayout_11.addWidget(self.label_tipo)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_11)
        self.label_descricao = QtWidgets.QLabel(self.formFrame)
        self.label_descricao.setObjectName("label_descricao")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_descricao)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_descricao = QtWidgets.QLineEdit(self.formFrame)
        self.lineEdit_descricao.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_descricao.setInputMask("")
        self.lineEdit_descricao.setMaxLength(120)
        self.lineEdit_descricao.setClearButtonEnabled(False)
        self.lineEdit_descricao.setObjectName("lineEdit_descricao")
        self.horizontalLayout.addWidget(self.lineEdit_descricao)
        self.checkBox_ativo = QtWidgets.QCheckBox(self.formFrame)
        self.checkBox_ativo.setObjectName("checkBox_ativo")
        self.horizontalLayout.addWidget(self.checkBox_ativo)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_fabricante = QtWidgets.QLabel(self.formFrame)
        self.label_fabricante.setObjectName("label_fabricante")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_fabricante)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_fabricante = QtWidgets.QComboBox(self.formFrame)
        self.comboBox_fabricante.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox_fabricante.setMaximumSize(QtCore.QSize(16777215, 20))
        self.comboBox_fabricante.setAcceptDrops(False)
        self.comboBox_fabricante.setEditable(False)
        self.comboBox_fabricante.setDuplicatesEnabled(False)
        self.comboBox_fabricante.setFrame(True)
        self.comboBox_fabricante.setObjectName("comboBox_fabricante")
        self.horizontalLayout_2.addWidget(self.comboBox_fabricante)
        self.lineEdit_fabricante = QtWidgets.QLineEdit(self.formFrame)
        self.lineEdit_fabricante.setMinimumSize(QtCore.QSize(200, 0))
        self.lineEdit_fabricante.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lineEdit_fabricante.setMaxLength(80)
        self.lineEdit_fabricante.setFrame(True)
        self.lineEdit_fabricante.setDragEnabled(True)
        self.lineEdit_fabricante.setClearButtonEnabled(True)
        self.lineEdit_fabricante.setObjectName("lineEdit_fabricante")
        self.horizontalLayout_2.addWidget(self.lineEdit_fabricante)
        self.toolButton_addFabricante = QtWidgets.QToolButton(self.formFrame)
        self.toolButton_addFabricante.setMinimumSize(QtCore.QSize(20, 20))
        self.toolButton_addFabricante.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setBold(False)
        self.toolButton_addFabricante.setFont(font)
        self.toolButton_addFabricante.setAutoFillBackground(True)
        self.toolButton_addFabricante.setIconSize(QtCore.QSize(16, 16))
        self.toolButton_addFabricante.setCheckable(True)
        self.toolButton_addFabricante.setChecked(False)
        self.toolButton_addFabricante.setAutoRepeat(False)
        self.toolButton_addFabricante.setAutoExclusive(False)
        self.toolButton_addFabricante.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButton_addFabricante.setAutoRaise(False)
        self.toolButton_addFabricante.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton_addFabricante.setObjectName("toolButton_addFabricante")
        self.horizontalLayout_2.addWidget(self.toolButton_addFabricante)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_valor_venda = QtWidgets.QLabel(self.formFrame)
        self.label_valor_venda.setObjectName("label_valor_venda")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_valor_venda)
        self.lineEdit_valor_venda = QtWidgets.QLineEdit(self.formFrame)
        self.lineEdit_valor_venda.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_valor_venda.setObjectName("lineEdit_valor_venda")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_valor_venda)
        self.gridLayout_2.addWidget(self.formFrame, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_mercadoria, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_contents)
        self.frame_buttons = QtWidgets.QFrame(CadastroMercadoria)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_buttons.sizePolicy().hasHeightForWidth())
        self.frame_buttons.setSizePolicy(sizePolicy)
        self.frame_buttons.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_buttons.setObjectName("frame_buttons")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_id = QtWidgets.QLabel(self.frame_buttons)
        self.label_id.setText("")
        self.label_id.setObjectName("label_id")
        self.horizontalLayout_8.addWidget(self.label_id)
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
        self.horizontalLayout_8.addWidget(self.lineEdit_id)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame_buttons)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_8.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.frame_buttons)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(CadastroMercadoria)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CadastroMercadoria)

    def retranslateUi(self, CadastroMercadoria):
        CadastroMercadoria.setWindowTitle(QtWidgets.QApplication.translate("CadastroMercadoria", "SOAD - Cadastrar Produto", None, -1))
        self.pushButton_cadastrar.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Cadastrar", None, -1))
        self.pushButton_editar.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Editar", None, -1))
        self.pushButton_excluir.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Excluir", None, -1))
        self.pushButton_localizar.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Localizar", None, -1))
        self.groupBox_mercadoria.setTitle(QtWidgets.QApplication.translate("CadastroMercadoria", "Mercadoria", None, -1))
        self.label_insumo.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Insumo", None, -1))
        self.label_quantidade.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Quantidade", None, -1))
        self.lineEdit_quantidade_insumo.setPlaceholderText(QtWidgets.QApplication.translate("CadastroMercadoria", "0,00", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Un. Medida", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Modo de Cor", None, -1))
        self.radioButton_pb.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Preto e Branco", None, -1))
        self.radioButton_cor.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Colorido", None, -1))
        self.label_quantidade_embalagem.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Quantidade (embalagem)", None, -1))
        self.lineEdit_quantidade_embalagem.setPlaceholderText(QtWidgets.QApplication.translate("CadastroMercadoria", "0,00", None, -1))
        self.label_un_medida.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Un. Medida", None, -1))
        self.label_codigo.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Código", None, -1))
        self.checkBox_permite_venda.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Permite Venda", None, -1))
        self.label_tipo.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "TIPO", None, -1))
        self.label_descricao.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Descrição", None, -1))
        self.checkBox_ativo.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Ativo", None, -1))
        self.label_fabricante.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Fabricante", None, -1))
        self.toolButton_addFabricante.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "+", None, -1))
        self.label_valor_venda.setText(QtWidgets.QApplication.translate("CadastroMercadoria", "Valor de venda (R$)", None, -1))
        self.lineEdit_valor_venda.setPlaceholderText(QtWidgets.QApplication.translate("CadastroMercadoria", "0,00", None, -1))

