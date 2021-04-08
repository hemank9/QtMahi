from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Utility.MahiUtility as Util


class DatePicker(QWidget):                           # <===
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../Resources/Group 97.png'))
        self.label.setGeometry(0, 0, 1220, 362)

        self.UiComponents()
    #
        # showing all the widgets
        self.show()

    #
    def UiComponents(self):

        self.btnStyle = "border-radius : 10; background-color: #F0F0F3; font : bold; color : #00A0B5; font-size:20px"
        self.btnStyleSelected = "border-radius : 10; background-color: #BCE6EC; font : bold; color : #00A0B5; font-size:20px"
        self.datebtnStyle = "border-radius : 7; background-color: #F0F0F3"
        self.date = 10
        self.month = "April"
        self.year = 2021

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

        btnDateInc = QPushButton(self)
        btnDateInc.setGeometry(60, 274, 60, 40)
        btnDateInc.setStyleSheet(self.datebtnStyle)
        btnDateInc.setGraphicsEffect(Util.getNeuShadow(0))

        btnDateInc1 = QPushButton(self)
        btnDateInc1.setGeometry(60, 274, 60, 40)
        btnDateInc1.setStyleSheet(self.datebtnStyle)
        btnDateInc1.setIcon(QtGui.QIcon('../Resources/incArrow.png'))
        btnDateInc1.setIconSize(QtCore.QSize(60,40))
        btnDateInc1.setGraphicsEffect(Util.getNeuShadow(1))

        self.lblDateInc = QLabel(str(self.date), self)
        self.lblDateInc.setGeometry(60, 322, 60, 40)
        self.lblDateInc.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDateInc.setStyleSheet("background-color : #0000")

        btnDateDec = QPushButton(self)
        btnDateDec.setGeometry(60, 370, 60, 40)
        btnDateDec.setStyleSheet(self.datebtnStyle)
        btnDateDec.setGraphicsEffect(Util.getNeuShadow(0))

        btnDateDec1 = QPushButton(self)
        btnDateDec1.setGeometry(60, 370, 60, 40)
        btnDateDec1.setStyleSheet(self.datebtnStyle)
        btnDateDec1.setIcon(QtGui.QIcon('../Resources/decArrow.png'))
        btnDateDec1.setIconSize(QtCore.QSize(60, 40))
        btnDateDec1.setGraphicsEffect(Util.getNeuShadow(1))

        # BUTTONS FOR MONTH INC AND DEC
        btnMonthInc = QPushButton(self)
        btnMonthInc.setGeometry(143, 274, 120, 40)
        btnMonthInc.setStyleSheet(self.datebtnStyle)
        btnMonthInc.setGraphicsEffect(Util.getNeuShadow(0))

        btnMonthInc1 = QPushButton(self)
        btnMonthInc1.setGeometry(143, 274, 120, 40)
        btnMonthInc1.setStyleSheet(self.datebtnStyle)
        btnMonthInc1.setIcon(QtGui.QIcon('../Resources/incArrow.png'))
        btnMonthInc1.setIconSize(QtCore.QSize(60, 40))
        btnMonthInc1.setGraphicsEffect(Util.getNeuShadow(1))

        btnMonthDec = QPushButton(self)
        btnMonthDec.setGeometry(143, 370, 120, 40)
        btnMonthDec.setStyleSheet(self.datebtnStyle)
        btnMonthDec.setGraphicsEffect(Util.getNeuShadow(0))

        btnMonthDec1 = QPushButton(self)
        btnMonthDec1.setGeometry(143, 370, 120, 40)
        btnMonthDec1.setStyleSheet(self.datebtnStyle)
        btnMonthDec1.setIcon(QtGui.QIcon('../Resources/decArrow.png'))
        btnMonthDec1.setIconSize(QtCore.QSize(60, 40))
        btnMonthDec1.setGraphicsEffect(Util.getNeuShadow(1))

        # BUTTONS FOR YEAR INC AND DEC
        btnYearInc = QPushButton(self)
        btnYearInc.setGeometry(286, 274, 60, 40)
        btnYearInc.setStyleSheet(self.datebtnStyle)
        btnYearInc.setGraphicsEffect(Util.getNeuShadow(0))

        btnYearInc1 = QPushButton(self)
        btnYearInc1.setGeometry(286, 274, 60, 40)
        btnYearInc1.setStyleSheet(self.datebtnStyle)
        btnYearInc1.setIcon(QtGui.QIcon('../Resources/incArrow.png'))
        btnYearInc1.setIconSize(QtCore.QSize(60, 40))
        btnYearInc1.setGraphicsEffect(Util.getNeuShadow(1))

        btnYearDec = QPushButton(self)
        btnYearDec.setGeometry(286, 370, 60, 40)
        btnYearDec.setStyleSheet(self.datebtnStyle)
        btnYearDec.setGraphicsEffect(Util.getNeuShadow(0))

        btnYearDec1 = QPushButton(self)
        btnYearDec1.setGeometry(286, 370, 60, 40)
        btnYearDec1.setStyleSheet(self.datebtnStyle)
        btnYearDec1.setIcon(QtGui.QIcon('../Resources/decArrow.png'))
        btnYearDec1.setIconSize(QtCore.QSize(60, 40))
        btnYearDec1.setGraphicsEffect(Util.getNeuShadow(1))


        # BUTTONS FOR DAY INC AND DEC
        btnEndDateInc = QPushButton(self)
        btnEndDateInc.setGeometry(500, 274, 60, 40)
        btnEndDateInc.setStyleSheet(self.datebtnStyle)
        btnEndDateInc.setGraphicsEffect(Util.getNeuShadow(0))

        btnEndDateInc1 = QPushButton(self)
        btnEndDateInc1.setGeometry(500, 274, 60, 40)
        btnEndDateInc1.setStyleSheet(self.datebtnStyle)
        btnEndDateInc1.setIcon(QtGui.QIcon('../Resources/incArrow.png'))
        btnEndDateInc1.setIconSize(QtCore.QSize(60, 40))
        btnEndDateInc1.setGraphicsEffect(Util.getNeuShadow(1))

        btnEndDateDec = QPushButton(self)
        btnEndDateDec.setGeometry(500, 370, 60, 40)
        btnEndDateDec.setStyleSheet(self.datebtnStyle)
        btnEndDateDec.setGraphicsEffect(Util.getNeuShadow(0))

        btnEndDateDec1 = QPushButton(self)
        btnEndDateDec1.setGeometry(500, 370, 60, 40)
        btnEndDateDec1.setStyleSheet(self.datebtnStyle)
        btnEndDateDec1.setIcon(QtGui.QIcon('../Resources/decArrow.png'))
        btnEndDateDec1.setIconSize(QtCore.QSize(60, 40))
        btnEndDateDec1.setGraphicsEffect(Util.getNeuShadow(1))

        # BUTTONS FOR MONTH INC AND DEC
        btnEndMonthInc = QPushButton(self)
        btnEndMonthInc.setGeometry(583, 274, 120, 40)
        btnEndMonthInc.setStyleSheet(self.datebtnStyle)
        btnEndMonthInc.setGraphicsEffect(Util.getNeuShadow(0))

        btnEndMonthInc1 = QPushButton(self)
        btnEndMonthInc1.setGeometry(583, 274, 120, 40)
        btnEndMonthInc1.setStyleSheet(self.datebtnStyle)
        btnEndMonthInc1.setIcon(QtGui.QIcon('../Resources/incArrow.png'))
        btnEndMonthInc1.setIconSize(QtCore.QSize(60, 40))
        btnEndMonthInc1.setGraphicsEffect(Util.getNeuShadow(1))

        btnEndMonthDec = QPushButton(self)
        btnEndMonthDec.setGeometry(583, 370, 120, 40)
        btnEndMonthDec.setStyleSheet(self.datebtnStyle)
        btnEndMonthDec.setGraphicsEffect(Util.getNeuShadow(0))

        btnEndMonthDec1 = QPushButton(self)
        btnEndMonthDec1.setGeometry(583, 370, 120, 40)
        btnEndMonthDec1.setStyleSheet(self.datebtnStyle)
        btnEndMonthDec1.setIcon(QtGui.QIcon('../Resources/decArrow.png'))
        btnEndMonthDec1.setIconSize(QtCore.QSize(60, 40))
        btnEndMonthDec1.setGraphicsEffect(Util.getNeuShadow(1))

        # BUTTONS FOR YEAR INC AND DEC
        btnEndYearInc = QPushButton(self)
        btnEndYearInc.setGeometry(726, 274, 60, 40)
        btnEndYearInc.setStyleSheet(self.datebtnStyle)
        btnEndYearInc.setGraphicsEffect(Util.getNeuShadow(0))

        btnEndYearInc1 = QPushButton(self)
        btnEndYearInc1.setGeometry(726, 274, 60, 40)
        btnEndYearInc1.setStyleSheet(self.datebtnStyle)
        btnEndYearInc1.setIcon(QtGui.QIcon('../Resources/incArrow.png'))
        btnEndYearInc1.setIconSize(QtCore.QSize(60, 40))
        btnEndYearInc1.setGraphicsEffect(Util.getNeuShadow(1))

        btnEndYearDec = QPushButton(self)
        btnEndYearDec.setGeometry(726, 370, 60, 40)
        btnEndYearDec.setStyleSheet(self.datebtnStyle)
        btnEndYearDec.setGraphicsEffect(Util.getNeuShadow(0))

        btnEndYearDec1 = QPushButton(self)
        btnEndYearDec1.setGeometry(726, 370, 60, 40)
        btnEndYearDec1.setStyleSheet(self.datebtnStyle)
        btnEndYearDec1.setIcon(QtGui.QIcon('../Resources/decArrow.png'))
        btnEndYearDec1.setIconSize(QtCore.QSize(60, 40))
        btnEndYearDec1.setGraphicsEffect(Util.getNeuShadow(1))

    def massEjectClicked(self):
        self.SetButtonClicked(1)

    def dailyEarlyClicked(self):
        self.SetButtonClicked(2)

    def ejectNextDoseClicked(self):
        self.SetButtonClicked(3)

    def SetButtonClicked(self, type):

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


if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = DatePicker()

    window.show()

# start the app
    sys.exit(App.exec())
