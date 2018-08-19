# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/manuel/projects/CryptoPrinterBot/mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from UI_filepage import DropResponeGraphicView
from UI_mainpage import IndicatorGraphicView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, -1, 601, 401))
        self.stackedWidget.setObjectName("stackedWidget")
        self.filechoose_page = QtWidgets.QWidget()
        self.filechoose_page.setObjectName("filechoose_page")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.filechoose_page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 581, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.filemanagement_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.filemanagement_layout.setContentsMargins(0, 0, 0, 0)
        self.filemanagement_layout.setObjectName("filemanagement_layout")
        self.response_graphic = DropResponeGraphicView(self.verticalLayoutWidget)
        self.response_graphic.setObjectName("response_graphic")
        self.filemanagement_layout.addWidget(self.response_graphic)
        self.usepath_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.usepath_button.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usepath_button.sizePolicy().hasHeightForWidth())
        self.usepath_button.setSizePolicy(sizePolicy)
        self.usepath_button.setMaximumSize(QtCore.QSize(16777215, 50))
        self.usepath_button.setFlat(False)
        self.usepath_button.setObjectName("usepath_button")
        self.filemanagement_layout.addWidget(self.usepath_button)
        self.stackedWidget.addWidget(self.filechoose_page)
        self.mainBot_page = QtWidgets.QWidget()
        self.mainBot_page.setObjectName("mainBot_page")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.mainBot_page)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 581, 381))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.indicator_graphicView = IndicatorGraphicView(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.indicator_graphicView.sizePolicy().hasHeightForWidth())
        self.indicator_graphicView.setSizePolicy(sizePolicy)
        self.indicator_graphicView.setMinimumSize(QtCore.QSize(0, 0))
        self.indicator_graphicView.setMaximumSize(QtCore.QSize(100, 16777215))
        self.indicator_graphicView.setSizeIncrement(QtCore.QSize(0, 0))
        self.indicator_graphicView.setBaseSize(QtCore.QSize(0, 0))
        self.indicator_graphicView.setObjectName("indicator_graphicView")
        self.horizontalLayout.addWidget(self.indicator_graphicView)
        self.start_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout.addWidget(self.start_button)
        self.stackedWidget.addWidget(self.mainBot_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.usepath_button.setText(_translate("MainWindow", "Start Trading"))
        self.start_button.setText(_translate("MainWindow", "Start"))

