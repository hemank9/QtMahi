from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window4(QWidget):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\massEjection.png'))
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





class Window3(QWidget):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\yellow.png'))
        self.label.setGeometry(0, 0, 1220, 39)

        self.UiComponents()
    #
    #     # showing all the widgets
        self.show()
    #
    def UiComponents(self):

        btn_back = QPushButton("", self)
        btn_back.setGeometry(40, 53, 173, 41)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('Resources\Group 49.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)

        btn_lnight = QPushButton("", self)
        btn_lnight.setGeometry(826, 100, 320, 320)
        btn_lnight.setStyleSheet("border-radius : 10; background-color: #0000")
        btn_lnight.setIcon(QtGui.QIcon('Resources\lnight.png'))
        btn_lnight.setIconSize(QtCore.QSize(330, 330))
        btn_lnight.clicked.connect(self.close)

        btn_mnight = QPushButton("", self)
        btn_mnight.setGeometry(457, 100, 320, 320)
        btn_mnight.setStyleSheet("border-radius : 10; background-color: #0000")
        btn_mnight.setIcon(QtGui.QIcon('Resources\\mnight.png'))
        btn_mnight.setIconSize(QtCore.QSize(330, 330))
        btn_mnight.clicked.connect(self.close)

        btn_emorning = QPushButton("", self)
        btn_emorning.setGeometry(88, 100, 320, 320)
        btn_emorning.setStyleSheet("border-radius : 10; background-color: #0000")
        btn_emorning.setIcon(QtGui.QIcon('Resources\emorning.png'))
        btn_emorning.setIconSize(QtCore.QSize(330, 330))
        btn_emorning.clicked.connect(self.close)

        frame = QFrame(self)
        frame.setFrameShape(QFrame.WinPanel)
        frame.setGeometry(115, 494, 270, 171)
        frame.setLineWidth(1)
        # frame.midLineWidth(3)
        frame.setStyleSheet("border-radius : 20; background-color: white ")




class Window2(QWidget):                           # <===
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\Group 71.png'))
        self.label.setGeometry(0, 0, 1220, 249)

        self.UiComponents()
    #
    #     # showing all the widgets
        self.show()
    #
    def UiComponents(self):

        btn_back = QPushButton("", self)
        btn_back.setGeometry(40, 53, 173, 41)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('Resources\Group 49.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)

        lblITabInfo = QLabel("Take Dolo 650 3 times a day!",self)
        lblITabInfo.setGeometry(43, 159, 657, 30)


        btnfreqHourlyDec = QPushButton("", self)
        btnfreqHourlyDec.setGeometry(142, 263, 33, 45)
        btnfreqHourlyDec.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnfreqHourlyDec.setIcon(QtGui.QIcon('Resources\cntDecrease.png'))
        btnfreqHourlyDec.setIconSize(QtCore.QSize(160, 90))
        btnfreqHourlyDec.clicked.connect(self.close)

        btnfreqHourlyInc = QPushButton("", self)
        btnfreqHourlyInc.setGeometry(242, 263, 33, 45)
        btnfreqHourlyInc.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnfreqHourlyInc.setIcon(QtGui.QIcon('Resources\cntIecrease.png'))
        btnfreqHourlyInc.setIconSize(QtCore.QSize(160, 90))
        btnfreqHourlyInc.clicked.connect(self.close)

        btnhourly = QPushButton("", self)
        btnhourly.setGeometry(280, 263, 100, 45)
        btnhourly.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnhourly.setIcon(QtGui.QIcon('Resources\hourly.png'))
        btnhourly.setIconSize(QtCore.QSize(110, 90))
        btnhourly.clicked.connect(self.close)

        btnfreqTimesDec = QPushButton("", self)
        btnfreqTimesDec.setGeometry(142, 315, 33, 45)
        btnfreqTimesDec.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnfreqTimesDec.setIcon(QtGui.QIcon('Resources\cntDecrease.png'))
        btnfreqTimesDec.setIconSize(QtCore.QSize(160, 90))
        btnfreqTimesDec.clicked.connect(self.close)

        btnfreqTimesInc = QPushButton("", self)
        btnfreqTimesInc.setGeometry(242, 315, 33, 45)
        btnfreqTimesInc.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnfreqTimesInc.setIcon(QtGui.QIcon('Resources\cntIecrease.png'))
        btnfreqTimesInc.setIconSize(QtCore.QSize(160, 90))
        btnfreqTimesInc.clicked.connect(self.close)

        displayIpHourly = QLabel(self)
        displayIpHourly.setPixmap(QPixmap('Resources\ipHourly.png'))
        displayIpHourly.setGeometry(191, 264, 45, 45)
        lblIpHourly = QLabel("10", self)
        lblIpHourly.setGeometry(197, 275, 30, 21)
        lblIpHourly.setAlignment(QtCore.Qt.AlignCenter)
        lblIpHourly.setStyleSheet("background-color : #0000")

        displayIpTimes = QLabel(self)
        displayIpTimes.setPixmap(QPixmap('Resources\ipTimes.png'))
        displayIpTimes.setGeometry(191, 316, 45, 45)
        lblIpTimes = QLabel("10", self)
        lblIpTimes.setGeometry(197, 328, 30, 21)
        lblIpTimes.setAlignment(QtCore.Qt.AlignCenter)
        lblIpTimes.setStyleSheet("background-color : #0000")

        btnTimes = QPushButton("", self)
        btnTimes.setGeometry(280, 315, 100, 45)
        btnTimes.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnTimes.setIcon(QtGui.QIcon('Resources\\times.png'))
        btnTimes.setIconSize(QtCore.QSize(110, 90))
        btnTimes.clicked.connect(self.close)

        # Timing Buttons

        btnHourAdd = QPushButton("", self)
        btnHourAdd.setGeometry(477, 263, 45, 33)
        btnHourAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnHourAdd.setIcon(QtGui.QIcon('Resources\mAddTime.png'))
        btnHourAdd.setIconSize(QtCore.QSize(160, 90))
        btnHourAdd.clicked.connect(self.close)

        btnHourSub = QPushButton("", self)
        btnHourSub.setGeometry(477, 348, 45, 33)
        btnHourSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnHourSub.setIcon(QtGui.QIcon('Resources\mSubTime.png'))
        btnHourSub.setIconSize(QtCore.QSize(160, 90))
        btnHourSub.clicked.connect(self.close)

        btnMinAdd = QPushButton("", self)
        btnMinAdd.setGeometry(553, 263, 45, 33)
        btnMinAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnMinAdd.setIcon(QtGui.QIcon('Resources\mAddTime.png'))
        btnMinAdd.setIconSize(QtCore.QSize(160, 90))
        btnMinAdd.clicked.connect(self.close)

        btnMinSub = QPushButton("", self)
        btnMinSub.setGeometry(553, 348, 45, 33)
        btnMinSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnMinSub.setIcon(QtGui.QIcon('Resources\mSubTime.png'))
        btnMinSub.setIconSize(QtCore.QSize(160, 90))
        btnMinSub.clicked.connect(self.close)

        btnAmPm = QPushButton("", self)
        btnAmPm.setGeometry(629, 305, 45, 33)
        btnAmPm.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAmPm.setIcon(QtGui.QIcon('Resources\pmbtn.png'))
        btnAmPm.setIconSize(QtCore.QSize(160, 90))
        btnAmPm.clicked.connect(self.close)

        lblAmPm = QLabel("am", self)
        lblAmPm.setGeometry(637, 305, 25, 25)

        display3_lbl = QLabel(self)
        display3_lbl.setPixmap(QPixmap('Resources\mBkg.png'))
        display3_lbl.setGeometry(477, 305, 45, 33)
        lblAfHour = QLabel("10", self)
        lblAfHour.setGeometry(483, 310, 30, 21)
        lblAfHour.setAlignment(QtCore.Qt.AlignCenter)
        lblAfHour.setStyleSheet("background-color : #0000")

        display4_lbl = QLabel(self)
        display4_lbl.setPixmap(QPixmap('Resources\mBkg.png'))
        display4_lbl.setGeometry(553, 305, 45, 33)
        lblAfMin = QLabel("10", self)
        lblAfMin.setGeometry(560, 310, 30, 21)
        lblAfMin.setAlignment(QtCore.Qt.AlignCenter)
        lblAfMin.setStyleSheet("background-color : #0000")





class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 700)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\\bckmedtime.png'))
        self.label.setGeometry(0, 0, 1220, 473)


        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        btn_adv = QPushButton("", self)
        btn_adv.setGeometry(96, 529, 250, 115)
        btn_adv.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_adv.setIcon(QtGui.QIcon('Resources\Group 52.png'))
        btn_adv.setIconSize(QtCore.QSize(280, 135))
        btn_adv.clicked.connect(self.massEjection)

        btn_ctime = QPushButton("", self)
        btn_ctime.setGeometry(360, 530, 250, 114)
        btn_ctime.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_ctime.setIcon(QtGui.QIcon('Resources\Group 51.png'))
        btn_ctime.setIconSize(QtCore.QSize(280, 135))
        btn_ctime.clicked.connect(self.close)

        btn_repetativeD = QPushButton("", self)
        btn_repetativeD.setGeometry(625, 530, 237, 115)
        btn_repetativeD.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_repetativeD.setIcon(QtGui.QIcon('Resources\\repetative.png'))
        btn_repetativeD.setIconSize(QtCore.QSize(280, 135))
        btn_repetativeD.clicked.connect(self.repeateD)

        btn_dosage = QPushButton("", self)
        btn_dosage.setGeometry(890, 530, 250, 114)
        btn_dosage.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_dosage.setIcon(QtGui.QIcon('Resources\Group 53.png'))
        btn_dosage.setIconSize(QtCore.QSize(280, 135))
        btn_dosage.clicked.connect(self.extraD)


        # MOrning, Afternoon, Evening Buttons

        btn_evening = QPushButton("", self)
        btn_evening.setGeometry(826, 100, 320, 320)
        btn_evening.setStyleSheet("border-radius : 10; background-color: #0000")
        btn_evening.setIcon(QtGui.QIcon('Resources\evening.png'))
        btn_evening.setIconSize(QtCore.QSize(330, 330))
        btn_evening.clicked.connect(self.close)

        btn_afternoon = QPushButton("", self)
        btn_afternoon.setGeometry(457, 100, 320, 320)
        btn_afternoon.setStyleSheet("border-radius : 10; background-color: #0000")
        btn_afternoon.setIcon(QtGui.QIcon('Resources\\afternoon.png'))
        btn_afternoon.setIconSize(QtCore.QSize(330, 330))
        btn_afternoon.clicked.connect(self.close)

        btn_morning = QPushButton("", self)
        btn_morning.setGeometry(88, 100, 320, 320)
        btn_morning.setStyleSheet("border-radius : 10; background-color: #0000")
        btn_morning.setIcon(QtGui.QIcon('Resources\morning.png'))
        btn_morning.setIconSize(QtCore.QSize(330, 330))
        btn_morning.clicked.connect(self.close)

        btn_bck = QPushButton("", self)
        btn_bck.setGeometry(43, 40, 150, 55)
        btn_bck.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_bck.setIcon(QtGui.QIcon('Resources\Group 34.png'))
        btn_bck.setIconSize(QtCore.QSize(160, 90))
        btn_bck.clicked.connect(self.close)


    def repeateD(self):
        self.l = Window2()

    def massEjection(self):
        self.n = Window4()

    def extraD(self):
        self.m = Window3()

App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec())



