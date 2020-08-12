#coding=utf-8
#project:PYQT
#file:main
#time 2020/8/10 17:19
#Author:Joey Wang

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
import sys
from u1 import Ui_Dialog
from u2 import Ui_MainWindow

class myWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Dialog(QDialog,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myWindow()
    d = Dialog()
    btn = w.pushButton
    btn.clicked.connect(lambda: d.show())
    w.show()
    sys.exit(app.exec_())

