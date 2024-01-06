# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RollingInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RollingForm(object):
    def setupUi(self, RollingForm):
        RollingForm.setObjectName("RollingForm")
        RollingForm.resize(804, 690)
        self.gridLayout = QtWidgets.QGridLayout(RollingForm)
        self.gridLayout.setObjectName("gridLayout")
        self.CardWidget_2 = CardWidget(RollingForm)
        self.CardWidget_2.setObjectName("CardWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.CardWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.TitleLabel_2 = TitleLabel(self.CardWidget_2)
        self.TitleLabel_2.setObjectName("TitleLabel_2")
        self.horizontalLayout_2.addWidget(self.TitleLabel_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_3.addItem(spacerItem3, 1, 1, 1, 1)
        self.rollerInfoPushButton = PrimaryPushButton(self.CardWidget_2)
        self.rollerInfoPushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.rollerInfoPushButton.setObjectName("rollerInfoPushButton")
        self.gridLayout_3.addWidget(self.rollerInfoPushButton, 4, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(37, 17, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 2, 2, 1, 1)
        self.IconWidget_7 = IconWidget(self.CardWidget_2)
        self.IconWidget_7.setMinimumSize(QtCore.QSize(50, 50))
        self.IconWidget_7.setMaximumSize(QtCore.QSize(50, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/跟踪.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_7.setIcon(icon)
        self.IconWidget_7.setObjectName("IconWidget_7")
        self.gridLayout_3.addWidget(self.IconWidget_7, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_3.addItem(spacerItem5, 3, 1, 1, 1)
        self.IconWidget_8 = IconWidget(self.CardWidget_2)
        self.IconWidget_8.setMinimumSize(QtCore.QSize(50, 50))
        self.IconWidget_8.setMaximumSize(QtCore.QSize(50, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/冷轧.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_8.setIcon(icon1)
        self.IconWidget_8.setObjectName("IconWidget_8")
        self.gridLayout_3.addWidget(self.IconWidget_8, 4, 1, 1, 1)
        self.IconWidget_6 = IconWidget(self.CardWidget_2)
        self.IconWidget_6.setMinimumSize(QtCore.QSize(50, 50))
        self.IconWidget_6.setMaximumSize(QtCore.QSize(50, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/查询.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_6.setIcon(icon2)
        self.IconWidget_6.setObjectName("IconWidget_6")
        self.gridLayout_3.addWidget(self.IconWidget_6, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 2, 4, 1, 1)
        self.IconWidget_9 = IconWidget(self.CardWidget_2)
        self.IconWidget_9.setMinimumSize(QtCore.QSize(50, 50))
        self.IconWidget_9.setMaximumSize(QtCore.QSize(50, 16777215))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/板形分析.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_9.setIcon(icon3)
        self.IconWidget_9.setObjectName("IconWidget_9")
        self.gridLayout_3.addWidget(self.IconWidget_9, 6, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(37, 17, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem7, 0, 2, 1, 1)
        self.searchPushButton = PrimaryPushButton(self.CardWidget_2)
        self.searchPushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.searchPushButton.setObjectName("searchPushButton")
        self.gridLayout_3.addWidget(self.searchPushButton, 0, 3, 1, 1)
        self.iuInfoPushButton = PrimaryPushButton(self.CardWidget_2)
        self.iuInfoPushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.iuInfoPushButton.setObjectName("iuInfoPushButton")
        self.gridLayout_3.addWidget(self.iuInfoPushButton, 6, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem8, 2, 0, 1, 1)
        self.rollingInfoPushButton = PrimaryPushButton(self.CardWidget_2)
        self.rollingInfoPushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.rollingInfoPushButton.setObjectName("rollingInfoPushButton")
        self.gridLayout_3.addWidget(self.rollingInfoPushButton, 2, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout_3.addItem(spacerItem9, 5, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        spacerItem10 = QtWidgets.QSpacerItem(20, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.gridLayout.addWidget(self.CardWidget_2, 0, 1, 1, 1)
        self.CardWidget = CardWidget(RollingForm)
        self.CardWidget.setObjectName("CardWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.CardWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.TitleLabel = TitleLabel(self.CardWidget)
        self.TitleLabel.setObjectName("TitleLabel")
        self.horizontalLayout.addWidget(self.TitleLabel)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem13 = QtWidgets.QSpacerItem(20, 65, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem13)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem14, 8, 4, 1, 1)
        self.IconWidget_10 = IconWidget(self.CardWidget)
        self.IconWidget_10.setMinimumSize(QtCore.QSize(50, 50))
        self.IconWidget_10.setMaximumSize(QtCore.QSize(50, 16777215))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/成功.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_10.setIcon(icon4)
        self.IconWidget_10.setObjectName("IconWidget_10")
        self.gridLayout_2.addWidget(self.IconWidget_10, 4, 1, 1, 1)
        self.IconWidget_5 = IconWidget(self.CardWidget)
        self.IconWidget_5.setMinimumSize(QtCore.QSize(50, 50))
        self.IconWidget_5.setMaximumSize(QtCore.QSize(50, 16777215))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/format.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_5.setIcon(icon5)
        self.IconWidget_5.setObjectName("IconWidget_5")
        self.gridLayout_2.addWidget(self.IconWidget_5, 2, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem15, 9, 1, 1, 1)
        self.exportPushButton = PrimaryPushButton(self.CardWidget)
        self.exportPushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.exportPushButton.setObjectName("exportPushButton")
        self.gridLayout_2.addWidget(self.exportPushButton, 8, 3, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem16, 2, 2, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem17, 8, 0, 1, 1)
        self.IconWidget_3 = IconWidget(self.CardWidget)
        self.IconWidget_3.setMinimumSize(QtCore.QSize(50, 50))
        self.IconWidget_3.setMaximumSize(QtCore.QSize(50, 16777215))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/预览.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_3.setIcon(icon6)
        self.IconWidget_3.setObjectName("IconWidget_3")
        self.gridLayout_2.addWidget(self.IconWidget_3, 6, 1, 1, 1)
        self.IconWidget_2 = IconWidget(self.CardWidget)
        self.IconWidget_2.setMinimumSize(QtCore.QSize(50, 50))
        self.IconWidget_2.setMaximumSize(QtCore.QSize(50, 16777215))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/导出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_2.setIcon(icon7)
        self.IconWidget_2.setObjectName("IconWidget_2")
        self.gridLayout_2.addWidget(self.IconWidget_2, 8, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem18, 5, 1, 1, 1)
        self.importPushButton = PrimaryPushButton(self.CardWidget)
        self.importPushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.importPushButton.setObjectName("importPushButton")
        self.gridLayout_2.addWidget(self.importPushButton, 0, 3, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem19, 1, 1, 1, 1)
        self.formatPushButton = PrimaryPushButton(self.CardWidget)
        self.formatPushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.formatPushButton.setObjectName("formatPushButton")
        self.gridLayout_2.addWidget(self.formatPushButton, 2, 3, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem20, 8, 2, 1, 1)
        self.IconWidget = IconWidget(self.CardWidget)
        self.IconWidget.setMinimumSize(QtCore.QSize(50, 50))
        self.IconWidget.setMaximumSize(QtCore.QSize(50, 16777215))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/导入.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget.setIcon(icon8)
        self.IconWidget.setObjectName("IconWidget")
        self.gridLayout_2.addWidget(self.IconWidget, 0, 1, 1, 1)
        self.mergePushButton = PrimaryPushButton(self.CardWidget)
        self.mergePushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.mergePushButton.setObjectName("mergePushButton")
        self.gridLayout_2.addWidget(self.mergePushButton, 10, 3, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem21, 3, 1, 1, 1)
        self.IconWidget_4 = IconWidget(self.CardWidget)
        self.IconWidget_4.setMinimumSize(QtCore.QSize(50, 50))
        self.IconWidget_4.setMaximumSize(QtCore.QSize(50, 16777215))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/数据集合并.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.IconWidget_4.setIcon(icon9)
        self.IconWidget_4.setObjectName("IconWidget_4")
        self.gridLayout_2.addWidget(self.IconWidget_4, 10, 1, 1, 1)
        self.matchPushButton = PrimaryPushButton(self.CardWidget)
        self.matchPushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.matchPushButton.setObjectName("matchPushButton")
        self.gridLayout_2.addWidget(self.matchPushButton, 4, 3, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem22, 10, 2, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem23, 0, 2, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem24, 7, 1, 1, 1)
        self.previewPushButton = PrimaryPushButton(self.CardWidget)
        self.previewPushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.previewPushButton.setObjectName("previewPushButton")
        self.gridLayout_2.addWidget(self.previewPushButton, 6, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem25 = QtWidgets.QSpacerItem(20, 47, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem25)
        self.gridLayout.addWidget(self.CardWidget, 0, 0, 1, 1)

        self.retranslateUi(RollingForm)
        QtCore.QMetaObject.connectSlotsByName(RollingForm)

    def retranslateUi(self, RollingForm):
        _translate = QtCore.QCoreApplication.translate
        RollingForm.setWindowTitle(_translate("RollingForm", "Form"))
        self.TitleLabel_2.setText(_translate("RollingForm", "数据分析"))
        self.rollerInfoPushButton.setToolTip(_translate("RollingForm", "导入单个酸轧在线判定表"))
        self.rollerInfoPushButton.setText(_translate("RollingForm", "轧辊参数总览"))
        self.searchPushButton.setToolTip(_translate("RollingForm", "导入单个酸轧在线判定表"))
        self.searchPushButton.setText(_translate("RollingForm", "钢卷号查询"))
        self.iuInfoPushButton.setToolTip(_translate("RollingForm", "导入单个酸轧在线判定表"))
        self.iuInfoPushButton.setText(_translate("RollingForm", "IU信息统计"))
        self.rollingInfoPushButton.setToolTip(_translate("RollingForm", "导入单个酸轧在线判定表"))
        self.rollingInfoPushButton.setText(_translate("RollingForm", "轧制时间重量总览"))
        self.TitleLabel.setText(_translate("RollingForm", "数据服务"))
        self.exportPushButton.setToolTip(_translate("RollingForm", "导出经过处理的酸轧在线判定表"))
        self.exportPushButton.setText(_translate("RollingForm", "导出"))
        self.importPushButton.setToolTip(_translate("RollingForm", "导入单个酸轧在线判定表"))
        self.importPushButton.setText(_translate("RollingForm", "导入"))
        self.formatPushButton.setToolTip(_translate("RollingForm", "格式化酸轧在线判定的板坯牌号"))
        self.formatPushButton.setText(_translate("RollingForm", "格式化"))
        self.mergePushButton.setToolTip(_translate("RollingForm", "合并酸轧在线判定表"))
        self.mergePushButton.setText(_translate("RollingForm", "合并"))
        self.matchPushButton.setToolTip(_translate("RollingForm", "格式化酸轧在线判定的板坯牌号"))
        self.matchPushButton.setText(_translate("RollingForm", "匹配冷卷号"))
        self.previewPushButton.setToolTip(_translate("RollingForm", "导出经过处理的酸轧在线判定表"))
        self.previewPushButton.setText(_translate("RollingForm", "预览数据"))
from qfluentwidgets import CardWidget, IconWidget, PrimaryPushButton, TitleLabel
from qtResource import resource_rc
