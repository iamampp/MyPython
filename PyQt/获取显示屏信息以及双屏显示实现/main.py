#coding=utf-8
#project:PYQT
#file:main
#time 2020/8/10 17:19
#Author:Joey Wang

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
import sys
from u2 import Ui_MainWindow

class myWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initSize()

    def initSize(self):
        desktop = QApplication.desktop()
        print(help(desktop))
        screen_count = desktop.screenCount()
        print(screen_count)
        screen_rect = desktop.screenGeometry(0)
        print(screen_rect)
        available_rect = desktop.screenGeometry(1)
        print(available_rect)
        self.resize(screen_rect.width(),screen_rect.height())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = myWindow()
    w.show()
    sys.exit(app.exec_())

