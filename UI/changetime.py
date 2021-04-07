import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Utility.MahiUtility as Util



class ChangeTime(QMainWindow):

    def __init__(self, type):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 700)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../Resources/mtry.png'))
        self.label.setGeometry(0, 0, 1220, 700)

        # calling method
        self.UiComponents()

        self.dayTimeSelected(type)

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        self.btnStyle = "border-radius : 15; background-color: #F0F03; color : #00A0B5;font:bold;font-size:20px"
        self.btnStyleSelected = "border-radius : 15; background-color: #BCE6EC; color : #00A0B5;font:bold;font-size:20px"

        self.bfHour = 10
        self.bfMin = 10

        self.afHour = 10
        self.afMin = 10

        self.IotHour = 10
        self.IotMin = 10


        btn_bck = QPushButton("", self)
        btn_bck.setGeometry(43, 48, 150, 75)
        btn_bck.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_bck.setIcon(QtGui.QIcon('../Resources/Group 34.png'))
        btn_bck.setIconSize(QtCore.QSize(160, 90))
        btn_bck.clicked.connect(self.close)

        self.lblt = QLabel("Morning", self)
        self.lblt.setGeometry(354, 70, 135, 40)
        self.lblt.setStyleSheet("color:#00A0B5;font-size:27px; font:bold")

        lblbf = QLabel("Before Food", self)
        lblbf.setGeometry(354, 143, 115, 29)
        lblbf.setStyleSheet("font-size:18px;")

        lblaf = QLabel("After Food", self)
        lblaf.setGeometry(651, 143, 105, 40)
        lblaf.setStyleSheet("font-size:18px;")

        lblnt = QLabel("IOT", self)
        lblnt.setGeometry(954, 143, 105, 40)
        lblnt.setStyleSheet("font-size:18px;")

        # Buttons for Morning Before Food

        btnbfHourAdd = QPushButton("", self)
        btnbfHourAdd.setGeometry(354, 211, 45, 33)
        btnbfHourAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnbfHourAdd.setIcon(QtGui.QIcon('../Resources/mAddTime.png'))
        btnbfHourAdd.setIconSize(QtCore.QSize(160, 90))
        btnbfHourAdd.clicked.connect(self.addBfHour)

        btnbfHourSub = QPushButton("", self)
        btnbfHourSub.setGeometry(354, 296, 45, 33)
        btnbfHourSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnbfHourSub.setIcon(QtGui.QIcon('../Resources/mSubTime.png'))
        btnbfHourSub.setIconSize(QtCore.QSize(160, 90))
        btnbfHourSub.clicked.connect(self.subBfHour)

        btnbfMinAdd = QPushButton("", self)
        btnbfMinAdd.setGeometry(430, 211, 45, 33)
        btnbfMinAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnbfMinAdd.setIcon(QtGui.QIcon('../Resources/mAddTime.png'))
        btnbfMinAdd.setIconSize(QtCore.QSize(160, 90))
        btnbfMinAdd.clicked.connect(self.addBfMin)

        btnbfMinSub = QPushButton("", self)
        btnbfMinSub.setGeometry(430, 296, 45, 33)
        btnbfMinSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnbfMinSub.setIcon(QtGui.QIcon('../Resources/mSubTime.png'))
        btnbfMinSub.setIconSize(QtCore.QSize(160, 90))
        btnbfMinSub.clicked.connect(self.subBfMin)

        btnBfAmPm = QPushButton("", self)
        btnBfAmPm.setGeometry(506, 253, 45, 33)
        btnBfAmPm.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnBfAmPm.setIcon(QtGui.QIcon('../Resources/pmbtn.png'))
        btnBfAmPm.setIconSize(QtCore.QSize(160, 90))
        btnBfAmPm.clicked.connect(self.close)

        self.lblBfAmPm = QLabel("am", self)
        self.lblBfAmPm.setGeometry(514, 253, 25, 25)

        display_lbl = QLabel(self)
        display_lbl.setPixmap(QPixmap('../Resources/mBkg.png'))
        display_lbl.setGeometry(354, 253, 45, 33)
        self.lblBfHour = QLabel(str(self.bfHour), self)
        self.lblBfHour.setGeometry(360, 260, 30, 21)
        self.lblBfHour.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBfHour.setStyleSheet("background-color : #0000")

        display2_lbl = QLabel(self)
        display2_lbl.setPixmap(QPixmap('../Resources/mBkg.png'))
        display2_lbl.setGeometry(430, 253, 45, 33)
        self.lblBfMin = QLabel(str(self.bfMin), self)
        self.lblBfMin.setGeometry(436, 260, 30, 21)
        self.lblBfMin.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBfMin.setStyleSheet("background-color : #0000")

        # Buttons for Morning After Food

        btnAfHourAdd = QPushButton("", self)
        btnAfHourAdd.setGeometry(651, 211, 45, 33)
        btnAfHourAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAfHourAdd.setIcon(QtGui.QIcon('../Resources/mAddTime.png'))
        btnAfHourAdd.setIconSize(QtCore.QSize(160, 90))
        btnAfHourAdd.clicked.connect(self.addAfHour)

        btnAfHourSub = QPushButton("", self)
        btnAfHourSub.setGeometry(651, 296, 45, 33)
        btnAfHourSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAfHourSub.setIcon(QtGui.QIcon('../Resources/mSubTime.png'))
        btnAfHourSub.setIconSize(QtCore.QSize(160, 90))
        btnAfHourSub.clicked.connect(self.subAfHour)

        btnAfMinAdd = QPushButton("", self)
        btnAfMinAdd.setGeometry(727, 211, 45, 33)
        btnAfMinAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAfMinAdd.setIcon(QtGui.QIcon('../Resources/mAddTime.png'))
        btnAfMinAdd.setIconSize(QtCore.QSize(160, 90))
        btnAfMinAdd.clicked.connect(self.addAfMin)

        btnAfMinSub = QPushButton("", self)
        btnAfMinSub.setGeometry(727, 296, 45, 33)
        btnAfMinSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAfMinSub.setIcon(QtGui.QIcon('../Resources/mSubTime.png'))
        btnAfMinSub.setIconSize(QtCore.QSize(160, 90))
        btnAfMinSub.clicked.connect(self.subAfMin)

        btnAfAmPm = QPushButton("", self)
        btnAfAmPm.setGeometry(803, 253, 45, 33)
        btnAfAmPm.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAfAmPm.setIcon(QtGui.QIcon('../Resources/pmbtn.png'))
        btnAfAmPm.setIconSize(QtCore.QSize(160, 90))
        btnAfAmPm.clicked.connect(self.close)

        self.lblAfAmPm = QLabel("am", self)
        self.lblAfAmPm.setGeometry(811, 253, 25, 25)

        display3_lbl = QLabel(self)
        display3_lbl.setPixmap(QPixmap('../Resources/mBkg.png'))
        display3_lbl.setGeometry(651, 253, 45, 33)
        self.lblAfHour = QLabel(str(self.afHour), self)
        self.lblAfHour.setGeometry(657, 260, 30, 21)
        self.lblAfHour.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAfHour.setStyleSheet("background-color : #0000")

        display4_lbl = QLabel(self)
        display4_lbl.setPixmap(QPixmap('../Resources/mBkg.png'))
        display4_lbl.setGeometry(727, 253, 45, 33)
        self.lblAfMin = QLabel(str(self.afMin), self)
        self.lblAfMin.setGeometry(733, 260, 30, 21)
        self.lblAfMin.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAfMin.setStyleSheet("background-color : #0000")

        # Buttons for IOT

        btnItHourAdd = QPushButton("", self)
        btnItHourAdd.setGeometry(954, 211, 45, 33)
        btnItHourAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnItHourAdd.setIcon(QtGui.QIcon('../Resources/mAddTime.png'))
        btnItHourAdd.setIconSize(QtCore.QSize(160, 90))
        btnItHourAdd.clicked.connect(self.addIotHour)

        btnItHourSub = QPushButton("", self)
        btnItHourSub.setGeometry(954, 296, 45, 33)
        btnItHourSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnItHourSub.setIcon(QtGui.QIcon('../Resources/mSubTime.png'))
        btnItHourSub.setIconSize(QtCore.QSize(160, 90))
        btnItHourSub.clicked.connect(self.subIotHour)

        btnItMinAdd = QPushButton("", self)
        btnItMinAdd.setGeometry(1030, 211, 45, 33)
        btnItMinAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnItMinAdd.setIcon(QtGui.QIcon('../Resources/mAddTime.png'))
        btnItMinAdd.setIconSize(QtCore.QSize(160, 90))
        btnItMinAdd.clicked.connect(self.addIotMin)

        btnItMinSub = QPushButton("", self)
        btnItMinSub.setGeometry(1030, 296, 45, 33)
        btnItMinSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnItMinSub.setIcon(QtGui.QIcon('../Resources/mSubTime.png'))
        btnItMinSub.setIconSize(QtCore.QSize(160, 90))
        btnItMinSub.clicked.connect(self.subIotMin)

        btnItAmPm = QPushButton("", self)
        btnItAmPm.setGeometry(1106, 253, 45, 33)
        btnItAmPm.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnItAmPm.setIcon(QtGui.QIcon('../Resources/pmbtn.png'))
        btnItAmPm.setIconSize(QtCore.QSize(160, 90))
        btnItAmPm.clicked.connect(self.close)

        self.lblItAmPm = QLabel("am", self)
        self.lblItAmPm.setGeometry(1114, 253, 25, 25)

        display5_lbl = QLabel(self)
        display5_lbl.setPixmap(QPixmap('../Resources/mBkg.png'))
        display5_lbl.setGeometry(954, 253, 45, 33)
        self.lblItHour = QLabel(str(self.IotHour), self)
        self.lblItHour.setGeometry(960, 260, 30, 21)
        self.lblItHour.setAlignment(QtCore.Qt.AlignCenter)
        self.lblItHour.setStyleSheet("background-color : #0000")

        display6_lbl = QLabel(self)
        display6_lbl.setPixmap(QPixmap('../Resources/mBkg.png'))
        display6_lbl.setGeometry(1030, 253, 45, 33)
        self.lblItMin = QLabel(str(self.IotMin), self)
        self.lblItMin.setGeometry(1036, 260, 30, 21)
        self.lblItMin.setAlignment(QtCore.Qt.AlignCenter)
        self.lblItMin.setStyleSheet("background-color : #0000")

        # Buttons of Morning, Evening, Afternoon

        btnMorning = QPushButton("Morning", self)
        btnMorning.setGeometry(41, 217, 200, 80)
        btnMorning.setStyleSheet(self.btnStyleSelected)
        btnMorning.setGraphicsEffect(Util.getNeuShadow(1))

        self.btnMorning1 = QPushButton("Morning", self)
        self.btnMorning1.setGeometry(41, 217, 200, 80)
        self.btnMorning1.setStyleSheet(self.btnStyleSelected)
        self.btnMorning1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnMorning1.clicked.connect(self.morningClicked)


        btnAfternoon = QPushButton("Afternoon", self)
        btnAfternoon.setGeometry(41, 326, 200, 80)
        btnAfternoon.setStyleSheet(self.btnStyle)
        btnAfternoon.setGraphicsEffect(Util.getNeuShadow(1))

        self.btnAfternoon1 = QPushButton("Afternoon", self)
        self.btnAfternoon1.setGeometry(41, 326, 200, 80)
        self.btnAfternoon1.setStyleSheet(self.btnStyle)
        self.btnAfternoon1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnAfternoon1.clicked.connect(self.afternoonClicked)


        btnEvening = QPushButton("Evening", self)
        btnEvening.setGeometry(41, 435, 200, 80)
        btnEvening.setStyleSheet(self.btnStyle)
        btnEvening.setGraphicsEffect(Util.getNeuShadow(1))
        # btnEvening.clicked.connect(self.close)

        self.btnEvening1 = QPushButton("Evening", self)
        self.btnEvening1.setGeometry(41, 435, 200, 80)
        self.btnEvening1.setStyleSheet(self.btnStyle)
        self.btnEvening1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnEvening1.clicked.connect(self.eveningClicked)


        btnOk = QPushButton("", self)
        btnOk.setGeometry(967, 459, 158, 92)
        btnOk.setStyleSheet("border-radius : 15; background-color: #F0F0F3; color : #00A0B5")
        btnOk.setIcon(QtGui.QIcon('../Resources/mOk.png'))
        btnOk.setIconSize(QtCore.QSize(180, 110))
        btnOk.clicked.connect(self.close)

# INCREMENT AND DECREMENT OF BEFORE FOOD
    def addBfHour(self):
        if self.bfHour < 12:
            self.bfHour = self.bfHour + 1
            self.lblBfHour.setText(str(self.bfHour))

    def subBfHour(self):
        if self.bfHour > 0:
            self.bfHour = self.bfHour - 1
            self.lblBfHour.setText(str(self.bfHour))


    def addBfMin(self):
        if self.bfMin < 60:
            self.bfMin = self.bfMin + 5
            self.lblBfMin.setText(str(self.bfMin))

    def subBfMin(self):
        if self.bfMin > 0:
            self.bfMin = self.bfMin - 5
            self.lblBfMin.setText(str(self.bfMin))

    # INCREMENT AND DECREMENT OF AFTER FOOD

    def addAfHour(self):
        if self.afHour < 12:
            self.afHour = self.afHour + 1
            self.lblAfHour.setText(str(self.afHour))

    def subAfHour(self):
        if self.afHour > 0:
            self.afHour = self.afHour - 1
            self.lblAfHour.setText(str(self.afHour))


    def addAfMin(self):
        if self.afMin < 60:
            self.afMin = self.afMin + 5
            self.lblAfMin.setText(str(self.afMin))

    def subAfMin(self):
        if self.afMin > 0:
            self.afMin = self.afMin - 5
            self.lblAfMin.setText(str(self.afMin))

    # INCREMENT AND DECREMENT OF IOT FOOD

    def addIotHour(self):
        if self.IotHour < 12:
            self.IotHour = self.IotHour + 1
            self.lblItHour.setText(str(self.IotHour))

    def subIotHour(self):
        if self.IotHour > 0:
            self.IotHour = self.IotHour - 1
            self.lblItHour.setText(str(self.IotHour))


    def addIotMin(self):
        if self.bfMin < 60:
            self.bfMin = self.bfMin + 5
            self.lblItMin.setText(str(self.bfMin))

    def subIotMin(self):
        if self.bfMin > 0:
            self.bfMin = self.bfMin - 5
            self.lblItMin.setText(str(self.bfMin))




    def morningClicked(self):
        self.dayTimeSelected(1)

    def afternoonClicked(self):
        self.dayTimeSelected(2)

    def eveningClicked(self):
        self.dayTimeSelected(3)

    def dayTimeSelected(self,type):

        if type == 1:
            self.btnMorning1.setStyleSheet(self.btnStyleSelected)
            self.btnAfternoon1.setStyleSheet(self.btnStyle)
            self.btnEvening1.setStyleSheet(self.btnStyle)
            self.lblt.setText("Morining")
            self.lblAfAmPm.setText("am")
            self.lblItAmPm.setText("am")
            self.lblBfAmPm.setText("am")

        elif type == 2:
            self.btnMorning1.setStyleSheet(self.btnStyle)
            self.btnAfternoon1.setStyleSheet(self.btnStyleSelected)
            self.btnEvening1.setStyleSheet(self.btnStyle)
            self.lblt.setText("Afternoon")
            self.lblAfAmPm.setText("pm")
            self.lblItAmPm.setText("pm")
            self.lblBfAmPm.setText("pm")

        elif type == 3:
            self.btnMorning1.setStyleSheet(self.btnStyle)
            self.btnAfternoon1.setStyleSheet(self.btnStyle)
            self.btnEvening1.setStyleSheet(self.btnStyleSelected)
            self.lblt.setText("Evening")
            self.lblAfAmPm.setText("pm")
            self.lblItAmPm.setText("pm")
            self.lblBfAmPm.setText("pm")

# if __name__ == '__main__':
#     App = QApplication(sys.argv)
#
#     # create the instance of our Window
#     window = ChangeTime()
#
#     window.show()
#
# # start the app
#     sys.exit(App.exec())

