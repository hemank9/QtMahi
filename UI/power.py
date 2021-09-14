import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import UI.login as log
import MyDatabase.my_database as db
import Utility.MahiUtility as Util


class Power(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Power")
        self.setGeometry(463, 193, 293, 239)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: #F0F0F3; ")
        # self.label = QLabel(self)
        # self.label.setPixmap(QPixmap('../Resources/Group 48.png'))
        # self.label.setGeometry(0, 0, 1220, 685)
        self.UiComponents()
        self.show()

    def UiComponents(self):

        # holdingLbl1 = QLabel(self)
        # holdingLbl1.setGeometry(463, 193, 293, 239)
        # holdingLbl1.setStyleSheet("background-color: #F0F0F3; border-radius:15")
        # holdingLbl1.setGraphicsEffect(Util.getNeuShadow(0))
        # holdingLbl = QLabel(self)
        # holdingLbl.setGeometry(463, 193, 293, 239)
        # holdingLbl.setStyleSheet("background-color: #F0F0F3; border-radius:15")
        # holdingLbl.setGraphicsEffect(Util.getNeuShadow(1))

        btn_back1 = QPushButton("X", self)
        btn_back1.setGeometry(251, 14, 23, 23)
        btn_back1.setStyleSheet("border-radius : 10; background-color: #F0F0F3; color: #C0C0C0; font-size:20px; font: bold")
        btn_back1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_back = QPushButton("X", self)
        btn_back.setGeometry(251, 14, 23, 23)
        btn_back.setStyleSheet(
            "border-radius : 10; background-color: #F0F0F3; color: #C0C0C0; font-size:30px; font: bold")
        btn_back.setGraphicsEffect(Util.getNeuShadow(1))
        btn_back.clicked.connect(self.close)

        btn_logout = QPushButton(self)
        btn_logout.setGeometry(29, 46, 200, 50)
        btn_logout.setStyleSheet(
            "border-radius : 3; background-color:#F0F0F3; text-align:center; color:#00A0B5; font-size:20px ")
        btn_logout.setGraphicsEffect(Util.getNeuShadow(0))
        btn_logout1 = QPushButton("LOGOUT", self)
        btn_logout1.setGeometry(29, 46, 200, 50)
        btn_logout1.setStyleSheet(
            "border-radius : 3; background-color:#F0F0F3; text-align:center; color:#00A0B5; font-size:20px ")
        btn_logout1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_logout1.clicked.connect(self.logoutUser)

        btn_reset = QPushButton(self)
        btn_reset.setGeometry(29, 108, 200, 50)
        btn_reset.setStyleSheet(
            "border-radius : 3; background-color:#F0F0F3; text-align:center; color:#00A0B5; font-size:20px")
        btn_reset.setGraphicsEffect(Util.getNeuShadow(0))
        btn_reset1 = QPushButton("RESET", self)
        btn_reset1.setGeometry(29, 108, 200, 50)
        btn_reset1.setStyleSheet(
            "border-radius : 3; background-color:#F0F0F3; text-align:center; color:#00A0B5; font-size:20px")
        btn_reset1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_reset1.clicked.connect(self.file)
    #
        btn_restart = QPushButton(self)
        btn_restart.setGeometry(29, 170, 200, 50)
        btn_restart.setStyleSheet(
            "border-radius : 3; background-color:#F0F0F3; text-align:center; color:#00A0B5; font-size:20px")
        btn_restart.setGraphicsEffect(Util.getNeuShadow(0))
        btn_restart1 = QPushButton("RESTART", self)
        btn_restart1.setGeometry(29, 170, 200, 50)
        btn_restart1.setStyleSheet(
            "border-radius : 3; background-color:#F0F0F3; text-align:center; color:#00A0B5; font-size:20px")
        btn_restart1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_restart1.clicked.connect(self.file)
    #
    def file(self):
        print("pressed")
    #
    def logoutUser(self):
        print("logout clicked")
        if db.logoutUser():
            self.close()
            self.s.close()
            self.home.close()
            self.l = log.LoginForm()
            self.l.show()

if __name__ == '__main__':

    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Power()

    # start the app
    sys.exit(App.exec())



