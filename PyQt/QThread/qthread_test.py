#coding=utf-8
#project:chip
#file:qthread_test
#time 2020/8/28 9:19
#Author:Joey Wang

from QThread import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class myWindow(Ui_Form,QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.thread = thread()
        self.thread.sinOut.connect(self.change)
        self.pushButton.clicked.connect(self.thread.start)

    def change(self,value):
        self.progressBar.setValue(value)

class thread(QThread):

    sinOut = pyqtSignal(int)

    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(101):
            self.sinOut.emit(i)
            self.msleep(100)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myWindow()
    w.show()
    sys.exit(app.exec_())