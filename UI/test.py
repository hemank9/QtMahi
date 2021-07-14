from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # setting title
        self.setWindowTitle("Python ")
        # setting geometry
        self.setGeometry(0, 0, 1220, 700)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('..\Resources\Group 45.png'))
        self.label.setGeometry(0, 0, 1220, 195)
        # calling method
        self.UiComponents()
        # showing all the widgets
        self.show()
    # method for widgets
    def UiComponents(self):
        # three buttons on the my medicine page
        # prescriptions
        btn_pre = QPushButton("", self)
        btn_pre.setGeometry(39, 48, 215, 67)
        btn_pre.setStyleSheet("border-radius : 30; background-color : #F0F0F3; text-align:top ; text-align:left; focus:pressed")
        btn_pre.setIcon(QtGui.QIcon('..\Resources\prescriptions.png'))
        btn_pre.setIconSize(QtCore.QSize(215, 67))
        # btn_pre.clicked.connect(self.clickme)
App = QApplication(sys.argv)
# create the instance of our Window
window = Window()
window.show()
# start the app
sys.exit(App.exec())