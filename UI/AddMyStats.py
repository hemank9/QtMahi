from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Utility.MahiUtility as Util
from datetime import datetime, timedelta as TimeDelta

class AddMyStats(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Stats")
        # setting geometry
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")

        self.vitalDiff = 1
        self.InitUi()

    def InitUi(self):


        self.datebtnStyle = "border-radius : 7; background-color: #F0F0F3"
        self.startDate = datetime.now().date()


        lblTitle = QPushButton(self)
        lblTitle.setStyleSheet("border-radius: 10;")
        lblTitle.setGeometry(112, 100, 500, 50)
        lblTitle.setGraphicsEffect(Util.getNeuShadow(0))
        lblTitleT = QPushButton(self)
        lblTitleT.setStyleSheet("border-radius: 10; text-align:left; padding-left:20px; font-size:20px; color:#00A0B5")
        lblTitleT.setGeometry(112, 100, 500, 50)
        lblTitleT.setText("Cholestrol")
        lblTitleT.setGraphicsEffect(Util.getNeuShadow(1))


        # Date
        lblDateTitle = QLabel(self)
        lblDateTitle.setStyleSheet("font-size:18px")
        lblDateTitle.setGeometry(112, 220, 303, 50)
        lblDateTitle.setText("Date")
        lblDateTitle.setAlignment(QtCore.Qt.AlignCenter)

        btnDateInc = QPushButton(self)
        btnDateInc.setGeometry(112, 274, 303, 40)
        btnDateInc.setStyleSheet(self.datebtnStyle)
        btnDateInc.setGraphicsEffect(Util.getNeuShadow(0))

        btnDateIncT = QPushButton(self)
        btnDateIncT.setGeometry(112, 274, 303, 40)
        btnDateIncT.setStyleSheet(self.datebtnStyle)
        btnDateIncT.setIcon(QtGui.QIcon('../Resources/incArrow.png'))
        btnDateIncT.setIconSize(QtCore.QSize(60, 40))
        btnDateIncT.setGraphicsEffect(Util.getNeuShadow(1))
        btnDateIncT.clicked.connect(lambda : self.changeDate(False))

        btnDateDec = QPushButton(self)
        btnDateDec.setGeometry(112, 395, 303, 40)
        btnDateDec.setStyleSheet(self.datebtnStyle)
        btnDateDec.setGraphicsEffect(Util.getNeuShadow(0))

        btnDateDecT = QPushButton(self)
        btnDateDecT.setGeometry(112, 395, 303, 40)
        btnDateDecT.setStyleSheet(self.datebtnStyle)
        btnDateDecT.setIcon(QtGui.QIcon('../Resources/decArrow.png'))
        btnDateDecT.setIconSize(QtCore.QSize(60, 40))
        btnDateDecT.setGraphicsEffect(Util.getNeuShadow(1))
        btnDateDecT.clicked.connect(lambda : self.changeDate(True))

        self.lblStartDateBkg = QLabel(self)
        self.lblStartDateBkg.setPixmap(QPixmap('../Resources/Rectangle 506.png'))
        self.lblStartDateBkg.setGeometry(112, 335, 303, 40)

        self.lblStartDate = QLabel(self)
        self.lblStartDate.setGeometry(115, 335, 303, 40)
        self.lblStartDate.setAlignment(Qt.AlignCenter)
        self.lblStartDate.setStyleSheet("color:#00A0B5; background-color:#00F0F0F3; font-size:16px; font:bold")
        self.lblStartDate.setText(self.startDate.strftime('%A, %d %B %Y'))


        # Vital Values
        self.lblVitalTitle = QLabel(self)
        self.lblVitalTitle.setStyleSheet("font-size:18px")
        self.lblVitalTitle.setGeometry(460, 220, 118, 50)
        self.lblVitalTitle.setText("Weight")
        self.lblVitalTitle.setAlignment(QtCore.Qt.AlignCenter)

        btnVitalInc = QPushButton(self)
        btnVitalInc.setGeometry(460, 274, 118, 40)
        btnVitalInc.setStyleSheet(self.datebtnStyle)
        btnVitalInc.setGraphicsEffect(Util.getNeuShadow(0))

        btnVitalIncT = QPushButton(self)
        btnVitalIncT.setGeometry(460, 274, 118, 40)
        btnVitalIncT.setStyleSheet(self.datebtnStyle)
        btnVitalIncT.setIcon(QtGui.QIcon('../Resources/incArrow.png'))
        btnVitalIncT.setIconSize(QtCore.QSize(60, 40))
        btnVitalIncT.setGraphicsEffect(Util.getNeuShadow(1))
        btnVitalIncT.clicked.connect(lambda: self.changeVitalValue(False))

        btnVitalDec = QPushButton(self)
        btnVitalDec.setGeometry(460, 395, 118, 40)
        btnVitalDec.setStyleSheet(self.datebtnStyle)
        btnVitalDec.setGraphicsEffect(Util.getNeuShadow(0))

        btnVitalDecT = QPushButton(self)
        btnVitalDecT.setGeometry(460, 395, 118, 40)
        btnVitalDecT.setStyleSheet(self.datebtnStyle)
        btnVitalDecT.setIcon(QtGui.QIcon('../Resources/decArrow.png'))
        btnVitalDecT.setIconSize(QtCore.QSize(60, 40))
        btnVitalDecT.setGraphicsEffect(Util.getNeuShadow(1))
        btnVitalDecT.clicked.connect(lambda: self.changeVitalValue(True))

        self.lblVitalBkg = QLabel(self)
        self.lblVitalBkg.setPixmap(QPixmap('../Resources/basin_bkg_small.png'))
        self.lblVitalBkg.setGeometry(460, 335, 118, 40)

        self.lblVital = QLabel(self)
        self.lblVital.setGeometry(463, 335, 118, 40)
        self.lblVital.setAlignment(Qt.AlignCenter)
        self.lblVital.setStyleSheet("color:#00A0B5; background-color:#00F0F0F3; font-size:16px; font:bold")
        self.lblVital.setText("5")

        # Sub Vitals
        self.lblSubVitalTitle = QLabel(self)
        self.lblSubVitalTitle.setStyleSheet("font-size:18px")
        self.lblSubVitalTitle.setGeometry(612, 220, 118, 50)
        self.lblSubVitalTitle.setText("Height")
        self.lblSubVitalTitle.setAlignment(QtCore.Qt.AlignCenter)

        btnSubVitalInc = QPushButton(self)
        btnSubVitalInc.setGeometry(612, 274, 118, 40)
        btnSubVitalInc.setStyleSheet(self.datebtnStyle)
        btnSubVitalInc.setGraphicsEffect(Util.getNeuShadow(0))

        btnSubVitalIncT = QPushButton(self)
        btnSubVitalIncT.setGeometry(612, 274, 118, 40)
        btnSubVitalIncT.setStyleSheet(self.datebtnStyle)
        btnSubVitalIncT.setIcon(QtGui.QIcon('../Resources/incArrow.png'))
        btnSubVitalIncT.setIconSize(QtCore.QSize(60, 40))
        btnSubVitalIncT.setGraphicsEffect(Util.getNeuShadow(1))
        btnSubVitalIncT.clicked.connect(lambda: self.changeSubVitalValue(False))

        btnSubVitalDec = QPushButton(self)
        btnSubVitalDec.setGeometry(612, 395, 118, 40)
        btnSubVitalDec.setStyleSheet(self.datebtnStyle)
        btnSubVitalDec.setGraphicsEffect(Util.getNeuShadow(0))

        btnSubVitalDecT = QPushButton(self)
        btnSubVitalDecT.setGeometry(612, 395, 118, 40)
        btnSubVitalDecT.setStyleSheet(self.datebtnStyle)
        btnSubVitalDecT.setIcon(QtGui.QIcon('../Resources/decArrow.png'))
        btnSubVitalDecT.setIconSize(QtCore.QSize(60, 40))
        btnSubVitalDecT.setGraphicsEffect(Util.getNeuShadow(1))
        btnSubVitalDecT.clicked.connect(lambda: self.changeSubVitalValue(True))

        self.lblSubVitalBkg = QLabel(self)
        self.lblSubVitalBkg.setPixmap(QPixmap('../Resources/basin_bkg_small.png'))
        self.lblSubVitalBkg.setGeometry(612, 335, 118, 40)

        self.lblSubVital = QLabel(self)
        self.lblSubVital.setGeometry(615, 335, 118, 40)
        self.lblSubVital.setAlignment(Qt.AlignCenter)
        self.lblSubVital.setStyleSheet("color:#00A0B5; background-color:#00F0F0F3; font-size:16px; font:bold")
        self.lblSubVital.setText("5")

        # Submit Button
        btnSubmitVital = QPushButton(self)
        btnSubmitVital.setGeometry(800, 335, 118, 40)
        btnSubmitVital.setStyleSheet(self.datebtnStyle)
        btnSubmitVital.setGraphicsEffect(Util.getNeuShadow(0))

        btnSubmitVitalT = QPushButton(self)
        btnSubmitVitalT.setGeometry(800, 335, 118, 40)
        btnSubmitVitalT.setStyleSheet("border-radius : 7; background-color: #F0F0F3; font-size:14px")
        btnSubmitVitalT.setGraphicsEffect(Util.getNeuShadow(1))
        btnSubmitVitalT.setText("Okay")
        btnSubmitVitalT.clicked.connect(lambda: self.changeSubVitalValue(True))

    def changeDate(self, decrease):
        currentDate = datetime.now().date()
        if decrease:
            self.startDate = (self.startDate - TimeDelta(1))
        elif self.startDate< currentDate:
            self.startDate = (self.startDate + TimeDelta(1))
        temp = self.startDate.strftime('%A, %d %B %Y')
        self.lblStartDate.setText(temp)

    def changeVitalValue(self, decrease):

        value = float(self.lblVital.text())
        if decrease and (value-self.vitalDiff>0):
            self.lblVital.setText(str(value - self.vitalDiff))
        elif not decrease:
            self.lblVital.setText(str(value + self.vitalDiff))

    def changeSubVitalValue(self, decrease):

        value = float(self.lblSubVital.text())
        if decrease and (value-self.vitalDiff>0):
            self.lblSubVital.setText(str(value - self.vitalDiff))
        elif not decrease:
            self.lblSubVital.setText(str(value + self.vitalDiff))

    def SubmitVitalData(self):
        print("Save Vitals Data")



if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = AddMyStats()

    window.show()

    # start the app
    sys.exit(App.exec_())