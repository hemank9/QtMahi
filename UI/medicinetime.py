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
import MyDatabase.my_database as myDb

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

        self.TextStyle = "text: bold; font-size:17px"
        self.lblMorningBf = QLabel(self)
        self.lblMorningBf.setStyleSheet(self.TextStyle)
        self.lblMorningBf.setGeometry(157, 285, 87, 38)
        self.lblMorningBf.setAlignment(Qt.AlignCenter)

        self.lblMorningAf = QLabel(self)
        self.lblMorningAf.setStyleSheet(self.TextStyle)
        self.lblMorningAf.setGeometry(277, 285, 87, 38)
        self.lblMorningAf.setAlignment(Qt.AlignCenter)

        self.lblAfternoonBf = QLabel(self)
        self.lblAfternoonBf.setStyleSheet(self.TextStyle)
        self.lblAfternoonBf.setGeometry(559, 285, 87, 38)
        self.lblAfternoonBf.setAlignment(Qt.AlignCenter)

        self.lblAfternoonAf = QLabel(self)
        self.lblAfternoonAf.setStyleSheet(self.TextStyle)
        self.lblAfternoonAf.setGeometry(679, 285, 87, 38)
        self.lblAfternoonAf.setAlignment(Qt.AlignCenter)

        self.lblEveningBf = QLabel(self)
        self.lblEveningBf.setStyleSheet(self.TextStyle)
        self.lblEveningBf.setGeometry(938, 285, 87, 38)
        self.lblEveningBf.setAlignment(Qt.AlignCenter)

        self.lblEveningAf = QLabel(self)
        self.lblEveningAf.setStyleSheet(self.TextStyle)
        self.lblEveningAf.setGeometry(1058, 285, 87, 38)
        self.lblEveningAf.setAlignment(Qt.AlignCenter)

        lblEarlyMorning = QLabel(self)
        lblEarlyMorning.setStyleSheet(self.TextStyle)
        lblEarlyMorning.setGeometry(157, 396, 87, 38)
        lblEarlyMorning.setText("7:30 pm")
        lblEarlyMorning.setAlignment(Qt.AlignCenter)

        lblMidNight = QLabel(self)
        lblMidNight.setStyleSheet(self.TextStyle)
        lblMidNight.setGeometry(560, 396, 87, 38)
        lblMidNight.setText("7:30 pm")
        lblMidNight.setAlignment(Qt.AlignCenter)

        lblLateNight = QLabel(self)
        lblLateNight.setStyleSheet(self.TextStyle)
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

        self.SetCylinderData()

    def SetCylinderData(self):

        try:
            cursor = myDb.getSlotTimings()

            for row in cursor:
                # print(row)

                time = Util.convert24to12Time(str(row[3]))

                if time == None:
                    time = "N.A."

                # Morning
                if str(row[1]).lower() == "morning":
                    if "before" in str(row[2]):
                        self.lblMorningBf.setText(time)
                    elif "after" in str(row[2]):
                        self.lblMorningAf.setText(time)

                # Afternoon
                elif str(row[1]).lower() == "afternoon" or str(row[1]).lower() == "noon":
                    if "before" in str(row[2]):
                        self.lblAfternoonBf.setText(time)
                    elif "after" in str(row[2]):
                        self.lblAfternoonAf.setText(time)

                # Evening
                elif str(row[1]).lower() == "evening":
                    if "before" in str(row[2]):
                        self.lblEveningBf.setText(time)
                    elif "after" in str(row[2]):
                        self.lblEveningAf.setText(time)


        except Exception as e:
            print(e.__cause__)


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
#
# if __name__ == '__main__':
#     App = QApplication(sys.argv)
#
#     # create the instance of our Window
#     window = MyMedicines()
#
#     window.show()
#
# # start the app
#     sys.exit(App.exec())



