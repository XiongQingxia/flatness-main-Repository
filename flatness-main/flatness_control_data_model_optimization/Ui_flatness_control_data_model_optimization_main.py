# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flatness_control_data_model_optimization_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from flatness_control_data_model_optimization.feedback_control_strategy_simulation_analysis.feedback_control_strategy_simulation_analysis import \
    反馈控制策略
from flatness_control_data_model_optimization.table_learn_self.table_learn_self import 表格自学习
from flatness_control_data_model_optimization.mechanism_online_optimization.mechanism_online_optimization import 机理在线优化
from flatness_control_data_model_optimization.roller_shape_design.roller_shape_design import 辊形设计



class Ui_banxingkongzhishumo(object):
    def setupUi(self, banxingkongzhishumo):
        banxingkongzhishumo.setObjectName("banxingkongzhishumo")
        banxingkongzhishumo.resize(1300, 1000)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/智能优化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        banxingkongzhishumo.setWindowIcon(icon)
        self.horizontalLayout = QtWidgets.QHBoxLayout(banxingkongzhishumo)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.NavigationBar = NavigationBar(banxingkongzhishumo)
        self.NavigationBar.setObjectName("NavigationBar")
        self.horizontalLayout.addWidget(self.NavigationBar)
        self.stackedWidget = QtWidgets.QStackedWidget(banxingkongzhishumo)
        self.stackedWidget.setObjectName("stackedWidget")
        self.tablePage = 表格自学习()
        self.tablePage.setObjectName("tablePage")
        self.stackedWidget.addWidget(self.tablePage)
        self.mechanismPage = 机理在线优化()
        self.mechanismPage.setObjectName("mechanismPage")
        self.stackedWidget.addWidget(self.mechanismPage)
        self.feedbackControlPage = 反馈控制策略()
        self.feedbackControlPage.setObjectName("feedbackControlPage")
        self.stackedWidget.addWidget(self.feedbackControlPage)
        self.designPage = 辊形设计()
        self.designPage.setObjectName("designPage")
        self.stackedWidget.addWidget(self.designPage)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 20)

        self.retranslateUi(banxingkongzhishumo)
        QtCore.QMetaObject.connectSlotsByName(banxingkongzhishumo)

    def retranslateUi(self, banxingkongzhishumo):
        _translate = QtCore.QCoreApplication.translate
        banxingkongzhishumo.setWindowTitle(_translate("banxingkongzhishumo", "板形反馈控制数模优化"))


from qfluentwidgets import NavigationBar
from qtResource import resource_rc