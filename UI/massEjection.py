from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Utility.MahiUtility as Util
from datetime import date
from datetime import datetime, timedelta as TimeDelta

#create a database function to return total dosages using start and end date

class MassEject(QWidget):                           # <===
    def __init__(self, startDate, noDays, endDate):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../Resources/massEjection.png'))
        self.label.setGeometry(0, 0, 1220, 497)

        self.totalDoses = 10

        self.pStartDate = str(startDate)
        tempX = self.pStartDate.split("-")
        tempY = str(endDate).split("-")

        self.startDate = QDate(int(tempX[0]),int(tempX[1]),int(tempX[2]))
        self.endDate = QDate(int(tempY[0]),int(tempY[1]),int(tempY[2]))
        self.noDays = int(noDays)
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

        cell_format = QtGui.QTextCharFormat()
        cell_format.setBackground(QtGui.QColor("blue"))
        cell_format.setForeground(QtGui.QColor("white"))

        # calender.setDisabled(True)

        tempX = self.pStartDate.split("-")
        tempStartDate = date(int(tempX[0]),int(tempX[1]),int(tempX[2]))
        for i in range(self.noDays):
            if i > 0:
                tempStartDate = tempStartDate + TimeDelta(days=1)
            else:
                tempStartDate = tempStartDate + TimeDelta(days=0)
            tempX = tempStartDate.strftime('%Y-%m-%d').split("-")
            y = QDate(int(tempX[0]),int(tempX[1]),int(tempX[2]))
            calender.setDateTextFormat(y, cell_format)

        # y = QDate(2021, 4, 12)
        # calender.setDateTextFormat(y, cell_format)


        calender.setDateRange(self.startDate,self.endDate)

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

        self.btnMassEjct = QPushButton("Mass Ejection", self)
        self.btnMassEjct.setGeometry(477, 54, 224, 55)
        self.btnMassEjct.setFont(QFont('Nunito', 10))
        self.btnMassEjct.setStyleSheet(self.btnStyleSelected)
        self.btnMassEjct.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnMassEjct.clicked.connect(self.massEjectClicked)

        btn_back = QPushButton("", self)
        btn_back.setGeometry(40, 53, 173, 41)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('../Resources/backButton.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)

        btnok = QPushButton("OK", self)
        btnok.setGeometry(981, 561, 83, 43)
        btnok.setFont(QFont('Nunito', 10))
        btnok.setStyleSheet(self.btnStyle)
        btnok.setGraphicsEffect(Util.getNeuShadow(0))
        btnok.clicked.connect(self.close)

        # outputs of the doses shown in the mass ejection page
        lblTotalDose = QLabel(self)
        lblTotalDose.setGeometry(779, 160, 50, 50)
        lblTotalDose.setStyleSheet("background-color:#00FF0000")
        lblTotalDose.setAlignment(Qt.AlignCenter)
        lblTotalDose.setFont(QFont('Arial', 10))
        lblTotalDose.setText(str(self.totalDoses))

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

    def ejectNextDoseClicked(self):
        self.SetButtonClicked(3)

    def SetButtonClicked(self,type):
        
        if type == 1:
            self.btnMassEjct.setStyleSheet(self.btnStyleSelected)
            self.btnejctNxtDose.setStyleSheet(self.btnStyle)

        elif type == 3:
            self.btnMassEjct.setStyleSheet(self.btnStyle)
            self.btnejctNxtDose.setStyleSheet(self.btnStyleSelected)

