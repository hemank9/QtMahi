from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QPushButton

import Utility.MahiUtility as Util
import sys


class RepeatDosage(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../Resources/Group 71.png'))
        self.label.setGeometry(0, 0, 1220, 249)

        self.UiComponents()
    #
    #     # showing all the widgets
        self.show()
    #
    def UiComponents(self):

        self.Hour = 10
        self.Min = 10
        self.FreqHour = 2
        self.FreqTimes = 5

        btnRefill = QPushButton("Refill Now",self)
        btnRefill.setGeometry(889, 56, 301, 59)
        btnRefill.setStyleSheet("background-color : #EE498D; border-radius : 6; font:bold; fond-size: 24")
        btnRefill.clicked.connect(self.close)

        btn_back = QPushButton("", self)
        btn_back.setGeometry(40, 53, 173, 41)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('../Resources/Group 49.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)

        btn_ok = QPushButton("OK", self)
        btn_ok.setGeometry(747, 220, 83, 43)
        btn_ok.setStyleSheet("border-radius : 10; background-color: #F0F0F3; color : #00A0B5; font-size:25; font: bold")
        btn_ok.setGraphicsEffect(Util.getNeuShadow(1))

        btn_ok1 = QPushButton("OK", self)
        btn_ok1.setGeometry(747, 220, 83, 43)
        btn_ok1.setStyleSheet("border-radius : 10; background-color: #F0F0F3; color : #00A0B5; font-size:25; font: bold")
        btn_ok1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_ok1.clicked.connect(self.close)



        lblITabInfo = QLabel("Take Dolo 650 3 times a day!",self)
        lblITabInfo.setGeometry(43, 159, 657, 30)


        btnfreqHourlyDec = QPushButton("", self)
        btnfreqHourlyDec.setGeometry(142, 263, 33, 45)
        btnfreqHourlyDec.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnfreqHourlyDec.setIcon(QtGui.QIcon('../Resources/cntDecrease.png'))
        btnfreqHourlyDec.setIconSize(QtCore.QSize(160, 90))
        btnfreqHourlyDec.clicked.connect(self.subFreqHour)

        btnfreqHourlyInc = QPushButton("", self)
        btnfreqHourlyInc.setGeometry(242, 263, 33, 45)
        btnfreqHourlyInc.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnfreqHourlyInc.setIcon(QtGui.QIcon('../Resources/cntIecrease.png'))
        btnfreqHourlyInc.setIconSize(QtCore.QSize(160, 90))
        btnfreqHourlyInc.clicked.connect(self.addFreqHour)

        btnhourly = QPushButton("", self)
        btnhourly.setGeometry(280, 263, 100, 45)
        btnhourly.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnhourly.setIcon(QtGui.QIcon('../Resources/hourly.png'))
        btnhourly.setIconSize(QtCore.QSize(110, 90))
        btnhourly.clicked.connect(self.close)

        btnfreqTimesDec = QPushButton("", self)
        btnfreqTimesDec.setGeometry(142, 315, 33, 45)
        btnfreqTimesDec.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnfreqTimesDec.setIcon(QtGui.QIcon('../Resources/cntDecrease.png'))
        btnfreqTimesDec.setIconSize(QtCore.QSize(160, 90))
        btnfreqTimesDec.clicked.connect(self.subFreqTimes)

        btnfreqTimesInc = QPushButton("", self)
        btnfreqTimesInc.setGeometry(242, 315, 33, 45)
        btnfreqTimesInc.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnfreqTimesInc.setIcon(QtGui.QIcon('../Resources/cntIecrease.png'))
        btnfreqTimesInc.setIconSize(QtCore.QSize(160, 90))
        btnfreqTimesInc.clicked.connect(self.addFreqTimes)

        displayIpHourly = QLabel(self)
        displayIpHourly.setPixmap(QPixmap('../Resources/ipHourly.png'))
        displayIpHourly.setGeometry(191, 264, 45, 45)
        self.lblFreqHourly = QLabel(str(self.FreqHour), self)
        self.lblFreqHourly.setGeometry(197, 275, 30, 21)
        self.lblFreqHourly.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFreqHourly.setStyleSheet("background-color : #0000")

        displayIpTimes = QLabel(self)
        displayIpTimes.setPixmap(QPixmap('../Resources/ipTimes.png'))
        displayIpTimes.setGeometry(191, 316, 45, 45)
        self.lblFreqTimes = QLabel(str(self.FreqTimes), self)
        self.lblFreqTimes.setGeometry(197, 328, 30, 21)
        self.lblFreqTimes.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFreqTimes.setStyleSheet("background-color : #0000")

        btnTimes = QPushButton("", self)
        btnTimes.setGeometry(280, 315, 100, 45)
        btnTimes.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnTimes.setIcon(QtGui.QIcon('../Resources/times.png'))
        btnTimes.setIconSize(QtCore.QSize(110, 90))
        btnTimes.clicked.connect(self.close)

        # Timing Buttons

        btnHourAdd = QPushButton("", self)
        btnHourAdd.setGeometry(477, 263, 45, 33)
        btnHourAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnHourAdd.setIcon(QtGui.QIcon('../Resources/mAddTime.png'))
        btnHourAdd.setIconSize(QtCore.QSize(160, 90))
        btnHourAdd.clicked.connect(self.addHour)

        btnHourSub = QPushButton("", self)
        btnHourSub.setGeometry(477, 348, 45, 33)
        btnHourSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnHourSub.setIcon(QtGui.QIcon('../Resources/mSubTime.png'))
        btnHourSub.setIconSize(QtCore.QSize(160, 90))
        btnHourSub.clicked.connect(self.subHour)

        btnMinAdd = QPushButton("", self)
        btnMinAdd.setGeometry(553, 263, 45, 33)
        btnMinAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnMinAdd.setIcon(QtGui.QIcon('../Resources/mAddTime.png'))
        btnMinAdd.setIconSize(QtCore.QSize(160, 90))
        btnMinAdd.clicked.connect(self.addMin)

        btnMinSub = QPushButton("", self)
        btnMinSub.setGeometry(553, 348, 45, 33)
        btnMinSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnMinSub.setIcon(QtGui.QIcon('../Resources/mSubTime.png'))
        btnMinSub.setIconSize(QtCore.QSize(160, 90))
        btnMinSub.clicked.connect(self.subMin)

        btnAmPm = QPushButton("", self)
        btnAmPm.setGeometry(629, 305, 45, 33)
        btnAmPm.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAmPm.setIcon(QtGui.QIcon('../Resources/pmbtn.png'))
        btnAmPm.setIconSize(QtCore.QSize(160, 90))
        btnAmPm.clicked.connect(self.close)

        lblAmPm = QLabel("am", self)
        lblAmPm.setGeometry(637, 305, 25, 25)

        display3_lbl = QLabel(self)
        display3_lbl.setPixmap(QPixmap('../Resources/mBkg.png'))
        display3_lbl.setGeometry(477, 305, 45, 33)
        self.lblHour = QLabel(str(self.Hour), self)
        self.lblHour.setGeometry(483, 310, 30, 21)
        self.lblHour.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour.setStyleSheet("background-color : #0000")

        display4_lbl = QLabel(self)
        display4_lbl.setPixmap(QPixmap('../Resources/mBkg.png'))
        display4_lbl.setGeometry(553, 305, 45, 33)
        self.lblMin = QLabel(str(self.Min), self)
        self.lblMin.setGeometry(560, 310, 30, 21)
        self.lblMin.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMin.setStyleSheet("background-color : #0000")


    def addFreqHour(self):
        if self.FreqHour < 12:
            self.FreqHour = self.FreqHour + 1
            self.lblFreqHourly.setText(str(self.FreqHour))

    def subFreqHour(self):
        if self.FreqHour > 0:
            self.FreqHour = self.FreqHour - 1
            self.lblFreqHourly.setText(str(self.FreqHour))

    def addFreqTimes(self):
        if self.FreqTimes < 60:
            self.FreqTimes = self.FreqTimes + 1
            self.lblFreqTimes.setText(str(self.FreqTimes))

    def subFreqTimes(self):
        if self.FreqTimes > 0:
            self.FreqTimes = self.FreqTimes - 1
            self.lblFreqTimes.setText(str(self.FreqTimes))


    def addHour(self):
        if self.Hour < 12:
            self.Hour = self.Hour + 1
            self.lblHour.setText(str(self.Hour))

    def subHour(self):
        if self.Hour > 0:
            self.Hour = self.Hour - 1
            self.lblHour.setText(str(self.Hour))

    def addMin(self):
        if self.Min < 60:
            self.Min = self.Min + 5
            self.lblMin.setText(str(self.Min))

    def subMin(self):
        if self.Min > 0:
            self.Min = self.bfMin - 5
            self.lblMin.setText(str(self.Min))


# if __name__ == '__main__':
#     App = QApplication(sys.argv)
#
#     # create the instance of our Window
#     window = RepeatDosage()
#
#     window.show()
#
# # start the app
#     sys.exit(App.exec())