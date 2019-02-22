# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys

class EmittingStream(QtCore.QObject):  
    textWritten = QtCore.pyqtSignal(str)  #定义一个发送str的信号
    def write(self, text):
        self.textWritten.emit(str(text))  
    def isatty(self):
        pass
    def flush(self):
        # QApplication.processEvents()
        pass

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(650, 501)
        Form.setWindowIcon(QtGui.QIcon('./youtube.png'))
        self.ExtractBtn = QtWidgets.QPushButton(Form)
        self.ExtractBtn.setGeometry(QtCore.QRect(528, 38, 115, 31))
        self.ExtractBtn.setFocusPolicy(QtCore.Qt.TabFocus)
        self.ExtractBtn.setObjectName("ExtractBtn")
        self.DownloadBtn = QtWidgets.QPushButton(Form)
        self.DownloadBtn.setGeometry(QtCore.QRect(534, 354, 113, 32))
        self.DownloadBtn.setObjectName("DownloadBtn")
        self.AddrEdit = QtWidgets.QLineEdit(Form)
        self.AddrEdit.setGeometry(QtCore.QRect(50, 44, 471, 21))
        self.AddrEdit.setObjectName("AddrEdit")
        self.AddrLbl = QtWidgets.QLabel(Form)
        self.AddrLbl.setGeometry(QtCore.QRect(10, 47, 54, 16))
        self.AddrLbl.setObjectName("AddrLbl")
        self.PxyEdit = QtWidgets.QLineEdit(Form)
        self.PxyEdit.setGeometry(QtCore.QRect(50, 14, 111, 21))
        self.PxyEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.PxyEdit.setObjectName("PxyEdit")
        self.ProxyLbl = QtWidgets.QLabel(Form)
        self.ProxyLbl.setGeometry(QtCore.QRect(10, 17, 41, 16))
        self.ProxyLbl.setObjectName("ProxyLbl")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 631, 271))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(126)
        self.tableWidget.verticalHeader().setVisible(False)
        self.shellWidget = QtWidgets.QTextEdit(Form)
        self.shellWidget.setGeometry(QtCore.QRect(10, 390, 631, 101))
        self.shellWidget.setObjectName("shellWidget")
        self.shellWidget.setReadOnly(True)
        self.SeleLbl = QtWidgets.QLabel(Form)
        self.SeleLbl.setGeometry(QtCore.QRect(10, 363, 250, 16))
        self.SeleLbl.setObjectName("SeleLbl")
        self.SeleEdit = QtWidgets.QLineEdit(Form)
        self.SeleEdit.setGeometry(QtCore.QRect(255, 360, 111, 21))
        self.SeleEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.SeleEdit.setText("")
        self.SeleEdit.setObjectName("SeleEdit")

        self.retranslateUi(Form)
        self.AddrEdit.returnPressed.connect(self.ExtractBtn.click)
        self.SeleEdit.returnPressed.connect(self.DownloadBtn.click)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.AddrEdit, self.ExtractBtn)
        Form.setTabOrder(self.ExtractBtn, self.DownloadBtn)
        sys.stdout = EmittingStream(textWritten=self.outputWritten)  
        sys.stderr = EmittingStream(textWritten=self.outputWritten)  

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Easy Download"))
        Form.setWindowIcon(QtGui.QIcon('youtube.ico'))
        self.ExtractBtn.setText(_translate("Form", "获取资源"))
        self.DownloadBtn.setText(_translate("Form", "下载"))
        self.AddrLbl.setText(_translate("Form", "地址:"))
        self.PxyEdit.setText(_translate("Form", "127.0.0.1:"))
        self.AddrEdit.setText(_translate("Form", "https://"))
        self.ProxyLbl.setText(_translate("Form", "代理:"))
        self.SeleLbl.setText(_translate("Form", "选择需要的Format code(video + audio):"))

    # 重定向sys输出，信号槽
    def outputWritten(self, text):  
        cursor = self.shellWidget.textCursor()  
        cursor.movePosition(QtGui.QTextCursor.End)  
        cursor.insertText(text)  
        self.shellWidget.setTextCursor(cursor)  
        self.shellWidget.ensureCursorVisible() 