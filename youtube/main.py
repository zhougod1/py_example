from ui_design import Ui_Form
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import method
import threading

# 在Python 2.x 版本中，默认类都是旧式类，除非顶层显式继承object。
# 在Python 3.x 版本中，默认类就是新式类，无需显示继承object。


class MyWindow(Ui_Form, QtWidgets.QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.tableWidget.setHorizontalHeaderLabels([
            '资源编号', 
            '后缀类型',
            '解析类型', 
            '描述',
            '文件大小'
        ])

        self.ExtractBtn.clicked.connect(self.threadShow)
        self.DownloadBtn.clicked.connect(self.threadDown)
        self.show()

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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()    
    method.proxy = myshow.PxyEdit.text()
    sys.exit(app.exec_())