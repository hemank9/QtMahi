from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Utility.MahiUtility as Util


class MassEject(QWidget):                           # <===
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../Resources/massEjection.png'))
        self.label.setGeometry(0, 0, 1220, 497)

        self.UiComponents()
    #
        # showing all the widgets
        self.show()

    #
    def UiComponents(self):
        calender = QCalendarWidget(self)

        # setting geometry to the calender
        calender.setGeometry(26, 142, 430, 430)
        calender.setStyleSheet("background : pink;")

        # setting calender horizontal header format
        # calender.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)
        calender.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)

        self.btnStyle = "border-radius : 10; background-color: #F0F0F3; font : bold; color : #00A0B5; font-size:20px"
        self.btnStyleSelected = "border-radius : 10; background-color: #BCE6EC; font : bold; color : #00A0B5; font-size:20px"

        self.btnejctNxtDose = QPushButton("Eject Next Dose", self)
        self.btnejctNxtDose.setGeometry(218, 54, 224, 55)
        self.btnejctNxtDose.setFont(QFont('Arial', 10))
        self.btnejctNxtDose.setStyleSheet(self.btnStyle)
        self.btnejctNxtDose.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnejctNxtDose.clicked.connect(self.ejectNextDoseClicked)

        self.btnDailyEarlyEjct = QPushButton("Daily Early Ejection", self)
        self.btnDailyEarlyEjct.setGeometry(477, 54, 260, 55)
        self.btnDailyEarlyEjct.setFont(QFont('Arial', 10))
        self.btnDailyEarlyEjct.setStyleSheet(self.btnStyle)
        self.btnDailyEarlyEjct.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnDailyEarlyEjct.clicked.connect(self.dailyEarlyClicked)

        self.btnMassEjct = QPushButton("Mass Ejection", self)
        self.btnMassEjct.setGeometry(771, 54, 224, 55)
        self.btnMassEjct.setFont(QFont('Nunito', 10))
        self.btnMassEjct.setStyleSheet(self.btnStyleSelected)
        self.btnMassEjct.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnMassEjct.clicked.connect(self.massEjectClicked)

        btnok = QPushButton("OK", self)
        btnok.setGeometry(981, 561, 83, 43)
        btnok.setFont(QFont('Nunito', 10))
        btnok.setStyleSheet(self.btnStyle)
        btnok.setGraphicsEffect(Util.getNeuShadow(0))
        btnok.clicked.connect(self.close)

        # outputs of the doses shown in the mass ejection page
        lblTotalDose = QLabel('60',self)
        lblTotalDose.setGeometry(779, 150, 50, 50)

        lblMorninBf = QLabel('60', self)
        lblMorninBf.setGeometry(789, 225, 56, 40)
        lblMorninBf.setAlignment(QtCore.Qt.AlignCenter)
        lblMorninBf.setFont(QFont('Arial', 10))

        lblMorninAf = QLabel('60', self)
        lblMorninAf.setGeometry(890, 225, 56, 40)
        lblMorninAf.setAlignment(QtCore.Qt.AlignCenter)
        lblMorninAf.setFont(QFont('Arial', 10))

        lblAftnoonBf = QLabel('60', self)
        lblAftnoonBf.setGeometry(789, 282, 56, 40)
        lblAftnoonBf.setAlignment(QtCore.Qt.AlignCenter)
        lblAftnoonBf.setFont(QFont('Arial', 10))

        lblAftnoonAf = QLabel('60', self)
        lblAftnoonAf.setGeometry(890, 282, 56, 40)
        lblAftnoonAf.setAlignment(QtCore.Qt.AlignCenter)
        lblAftnoonAf.setFont(QFont('Arial', 10))

        lblEvningBf = QLabel('60', self)
        lblEvningBf.setGeometry(789, 339, 56, 40)
        lblEvningBf.setAlignment(QtCore.Qt.AlignCenter)
        lblEvningBf.setFont(QFont('Arial', 10))

        lblEvningAf = QLabel('60', self)
        lblEvningAf.setGeometry(890, 339, 56, 40)
        lblEvningAf.setAlignment(QtCore.Qt.AlignCenter)
        lblEvningAf.setFont(QFont('Arial', 10))

        lblExtrDos1 = QLabel('60', self)
        lblExtrDos1.setGeometry(789, 396, 56, 40)
        lblExtrDos1.setAlignment(QtCore.Qt.AlignCenter)
        lblExtrDos1.setFont(QFont('Arial', 10))

        lblExtrDos2 = QLabel('60', self)
        lblExtrDos2.setGeometry(890, 396, 56, 40)
        lblExtrDos2.setAlignment(QtCore.Qt.AlignCenter)
        lblExtrDos2.setFont(QFont('Arial', 10))

        lblExtrDos3 = QLabel('60', self)
        lblExtrDos3.setGeometry(991, 396, 56, 40)
        lblExtrDos3.setAlignment(QtCore.Qt.AlignCenter)
        lblExtrDos3.setFont(QFont('Arial', 10))

        lblRepetDos1 = QLabel('60', self)
        lblRepetDos1.setGeometry(789, 453, 56, 40)
        lblRepetDos1.setAlignment(QtCore.Qt.AlignCenter)
        lblRepetDos1.setFont(QFont('Arial', 10))

        lblRepetDos2 = QLabel('60', self)
        lblRepetDos2.setGeometry(890, 453, 56, 40)
        lblRepetDos2.setAlignment(QtCore.Qt.AlignCenter)
        lblRepetDos2.setFont(QFont('Arial', 10))

    def massEjectClicked(self):
        self.SetButtonClicked(1)

    def dailyEarlyClicked(self):
        self.SetButtonClicked(2)

    def ejectNextDoseClicked(self):
        self.SetButtonClicked(3)

    def SetButtonClicked(self,type):
        
        if type == 1:
            self.btnMassEjct.setStyleSheet(self.btnStyleSelected)
            self.btnDailyEarlyEjct.setStyleSheet(self.btnStyle)
            self.btnejctNxtDose.setStyleSheet(self.btnStyle)

        elif type == 2:
            self.btnMassEjct.setStyleSheet(self.btnStyle)
            self.btnDailyEarlyEjct.setStyleSheet(self.btnStyleSelected)
            self.btnejctNxtDose.setStyleSheet(self.btnStyle)

        elif type == 3:
            self.btnMassEjct.setStyleSheet(self.btnStyle)
            self.btnDailyEarlyEjct.setStyleSheet(self.btnStyle)
            self.btnejctNxtDose.setStyleSheet(self.btnStyleSelected)

