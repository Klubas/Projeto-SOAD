# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/UI/Componentes/FiltroEstoque.ui',
# licensing of 'Resources/UI/Componentes/FiltroEstoque.ui' applies.
#
# Created: Sun Nov  3 01:30:14 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FiltroEstoque(object):
    def setupUi(self, FiltroEstoque):
        FiltroEstoque.setObjectName("FiltroEstoque")
        FiltroEstoque.resize(645, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FiltroEstoque.sizePolicy().hasHeightForWidth())
        FiltroEstoque.setSizePolicy(sizePolicy)
        FiltroEstoque.setMinimumSize(QtCore.QSize(600, 250))
        FiltroEstoque.setMaximumSize(QtCore.QSize(645, 280))
        FiltroEstoque.setSizeIncrement(QtCore.QSize(100, 50))
        FiltroEstoque.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        FiltroEstoque.setSizeGripEnabled(False)
        self.gridLayout = QtWidgets.QGridLayout(FiltroEstoque)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(FiltroEstoque)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formFrame = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formFrame.sizePolicy().hasHeightForWidth())
        self.formFrame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.formFrame.setFont(font)
        self.formFrame.setObjectName("formFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.formFrame)
        self.gridLayout_3.setContentsMargins(9, -1, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.formFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_abertos = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_abertos.setObjectName("checkBox_abertos")
        self.verticalLayout_2.addWidget(self.checkBox_abertos)
        self.checkBox_vazios = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_vazios.setObjectName("checkBox_vazios")
        self.verticalLayout_2.addWidget(self.checkBox_vazios)
        self.checkBox_inativos = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_inativos.setEnabled(True)
        self.checkBox_inativos.setObjectName("checkBox_inativos")
        self.verticalLayout_2.addWidget(self.checkBox_inativos)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_mercadoria = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_mercadoria.setObjectName("checkBox_mercadoria")
        self.verticalLayout.addWidget(self.checkBox_mercadoria)
        self.checkBox_insumo = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_insumo.setObjectName("checkBox_insumo")
        self.verticalLayout.addWidget(self.checkBox_insumo)
        self.checkBox_casco = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_casco.setObjectName("checkBox_casco")
        self.verticalLayout.addWidget(self.checkBox_casco)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.gridLayout_3.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.formFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalGroupBox_2 = QtWidgets.QGroupBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalGroupBox_2.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox_2.setSizePolicy(sizePolicy)
        self.horizontalGroupBox_2.setCheckable(False)
        self.horizontalGroupBox_2.setObjectName("horizontalGroupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalGroupBox_2)
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_fornecedor_documento = QtWidgets.QLineEdit(self.horizontalGroupBox_2)
        self.lineEdit_fornecedor_documento.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_fornecedor_documento.setObjectName("lineEdit_fornecedor_documento")
        self.horizontalLayout_2.addWidget(self.lineEdit_fornecedor_documento)
        self.lineEdit_fornecedor = QtWidgets.QLineEdit(self.horizontalGroupBox_2)
        self.lineEdit_fornecedor.setEnabled(False)
        self.lineEdit_fornecedor.setObjectName("lineEdit_fornecedor")
        self.horizontalLayout_2.addWidget(self.lineEdit_fornecedor)
        self.verticalLayout_5.addWidget(self.horizontalGroupBox_2)
        self.horizontalGroupBox_3 = QtWidgets.QGroupBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalGroupBox_3.sizePolicy().hasHeightForWidth())
        self.horizontalGroupBox_3.setSizePolicy(sizePolicy)
        self.horizontalGroupBox_3.setCheckable(False)
        self.horizontalGroupBox_3.setObjectName("horizontalGroupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalGroupBox_3)
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_mercadoria_id = QtWidgets.QLineEdit(self.horizontalGroupBox_3)
        self.lineEdit_mercadoria_id.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_mercadoria_id.setObjectName("lineEdit_mercadoria_id")
        self.horizontalLayout_3.addWidget(self.lineEdit_mercadoria_id)
        self.lineEdit_mercadoria = QtWidgets.QLineEdit(self.horizontalGroupBox_3)
        self.lineEdit_mercadoria.setEnabled(False)
        self.lineEdit_mercadoria.setObjectName("lineEdit_mercadoria")
        self.horizontalLayout_3.addWidget(self.lineEdit_mercadoria)
        self.verticalLayout_5.addWidget(self.horizontalGroupBox_3)
        self.widget_4 = QtWidgets.QWidget(self.frame_3)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_entrada = QtWidgets.QGroupBox(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_entrada.sizePolicy().hasHeightForWidth())
        self.groupBox_entrada.setSizePolicy(sizePolicy)
        self.groupBox_entrada.setCheckable(True)
        self.groupBox_entrada.setChecked(False)
        self.groupBox_entrada.setObjectName("groupBox_entrada")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_entrada)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dateEdit_data_entrada1 = QtWidgets.QDateEdit(self.groupBox_entrada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_data_entrada1.sizePolicy().hasHeightForWidth())
        self.dateEdit_data_entrada1.setSizePolicy(sizePolicy)
        self.dateEdit_data_entrada1.setWrapping(False)
        self.dateEdit_data_entrada1.setFrame(False)
        self.dateEdit_data_entrada1.setReadOnly(False)
        self.dateEdit_data_entrada1.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit_data_entrada1.setCalendarPopup(True)
        self.dateEdit_data_entrada1.setDate(QtCore.QDate(2019, 1, 1))
        self.dateEdit_data_entrada1.setObjectName("dateEdit_data_entrada1")
        self.horizontalLayout.addWidget(self.dateEdit_data_entrada1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_entrada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dateEdit_data_entrada2 = QtWidgets.QDateEdit(self.groupBox_entrada)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_data_entrada2.sizePolicy().hasHeightForWidth())
        self.dateEdit_data_entrada2.setSizePolicy(sizePolicy)
        self.dateEdit_data_entrada2.setWrapping(False)
        self.dateEdit_data_entrada2.setFrame(False)
        self.dateEdit_data_entrada2.setReadOnly(False)
        self.dateEdit_data_entrada2.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit_data_entrada2.setCalendarPopup(True)
        self.dateEdit_data_entrada2.setDate(QtCore.QDate(2019, 12, 31))
        self.dateEdit_data_entrada2.setObjectName("dateEdit_data_entrada2")
        self.horizontalLayout.addWidget(self.dateEdit_data_entrada2)
        self.horizontalLayout_6.addWidget(self.groupBox_entrada)
        self.groupBox_saida = QtWidgets.QGroupBox(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_saida.sizePolicy().hasHeightForWidth())
        self.groupBox_saida.setSizePolicy(sizePolicy)
        self.groupBox_saida.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_saida.setCheckable(True)
        self.groupBox_saida.setChecked(False)
        self.groupBox_saida.setObjectName("groupBox_saida")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_saida)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dateEdit_data_saida1 = QtWidgets.QDateEdit(self.groupBox_saida)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_data_saida1.sizePolicy().hasHeightForWidth())
        self.dateEdit_data_saida1.setSizePolicy(sizePolicy)
        self.dateEdit_data_saida1.setWrapping(False)
        self.dateEdit_data_saida1.setFrame(False)
        self.dateEdit_data_saida1.setReadOnly(False)
        self.dateEdit_data_saida1.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit_data_saida1.setCalendarPopup(True)
        self.dateEdit_data_saida1.setDate(QtCore.QDate(2019, 1, 1))
        self.dateEdit_data_saida1.setObjectName("dateEdit_data_saida1")
        self.horizontalLayout_4.addWidget(self.dateEdit_data_saida1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_saida)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.dateEdit_data_saida2 = QtWidgets.QDateEdit(self.groupBox_saida)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit_data_saida2.sizePolicy().hasHeightForWidth())
        self.dateEdit_data_saida2.setSizePolicy(sizePolicy)
        self.dateEdit_data_saida2.setWrapping(False)
        self.dateEdit_data_saida2.setFrame(False)
        self.dateEdit_data_saida2.setReadOnly(False)
        self.dateEdit_data_saida2.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.dateEdit_data_saida2.setCalendarPopup(True)
        self.dateEdit_data_saida2.setDate(QtCore.QDate(2019, 12, 31))
        self.dateEdit_data_saida2.setObjectName("dateEdit_data_saida2")
        self.horizontalLayout_4.addWidget(self.dateEdit_data_saida2)
        self.horizontalLayout_6.addWidget(self.groupBox_saida)
        self.verticalLayout_5.addWidget(self.widget_4)
        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.formFrame, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(FiltroEstoque)
        QtCore.QMetaObject.connectSlotsByName(FiltroEstoque)

    def retranslateUi(self, FiltroEstoque):
        FiltroEstoque.setWindowTitle(QtWidgets.QApplication.translate("FiltroEstoque", "Filtro Estoque", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("FiltroEstoque", "Estoque", None, -1))
        self.checkBox_abertos.setText(QtWidgets.QApplication.translate("FiltroEstoque", "Abertos", None, -1))
        self.checkBox_vazios.setText(QtWidgets.QApplication.translate("FiltroEstoque", "Exibir vazios", None, -1))
        self.checkBox_inativos.setText(QtWidgets.QApplication.translate("FiltroEstoque", "Exibir inativos", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("FiltroEstoque", "Classificação", None, -1))
        self.checkBox_mercadoria.setText(QtWidgets.QApplication.translate("FiltroEstoque", "Mercadoria", None, -1))
        self.checkBox_insumo.setText(QtWidgets.QApplication.translate("FiltroEstoque", "Insumo", None, -1))
        self.checkBox_casco.setText(QtWidgets.QApplication.translate("FiltroEstoque", "Casco", None, -1))
        self.horizontalGroupBox_2.setTitle(QtWidgets.QApplication.translate("FiltroEstoque", "Fornecedor", None, -1))
        self.horizontalGroupBox_3.setTitle(QtWidgets.QApplication.translate("FiltroEstoque", "Mercadoria", None, -1))
        self.groupBox_entrada.setTitle(QtWidgets.QApplication.translate("FiltroEstoque", "Data de entrada", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("FiltroEstoque", "até", None, -1))
        self.groupBox_saida.setTitle(QtWidgets.QApplication.translate("FiltroEstoque", "Data de saída", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("FiltroEstoque", "até", None, -1))

