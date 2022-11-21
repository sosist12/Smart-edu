import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

ui_path = r"C:\Users\user\Desktop\33.계산기 만들기(PYQT)\계산기.ui"
form_class = uic.loadUiType(ui_path)[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    mywindow = WindowClass()
    mywindow.show()
    app.exec_()

    
    
    
