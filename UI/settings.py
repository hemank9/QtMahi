from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import UI.login as log
import MyDatabase.my_database as db
import Utility.MahiUtility as Util


class Window2(QWidget):
    def __init__(self,settings, home):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(260, 160, 550, 500)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../Resources\yellow.png'))
        self.label.setGeometry(0, 0, 1220, 39)
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
        self.label.setPixmap(QPixmap('..\Resources\yellow.png'))
        self.label.setGeometry(0, 0, 1220, 39)

        self.home = home
        self.UiComponents()
        #
        #     # showing all the widgets
        self.show()

    #

    def UiComponents(self):

        btn_power = QPushButton("", self)
        btn_power.setGeometry(925, 531, 260, 115)
        btn_power.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        btn_power.setGraphicsEffect(Util.getNeuShadow(0))
        btn_power.clicked.connect(self.logout)

        btn_power1 = QPushButton("", self)
        btn_power1.setGeometry(925, 531, 260, 115)
        btn_power1.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        btn_power1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_power1.setIcon(QtGui.QIcon('..\Resources\power.png'))
        btn_power1.setIconSize(QtCore.QSize(260, 115))
        btn_power1.clicked.connect(self.logout)

        btn_privacy = QPushButton("", self)
        btn_privacy.setGeometry(925, 374, 260, 115)
        btn_privacy.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        btn_privacy.setGraphicsEffect(Util.getNeuShadow(0))
        btn_privacy.clicked.connect(self.logout)

        btn_privacy1 = QPushButton("", self)
        btn_privacy1.setGeometry(925, 374, 260, 115)
        btn_privacy1.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        btn_privacy1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_privacy1.setIcon(QtGui.QIcon('..\Resources\privacy.png'))
        btn_privacy1.setIconSize(QtCore.QSize(260, 115))
        btn_privacy1.clicked.connect(self.logout)

        btn_terms = QPushButton("", self)
        btn_terms.setGeometry(925, 217, 260, 115)
        btn_terms.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        btn_terms.setGraphicsEffect(Util.getNeuShadow(0))
        btn_terms.clicked.connect(self.logout)

        btn_terms1 = QPushButton("", self)
        btn_terms1.setGeometry(925, 217, 260, 115)
        btn_terms1.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        btn_terms1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_terms1.setIcon(QtGui.QIcon('..\Resources\\terms.png'))
        btn_terms1.setIconSize(QtCore.QSize(260, 115))
        btn_terms1.clicked.connect(self.logout)

        btn_help = QPushButton("", self)
        btn_help.setGeometry(925, 60, 260, 115)
        btn_help.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        btn_help.setGraphicsEffect(Util.getNeuShadow(0))
        btn_help.clicked.connect(self.logout)

        btn_help1 = QPushButton("", self)
        btn_help1.setGeometry(925, 60, 260, 115)
        btn_help1.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        btn_help1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_help1.setIcon(QtGui.QIcon('..\Resources\\help.png'))
        btn_help1.setIconSize(QtCore.QSize(260, 115))
        btn_help1.clicked.connect(self.logout)

        btn_music = QPushButton("", self)
        btn_music.setGeometry(630, 60, 260, 115)
        btn_music.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        btn_music.setGraphicsEffect(Util.getNeuShadow(0))
        btn_music.clicked.connect(self.logout)

        btn_music1 = QPushButton("", self)
        btn_music1.setGeometry(630, 60, 260, 115)
        btn_music1.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        btn_music1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_music1.setIcon(QtGui.QIcon('..\Resources\\music.png'))
        btn_music1.setIconSize(QtCore.QSize(260, 115))
        btn_music1.clicked.connect(self.logout)

        btn_sync = QPushButton("", self)
        btn_sync.setGeometry(630, 217, 260, 115)
        btn_sync.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        btn_sync.setGraphicsEffect(Util.getNeuShadow(0))
        btn_sync.clicked.connect(self.logout)

        btn_sync1 = QPushButton("", self)
        btn_sync1.setGeometry(630, 217, 260, 115)
        btn_sync1.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        btn_sync1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_sync1.setIcon(QtGui.QIcon('..\Resources\\sync.png'))
        btn_sync1.setIconSize(QtCore.QSize(260, 115))
        btn_sync1.clicked.connect(self.logout)

    def logout(self):
        # printing pressed
        self.l = Window2(self,self.home)
        self.l.show()

#
# App = QApplication(sys.argv)
#
# # create the instance of our Window
# window = Settings()
#
# window.show()
#
# # start the app
# sys.exit(App.exec())
