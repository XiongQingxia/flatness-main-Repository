# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\programdata\pycharm\首钢报告\GUI\wsk_work\轧辊服役期2022\rolling_time_weight.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RollingInfo(object):
    def setupUi(self, Dialog_3):
        Dialog_3.setObjectName("Dialog_3")
        Dialog_3.resize(1106, 865)
        Dialog_3.setMinimumSize(QtCore.QSize(1106, 865))
        self.gridLayout = QtWidgets.QGridLayout(Dialog_3)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog_3)
        font = QtGui.QFont()
        font.setFamily("华光细圆_CNKI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox::title{\n"
"    font-size: 13px;\n"
"    font-weight: bold;\n"
"    }")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.comboBox_jijia = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_jijia.setFont(font)
        self.comboBox_jijia.setObjectName("comboBox_jijia")
        self.comboBox_jijia.addItem("")
        self.comboBox_jijia.addItem("")
        self.comboBox_jijia.addItem("")
        self.comboBox_jijia.addItem("")
        self.comboBox_jijia.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_jijia)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_5.setStretch(2, 1)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.comboBox_BUR = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_BUR.setFont(font)
        self.comboBox_BUR.setObjectName("comboBox_BUR")
        self.verticalLayout_4.addWidget(self.comboBox_BUR)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.horizontalLayout_9.setStretch(0, 8)
        self.horizontalLayout_9.setStretch(1, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.comboBox_IMR = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_IMR.setFont(font)
        self.comboBox_IMR.setObjectName("comboBox_IMR")
        self.verticalLayout_5.addWidget(self.comboBox_IMR)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.lineEdit_IMR = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_IMR.setEnabled(True)
        self.lineEdit_IMR.setObjectName("lineEdit_IMR")
        self.horizontalLayout_6.addWidget(self.lineEdit_IMR)
        self.horizontalLayout_6.setStretch(0, 8)
        self.horizontalLayout_6.setStretch(1, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.comboBox_WR = QtWidgets.QComboBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_WR.setFont(font)
        self.comboBox_WR.setObjectName("comboBox_WR")
        self.verticalLayout_6.addWidget(self.comboBox_WR)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem10)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.lineEdit_WR = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_WR.setEnabled(True)
        self.lineEdit_WR.setObjectName("lineEdit_WR")
        self.horizontalLayout_7.addWidget(self.lineEdit_WR)
        self.horizontalLayout_7.setStretch(0, 8)
        self.horizontalLayout_7.setStretch(1, 1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 2)
        self.verticalLayout_8.setStretch(2, 2)
        self.verticalLayout_8.setStretch(3, 2)
        self.horizontalLayout_18.addWidget(self.groupBox_2)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton_BUR_shang = QtWidgets.QPushButton(Dialog_3)
        self.pushButton_BUR_shang.setObjectName("pushButton_BUR_shang")
        self.horizontalLayout_11.addWidget(self.pushButton_BUR_shang)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.pushButton_BUR = QtWidgets.QPushButton(Dialog_3)
        self.pushButton_BUR.setObjectName("pushButton_BUR")
        self.horizontalLayout_11.addWidget(self.pushButton_BUR)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.pushButton_BUR_xia = QtWidgets.QPushButton(Dialog_3)
        self.pushButton_BUR_xia.setObjectName("pushButton_BUR_xia")
        self.horizontalLayout_11.addWidget(self.pushButton_BUR_xia)
        self.horizontalLayout_11.setStretch(0, 2)
        self.horizontalLayout_11.setStretch(1, 1)
        self.horizontalLayout_11.setStretch(2, 2)
        self.horizontalLayout_11.setStretch(3, 1)
        self.horizontalLayout_11.setStretch(4, 2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_BUR = QtWidgets.QHBoxLayout()
        self.horizontalLayout_BUR.setObjectName("horizontalLayout_BUR")
        self.textEdit = QtWidgets.QTextEdit(Dialog_3)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_BUR.addWidget(self.textEdit)
        self.verticalLayout_9.addLayout(self.horizontalLayout_BUR)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem13)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_12.addLayout(self.verticalLayout)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem14)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_18.addLayout(self.verticalLayout_9)
        self.horizontalLayout_18.setStretch(0, 2)
        self.horizontalLayout_18.setStretch(1, 3)
        self.verticalLayout_12.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.pushButton_IMR_shang = QtWidgets.QPushButton(Dialog_3)
        self.pushButton_IMR_shang.setObjectName("pushButton_IMR_shang")
        self.horizontalLayout_13.addWidget(self.pushButton_IMR_shang)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem15)
        self.pushButton_IMR = QtWidgets.QPushButton(Dialog_3)
        self.pushButton_IMR.setObjectName("pushButton_IMR")
        self.horizontalLayout_13.addWidget(self.pushButton_IMR)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem16)
        self.pushButton_IMR_xia = QtWidgets.QPushButton(Dialog_3)
        self.pushButton_IMR_xia.setObjectName("pushButton_IMR_xia")
        self.horizontalLayout_13.addWidget(self.pushButton_IMR_xia)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_IMR = QtWidgets.QHBoxLayout()
        self.horizontalLayout_IMR.setObjectName("horizontalLayout_IMR")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog_3)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_IMR.addWidget(self.textEdit_2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_IMR)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem17)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_14.addLayout(self.verticalLayout_2)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem18)
        self.verticalLayout_10.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_17.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushButton_WR_shang = QtWidgets.QPushButton(Dialog_3)
        self.pushButton_WR_shang.setObjectName("pushButton_WR_shang")
        self.horizontalLayout_16.addWidget(self.pushButton_WR_shang)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem19)
        self.pushButton_WR = QtWidgets.QPushButton(Dialog_3)
        self.pushButton_WR.setObjectName("pushButton_WR")
        self.horizontalLayout_16.addWidget(self.pushButton_WR)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem20)
        self.pushButton_WR_xia = QtWidgets.QPushButton(Dialog_3)
        self.pushButton_WR_xia.setObjectName("pushButton_WR_xia")
        self.horizontalLayout_16.addWidget(self.pushButton_WR_xia)
        self.verticalLayout_11.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_WR = QtWidgets.QHBoxLayout()
        self.horizontalLayout_WR.setObjectName("horizontalLayout_WR")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog_3)
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout_WR.addWidget(self.textEdit_3)
        self.verticalLayout_11.addLayout(self.horizontalLayout_WR)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem21)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_15.addLayout(self.verticalLayout_3)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem22)
        self.verticalLayout_11.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_17.addLayout(self.verticalLayout_11)
        self.horizontalLayout_17.setStretch(0, 2)
        self.horizontalLayout_17.setStretch(1, 3)
        self.verticalLayout_12.addLayout(self.horizontalLayout_17)
        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 1)
        self.gridLayout.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.retranslateUi(Dialog_3)
        QtCore.QMetaObject.connectSlotsByName(Dialog_3)

    def retranslateUi(self, Dialog_3):
        _translate = QtCore.QCoreApplication.translate
        Dialog_3.setWindowTitle(_translate("Dialog_3", "轧辊服役天数和轧制信息"))
        self.groupBox_2.setTitle(_translate("Dialog_3", "轧辊选择"))
        self.label_8.setText(_translate("Dialog_3", "选择机架："))
        self.comboBox_jijia.setItemText(0, _translate("Dialog_3", "1"))
        self.comboBox_jijia.setItemText(1, _translate("Dialog_3", "2"))
        self.comboBox_jijia.setItemText(2, _translate("Dialog_3", "3"))
        self.comboBox_jijia.setItemText(3, _translate("Dialog_3", "4"))
        self.comboBox_jijia.setItemText(4, _translate("Dialog_3", "5"))
        self.label.setText(_translate("Dialog_3", "支撑辊BUR"))
        self.label_2.setText(_translate("Dialog_3", "支撑辊下的中间辊IMR"))
        self.label_3.setText(_translate("Dialog_3", "中间辊下的工作辊WR"))
        self.pushButton_BUR_shang.setText(_translate("Dialog_3", "上一辊"))
        self.pushButton_BUR.setText(_translate("Dialog_3", "显示支撑辊下中间辊服役信息"))
        self.pushButton_BUR_xia.setText(_translate("Dialog_3", "下一辊"))
        self.pushButton_IMR_shang.setText(_translate("Dialog_3", "上一辊"))
        self.pushButton_IMR.setText(_translate("Dialog_3", "显示中间辊下工作辊服役信息"))
        self.pushButton_IMR_xia.setText(_translate("Dialog_3", "下一辊"))
        self.pushButton_WR_shang.setText(_translate("Dialog_3", "上一辊"))
        self.pushButton_WR.setText(_translate("Dialog_3", "显示工作辊下的带钢信息"))
        self.pushButton_WR_xia.setText(_translate("Dialog_3", "下一辊"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_3 = QtWidgets.QDialog()
    ui = Ui_RollingInfo()
    ui.setupUi(Dialog_3)
    Dialog_3.show()
    sys.exit(app.exec_())
