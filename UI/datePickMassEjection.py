from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Utility.MahiUtility as Util
from datetime import datetime, timedelta as TimeDelta
import UI.massEjection as massEject
import MyDatabase.my_database as myDb


# if user chooses current date and his some doses are already ejected then eject the remaining doses for that day
# if user selected current date and no of days as 1 then show current date as start date and tomorrow's date as end date


class MassEjectDateTime(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setStyleSheet("background-color:#FEC32E")
        self.label.setGeometry(0, 0, 1220, 39)

        self.startDate = datetime.now().date()

        # max available days we have in our cylinder
        self.maxDays = int(myDb.getDosagesMaxDays())
        self.noDays = 1
        self.lastDate = datetime.now().date()+TimeDelta(days=(self.maxDays-1))

        print(self.startDate.strftime('%Y-%m-%d')+" | "+self.lastDate.strftime('%Y-%m-%d'))

        # self.startdate = (self.startdate + TimeDelta(days=1)).strftime('%Y-%m-%d')
        # self.enddate = (self.enddate + TimeDelta(days=1)).strftime('%Y-%m-%d')

        self.UiComponents()
    #
        # showing all the widgets
        self.show()

    #
    def UiComponents(self):

        self.btnStyle = "border-radius : 10; background-color: #F0F0F3; font : bold; color : #00A0B5; font-size:20px"
        self.btnStyleSelected = "border-radius : 10; background-color: #BCE6EC; font : bold; color : #00A0B5; font-size:20px"
        self.datebtnStyle = "border-radius : 7; background-color: #F0F0F3"


        btn_back = QPushButton("", self)
        btn_back.setGeometry(30, 53, 173, 41)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('../Resources/backButton.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)


        lblHeader = QLabel("Select Dates",self)
        lblHeader.setGeometry(60,146,146,27)
        lblHeader.setStyleSheet("background-color:#00FF0000;color:#555; font:normal; font-size:20px")


        lblDateHeader = QLabel("Start Date",self)
        lblDateHeader.setGeometry(60,224,303,27)
        lblDateHeader.setAlignment(Qt.AlignCenter)
        lblDateHeader.setStyleSheet("background-color:#00FF0000; font:normal; font-size:18px")

        lblDaysHeader = QLabel("Number of Days",self)
        lblDaysHeader.setGeometry(441,224,130,27)
        lblDaysHeader.setStyleSheet("background-color:#00FF0000; font:normal; font-size:18px")

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

        btnok = QPushButton("OK", self)
        btnok.setGeometry(981, 561, 83, 43)
        btnok.setFont(QFont('Nunito', 10))
        btnok.setStyleSheet(self.btnStyle)
        btnok.setGraphicsEffect(Util.getNeuShadow(0))
        btnok.clicked.connect(self.gotoMassEject)

        self.lblStartDateBkg = QLabel(self)
        self.lblStartDateBkg.setPixmap(QPixmap('../Resources/Rectangle 506.png'))
        self.lblStartDateBkg.setGeometry(60,335,303,40)


        self.lblStartDate = QLabel(self)
        self.lblStartDate.setGeometry(63,335,303,40)
        self.lblStartDate.setAlignment(Qt.AlignCenter)
        self.lblStartDate.setStyleSheet("color:#00A0B5; background-color:#00F0F0F3; font-size:16px; font:bold")
        self.lblStartDate.setText(self.startDate.strftime('%A %d %B %Y'))


        self.lblNoDaysBkg = QLabel(self)
        self.lblNoDaysBkg.setPixmap(QPixmap('../Resources/Rectangle 508.png'))
        self.lblNoDaysBkg.setGeometry(466,335,68,40)


        self.lblNoDays = QLabel(self)
        self.lblNoDays.setGeometry(466,335,68,40)
        self.lblNoDays.setAlignment(Qt.AlignCenter)
        self.lblNoDays.setStyleSheet("color:#00A0B5; background-color:#00F0F0F3; font-size:16px; font:bold")
        self.lblNoDays.setText(str(self.noDays))

        self.lblSummary = QLabel(self)
        self.lblSummary.setGeometry(666,300,250,120)
        self.lblSummary.setAlignment(Qt.AlignCenter)
        self.lblSummary.setWordWrap(True)
        self.lblSummary.setStyleSheet("background-color:#00FF0000; font:normal; font-size:15px")

        self.SetSummary()


        # BUTTONS FOR MONTH INC AND DEC
        btnMonthInc = QPushButton(self)
        btnMonthInc.setGeometry(60, 274, 303, 40)
        btnMonthInc.setStyleSheet(self.datebtnStyle)
        btnMonthInc.setGraphicsEffect(Util.getNeuShadow(0))

        btnMonthInc1 = QPushButton(self)
        btnMonthInc1.setGeometry(60, 274, 303, 40)
        btnMonthInc1.setStyleSheet(self.datebtnStyle)
        btnMonthInc1.setIcon(QtGui.QIcon('../Resources/incArrow.png'))
        btnMonthInc1.setIconSize(QtCore.QSize(60, 40))
        btnMonthInc1.setGraphicsEffect(Util.getNeuShadow(1))
        btnMonthInc1.clicked.connect(self.addDate)

        btnMonthDec = QPushButton(self)
        btnMonthDec.setGeometry(60, 395, 303, 40)
        btnMonthDec.setStyleSheet(self.datebtnStyle)
        btnMonthDec.setGraphicsEffect(Util.getNeuShadow(0))

        btnMonthDec1 = QPushButton(self)
        btnMonthDec1.setGeometry(60, 395, 303, 40)
        btnMonthDec1.setStyleSheet(self.datebtnStyle)
        btnMonthDec1.setIcon(QtGui.QIcon('../Resources/decArrow.png'))
        btnMonthDec1.setIconSize(QtCore.QSize(60, 40))
        btnMonthDec1.setGraphicsEffect(Util.getNeuShadow(1))
        btnMonthDec1.clicked.connect(self.subDate)

        # Number of days
        btnNoDaysInc = QPushButton(self)
        btnNoDaysInc.setGeometry(466, 274, 68, 40)
        btnNoDaysInc.setStyleSheet(self.datebtnStyle)
        btnNoDaysInc.setGraphicsEffect(Util.getNeuShadow(0))

        btnNoDaysInc1 = QPushButton(self)
        btnNoDaysInc1.setGeometry(466, 274, 68, 40)
        btnNoDaysInc1.setStyleSheet(self.datebtnStyle)
        btnNoDaysInc1.setIcon(QtGui.QIcon('../Resources/incArrow.png'))
        btnNoDaysInc1.setIconSize(QtCore.QSize(60, 40))
        btnNoDaysInc1.setGraphicsEffect(Util.getNeuShadow(1))
        btnNoDaysInc1.clicked.connect(self.addDays)

        btnNoDaysDec = QPushButton(self)
        btnNoDaysDec.setGeometry(466, 395, 68, 40)
        btnNoDaysDec.setStyleSheet(self.datebtnStyle)
        btnNoDaysDec.setGraphicsEffect(Util.getNeuShadow(0))

        btnNoDaysDec1 = QPushButton(self)
        btnNoDaysDec1.setGeometry(466, 395, 68, 40)
        btnNoDaysDec1.setStyleSheet(self.datebtnStyle)
        btnNoDaysDec1.setIcon(QtGui.QIcon('../Resources/decArrow.png'))
        btnNoDaysDec1.setIconSize(QtCore.QSize(60, 40))
        btnNoDaysDec1.setGraphicsEffect(Util.getNeuShadow(1))
        btnNoDaysDec1.clicked.connect(self.subDays)

        #POP UP FRAMES FOR EJECT NEXT DOSE

        # self.popFrame1 = QLabel(self)
        # self.popFrame1.setGeometry(165, 265, 874, 154)
        # self.popFrame1.setStyleSheet("background-color: white; border-radius: 26; color: #00A0B5; font-size: 42px")
        # self.popFrame1.setText("  Your next dose is Afternoon dose")
        # self.popFrame1.setGraphicsEffect(Util.getNeuShadow(0))
        #
        # self.okBtn1 = QPushButton("OK", self)
        # self.okBtn1.setGeometry(844, 311, 90, 60)
        # self.okBtn1.setStyleSheet("color:#00A0B5; border-radius: 7; background-color: #F0F0F3")
        # self.okBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        # self.okBtn = QPushButton("OK", self)
        # self.okBtn.setGeometry(844, 311, 90, 60)
        # self.okBtn.setStyleSheet("color:#00A0B5; border-radius: 7; background-color: #F0F0F3; font-size: 30px")
        # self.okBtn.setGraphicsEffect(Util.getNeuShadow(0))
        #
        # self.cancelBtn1 = QPushButton( self)
        # self.cancelBtn1.setGeometry(949, 311, 50, 60)
        # self.cancelBtn1.setStyleSheet("background-color: #F0F0F3; font: bold; border-radius: 7")
        # self.cancelBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        # self.cancelBtn = QPushButton("X", self)
        # self.cancelBtn.setGeometry(949, 311, 50, 60)
        # self.cancelBtn.setStyleSheet("background-color: #F0F0F3; font: bold; border-radius: 7; color: red;font-size: 30px")
        # self.cancelBtn.setGraphicsEffect(Util.getNeuShadow(1))

        # self.confirmEject = QLabel(self)
        # self.confirmEject.setText("   Eject next Dosage")
        # self.confirmEject.setGeometry(165, 265, 874, 154)
        # self.confirmEject.setStyleSheet("color: #00A0B5; background-color: #FFFFFF; border-radius: 26; font-size: 42px")
        # self.confirmEject.setGraphicsEffect(Util.getNeuShadow(0))
        #
        # self.confirmBtn1 = QPushButton("Confirm", self)
        # self.confirmBtn1.setGeometry(780, 311, 151, 60)
        # self.confirmBtn1.setStyleSheet("color:#00A0B5; border-radius: 7; background-color: #F0F0F3; font-size: 30px")
        # self.confirmBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        # self.confirmBtn = QPushButton("Confirm", self)
        # self.confirmBtn.setGeometry(780, 311, 151, 60)
        # self.confirmBtn.setStyleSheet("color:#00A0B5; border-radius: 7; background-color: #F0F0F3; font-size: 30px")
        # self.confirmBtn.setGraphicsEffect(Util.getNeuShadow(1))

        # self.notifFrame = QLabel(self)
        # self.notifFrame.setText("Notification for the early ejected medicine will be given on your phone")
        # self.notifFrame.setWordWrap(True)
        # self.notifFrame.setGeometry(165, 265, 874, 154)
        # self.notifFrame.setStyleSheet("color: #00A0B5; background-color: #FFFFFF; border-radius: 26; font-size: 35px")
        #
        # self.confirmBtn2 = QPushButton("Confirm", self)
        # self.confirmBtn2.setGeometry(850, 311, 151, 60)
        # self.confirmBtn2.setStyleSheet("color:#00A0B5; border-radius: 7; background-color: #F0F0F3; font-size: 30px")
        # self.confirmBtn2.setGraphicsEffect(Util.getNeuShadow(0))
        # self.confirmBtn21 = QPushButton("Confirm", self)
        # self.confirmBtn21.setGeometry(850, 311, 151, 60)
        # self.confirmBtn21.setStyleSheet("color:#00A0B5; border-radius: 7; background-color: #F0F0F3; font-size: 30px")
        # self.confirmBtn21.setGraphicsEffect(Util.getNeuShadow(1))

    def SetSummary(self):
        if self.noDays == 1:
            summary = '<font color="#333">Your medicines will be ejected for the day </font><font color="#D00">'\
                      +self.startDate.strftime('%A %d %B %Y')+'</font>'
        else:
            endDate = (self.startDate + TimeDelta(days=(self.noDays-1))).strftime('%A %d %B %Y')
            summary = '<font color="#333">Your medicines will be ejected from </font><font color="#D00" >'\
                  +self.startDate.strftime('%A %d %B %Y')+'</font><font color="#333"> to </font> <font color="#D00">'+endDate+'</font>'

        self.lblSummary.setText(summary)

    def massEjectClicked(self):
        self.SetButtonClicked(1)

    def ejectNextDoseClicked(self):
        self.SetButtonClicked(3)

    def SetButtonClicked(self, type):

        if type == 1:
            self.btnMassEjct.setStyleSheet(self.btnStyleSelected)
            self.btnejctNxtDose.setStyleSheet(self.btnStyle)

        elif type == 3:
            self.btnMassEjct.setStyleSheet(self.btnStyle)
            self.btnejctNxtDose.setStyleSheet(self.btnStyleSelected)

    def addDays(self):
        if self.noDays < self.maxDays:
            self.noDays = self.noDays+1
            self.lblNoDays.setText(str(self.noDays))

        self.SetSummary()

    def subDays(self):
        if self.noDays > 1:
            self.noDays = self.noDays-1
            self.lblNoDays.setText(str(self.noDays))

        self.SetSummary()

    def subDate(self):
        currentDate = datetime.now().date()
        if currentDate < self.startDate:
            self.changeDate(-1)

    def addDate(self):

        if self.startDate < self.lastDate:
            self.changeDate(1)

    def changeDate(self,noDays):
        self.startDate = (self.startDate + TimeDelta(days=noDays))
        self.maxDays = self.maxDays - noDays
        print(str(self.maxDays))
        temp = self.startDate.strftime('%A %d %B %Y')
        self.lblStartDate.setText(temp)
        print("startdate : "+temp)

        if self.noDays > self.maxDays:
            self.noDays = self.maxDays
            self.lblNoDays.setText(str(self.noDays))

        self.SetSummary()

    def gotoMassEject(self):

        if self.noDays>1:
            endDate = self.startDate + TimeDelta(days=(self.noDays-1))
        else:
            endDate = self.startDate

        self.n = massEject.MassEject(self.startDate.strftime('%Y-%m-%d'),self.noDays,endDate.strftime('%Y-%m-%d'))
        self.n.show()

if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = MassEjectDateTime()

    window.show()

    # start the app
    sys.exit(App.exec())
