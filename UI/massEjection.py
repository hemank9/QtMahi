from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


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

        btnejctNxtDose = QPushButton("Eject Next Dose", self)
        btnejctNxtDose.setGeometry(218, 54, 224, 55)
        btnejctNxtDose.setFont(QFont('Arial', 10))
        btnejctNxtDose.setStyleSheet("border-radius : 10; background-color: white; font : bold; color : #00A0B5")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        btnejctNxtDose.setGraphicsEffect(shadow)
        shadow.setColor(Qt.lightGray)
        btnejctNxtDose.clicked.connect(self.close)

        btnDailyEarlyEjct = QPushButton("Daily Early Ejection", self)
        btnDailyEarlyEjct.setGeometry(477, 54, 260, 55)
        btnDailyEarlyEjct.setFont(QFont('Arial', 10))
        btnDailyEarlyEjct.setStyleSheet("border-radius : 10; background-color: white; font : bold; color : #00A0B5")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        btnDailyEarlyEjct.setGraphicsEffect(shadow)
        shadow.setColor(Qt.lightGray)
        btnDailyEarlyEjct.clicked.connect(self.close)

        btnMassEjct = QPushButton("Afternoon", self)
        btnMassEjct.setGeometry(771, 54, 224, 55)
        btnMassEjct.setFont(QFont('Nunito', 10))
        btnMassEjct.setStyleSheet("border-radius : 10; background-color: white; font : bold; color : #00A0B5")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        btnMassEjct.setGraphicsEffect(shadow)
        shadow.setColor(Qt.lightGray)
        btnMassEjct.clicked.connect(self.close)

        btnok = QPushButton("OK", self)
        btnok.setGeometry(981, 561, 83, 43)
        btnok.setFont(QFont('Nunito', 10))
        btnok.setStyleSheet("border-radius : 10; background-color: white; font : bold; color : #00A0B5")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        btnok.setGraphicsEffect(shadow)
        shadow.setColor(Qt.lightGray)
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



