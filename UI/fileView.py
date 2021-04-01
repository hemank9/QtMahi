from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\yellow.png'))
        self.label.setGeometry(0, 0, 1220, 39)

App = QApplication(sys.argv)

# create the instance of our Window
window = Window3()

window.show()

# start the app
sys.exit(App.exec_())
