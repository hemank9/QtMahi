from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\yellow.png'))
        self.label.setGeometry(0, 0, 1220, 39)

        self.UiComponents()
        #
        #     # showing all the widgets
        self.show()
    #
    def UiComponents(self):


        btn_file1 = QPushButton("", self)
        btn_file1.setGeometry(41, 150, 1138, 76)
        btn_file1.setStyleSheet("border-radius : 10; color:#FFFFFF; text-align:left")
        btn_file1.setIcon(QtGui.QIcon('Resources\mfile1.png'))
        btn_file1.setIconSize(QtCore.QSize(1138, 76))
        btn_file1.clicked.connect(self.file)

        btn_file2 = QPushButton("", self)
        btn_file2.setGeometry(41, 236, 1138, 76)
        btn_file2.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_file2.setIcon(QtGui.QIcon('Resources\myfile2.png'))
        btn_file2.setIconSize(QtCore.QSize(1138, 76))
        btn_file2.clicked.connect(self.file)

        btn_file3 = QPushButton("", self)
        btn_file3.setGeometry(41, 327, 1138, 76)
        btn_file3.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_file3.setIcon(QtGui.QIcon('Resources\myfile3.png'))
        btn_file3.setIconSize(QtCore.QSize(1138, 76))
        btn_file3.clicked.connect(self.file)

    def file(self):
            self.m = Window3()
            self.m.show()

App = QApplication(sys.argv)

# create the instance of our Window
window = Window2()

window.show()

# start the app
sys.exit(App.exec_())
