# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BUR_evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BUREvaluate(object):
    def setupUi(self, BUREvaluate):
        BUREvaluate.setObjectName("BUREvaluate")
        BUREvaluate.resize(1007, 729)
        self.gridLayout = QtWidgets.QGridLayout(BUREvaluate)
        self.gridLayout.setObjectName("gridLayout")
        self.CardWidget_7 = CardWidget(BUREvaluate)
        self.CardWidget_7.setObjectName("CardWidget_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.CardWidget_7)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.CardWidget_8 = CardWidget(self.CardWidget_7)
        self.CardWidget_8.setMinimumSize(QtCore.QSize(0, 138))
        self.CardWidget_8.setObjectName("CardWidget_8")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.CardWidget_8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.CaptionLabel_5 = CaptionLabel(self.CardWidget_8)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.CaptionLabel_5.setFont(font)
        self.CaptionLabel_5.setObjectName("CaptionLabel_5")
        self.gridLayout_4.addWidget(self.CaptionLabel_5, 0, 0, 1, 1)
        self.CalendarPicker_3 = CalendarPicker(self.CardWidget_8)
        self.CalendarPicker_3.setObjectName("CalendarPicker_3")
        self.gridLayout_4.addWidget(self.CalendarPicker_3, 0, 1, 1, 1)
        self.CaptionLabel_6 = CaptionLabel(self.CardWidget_8)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.CaptionLabel_6.setFont(font)
        self.CaptionLabel_6.setObjectName("CaptionLabel_6")
        self.gridLayout_4.addWidget(self.CaptionLabel_6, 1, 0, 1, 1)
        self.CalendarPicker_4 = CalendarPicker(self.CardWidget_8)
        self.CalendarPicker_4.setObjectName("CalendarPicker_4")
        self.gridLayout_4.addWidget(self.CalendarPicker_4, 1, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 3)
        self.verticalLayout_2.addWidget(self.CardWidget_8)
        self.CardWidget_9 = CardWidget(self.CardWidget_7)
        self.CardWidget_9.setObjectName("CardWidget_9")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.CardWidget_9)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem = QtWidgets.QSpacerItem(132, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 1, 2, 1, 1)
        self.importPushButtonBUR = PrimaryPushButton(self.CardWidget_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.importPushButtonBUR.sizePolicy().hasHeightForWidth())
        self.importPushButtonBUR.setSizePolicy(sizePolicy)
        self.importPushButtonBUR.setObjectName("importPushButtonBUR")
        self.gridLayout_7.addWidget(self.importPushButtonBUR, 1, 1, 1, 1)
        self.preViewTableBUR = TableView(self.CardWidget_9)
        self.preViewTableBUR.setObjectName("preViewTableBUR")
        self.gridLayout_7.addWidget(self.preViewTableBUR, 0, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(133, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.CardWidget_9)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 13)
        self.gridLayout.addWidget(self.CardWidget_7, 0, 0, 1, 1)
        self.CardWidget_10 = CardWidget(BUREvaluate)
        self.CardWidget_10.setObjectName("CardWidget_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.CardWidget_10)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.CardWidget_11 = CardWidget(self.CardWidget_10)
        self.CardWidget_11.setMinimumSize(QtCore.QSize(0, 138))
        self.CardWidget_11.setObjectName("CardWidget_11")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.CardWidget_11)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.SubtitleLabel_2 = SubtitleLabel(self.CardWidget_11)
        self.SubtitleLabel_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.SubtitleLabel_2.setObjectName("SubtitleLabel_2")
        self.gridLayout_8.addWidget(self.SubtitleLabel_2, 0, 0, 1, 3)
        self.ComboBoxBUR = ComboBox(self.CardWidget_11)
        self.ComboBoxBUR.setObjectName("ComboBoxBUR")
        self.gridLayout_8.addWidget(self.ComboBoxBUR, 0, 3, 1, 1)
        self.CaptionLabel_7 = CaptionLabel(self.CardWidget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CaptionLabel_7.sizePolicy().hasHeightForWidth())
        self.CaptionLabel_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.CaptionLabel_7.setFont(font)
        self.CaptionLabel_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.CaptionLabel_7.setWordWrap(True)
        self.CaptionLabel_7.setObjectName("CaptionLabel_7")
        self.gridLayout_8.addWidget(self.CaptionLabel_7, 1, 0, 1, 4)
        self.LineEditBUR = LineEdit(self.CardWidget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineEditBUR.sizePolicy().hasHeightForWidth())
        self.LineEditBUR.setSizePolicy(sizePolicy)
        self.LineEditBUR.setObjectName("LineEditBUR")
        self.gridLayout_8.addWidget(self.LineEditBUR, 2, 0, 1, 1)
        self.CaptionLabel_8 = CaptionLabel(self.CardWidget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CaptionLabel_8.sizePolicy().hasHeightForWidth())
        self.CaptionLabel_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.CaptionLabel_8.setFont(font)
        self.CaptionLabel_8.setObjectName("CaptionLabel_8")
        self.gridLayout_8.addWidget(self.CaptionLabel_8, 2, 1, 1, 1)
        self.SliderBUR = Slider(self.CardWidget_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SliderBUR.sizePolicy().hasHeightForWidth())
        self.SliderBUR.setSizePolicy(sizePolicy)
        self.SliderBUR.setOrientation(QtCore.Qt.Horizontal)
        self.SliderBUR.setObjectName("SliderBUR")
        self.gridLayout_8.addWidget(self.SliderBUR, 2, 2, 1, 2)
        self.verticalLayout_3.addWidget(self.CardWidget_11)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.CardWidget = CardWidget(self.CardWidget_10)
        self.CardWidget.setObjectName("CardWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.CardWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.highValueTableBUR = TableView(self.CardWidget)
        self.highValueTableBUR.setObjectName("highValueTableBUR")
        self.horizontalLayout_3.addWidget(self.highValueTableBUR)
        self.verticalLayout.addWidget(self.CardWidget)
        self.CardWidget_12 = CardWidget(self.CardWidget_10)
        self.CardWidget_12.setObjectName("CardWidget_12")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.CardWidget_12)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.SpecificLabelBUR = CaptionLabel(self.CardWidget_12)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SpecificLabelBUR.setFont(font)
        self.SpecificLabelBUR.setText("")
        self.SpecificLabelBUR.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.SpecificLabelBUR.setObjectName("SpecificLabelBUR")
        self.gridLayout_9.addWidget(self.SpecificLabelBUR, 1, 0, 1, 2)
        self.SubtitleLabel_3 = SubtitleLabel(self.CardWidget_12)
        self.SubtitleLabel_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.SubtitleLabel_3.setObjectName("SubtitleLabel_3")
        self.gridLayout_9.addWidget(self.SubtitleLabel_3, 0, 0, 1, 1)
        self.PercentLabelBUR = SubtitleLabel(self.CardWidget_12)
        self.PercentLabelBUR.setText("")
        self.PercentLabelBUR.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.PercentLabelBUR.setObjectName("PercentLabelBUR")
        self.gridLayout_9.addWidget(self.PercentLabelBUR, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.CardWidget_12)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.displayPushButtonBUR = PrimaryPushButton(self.CardWidget_10)
        self.displayPushButtonBUR.setObjectName("displayPushButtonBUR")
        self.horizontalLayout_2.addWidget(self.displayPushButtonBUR)
        self.moreInfoPushButtonBUR = PrimaryPushButton(self.CardWidget_10)
        self.moreInfoPushButtonBUR.setObjectName("moreInfoPushButtonBUR")
        self.horizontalLayout_2.addWidget(self.moreInfoPushButtonBUR)
        spacerItem3 = QtWidgets.QSpacerItem(99, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 13)
        self.gridLayout.addWidget(self.CardWidget_10, 0, 1, 1, 1)

        self.retranslateUi(BUREvaluate)
        QtCore.QMetaObject.connectSlotsByName(BUREvaluate)

    def retranslateUi(self, BUREvaluate):
        _translate = QtCore.QCoreApplication.translate
        BUREvaluate.setWindowTitle(_translate("BUREvaluate", "BUR辊形评价"))
        self.CaptionLabel_5.setText(_translate("BUREvaluate", "开始日期"))
        self.CaptionLabel_6.setText(_translate("BUREvaluate", "截至日期"))
        self.importPushButtonBUR.setText(_translate("BUREvaluate", "导入"))
        self.SubtitleLabel_2.setText(_translate("BUREvaluate", "视为打满的百分比"))
        self.ComboBoxBUR.setText(_translate("BUREvaluate", "选择机架"))
        self.CaptionLabel_7.setText(_translate("BUREvaluate", "各个设定值占打满值的百分比，其中中间辊弯辊[0,2600]，中间辊窜辊[-142.5,142.5]，工作辊弯辊[-700,1000]"))
        self.CaptionLabel_8.setText(_translate("BUREvaluate", "%"))
        self.SubtitleLabel_3.setText(_translate("BUREvaluate", "3个设定值都打满卷数百分比"))
        self.displayPushButtonBUR.setText(_translate("BUREvaluate", "打满显示"))
        self.moreInfoPushButtonBUR.setText(_translate("BUREvaluate", "详细信息"))
from qfluentwidgets import CalendarPicker, CaptionLabel, CardWidget, ComboBox, LineEdit, PrimaryPushButton, Slider, SubtitleLabel, TableView
