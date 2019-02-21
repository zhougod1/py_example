# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject , pyqtSignal
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 247)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 271, 31))
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit.setObjectName("textEdit")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(10, 50, 271, 151))
        self.listView.setObjectName("listView")
        self.ensure = QtWidgets.QPushButton(self.centralwidget)
        self.ensure.setEnabled(True)
        self.ensure.setGeometry(QtCore.QRect(290, 10, 81, 31))
        self.ensure.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.ensure.clicked.connect(pyMzt.init)
        self.ensure.setObjectName("ensure")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt5"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "请输入"))
        self.ensure.setText(_translate("MainWindow", "确定"))
    


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
win = Ui_MainWindow()
win.setupUi(MainWindow)
MainWindow.show()
app.exec_()
