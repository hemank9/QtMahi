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
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: #F0F0F3")
        self.UiComponents()
        self.s = settings
        self.home = home
        #
        #     # showing all the widgets
        self.show()
        #

    def UiComponents(self):
        btn_logout = QPushButton(self)
        btn_logout.setGeometry(41, 50, 470, 127)
        btn_logout.setStyleSheet("border-radius : 15; background-color:#F0F0F3; text-align:center; color:#EE488D; font-size:20px ")
        btn_logout.setGraphicsEffect(Util.getNeuShadow(0))
        btn_logout1 = QPushButton("LOGOUT", self)
        btn_logout1.setGeometry(41, 50, 470, 127)
        btn_logout1.setStyleSheet("border-radius : 15; background-color:#F0F0F3; text-align:center; color:#EE488D; font-size:20px ")
        btn_logout1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_logout1.clicked.connect(self.logoutUser)

        btn_reset = QPushButton(self)
        btn_reset.setGeometry(41, 208, 470, 127)
        btn_reset.setStyleSheet("border-radius : 15; background-color:#F0F0F3; text-align:center; color:#00A0B5; font-size:20px")
        btn_reset.setGraphicsEffect(Util.getNeuShadow(0))
        btn_reset1 = QPushButton("RESET", self)
        btn_reset1.setGeometry(41, 208, 470, 127)
        btn_reset1.setStyleSheet("border-radius : 15; background-color:#F0F0F3; text-align:center; color:#00A0B5; font-size:20px")
        btn_reset1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_reset1.clicked.connect(self.file)

        btn_restart = QPushButton(self)
        btn_restart.setGeometry(41, 365, 470, 127)
        btn_restart.setStyleSheet("border-radius : 15; background-color:#F0F0F3; text-align:center; color:#006CB5; font-size:20px")
        btn_restart.setGraphicsEffect(Util.getNeuShadow(0))
        btn_restart1 = QPushButton("RESTART", self)
        btn_restart1.setGeometry(41, 365, 470, 127)
        btn_restart1.setStyleSheet("border-radius : 15; background-color:#F0F0F3; text-align:center; color:#006CB5; font-size:20px")
        btn_restart1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_restart1.clicked.connect(self.file)

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

        self.home = home
        self.UiComponents()
        #
        #     # showing all the widgets
        self.show()

    #

    def UiComponents(self):

        self.line = QLabel(self)
        self.line.setGeometry(267, 24, 3, 637)
        self.line.setPixmap(QPixmap('../Resources/line.png'))

        self.wifiBtn1 = QPushButton("Wifi", self)
        self.wifiBtn1.setGeometry(26, 99, 180, 48)
        self.wifiBtn1.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.wifiBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        self.wifiBtn = QPushButton("Wifi", self)
        self.wifiBtn.setGeometry(26, 99, 180, 48)
        self.wifiBtn.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.wifiBtn.setGraphicsEffect(Util.getNeuShadow(1))

        self.BluetoothBtn1 = QPushButton("Wifi", self)
        self.BluetoothBtn1.setGeometry(26, 163, 180, 48)
        self.BluetoothBtn1.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.BluetoothBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        self.BluetoothBtn = QPushButton("Bluetooth", self)
        self.BluetoothBtn.setGeometry(26, 163, 180, 48)
        self.BluetoothBtn.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.BluetoothBtn.setGraphicsEffect(Util.getNeuShadow(1))

        self.UserSetBtn1 = QPushButton( self)
        self.UserSetBtn1.setGeometry(26, 227, 180, 48)
        self.UserSetBtn1.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.UserSetBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        self.UserSetBtn = QPushButton("User Settings", self)
        self.UserSetBtn.setGeometry(26, 227, 180, 48)
        self.UserSetBtn.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.UserSetBtn.setGraphicsEffect(Util.getNeuShadow(1))

        self.NotifBtn1 = QPushButton(self)
        self.NotifBtn1.setGeometry(26, 291, 180, 48)
        self.NotifBtn1.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.NotifBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        self.NotifBtn = QPushButton("Notifications", self)
        self.NotifBtn.setGeometry(26, 291, 180, 48)
        self.NotifBtn.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.NotifBtn.setGraphicsEffect(Util.getNeuShadow(1))

        self.DevicesBtn1 = QPushButton(self)
        self.DevicesBtn1.setGeometry(26, 355, 180, 48)
        self.DevicesBtn1.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.DevicesBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        self.DevicesBtn = QPushButton("Devices", self)
        self.DevicesBtn.setGeometry(26, 355, 180, 48)
        self.DevicesBtn.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.DevicesBtn.setGraphicsEffect(Util.getNeuShadow(1))

        self.HelpBtn1 = QPushButton(self)
        self.HelpBtn1.setGeometry(26, 419, 180, 48)
        self.HelpBtn1.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.HelpBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        self.HelpBtn = QPushButton("Help", self)
        self.HelpBtn.setGeometry(26, 419, 180, 48)
        self.HelpBtn.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.HelpBtn.setGraphicsEffect(Util.getNeuShadow(1))

        self.SyncBtn1 = QPushButton(self)
        self.SyncBtn1.setGeometry(26, 483, 180, 48)
        self.SyncBtn1.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.SyncBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        self.SyncBtn = QPushButton("Sync", self)
        self.SyncBtn.setGeometry(26, 483, 180, 48)
        self.SyncBtn.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.SyncBtn.setGraphicsEffect(Util.getNeuShadow(1))

        self.FaqBtn1 = QPushButton(self)
        self.FaqBtn1.setGeometry(26, 547, 180, 48)
        self.FaqBtn1.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.FaqBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        self.FaqBtn = QPushButton("FAQ", self)
        self.FaqBtn.setGeometry(26, 547, 180, 48)
        self.FaqBtn.setStyleSheet("background-color:#F0F0F3; border-radius: 5; color: #00A0B5")
        self.FaqBtn.setGraphicsEffect(Util.getNeuShadow(1))

        self.quesRefillLbl = QLabel("Do you want to refill now?", self)
        self.quesRefillLbl.setGeometry(29, 21, 194, 48)
        self.quesRefillLbl.setPixmap(QPixmap('../Resources/settingsScreen.png'))


        # btn_power = QPushButton("", self)
        # btn_power.setGeometry(925, 531, 260, 115)
        # btn_power.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        # btn_power.setGraphicsEffect(Util.getNeuShadow(0))
        # btn_power.clicked.connect(self.logout)
        #
        # btn_power1 = QPushButton("", self)
        # btn_power1.setGeometry(925, 531, 260, 115)
        # btn_power1.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        # btn_power1.setGraphicsEffect(Util.getNeuShadow(1))
        # btn_power1.setIcon(QtGui.QIcon('..\Resources\power.png'))
        # btn_power1.setIconSize(QtCore.QSize(260, 115))
        # btn_power1.clicked.connect(self.logout)
        #
        # btn_privacy = QPushButton("", self)
        # btn_privacy.setGeometry(925, 374, 260, 115)
        # btn_privacy.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        # btn_privacy.setGraphicsEffect(Util.getNeuShadow(0))
        # btn_privacy.clicked.connect(self.logout)
        #
        # btn_privacy1 = QPushButton("", self)
        # btn_privacy1.setGeometry(925, 374, 260, 115)
        # btn_privacy1.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        # btn_privacy1.setGraphicsEffect(Util.getNeuShadow(1))
        # btn_privacy1.setIcon(QtGui.QIcon('..\Resources\privacy.png'))
        # btn_privacy1.setIconSize(QtCore.QSize(260, 115))
        # btn_privacy1.clicked.connect(self.logout)
        #
        # btn_terms = QPushButton("", self)
        # btn_terms.setGeometry(925, 217, 260, 115)
        # btn_terms.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        # btn_terms.setGraphicsEffect(Util.getNeuShadow(0))
        # btn_terms.clicked.connect(self.logout)
        #
        # btn_terms1 = QPushButton("", self)
        # btn_terms1.setGeometry(925, 217, 260, 115)
        # btn_terms1.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        # btn_terms1.setGraphicsEffect(Util.getNeuShadow(1))
        # btn_terms1.setIcon(QtGui.QIcon('..\Resources\\terms.png'))
        # btn_terms1.setIconSize(QtCore.QSize(260, 115))
        # btn_terms1.clicked.connect(self.logout)
        #
        # btn_help = QPushButton("", self)
        # btn_help.setGeometry(925, 60, 260, 115)
        # btn_help.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        # btn_help.setGraphicsEffect(Util.getNeuShadow(0))
        # btn_help.clicked.connect(self.logout)
        #
        # btn_help1 = QPushButton("", self)
        # btn_help1.setGeometry(925, 60, 260, 115)
        # btn_help1.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        # btn_help1.setGraphicsEffect(Util.getNeuShadow(1))
        # btn_help1.setIcon(QtGui.QIcon('..\Resources\\help.png'))
        # btn_help1.setIconSize(QtCore.QSize(260, 115))
        # btn_help1.clicked.connect(self.logout)
        #
        # btn_music = QPushButton("", self)
        # btn_music.setGeometry(630, 60, 260, 115)
        # btn_music.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        # btn_music.setGraphicsEffect(Util.getNeuShadow(0))
        # btn_music.clicked.connect(self.logout)
        #
        # btn_music1 = QPushButton("", self)
        # btn_music1.setGeometry(630, 60, 260, 115)
        # btn_music1.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        # btn_music1.setGraphicsEffect(Util.getNeuShadow(1))
        # btn_music1.setIcon(QtGui.QIcon('..\Resources\\music.png'))
        # btn_music1.setIconSize(QtCore.QSize(260, 115))
        # btn_music1.clicked.connect(self.logout)
        #
        # btn_sync = QPushButton("", self)
        # btn_sync.setGeometry(630, 217, 260, 115)
        # btn_sync.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        # btn_sync.setGraphicsEffect(Util.getNeuShadow(0))
        # btn_sync.clicked.connect(self.logout)
        #
        # btn_sync1 = QPushButton("", self)
        # btn_sync1.setGeometry(630, 217, 260, 115)
        # btn_sync1.setStyleSheet("border-radius : 15; background-color: #F0F0F3")
        # btn_sync1.setGraphicsEffect(Util.getNeuShadow(1))
        # btn_sync1.setIcon(QtGui.QIcon('..\Resources\\sync.png'))
        # btn_sync1.setIconSize(QtCore.QSize(260, 115))
        # btn_sync1.clicked.connect(self.logout)

    def logout(self):
        # printing pressed
        self.l = Window2(self, self.home)
        self.l.show()

# #
App = QApplication(sys.argv)

# create the instance of our Window
window = Settings(home=0)

window.show()

# start the app
sys.exit(App.exec())
