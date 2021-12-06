from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
from login1 import *
from login22 import *
from login31 import *
from chatbot import *
class birthday(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow1()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login22)
        self.ui.pushButton_3.clicked.connect(self.login31)
    def login22(self):
        self.login22=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow22()
        self.ui.setupUi(self.login22)
        self.login22.show()
        self.ui.pushButton_56.clicked.connect(self.ui.chatbot)
        self.ui.pushButton.clicked.connect(self.ui.paschange)

    def login31(self):
        self.login31=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow31()
        self.ui.setupUi(self.login31)
        self.login31.show()
        self.ui.pushButton.clicked.connect(self.ui.create)
        
        
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = birthday()
    w.show()
    sys.exit(app.exec_())
