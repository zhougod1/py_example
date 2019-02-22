from ui_design import Ui_Form
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import method
import threading


# main window class
class MyWindow(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.new = Ui_Form()
        self.setupUi(self)
        self.tableWidget.setHorizontalHeaderLabels([
            '资源编号', 
            '后缀类型',
            '解析类型', 
            '描述',
            '文件大小'
        ])  # set H label

        self.ExtractBtn.clicked.connect(self.threadShow)
        self.DownloadBtn.clicked.connect(self.threadDown)
        self.show()

    # function that display output at the textBrowser
    # def normalOutputWritten(self, text):
    #     cursor = self.textBrowser.textCursor()
    #     cursor.movePosition(QtGui.QTextCursor.End)
    #     cursor.insertText(text)
    #     self.textBrowser.setTextCursor(cursor)
    #     self.textBrowser.ensureCursorVisible()

    def showinfo(self):
        method.RetrieveInfo(self)
        self.tableWidget.setRowCount(method.file_count)
        method.FillInfo(self)

    def download(self):
        method.ydl.params = {'format': self.SeleEdit.text()}
        try:
            method.ydl.process_video_result(method.video)
        except Exception as e:
            pass

    def threadShow(self):
        return threading.Thread(target=self.showinfo).start()
        
    def threadDown(self):
        return threading.Thread(target=self.download).start()
# youtube-dl uses logger to redirect output
# class MyLogger():
#     def debug(self, msg, w):
#         w.normalOutputWritten(w, msg)
#
#     def warning(self, msg, w):
#         w.normalOutputWritten(w, msg)
#
#     def error(self, msg, w):
#         w.normalOutputWritten(w, msg)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()     # construct and show the window
    method.proxy = myshow.PxyEdit.text()   # initiate the proxy
    sys.exit(app.exec_())