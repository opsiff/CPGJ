# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inEdt = QtWidgets.QLineEdit(self.centralwidget)
        self.inEdt.setMinimumSize(QtCore.QSize(160, 60))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.inEdt.setFont(font)
        self.inEdt.setObjectName("inEdt")
        self.horizontalLayout.addWidget(self.inEdt)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.sBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sBtn.setMinimumSize(QtCore.QSize(40, 30))
        self.sBtn.setObjectName("sBtn")
        self.verticalLayout.addWidget(self.sBtn)
        self.modeBox = QtWidgets.QCheckBox(self.centralwidget)
        self.modeBox.setObjectName("modeBox")
        self.verticalLayout.addWidget(self.modeBox)
        self.cBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.cBtn.setObjectName("cBtn")
        self.verticalLayout.addWidget(self.cBtn)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.outEdt = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.outEdt.setFont(font)
        self.outEdt.setReadOnly(True)
        self.outEdt.setObjectName("outEdt")
        self.verticalLayout_2.addWidget(self.outEdt)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 961, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inEdt.setText(_translate("MainWindow", "这里输入仓库地址"))
        self.sBtn.setText(_translate("MainWindow", "确定"))
        self.modeBox.setText(_translate("MainWindow", "Mode Slow"))
        self.cBtn.setText(_translate("MainWindow", "清空"))
        self.outEdt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\';\">这是消息界面，返回必要消息!</span></p></body></html>"))

