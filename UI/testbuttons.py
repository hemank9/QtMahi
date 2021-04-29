from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5 import QtCore
import sys


class HomeScreen(QMainWindow):
    def __init__(self, parent = None):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 685)

        # calling method
        self.UiComponents()
        self.setStyleSheet("background-color: #E5E5E5")
        self.label = QLabel(self)
        self.label.setStyleSheet("background-color: #FEC32E")
        self.label.setGeometry(0,0,1220,39)

        # showing all the widgets
        self.show()

        # method for widgets

    def UiComponents(self):

        # creating a push button
        btn_cal = QPushButton("", self)
        # self.lblCal = QLabel(self)
        # # self.lblCal.setStyleSheet("background-color: red; border-radius : 10")
        # self.lblCal.setGeometry(40, 77, 194, 276)
        # self.lblCal.setPixmap(QPixmap('Resources/newCal.png'))

        # setting geometry of button
        btn_cal.setGeometry(40, 77, 194, 276)

        # setting radius and border
        btn_cal.setStyleSheet("border-radius : 30; background-color : #E0E0E5")
        btn_cal.setIcon(QtGui.QIcon('Resources/newCal.png'))
        btn_cal.setIconSize(QtCore.QSize(214, 296))
        # adding action to a button
        # btn_cal.clicked.connect(self.Calendar)

        #profilebutton
        btn_pro = QPushButton("PROFILE", self)
        btn_pro.setGeometry(272, 77, 349, 194)
        btn_pro.setStyleSheet("border-radius : 30; background-color : #E0E0E5 ; color:#FFFFFF; text-align:left")
        btn_pro.setIcon(QtGui.QIcon('Resources/myprofile.png'))
        btn_pro.setIconSize(QtCore.QSize(349, 194))
        # btn_pro.clicked.connect(self.profileClicked)

        # mymedcicinebutton
        btn_med = QPushButton("MY MEDICINE", self)
        btn_med.setGeometry(660, 77, 379, 194)
        btn_med.setStyleSheet("border-radius : 30; background-color : #E5E5E5; text-align:top ; text-align:left; focus:pressed")
        btn_med.setIcon(QtGui.QIcon('Resources/mymed.png'))
        btn_med.setIconSize(QtCore.QSize(379, 194))
        # btn_med.clicked.connect(self.myMedsClicked)

        # mystatsbutton
        btn_stat = QPushButton("MY STATS", self)
        btn_stat.setGeometry(40, 390, 346, 261)
        btn_stat.setStyleSheet("border-radius : 30; background-color : #E5E5E5; color:#FFFFFF; text-align:left")
        btn_stat.setIcon(QtGui.QIcon('Resources/mystats.png'))
        btn_stat.setIconSize(QtCore.QSize(346, 261))
        # btn_stat.clicked.connect(self.clickme)

        # settingsbutton    background-image : Resources(setm.png)  background-color : #F5A5BF  color:#FFFFFF
        btn_sett = QPushButton("", self)
        btn_sett.setGeometry(415, 430, 194, 221)
        btn_sett.setStyleSheet("border-radius : 30; background-color : #E5E5E5; text-align:left")
        btn_sett.setIcon(QtGui.QIcon('Resources/set.png'))
        btn_sett.setIconSize(QtCore.QSize(194,221))
        # btn_sett.clicked.connect(self.settingsClicked)

        # medtimebutton
        btn_time = QPushButton("", self)
        btn_time.setGeometry(635, 430, 191, 124)
        btn_time.setStyleSheet("border-radius : 15; background-color : #E5E5E5; color:#FFFFFF; text-align:left")
        btn_time.setIcon(QtGui.QIcon('Resources/medtime.png'))
        btn_time.setIconSize(QtCore.QSize(191, 124))
        # btn_time.clicked.connect(self.medTimeClicked)


        # hummbutton
        btn_humm = QPushButton("", self)
        btn_humm.setGeometry(857, 430, 181, 125)
        btn_humm.setStyleSheet("border-radius : 15; background-color : #E5E5E5; color:#FFFFFF; text-align:left")
        btn_humm.setIcon(QtGui.QIcon('Resources/hum.png'))
        btn_humm.setIconSize(QtCore.QSize(181, 125))
        # btn_humm.clicked.connect(self.hummClicked)


        # barbutton
        btn_bar = QPushButton("", self)
        btn_bar.setGeometry(272, 313, 767, 83)
        btn_bar.setStyleSheet("border-radius : 20; background-color : #E5E5E5; color:#FFFFFF; text-align:left")
        btn_bar.setIcon(QtGui.QIcon('Resources/menubar.png'))
        btn_bar.setIconSize(QtCore.QSize(767, 83))
        # btn_bar.clicked.connect(self.clickme)


        # refill
        lblRefill = QLabel(self)
        lblRefill.setPixmap(QPixmap('Resources/newRefill.png'))
        lblRefill.setGeometry(1057, 76, 140, 477)
        lblRefill.setStyleSheet("background-color: red")
        # btn_refill = QPushButton("", self)
        # btn_refill.setGeometry(1057, 47, 134, 517)
        # btn_refill.setStyleSheet("border-radius : 20; background-color : #E5E5E5; text-align:left")
        # # btn_refill.setIcon(QtGui.QIcon('Resources/medfill.png'))
        # btn_refill.setIconSize(QtCore.QSize(134, 477))
        # btn_refill.clicked.connect(self.clickme)


        # doc_appointment_button
        btn_doc = QPushButton("", self)
        btn_doc.setGeometry(635, 574, 551, 92)
        btn_doc.setStyleSheet("border-radius : 15; background-color : #E5E5E5; color:#FFFFFF; text-align:left")
        btn_doc.setIcon(QtGui.QIcon('Resources/doc.png'))
        btn_doc.setIconSize(QtCore.QSize(551, 92))
        # btn_doc.clicked.connect(self.docAppoClicked)



if __name__ == '__main__':

    App = QApplication(sys.argv)

    # create the instance of our Window
    window = HomeScreen()
    window.show()

    # start the app
    sys.exit(App.exec())