# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 489)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(530, 120, 111, 16))
        font = QtGui.QFont()
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.joinButton = QtWidgets.QPushButton(self.centralwidget)
        self.joinButton.setGeometry(QtCore.QRect(540, 180, 93, 28))
        self.joinButton.setObjectName("joinButton")
        self.leaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.leaveButton.setGeometry(QtCore.QRect(650, 180, 93, 28))
        self.leaveButton.setObjectName("leaveButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(520, 260, 251, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 60, 471, 351))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.img_label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.img_label.setEnabled(True)
        self.img_label.setAutoFillBackground(False)
        self.img_label.setText("")
        self.img_label.setObjectName("img_label")
        black_background = QtGui.QPixmap(469, 349)
        black_background.fill(QtGui.QColor("black"))
        self.img_label.setPixmap(black_background)
        self.img_label.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.img_label, 0, 0, 1, 1)
        self.disableButton = QtWidgets.QPushButton(self.centralwidget)
        self.disableButton.setGeometry(QtCore.QRect(640, 210, 130, 28))
        self.disableButton.setObjectName("disableButton")
        self.enableButton = QtWidgets.QPushButton(self.centralwidget)
        self.enableButton.setGeometry(QtCore.QRect(510, 210, 130, 28))
        self.enableButton.setObjectName("enableButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 60, 111, 16))
        font = QtGui.QFont()
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.enable_ap_btn = QtWidgets.QPushButton(self.centralwidget)
        self.enable_ap_btn.setGeometry(QtCore.QRect(70, 20, 171, 32))
        self.enable_ap_btn.setObjectName("enable_ap_btn")
        self.disable_ap_btn = QtWidgets.QPushButton(self.centralwidget)
        self.disable_ap_btn.setGeometry(QtCore.QRect(250, 20, 171, 32))
        self.disable_ap_btn.setObjectName("disable_ap_btn")
        self.appIdEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.appIdEdit.setGeometry(QtCore.QRect(530, 80, 231, 31))
        self.appIdEdit.setObjectName("appIdEdit")
        self.channelEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.channelEdit.setGeometry(QtCore.QRect(530, 140, 231, 31))
        self.channelEdit.setObjectName("channelEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("face-recognition-demo", "face-recognition-demo"))
        self.label.setText(_translate("MainWindow", "Channel Name:"))
        self.joinButton.setText(_translate("MainWindow", "join"))
        self.leaveButton.setText(_translate("MainWindow", "leave"))
        self.disableButton.setText(_translate("MainWindow", "disableLocalVideo"))
        self.enableButton.setText(_translate("MainWindow", "enableLocalVideo"))
        self.label_2.setText(_translate("MainWindow", "AppId:"))
        self.enable_ap_btn.setText(_translate("MainWindow", "enableAdvancedPredict"))
        self.disable_ap_btn.setText(_translate("MainWindow", "disableAdvancedPredict"))