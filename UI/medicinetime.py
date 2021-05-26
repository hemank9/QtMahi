from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import UI.repeatDosage as rDosage
import UI.extraDosage as extraDosage
import UI.datePickMassEjection as massEject
import UI.changetime as changeTime
import sys
import Utility.MahiUtility as Util

class MyMedicines(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 700)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setStyleSheet("background-color:#FEC32E")
        self.label.setGeometry(0, 0, 1220, 39)
        self.label1 = QLabel(self)
        self.label1.setPixmap(QPixmap('../Resources/medTimeSreen.png'))
        self.label1.setGeometry(48, 242, 1111, 204)


        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        lblMorningBf = QLabel(self)
        lblMorningBf.setStyleSheet("background-color: red; text: bold")
        lblMorningBf.setGeometry(157, 285, 87, 38)
        lblMorningBf.setText("7:30 pm")
        lblMorningBf.setAlignment(Qt.AlignCenter)

        lblMorningAf = QLabel(self)
        lblMorningAf.setStyleSheet("background-color: red; text: bold")
        lblMorningAf.setGeometry(277, 285, 87, 38)
        lblMorningAf.setText("7:30 pm")
        lblMorningAf.setAlignment(Qt.AlignCenter)

        lblAfternoonBf = QLabel(self)
        lblAfternoonBf.setStyleSheet("background-color: red; text: bold")
        lblAfternoonBf.setGeometry(559, 285, 87, 38)
        lblAfternoonBf.setText("7:30 pm")
        lblAfternoonBf.setAlignment(Qt.AlignCenter)

        lblAfternoonAf = QLabel(self)
        lblAfternoonAf.setStyleSheet("background-color: red; text: bold")
        lblAfternoonAf.setGeometry(679, 285, 87, 38)
        lblAfternoonAf.setText("7:30 pm")
        lblAfternoonAf.setAlignment(Qt.AlignCenter)

        lblEveningBf = QLabel(self)
        lblEveningBf.setStyleSheet("background-color: red; text: bold")
        lblEveningBf.setGeometry(946, 285, 87, 38)
        lblEveningBf.setText("7:30 pm")
        lblEveningBf.setAlignment(Qt.AlignCenter)

        lblEveningAf = QLabel(self)
        lblEveningAf.setStyleSheet("background-color: red; text: bold")
        lblEveningAf.setGeometry(1066, 285, 87, 38)
        lblEveningAf.setText("7:30 pm")
        lblEveningAf.setAlignment(Qt.AlignCenter)

        lblEarlyMorning = QLabel(self)
        lblEarlyMorning.setStyleSheet("background-color: red; text: bold")
        lblEarlyMorning.setGeometry(157, 396, 87, 38)
        lblEarlyMorning.setText("7:30 pm")
        lblEarlyMorning.setAlignment(Qt.AlignCenter)

        lblMidNight = QLabel(self)
        lblMidNight.setStyleSheet("background-color: red; text: bold")
        lblMidNight.setGeometry(560, 396, 87, 38)
        lblMidNight.setText("7:30 pm")
        lblMidNight.setAlignment(Qt.AlignCenter)

        lblLateNight = QLabel(self)
        lblLateNight.setStyleSheet("background-color: red; text: bold")
        lblLateNight.setGeometry(939, 396, 87, 38)
        lblLateNight.setText("7:30 pm")
        lblLateNight.setAlignment(Qt.AlignCenter)


        btn_adv1 = QPushButton("", self)
        btn_adv1.setGeometry(218, 55, 237, 105)
        btn_adv1.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_adv1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_adv = QPushButton("", self)
        btn_adv.setGeometry(218, 55, 237, 105)
        btn_adv.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_adv.setGraphicsEffect(Util.getNeuShadow(0))
        btn_adv.setIcon(QtGui.QIcon('../Resources/medAdv.png'))
        btn_adv.setIconSize(QtCore.QSize(237, 105))
        btn_adv.clicked.connect(self.massEjection)

        btn_changeTime1 = QPushButton("", self)
        btn_changeTime1.setGeometry(491, 55, 237, 105)
        btn_changeTime1.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_changeTime1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_changeTime = QPushButton("", self)
        btn_changeTime.setGeometry(491, 55, 237, 105)
        btn_changeTime.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_changeTime.setIcon(QtGui.QIcon('../Resources/changeTime.png'))
        btn_changeTime.setIconSize(QtCore.QSize(237, 105))
        btn_changeTime1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_changeTime.clicked.connect(self.cTime)


        btn_extraDosage = QPushButton("", self)
        btn_extraDosage.setGeometry(765, 55, 237, 105)
        btn_extraDosage.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_extraDosage.setGraphicsEffect(Util.getNeuShadow(1))
        btn_extraDosage = QPushButton("", self)
        btn_extraDosage.setGeometry(765, 55, 237, 105)
        btn_extraDosage.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_extraDosage.setIcon(QtGui.QIcon('../Resources/extraDose.png'))
        btn_extraDosage.setIconSize(QtCore.QSize(237, 105))
        btn_extraDosage.setGraphicsEffect(Util.getNeuShadow(0))
        btn_extraDosage.clicked.connect(self.extraD)

        btn_bck = QPushButton("", self)
        btn_bck.setGeometry(43, 40, 150, 55)
        btn_bck.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_bck.setIcon(QtGui.QIcon('../Resources/backButton.png'))
        btn_bck.setIconSize(QtCore.QSize(160, 90))
        btn_bck.clicked.connect(self.close)


    # def afterNoonClicked(self):
    #     self.k = changeTime.ChangeTime(2)
    #     self.k.show()
    #
    # def morningClicked(self):
    #     self.k = changeTime.ChangeTime(1)
    #     self.k.show()
    #
    # def eveningClicked(self):
    #     self.k = changeTime.ChangeTime(3)
    #     self.k.show()


    def repeateD(self):
        self.l = rDosage.RepeatDosage()
        self.l.show()

    def massEjection(self):
        self.n = massEject.MassEjectDateTime()
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
    window = MyMedicines()

    window.show()

# start the app
    sys.exit(App.exec())



