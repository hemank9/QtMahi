from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from datetime import date
import Utility.MahiUtility as Util
from datetime import datetime, timedelta as TimeDelta


class ExtraDosage(QWidget):                           # <===
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setStyleSheet("background-color:#FEC32E")
        self.label.setGeometry(0, 0, 1220, 39)

        self.startDate = datetime.now().date()
        self.maxDays = 10
        self.noDays = 1
        self.lastDate = datetime.now().date() + TimeDelta(days=(self.maxDays - 1))

        print(self.startDate.strftime('%Y-%m-%d') + " | " + self.lastDate.strftime('%Y-%m-%d'))

        self.UiComponents()
    #
    #     # showing all the widgets
        self.show()
    #
    def UiComponents(self):

        self.datebtnStyle = "border-radius : 7; background-color: #F0F0F3"
        self.FreqHour = 2
        self.FreqTimes = 5
        self.Hour = 10
        self.Min = 10

        btn_back = QPushButton("", self)
        btn_back.setGeometry(40, 53, 173, 41)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('../Resources/backButton.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)

        lblFreq = QLabel(self)
        lblFreq.setGeometry(17, 123, 312, 27)
        lblFreq.setStyleSheet("text: bold")
        lblFreq.setText("Existing Frequency of the Medicine")

        lblMedicine = QLabel(self)
        lblMedicine.setGeometry(18, 158, 184, 29)
        lblMedicine.setStyleSheet("text: bold")
        lblMedicine.setText("Medicine   Dolo-650")

        lblNoOfDose = QLabel(self)
        lblNoOfDose.setGeometry(18, 187, 184, 29)
        lblNoOfDose.setStyleSheet("text: bold")
        lblNoOfDose.setText("No. of Dose   12 Capsules")

        lblTime = QLabel(self)
        lblTime.setGeometry(18, 216, 184, 29)
        lblTime.setStyleSheet("text: bold")
        lblTime.setText("Time   7:00 am")

        lblWhen = QLabel(self)
        lblWhen.setGeometry(18, 242, 184, 29)
        lblWhen.setStyleSheet("text: bold")
        lblWhen.setText("When   12 Months")

        lblStartDate = QLabel(self)
        lblStartDate.setGeometry(18, 273, 184, 29)
        lblStartDate.setStyleSheet("text: bold")
        lblStartDate.setText("Start Date   26/05/2021")

        lblChangeFreq = QLabel(self)
        lblChangeFreq.setGeometry(18, 322, 184, 29)
        lblChangeFreq.setStyleSheet("text: bold")
        lblChangeFreq.setText("Change Frequency of the Medicine")

        lblHeader = QLabel("Select Dates", self)
        lblHeader.setGeometry(60, 146, 146, 27)
        lblHeader.setStyleSheet("background-color:#00FF0000;color:#555; font:normal; font-size:20px")

        lblDateHeader = QLabel("1.Start Date", self)
        lblDateHeader.setGeometry(26, 425, 121, 40)
        lblDateHeader.setAlignment(Qt.AlignCenter)
        lblDateHeader.setStyleSheet("background-color:#00FF0000; font:normal; font-size:18px; color: #00A0B5")

        lblDate = QLabel("Date",self)
        lblDate.setGeometry(44, 475, 46, 29)
        lblDate.setAlignment(Qt.AlignCenter)

        lblMonth = QLabel("Month", self)
        lblMonth.setGeometry(157, 475, 46, 29)
        lblMonth.setAlignment(Qt.AlignCenter)

        lblYear = QLabel("Year", self)
        lblYear.setGeometry(280, 475, 46, 29)
        lblYear.setAlignment(Qt.AlignCenter)

        self.lblStartDateBkg = QLabel(self)
        self.lblStartDateBkg.setPixmap(QPixmap('../Resources/Rectangle 506.png'))
        self.lblStartDateBkg.setGeometry(33, 562, 303, 40)

        self.lblStartDate = QLabel(self)   #Label showing the date
        self.lblStartDate.setGeometry(33, 562, 303, 40)
        self.lblStartDate.setAlignment(Qt.AlignCenter)
        self.lblStartDate.setStyleSheet("color:#00A0B5; background-color:#00F0F0F3; font-size:16px; font:bold")
        self.lblStartDate.setText(self.startDate.strftime('%d %A  ' + '%B ' +'     %Y '))


        # BUTTONS FOR MONTH INC AND DEC
        btnMonthInc = QPushButton(self)
        btnMonthInc.setGeometry(33, 514, 303, 40)
        btnMonthInc.setStyleSheet(self.datebtnStyle)
        btnMonthInc.setGraphicsEffect(Util.getNeuShadow(0))

        btnMonthInc1 = QPushButton(self)
        btnMonthInc1.setGeometry(33, 514, 303, 40)
        btnMonthInc1.setStyleSheet(self.datebtnStyle)
        btnMonthInc1.setIcon(QtGui.QIcon('../Resources/incArrow.png'))
        btnMonthInc1.setIconSize(QtCore.QSize(60, 40))
        btnMonthInc1.setGraphicsEffect(Util.getNeuShadow(1))
        btnMonthInc1.clicked.connect(self.addDate)

        btnMonthDec = QPushButton(self)
        btnMonthDec.setGeometry(33, 610, 303, 40)
        btnMonthDec.setStyleSheet(self.datebtnStyle)
        btnMonthDec.setGraphicsEffect(Util.getNeuShadow(0))

        btnMonthDec1 = QPushButton(self)
        btnMonthDec1.setGeometry(33, 610, 303, 40)
        btnMonthDec1.setStyleSheet(self.datebtnStyle)
        btnMonthDec1.setIcon(QtGui.QIcon('../Resources/decArrow.png'))
        btnMonthDec1.setIconSize(QtCore.QSize(60, 40))
        btnMonthDec1.setGraphicsEffect(Util.getNeuShadow(1))
        btnMonthDec1.clicked.connect(self.subDate)

        # Label & BUTTONS of WHEN
        lblWhen = QLabel("2. When", self)
        lblWhen.setGeometry(411, 425, 121, 40)
        lblWhen.setAlignment(Qt.AlignCenter)
        lblWhen.setStyleSheet("background-color:#00FF0000; font:normal; font-size:18px; color: #00A0B5")

        lblTimes1 = QLabel(self)
        lblTimes1.setGeometry(562, 532, 93, 45)
        lblTimes1.setStyleSheet("border-radius: 7")
        lblTimes1.setGraphicsEffect(Util.getNeuShadow(0))
        lblTimes = QLabel("Times",self)
        lblTimes.setGeometry(562, 532, 93, 45)
        lblTimes.setStyleSheet("border-radius: 7; color: black; font-size:15px")
        lblTimes.setGraphicsEffect(Util.getNeuShadow(1))

        lblHourly1 = QLabel(self)
        lblHourly1.setGeometry(562, 628, 93, 45)
        lblHourly1.setStyleSheet("border-radius: 7")
        lblHourly1.setGraphicsEffect(Util.getNeuShadow(0))
        lblHourly = QLabel("Hourly", self)
        lblHourly.setGeometry(562, 628, 93, 45)
        lblHourly.setStyleSheet("border-radius: 7; color: black; font-size:15px")
        lblHourly.setGraphicsEffect(Util.getNeuShadow(1))

        displayIpHourly = QLabel(self)
        displayIpHourly.setGeometry(500, 534, 45, 45)
        displayIpHourly.setPixmap(QPixmap('../Resources/ipHourly.png'))
        self.lblFreqHourly = QLabel(str(self.FreqHour), self)
        self.lblFreqHourly.setGeometry(500, 534, 45, 45)
        self.lblFreqHourly.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFreqHourly.setStyleSheet("background-color : #0000")

        displayIpTimes = QLabel(self)
        displayIpTimes.setGeometry(500, 583, 45, 45)
        displayIpTimes.setPixmap(QPixmap('../Resources/ipTimes.png'))
        self.lblFreqTimes = QLabel(str(self.FreqTimes), self)
        self.lblFreqTimes.setGeometry(500, 583, 45, 45)
        self.lblFreqTimes.setAlignment(QtCore.Qt.AlignCenter)
        self.lblFreqTimes.setStyleSheet("background-color : #0000")

        self.vitalsCombo1 = QComboBox(self)
        self.vitalsCombo1.setGeometry(411, 483, 214, 40)
        self.vitalsCombo1.setStyleSheet("QComboBox {border-radius: 10; color: #00A0B5; }"
                                        "QComboBox::drop-down { background:rgb(255,255,255,0)}")
        self.vitalsCombo1.setGraphicsEffect(Util.getNeuShadow(1))

        self.vitalsCombo = QComboBox(self)
        self.vitalsCombo.setGeometry(411, 483, 214, 40)
        self.vitalsCombo.setStyleSheet("QComboBox {border-radius: 10; color: black; padding-left:15px;font-size:18px}"
                                       "QComboBox::drop-down { background:rgb(255,255,255,0);padding-right:20px}"
                                       "QComboBox::down-arrow{image: url(../Resources/down.png)}")
        self.vitalsCombo.setGraphicsEffect(Util.getNeuShadow(0))
        self.vitalsCombo.addItem("Monthly")
        self.vitalsCombo.addItem("Daily")
        self.vitalsCombo.addItem("Weekly")
        self.vitalsCombo.addItem("Alternate Days")

        # self.vitalsCombo.currentIndexChanged.connect(self.vitalChanged)

        btnfreqHourlyDec1 = QPushButton("<", self)
        btnfreqHourlyDec1.setGeometry(411, 534, 33, 45)
        btnfreqHourlyDec1.setStyleSheet("border-radius : 7; background-color: #F0F0F3")
        btnfreqHourlyDec1.setGraphicsEffect(Util.getNeuShadow(0))
        btnfreqHourlyDec = QPushButton("<", self)
        btnfreqHourlyDec.setGeometry(411, 534, 33, 45)
        btnfreqHourlyDec.setStyleSheet("border-radius : 7; background-color: #F0F0F3")
        btnfreqHourlyDec.setGraphicsEffect(Util.getNeuShadow(1))
        btnfreqHourlyDec.clicked.connect(self.subFreqHour)

        btnfreqHourlyInc1 = QPushButton(">", self)
        btnfreqHourlyInc1.setGeometry(544, 534, 33, 45)
        btnfreqHourlyInc1.setStyleSheet("border-radius : 7; background-color: #F0F0F3")
        btnfreqHourlyInc1.setGraphicsEffect(Util.getNeuShadow(0))
        btnfreqHourlyInc = QPushButton(">", self)
        btnfreqHourlyInc.setGeometry(544, 534, 33, 45)
        btnfreqHourlyInc.setStyleSheet("border-radius : 7; background-color: #F0F0F3")
        btnfreqHourlyInc.setGraphicsEffect(Util.getNeuShadow(1))
        btnfreqHourlyInc.clicked.connect(self.addFreqHour)

        btnfreqTimesDec1 = QPushButton("", self)
        btnfreqTimesDec1.setGeometry(411, 583, 33, 45)
        btnfreqTimesDec1.setStyleSheet("border-radius : 7; background-color: #F0F0F3")
        btnfreqTimesDec1.setGraphicsEffect(Util.getNeuShadow(0))
        btnfreqTimesDec = QPushButton("<", self)
        btnfreqTimesDec.setGeometry(411, 583, 33, 45)
        btnfreqTimesDec.setStyleSheet("border-radius : 7; background-color: #F0F0F3")
        btnfreqTimesDec.setGraphicsEffect(Util.getNeuShadow(1))
        btnfreqTimesDec.clicked.connect(self.subFreqTimes)


        btnfreqTimesInc1 = QPushButton("", self)
        btnfreqTimesInc1.setGeometry(545, 583, 33, 45)
        btnfreqTimesInc1.setStyleSheet("border-radius : 7; background-color: #F0F0F3")
        btnfreqTimesInc1.setGraphicsEffect(Util.getNeuShadow(0))
        btnfreqTimesInc = QPushButton(">", self)
        btnfreqTimesInc.setGeometry(545, 583, 33, 45)
        btnfreqTimesInc.setStyleSheet("border-radius : 7; background-color: #F0F0F3")
        btnfreqTimesInc.setGraphicsEffect(Util.getNeuShadow(1))
        btnfreqTimesInc.clicked.connect(self.addFreqTimes)

        #LABEL and BUTTONS of Timing

        lblTiming = QLabel("3. Timing", self)
        lblTiming.setGeometry(740, 425, 90, 30)
        lblTiming.setStyleSheet("color: #00A0B5")

        btnHourAdd1 = QPushButton("", self)
        btnHourAdd1.setGeometry(740, 483, 45, 33)
        btnHourAdd1.setStyleSheet("border-radius : 7; background-color: #F0F0F3")
        btnHourAdd1.setGraphicsEffect(Util.getNeuShadow(0))
        btnHourAdd = QPushButton("", self)
        btnHourAdd.setGeometry(740, 483, 45, 33)
        btnHourAdd.setStyleSheet("border-radius : 7; background-color: #F0F0F3")
        btnHourAdd.setIcon(QtGui.QIcon('../Resources/up.png'))
        btnHourAdd.setGraphicsEffect(Util.getNeuShadow(1))
        btnHourAdd.setIconSize(QtCore.QSize(45, 33))
        btnHourAdd.clicked.connect(self.addBfHour)

        btnHourSub1 = QPushButton("", self)
        btnHourSub1.setGeometry(740, 568, 45, 33)
        btnHourSub1.setStyleSheet("border-radius : 7; background-color: #F0F0F3")
        btnHourSub1.setGraphicsEffect(Util.getNeuShadow(0))
        btnHourSub = QPushButton("", self)
        btnHourSub.setGeometry(740, 568, 45, 33)
        btnHourSub.setStyleSheet("border-radius : 7; background-color: #F0F0F3")
        btnHourSub.setIcon(QtGui.QIcon('../Resources/down.png'))
        btnHourSub.setIconSize(QtCore.QSize(45, 33))
        btnHourSub.setGraphicsEffect(Util.getNeuShadow(1))
        btnHourSub.clicked.connect(self.subBfHour)

        btnMinAdd1 = QPushButton("", self)
        btnMinAdd1.setGeometry(816, 483, 45, 33)
        btnMinAdd1.setStyleSheet("border-radius : 7; background-color: #F0F0F3")
        btnMinAdd1.setGraphicsEffect(Util.getNeuShadow(0))
        btnMinAdd = QPushButton("", self)
        btnMinAdd.setGeometry(816, 483, 45, 33)
        btnMinAdd.setStyleSheet("border-radius : 7; background-color: #F0F0F3")
        btnMinAdd.setIcon(QtGui.QIcon('../Resources/up.png'))
        btnMinAdd.setIconSize(QtCore.QSize(45, 33))
        btnMinAdd.setGraphicsEffect(Util.getNeuShadow(1))
        btnMinAdd.clicked.connect(self.addBfMin)

        btnMinSub1 = QPushButton("", self)
        btnMinSub1.setGeometry(816, 568, 45, 33)
        btnMinSub1.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnMinSub1.setGraphicsEffect(Util.getNeuShadow(0))
        btnMinSub = QPushButton("", self)
        btnMinSub.setGeometry(816, 568, 45, 33)
        btnMinSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnMinSub.setIcon(QtGui.QIcon('../Resources/down.png'))
        btnMinSub.setIconSize(QtCore.QSize(45, 33))
        btnMinSub.setGraphicsEffect(Util.getNeuShadow(1))
        btnMinSub.clicked.connect(self.subBfMin)



        display3_lbl = QLabel(self)
        display3_lbl.setPixmap(QPixmap('../Resources/mBkg.png'))
        display3_lbl.setGeometry(740, 525, 45, 33)
        self.lblHour = QLabel(str(self.Hour), self)
        self.lblHour.setGeometry(756, 527, 30, 21)
        self.lblHour.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHour.setStyleSheet("background-color : #0000")

        display4_lbl = QLabel(self)
        display4_lbl.setPixmap(QPixmap('../Resources/mBkg.png'))
        display4_lbl.setGeometry(816, 525, 45, 33)
        self.lblMin = QLabel(str(self.Min), self)
        self.lblMin.setGeometry(832, 527, 30, 21)
        self.lblMin.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMin.setStyleSheet("background-color : #0000")

    def addBfHour(self):
        if self.Hour < 12:
            self.Hour = self.Hour + 1
            self.lblHour.setText(str(self.Hour))

    def subBfHour(self):
        if self.Hour > 0:
            self.Hour = self.Hour - 1
            self.lblHour.setText(str(self.Hour))


    def addBfMin(self):
        if self.Min < 60:
            self.Min = self.Min + 5
            self.lblMin.setText(str(self.Min))

    def subBfMin(self):
        if self.Min > 0:
            self.Min = self.Min - 5
            self.lblMin.setText(str(self.Min))

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



if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = ExtraDosage(QWidget)

    window.show()

# start the app
    sys.exit(App.exec())
