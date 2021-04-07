from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import UI.repeatDosage as rDosage
import UI.extraDosage as extraDosage
import UI.massEjection as massEject
import UI.changetime as changeTime
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
        self.label.setPixmap(QPixmap('../Resources/bckmedtime.png'))
        self.label.setGeometry(0, 0, 1220, 473)


        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        btn_adv = QPushButton("", self)
        btn_adv.setGeometry(96, 529, 250, 115)
        btn_adv.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_adv.setIcon(QtGui.QIcon('../Resources/Group 52.png'))
        btn_adv.setIconSize(QtCore.QSize(280, 135))
        btn_adv.clicked.connect(self.massEjection)

        btn_ctime = QPushButton("", self)
        btn_ctime.setGeometry(360, 530, 250, 114)
        btn_ctime.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_ctime.setIcon(QtGui.QIcon('../Resources/Group 51.png'))
        btn_ctime.setIconSize(QtCore.QSize(280, 135))
        btn_ctime.clicked.connect(self.cTime)

        btn_repetativeD = QPushButton("", self)
        btn_repetativeD.setGeometry(625, 530, 237, 115)
        btn_repetativeD.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_repetativeD.setIcon(QtGui.QIcon('../Resources/repetative.png'))
        btn_repetativeD.setIconSize(QtCore.QSize(280, 135))
        btn_repetativeD.clicked.connect(self.repeateD)

        btn_dosage = QPushButton("", self)
        btn_dosage.setGeometry(890, 530, 250, 114)
        btn_dosage.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_dosage.setIcon(QtGui.QIcon('../Resources/Group 53.png'))
        btn_dosage.setIconSize(QtCore.QSize(280, 135))
        btn_dosage.clicked.connect(self.extraD)


        # MOrning, Afternoon, Evening Buttons

        btn_evening = QPushButton("", self)
        btn_evening.setGeometry(826, 100, 320, 320)
        btn_evening.setStyleSheet("border-radius : 10; background-color: #0000")
        btn_evening.setIcon(QtGui.QIcon('../Resources/evening.png'))
        btn_evening.setIconSize(QtCore.QSize(330, 330))
        btn_evening.clicked.connect(self.eveningClicked)

        btn_afternoon = QPushButton("", self)
        btn_afternoon.setGeometry(457, 100, 320, 320)
        btn_afternoon.setStyleSheet("border-radius : 10; background-color: #0000")
        btn_afternoon.setIcon(QtGui.QIcon('../Resources/afternoon.png'))
        btn_afternoon.setIconSize(QtCore.QSize(330, 330))
        btn_afternoon.clicked.connect(self.afterNoonClicked)

        btn_morning = QPushButton("", self)
        btn_morning.setGeometry(88, 100, 320, 320)
        btn_morning.setStyleSheet("border-radius : 10; background-color: #0000")
        btn_morning.setIcon(QtGui.QIcon('../Resources/morning.png'))
        btn_morning.setIconSize(QtCore.QSize(330, 330))
        btn_morning.clicked.connect(self.morningClicked)

        btn_bck = QPushButton("", self)
        btn_bck.setGeometry(43, 40, 150, 55)
        btn_bck.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_bck.setIcon(QtGui.QIcon('../Resources/Group 34.png'))
        btn_bck.setIconSize(QtCore.QSize(160, 90))
        btn_bck.clicked.connect(self.close)


    def afterNoonClicked(self):
        self.k = changeTime.ChangeTime(2)
        self.k.show()

    def morningClicked(self):
        self.k = changeTime.ChangeTime(1)
        self.k.show()

    def eveningClicked(self):
        self.k = changeTime.ChangeTime(3)
        self.k.show()


    def repeateD(self):
        self.l = rDosage.RepeatDosage()
        self.l.show()

    def massEjection(self):
        self.n = massEject.MassEject()
        self.n.show()


    def extraD(self):
        self.m = extraDosage.ExtraDosage()
        self.m.show()

    def cTime(self):
        self.k = changeTime.ChangeTime(1)
        self.k.show()

if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    window.show()

# start the app
    sys.exit(App.exec())



