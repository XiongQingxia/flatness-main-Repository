# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiple_strategy.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SinglePolicyCompare")
        MainWindow.resize(1406, 1100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_xuanzeshuju = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_xuanzeshuju.setObjectName("pushButton_xuanzeshuju")
        self.horizontalLayout.addWidget(self.pushButton_xuanzeshuju)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox_celue1 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_celue1.setObjectName("comboBox_celue1")
        self.comboBox_celue1.addItem("")
        self.comboBox_celue1.addItem("")
        self.comboBox_celue1.addItem("")
        self.comboBox_celue1.addItem("")
        self.comboBox_celue1.addItem("")
        self.verticalLayout.addWidget(self.comboBox_celue1)
        self.comboBox_celue2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_celue2.setObjectName("comboBox_celue2")
        self.comboBox_celue2.addItem("")
        self.comboBox_celue2.addItem("")
        self.comboBox_celue2.addItem("")
        self.comboBox_celue2.addItem("")
        self.comboBox_celue2.addItem("")
        self.verticalLayout.addWidget(self.comboBox_celue2)
        self.pushButton_xianshituxiang = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_xianshituxiang.setObjectName("pushButton_xianshituxiang")
        self.verticalLayout.addWidget(self.pushButton_xianshituxiang)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.graphicsView_tuxing = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView_tuxing.setObjectName("graphicsView_tuxing")
        self.gridLayout_9.addWidget(self.graphicsView_tuxing, 0, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_qingkonghuabu = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_qingkonghuabu.setObjectName("pushButton_qingkonghuabu")
        self.horizontalLayout_6.addWidget(self.pushButton_qingkonghuabu)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.setStretch(0, 6)
        self.verticalLayout_6.setStretch(1, 1)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.graphicsView_tuxing_2 = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView_tuxing_2.setObjectName("graphicsView_tuxing_2")
        self.gridLayout_10.addWidget(self.graphicsView_tuxing_2, 0, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_qingkonghuabu_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_qingkonghuabu_2.setObjectName("pushButton_qingkonghuabu_2")
        self.horizontalLayout_7.addWidget(self.pushButton_qingkonghuabu_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.verticalLayout_7.setStretch(0, 6)
        self.verticalLayout_7.setStretch(1, 1)
        self.gridLayout.addLayout(self.verticalLayout_7, 0, 1, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.graphicsView_tuxing_3 = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView_tuxing_3.setObjectName("graphicsView_tuxing_3")
        self.gridLayout_11.addWidget(self.graphicsView_tuxing_3, 0, 0, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_11)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_qingkonghuabu_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_qingkonghuabu_3.setObjectName("pushButton_qingkonghuabu_3")
        self.horizontalLayout_8.addWidget(self.pushButton_qingkonghuabu_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.verticalLayout_8.setStretch(0, 6)
        self.verticalLayout_8.setStretch(1, 1)
        self.gridLayout.addLayout(self.verticalLayout_8, 0, 2, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.graphicsView_tuxing_4 = QtWidgets.QGraphicsView(self.groupBox_2)
        self.graphicsView_tuxing_4.setObjectName("graphicsView_tuxing_4")
        self.gridLayout_12.addWidget(self.graphicsView_tuxing_4, 0, 0, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_12)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton_qingkonghuabu_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_qingkonghuabu_4.setObjectName("pushButton_qingkonghuabu_4")
        self.horizontalLayout_9.addWidget(self.pushButton_qingkonghuabu_4)
        self.verticalLayout_9.addLayout(self.horizontalLayout_9)
        self.verticalLayout_9.setStretch(0, 6)
        self.verticalLayout_9.setStretch(1, 1)
        self.gridLayout.addLayout(self.verticalLayout_9, 1, 0, 1, 3)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.gridLayout_2.setColumnStretch(0, 8)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 9)
        self.gridLayout_3.addWidget(self.groupBox_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SinglePolicyCompare", "multiple_strategy"))
        self.pushButton_xuanzeshuju.setText(_translate("SinglePolicyCompare", "选择数据"))
        self.groupBox.setTitle(_translate("SinglePolicyCompare", "策略选择"))
        self.comboBox_celue1.setItemText(0, _translate("SinglePolicyCompare", "---请选择控制策略---"))
        self.comboBox_celue1.setItemText(1, _translate("SinglePolicyCompare", "固定优先序列"))
        self.comboBox_celue1.setItemText(2, _translate("SinglePolicyCompare", "动态优先序列"))
        self.comboBox_celue1.setItemText(3, _translate("SinglePolicyCompare", "比例控制策略"))
        self.comboBox_celue1.setItemText(4, _translate("SinglePolicyCompare", "Adam优化控制策略"))
        self.comboBox_celue2.setItemText(0, _translate("SinglePolicyCompare", "---请选择控制策略---"))
        self.comboBox_celue2.setItemText(1, _translate("SinglePolicyCompare", "固定优先序列"))
        self.comboBox_celue2.setItemText(2, _translate("SinglePolicyCompare", "动态优先序列"))
        self.comboBox_celue2.setItemText(3, _translate("SinglePolicyCompare", "比例控制策略"))
        self.comboBox_celue2.setItemText(4, _translate("SinglePolicyCompare", "Adam优化控制策略"))
        self.pushButton_xianshituxiang.setText(_translate("SinglePolicyCompare", "显示图像"))
        self.groupBox_2.setTitle(_translate("SinglePolicyCompare", "图像显示"))
        self.pushButton_qingkonghuabu.setText(_translate("SinglePolicyCompare", "清空画布"))
        self.pushButton_qingkonghuabu_2.setText(_translate("SinglePolicyCompare", "清空画布"))
        self.pushButton_qingkonghuabu_3.setText(_translate("SinglePolicyCompare", "清空画布"))
        self.pushButton_qingkonghuabu_4.setText(_translate("SinglePolicyCompare", "清空画布"))
