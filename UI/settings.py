from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import UI.login as log
import MyDatabase.my_database as db

class Window2(QWidget):
    def __init__(self,settings, home):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(260, 160, 550, 500)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        # self.label.setPixmap(QPixmap('Resources\yellow.png'))
        # self.label.setGeometry(0, 0, 1220, 39)
        self.UiComponents()
        self.s = settings
        self.home = home
        #
        #     # showing all the widgets
        self.show()
        #

    def UiComponents(self):
        btn_logout = QPushButton("LOGOUT", self)
        btn_logout.setGeometry(41, 50, 470, 127)
        btn_logout.setStyleSheet("border-radius : 15; background-color:#EE488D; text-align:center; color:white; font-size:20px ")
        # btn_logout.setIcon(QtGui.QIcon('Resources\mfile1.png'))
        # btn_logout.setIconSize(QtCore.QSize(1138, 76))
        btn_logout.clicked.connect(self.logoutUser)

        btn_reset = QPushButton("RESET", self)
        btn_reset.setGeometry(41, 208, 470, 127)
        btn_reset.setStyleSheet("border-radius : 15; background-color:#00A0B5; text-align:center; color:white; font-size:20px")
        # btn_reset.setIcon(QtGui.QIcon('Resources\mfile1.png'))
        # btn_reset.setIconSize(QtCore.QSize(1138, 76))
        btn_reset.clicked.connect(self.file)

        btn_restart = QPushButton("RESTART", self)
        btn_restart.setGeometry(41, 365, 470, 127)
        btn_restart.setStyleSheet("border-radius : 15; background-color:#00A0B5; text-align:center; color:white; font-size:20px")
        # btn_restart.setIcon(QtGui.QIcon('Resources\mfile1.png'))
        # btn_restart.setIconSize(QtCore.QSize(1138, 76))
        btn_restart.clicked.connect(self.file)

    def file(self):
        print("pressed")
    def logoutUser(self):
        print("logout clicked")
        if db.logoutUser():
            self.close()
            self.s.close()
            self.home.close()
            self.l = log.LoginForm()
            self.l.show()





class Settings(QWidget):  # <===
    def __init__(self,home):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 700)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\yellow.png'))
        self.label.setGeometry(0, 0, 1220, 39)

        self.home = home
        self.UiComponents()
        #
        #     # showing all the widgets
        self.show()

    #

    def UiComponents(self):

        btn_file1 = QPushButton("", self)
        btn_file1.setGeometry(925, 531, 260, 105)
        btn_file1.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        btn_file1.setIcon(QtGui.QIcon('../Resources/power.png'))
        btn_file1.setIconSize(QtCore.QSize(290, 185))
        btn_file1.clicked.connect(self.logout)

    def logout(self):
        # printing pressed
        self.l = Window2(self,self.home)
        self.l.show()


# App = QApplication(sys.argv)
#
# # create the instance of our Window
# window = Settings()
#
# window.show()
#
# # start the app
# sys.exit(App.exec())