# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 446)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DetectOnBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DetectOnBtn.setGeometry(QtCore.QRect(20, 320, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.DetectOnBtn.setFont(font)
        self.DetectOnBtn.setObjectName("DetectOnBtn")
        self.Cameralabel = QtWidgets.QLabel(self.centralwidget)
        self.Cameralabel.setGeometry(QtCore.QRect(30, 10, 161, 151))
        self.Cameralabel.setText("")
        self.Cameralabel.setObjectName("Cameralabel")
        self.Detectlabel = QtWidgets.QLabel(self.centralwidget)
        self.Detectlabel.setGeometry(QtCore.QRect(210, 10, 161, 151))
        self.Detectlabel.setText("")
        self.Detectlabel.setObjectName("Detectlabel")
        self.shibiejieguo = QtWidgets.QLabel(self.centralwidget)
        self.shibiejieguo.setGeometry(QtCore.QRect(30, 280, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.shibiejieguo.setFont(font)
        self.shibiejieguo.setStyleSheet("color:white")
        self.shibiejieguo.setObjectName("shibiejieguo")
        self.emtiontextlabel = QtWidgets.QLabel(self.centralwidget)
        self.emtiontextlabel.setGeometry(QtCore.QRect(140, 280, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.emtiontextlabel.setFont(font)
        self.emtiontextlabel.setStyleSheet("color:white")
        self.emtiontextlabel.setObjectName("emtiontextlabel")
        self.Face_Label = QtWidgets.QLabel(self.centralwidget)
        self.Face_Label.setGeometry(QtCore.QRect(390, 10, 161, 151))
        self.Face_Label.setText("")
        self.Face_Label.setObjectName("Face_Label")
        self.EmojiLabel = QtWidgets.QLabel(self.centralwidget)
        self.EmojiLabel.setGeometry(QtCore.QRect(390, 170, 161, 151))
        self.EmojiLabel.setText("")
        self.EmojiLabel.setObjectName("EmojiLabel")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(560, 10, 361, 401))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.DetectOffBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DetectOffBtn.setGeometry(QtCore.QRect(210, 320, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.DetectOffBtn.setFont(font)
        self.DetectOffBtn.setObjectName("DetectOffBtn")
        self.noticetext = QtWidgets.QTextBrowser(self.centralwidget)
        self.noticetext.setGeometry(QtCore.QRect(20, 170, 351, 101))
        self.noticetext.setObjectName("noticetext")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 936, 24))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DetectOnBtn.setText(_translate("MainWindow", "????????????\n"
"Start"))
        self.shibiejieguo.setText(_translate("MainWindow", "???????????????"))
        self.emtiontextlabel.setText(_translate("MainWindow", "Loading........"))
        self.DetectOffBtn.setText(_translate("MainWindow", "????????????\n"
"Stop"))
