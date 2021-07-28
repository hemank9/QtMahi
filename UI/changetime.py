import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Utility.MahiUtility as Util
import MyDatabase.my_database as myDb
import constants as MyConst


class ChangeTime(QMainWindow):

    def __init__(self, type):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 700)
        self.setStyleSheet("background-color: #F0F0F3")
        # self.label = QLabel(self)
        # self.label.setPixmap(QPixmap('../Resources/mtry.png'))
        # self.label.setGeometry(0, 0, 1220, 700)

        # calling method
        self.UiComponents()

        # self.FetchTimings()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        self.btnStyle = "border-radius : 15; background-color: #F0F03; color : #00A0B5;font:bold;font-size:16px"
        self.btnStyleSelected = "border-radius : 15; background-color: #BCE6EC; color : #00A0B5;font:bold;font-size:16px"


        # # self.FetchTimings()
        # self.bfHour = 10
        # self.bfMin = 10
        #
        # self.afHour = 10
        # self.afMin = 10



        btn_bck = QPushButton("", self)
        btn_bck.setGeometry(29, 35, 112, 41)
        btn_bck.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_bck.setIcon(QtGui.QIcon('../Resources/backButton.png'))
        btn_bck.setIconSize(QtCore.QSize(160, 90))
        btn_bck.clicked.connect(self.close)

        btnSync1 = QPushButton(self)
        btnSync1.setGeometry(152, 35, 39, 39)
        btnSync1.setStyleSheet("border-radius : 10; background-color : #F0F0F3")
        btnSync1.setIcon(QtGui.QIcon('../Resources/syncBtn.png'))
        btnSync1.setIconSize(QtCore.QSize(39, 39))
        btnSync1.setGraphicsEffect(Util.getNeuShadow(0))
        btnSync = QPushButton(self)
        btnSync.setGeometry(152, 35, 39, 39)
        btnSync.setStyleSheet("border-radius : 10; background-color : #F0F0F3")
        btnSync.setIcon(QtGui.QIcon('../Resources/syncBtn.png'))
        btnSync.setIconSize(QtCore.QSize(39, 39))
        btnSync.setGraphicsEffect(Util.getNeuShadow(1))

        lblbf = QLabel("Before Food (BF)", self)
        lblbf.setGeometry(234, 302, 160, 29)
        lblbf.setStyleSheet("font-size:20px;")

        lblaf = QLabel("After Food (AF)", self)
        lblaf.setGeometry(540, 302, 160, 40)
        lblaf.setStyleSheet("font-size:20px;")

        # Buttons for Morning Before Food


        btnbfHourAdd = QPushButton("", self)
        btnbfHourAdd.setGeometry(233, 370, 45, 33)
        btnbfHourAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnbfHourAdd.setIcon(QtGui.QIcon('../Resources/mAddTime.png'))
        btnbfHourAdd.setIconSize(QtCore.QSize(160, 90))
        btnbfHourAdd.clicked.connect(lambda : self.addSubBfHour(True))

        btnbfHourSub = QPushButton("", self)
        btnbfHourSub.setGeometry(233, 455, 45, 33)
        btnbfHourSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnbfHourSub.setIcon(QtGui.QIcon('../Resources/mSubTime.png'))
        btnbfHourSub.setIconSize(QtCore.QSize(160, 90))
        btnbfHourSub.clicked.connect(lambda : self.addSubBfHour(False))

        display_lbl = QLabel(self)
        display_lbl.setPixmap(QPixmap('../Resources/mBkg.png'))
        display_lbl.setGeometry(235, 412, 45, 33)
        self.lblBfHour = QLabel(self)
        self.lblBfHour.setGeometry(241, 418, 30, 21)
        self.lblBfHour.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBfHour.setStyleSheet("background-color : #0000")

        btnbfMinAdd = QPushButton("", self)
        btnbfMinAdd.setGeometry(310, 370, 45, 33)
        btnbfMinAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnbfMinAdd.setIcon(QtGui.QIcon('../Resources/mAddTime.png'))
        btnbfMinAdd.setIconSize(QtCore.QSize(160, 90))
        btnbfMinAdd.clicked.connect(lambda : self.addSubBfMin(True))

        btnbfMinSub = QPushButton("", self)
        btnbfMinSub.setGeometry(310, 455, 45, 33)
        btnbfMinSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnbfMinSub.setIcon(QtGui.QIcon('../Resources/mSubTime.png'))
        btnbfMinSub.setIconSize(QtCore.QSize(160, 90))
        btnbfMinSub.clicked.connect(lambda : self.addSubBfMin(False))

        display2_lbl = QLabel(self)
        display2_lbl.setPixmap(QPixmap('../Resources/mBkg.png'))
        display2_lbl.setGeometry(312, 412, 45, 33)
        self.lblBfMin = QLabel(self)
        self.lblBfMin.setGeometry(318, 418, 30, 21)
        self.lblBfMin.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBfMin.setStyleSheet("background-color : #0000")

        # btnBfAmPm = QPushButton("", self)
        # btnBfAmPm.setGeometry(386, 412, 45, 33)
        # btnBfAmPm.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        # btnBfAmPm.setIcon(QtGui.QIcon('../Resources/pmbtn.png'))
        # btnBfAmPm.setIconSize(QtCore.QSize(160, 90))
        # btnBfAmPm.clicked.connect(self.close)


        lblBfAmPmBkg = QLabel("", self)
        lblBfAmPmBkg.setGeometry(395, 412, 40, 33)
        lblBfAmPmBkg.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        lblBfAmPmBkg.setGraphicsEffect(Util.getNeuShadow2(1,5,-2))

        self.lblBfAmPm = QLabel("am", self)
        self.lblBfAmPm.setAlignment(Qt.AlignCenter)
        self.lblBfAmPm.setGeometry(395, 412, 40, 33)
        self.lblBfAmPm.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        self.lblBfAmPm.setGraphicsEffect(Util.getNeuShadow2(0,5,1))



        # Buttons for Morning After Food

        btnAfHourAdd = QPushButton("", self)
        btnAfHourAdd.setGeometry(540, 370, 45, 33)
        btnAfHourAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAfHourAdd.setIcon(QtGui.QIcon('../Resources/mAddTime.png'))
        btnAfHourAdd.setIconSize(QtCore.QSize(160, 90))
        btnAfHourAdd.clicked.connect(self.addAfHour)

        btnAfHourSub = QPushButton("", self)
        btnAfHourSub.setGeometry(540, 455, 45, 33)
        btnAfHourSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAfHourSub.setIcon(QtGui.QIcon('../Resources/mSubTime.png'))
        btnAfHourSub.setIconSize(QtCore.QSize(160, 90))
        btnAfHourSub.clicked.connect(self.subAfHour)


        display3_lbl = QLabel(self)
        display3_lbl.setPixmap(QPixmap('../Resources/mBkg.png'))
        display3_lbl.setGeometry(540, 412, 45, 33)
        self.lblAfHour = QLabel( self)
        self.lblAfHour.setGeometry(546, 418, 30, 21)
        self.lblAfHour.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAfHour.setStyleSheet("background-color : #0000")

        btnAfMinAdd = QPushButton("", self)
        btnAfMinAdd.setGeometry(616, 370, 45, 33)
        btnAfMinAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAfMinAdd.setIcon(QtGui.QIcon('../Resources/mAddTime.png'))
        btnAfMinAdd.setIconSize(QtCore.QSize(160, 90))
        btnAfMinAdd.clicked.connect(self.addAfMin)

        btnAfMinSub = QPushButton("", self)
        btnAfMinSub.setGeometry(616, 455, 45, 33)
        btnAfMinSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAfMinSub.setIcon(QtGui.QIcon('../Resources/mSubTime.png'))
        btnAfMinSub.setIconSize(QtCore.QSize(160, 90))
        btnAfMinSub.clicked.connect(self.subAfMin)

        display4_lbl = QLabel(self)
        display4_lbl.setPixmap(QPixmap('../Resources/mBkg.png'))
        display4_lbl.setGeometry(616, 412, 45, 33)
        self.lblAfMin = QLabel(self)
        self.lblAfMin.setGeometry(622, 418, 30, 21)
        self.lblAfMin.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAfMin.setStyleSheet("background-color : #0000")

        btnAfAmPm = QLabel("", self)
        btnAfAmPm.setGeometry(692, 412, 40, 33)
        btnAfAmPm.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAfAmPm.setGraphicsEffect(Util.getNeuShadow2(1,5,-2))

        self.lblAfAmPm = QLabel("am", self)
        self.lblAfAmPm.setAlignment(Qt.AlignCenter)
        self.lblAfAmPm.setGeometry(692, 412, 40, 33)
        self.lblAfAmPm.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        self.lblAfAmPm.setGraphicsEffect(Util.getNeuShadow2(0,5,1))

        # Buttons of Morning, Evening, Afternoon, Mid Night, Late Night, Early Morning

        btnMorning = QPushButton("Morning", self)
        btnMorning.setGeometry(30, 120, 165, 50)
        btnMorning.setStyleSheet(self.btnStyleSelected)
        btnMorning.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnMorning1 = QPushButton("Morning", self)
        self.btnMorning1.setGeometry(30, 120, 165, 50)
        self.btnMorning1.setStyleSheet(self.btnStyleSelected) 
        self.btnMorning1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnMorning1.clicked.connect(self.morningClicked)


        btnAfternoon = QPushButton("Afternoon", self)
        btnAfternoon.setGeometry(215, 120, 165, 50)
        btnAfternoon.setStyleSheet(self.btnStyle)
        btnAfternoon.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnAfternoon1 = QPushButton("Afternoon", self)
        self.btnAfternoon1.setGeometry(215, 120, 165, 50)
        self.btnAfternoon1.setStyleSheet(self.btnStyle)
        self.btnAfternoon1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnAfternoon1.clicked.connect(self.afternoonClicked)


        btnEvening = QPushButton("Evening", self)
        btnEvening.setGeometry(400, 120, 165, 50)
        btnEvening.setStyleSheet(self.btnStyle)
        btnEvening.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnEvening1 = QPushButton("Evening", self)
        self.btnEvening1.setGeometry(400, 120, 165, 50)
        self.btnEvening1.setStyleSheet(self.btnStyle)
        self.btnEvening1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnEvening1.clicked.connect(self.eveningClicked)


        btnMidNight = QPushButton( self)
        btnMidNight.setGeometry(585, 120, 165, 50)
        btnMidNight.setStyleSheet(self.btnStyle)
        btnMidNight.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnMidNight1 = QPushButton("Mid Night", self)
        self.btnMidNight1.setGeometry(585, 120, 165, 50)
        self.btnMidNight1.setStyleSheet(self.btnStyle)
        self.btnMidNight1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnMidNight1.clicked.connect(self.midNightClicked)

        btnLateNight = QPushButton( self)
        btnLateNight.setGeometry(770, 120, 165, 50)
        btnLateNight.setStyleSheet(self.btnStyle)
        btnLateNight.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnLateNight1 = QPushButton("Late Night", self)
        self.btnLateNight1.setGeometry(770, 120, 165, 50)
        self.btnLateNight1.setStyleSheet(self.btnStyle)
        self.btnLateNight1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnLateNight1.clicked.connect(self.lateNightClicked)

        btnEarlyMorning = QPushButton( self)
        btnEarlyMorning.setGeometry(955, 120, 165, 50)
        btnEarlyMorning.setStyleSheet(self.btnStyle)
        btnEarlyMorning.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnEarlyMorning1 = QPushButton("Early Morning", self)
        self.btnEarlyMorning1.setGeometry(955, 120, 165, 50)
        self.btnEarlyMorning1.setStyleSheet(self.btnStyle)
        self.btnEarlyMorning1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnEarlyMorning1.clicked.connect(self.earlyMorningClicked)

        btnOk = QPushButton("", self)
        btnOk.setGeometry(967, 459, 158, 92)
        btnOk.setStyleSheet("border-radius : 15; background-color: #F0F0F3; color : #00A0B5")
        btnOk.setIcon(QtGui.QIcon('../Resources/mOk.png'))
        btnOk.setIconSize(QtCore.QSize(180, 110))
        btnOk.clicked.connect(self.close)

        self.dayTimeSelected(1)

    # def FetchTimings(self):
    #
    #     try:
    #         timeCursor = myDb.getSlotTimings()
    #         self.timeList = []
    #         for row in timeCursor:
    #
    #             self.timeList.append(tuple(row))
    #             print(row)
    #
    #             # time = Util.convert24to12Time(str(row[3]))
    #             #
    #             # if time == None:
    #             #     time = "N.A."
    #             #
    #             # # Morning
    #             # if str(row[1]).lower() == "morning":
    #             #     if "before" in str(row[2]):
    #             #         self.lblMorningBf.setText(time)
    #             #     elif "after" in str(row[2]):
    #             #         self.lblMorningAf.setText(time)
    #             #
    #             # # Afternoon
    #             # elif str(row[1]).lower() == "afternoon" or str(row[1]).lower() == "noon":
    #             #     if "before" in str(row[2]):
    #             #         self.lblAfternoonBf.setText(time)
    #             #     elif "after" in str(row[2]):
    #             #         self.lblAfternoonAf.setText(time)
    #             #
    #             # # Evening
    #             # elif str(row[1]).lower() == "evening":
    #             #     if "before" in str(row[2]):
    #             #         self.lblEveningBf.setText(time)
    #             #     elif "after" in str(row[2]):
    #             #         self.lblEveningAf.setText(time)
    #
    #         # self.onTimeSelected()
    #
    #         if len(self.timeList)>0:
    #             self.selectedSlot = self.timeList[0]
    #
    #     except Exception as e:
    #         print(e.__cause__)

    def onTimeSelected(self):
        try:
            print(len(self.timeList))
            # print(self.timeList[0])
        except Exception as e:
            print(e.__cause__)


    # INCREMENT AND DECREMENT OF BEFORE FOOD
    def addSubBfHour(self, isAdd):

        tempTime = (int(self.lblBfHour.text()) * 60) + int(self.lblBfMin.text())

        if isAdd:

            afTime = (int(self.lblAfHour.text()) * 60) + int(self.lblAfMin.text())
            if(self.isAfPm):
                afTime = afTime + (60*12)

            print("after time:"+str(afTime))
            if (tempTime + 60) < afTime:
                self.bfHour = self.bfHour + 1
                if self.bfHour>12:
                    self.bfHour-12
                self.lblBfHour.setText(str(self.bfHour))
                tempTime = tempTime+60

        else:


            if (tempTime-60) > self.lowerTimeLimit:
                self.bfHour = self.bfHour - 1
                self.lblBfHour.setText(str(self.bfHour))
                tempTime = tempTime-60

        self.setAmPm(True)
        print(tempTime)

    def addSubBfMin(self, isAdd):

        tempTime = (int(self.lblBfHour.text()) * 60) + int(self.lblBfMin.text())

        if isAdd:

            afTime = (int(self.lblAfHour.text()) * 60) + int(self.lblAfMin.text()) - 30
            if (self.isAfPm):
                afTime = afTime + (60 * 12)


            print("after time:" + str(afTime))
            if (tempTime + 5) <= afTime and (self.bfMin+5)<60:
                self.bfMin = self.bfMin + 5

                self.lblBfMin.setText(str(self.bfMin))
                tempTime = tempTime + 5

        else:

            if (tempTime - 5) > self.lowerTimeLimit and (self.bfMin-5)>=0:
                self.bfMin = self.bfMin - 5
                self.lblBfMin.setText(str(self.bfMin))
                tempTime = tempTime - 5

        self.setAmPm(True)
        print(tempTime)

    def setAmPm(self, isBf):

        if isBf:
            tempTime = (int(self.lblBfHour.text()) * 60) + int(self.lblBfMin.text())

            if tempTime>0 and tempTime<60*12:
                self.isBfPm = False
                self.lblBfAmPm.setText("am")
            else:
                self.isBfPm = True
                self.lblBfAmPm.setText("pm")
        else :
            tempTime = (int(self.lblAfHour.text()) * 60) + int(self.lblAfMin.text())

            if tempTime>0 and tempTime<60*12:
                self.isAfPm = False
                self.lblAfAmPm.setText("am")
            else:
                self.isAfPm = True
                self.lblAfAmPm.setText("pm")


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

    def morningClicked(self):
        self.dayTimeSelected(1)

    def afternoonClicked(self):
        self.dayTimeSelected(2)

    def eveningClicked(self):
        self.dayTimeSelected(3)

    def midNightClicked(self):
        self.dayTimeSelected(4)

    def lateNightClicked(self):
        self.dayTimeSelected(5)

    def earlyMorningClicked(self):
        self.dayTimeSelected(6)

    def dayTimeSelected(self,type):

        if type == 1:
            self.btnMorning1.setStyleSheet(self.btnStyleSelected)
            self.btnAfternoon1.setStyleSheet(self.btnStyle)
            self.btnEvening1.setStyleSheet(self.btnStyle)
            self.btnMidNight1.setStyleSheet(self.btnStyle)
            self.btnLateNight1.setStyleSheet(self.btnStyle)
            self.btnEarlyMorning1.setStyleSheet(self.btnStyle)

            self.SetSelectedData(0)

        elif type == 2:
            self.btnMorning1.setStyleSheet(self.btnStyle)
            self.btnAfternoon1.setStyleSheet(self.btnStyleSelected)
            self.btnEvening1.setStyleSheet(self.btnStyle)
            self.btnMidNight1.setStyleSheet(self.btnStyle)
            self.btnLateNight1.setStyleSheet(self.btnStyle)
            self.btnEarlyMorning1.setStyleSheet(self.btnStyle)
            self.SetSelectedData(1)

        elif type == 3:
            self.btnMorning1.setStyleSheet(self.btnStyle)
            self.btnAfternoon1.setStyleSheet(self.btnStyle)
            self.btnEvening1.setStyleSheet(self.btnStyleSelected)
            self.btnMidNight1.setStyleSheet(self.btnStyle)
            self.btnLateNight1.setStyleSheet(self.btnStyle)
            self.btnEarlyMorning1.setStyleSheet(self.btnStyle)
            self.SetSelectedData(2)

        elif type == 4:
            self.btnMorning1.setStyleSheet(self.btnStyle)
            self.btnAfternoon1.setStyleSheet(self.btnStyle)
            self.btnEvening1.setStyleSheet(self.btnStyle)
            self.btnMidNight1.setStyleSheet(self.btnStyleSelected)
            self.btnLateNight1.setStyleSheet(self.btnStyle)
            self.btnEarlyMorning1.setStyleSheet(self.btnStyle)
            self.SetSelectedData(3)

        elif type == 5:
            self.btnMorning1.setStyleSheet(self.btnStyle)
            self.btnAfternoon1.setStyleSheet(self.btnStyle)
            self.btnEvening1.setStyleSheet(self.btnStyle)
            self.btnMidNight1.setStyleSheet(self.btnStyle)
            self.btnLateNight1.setStyleSheet(self.btnStyleSelected)
            self.btnEarlyMorning1.setStyleSheet(self.btnStyle)
            self.SetSelectedData(4)

        elif type == 6:
            self.btnMorning1.setStyleSheet(self.btnStyle)
            self.btnAfternoon1.setStyleSheet(self.btnStyle)
            self.btnEvening1.setStyleSheet(self.btnStyle)
            self.btnMidNight1.setStyleSheet(self.btnStyle)
            self.btnLateNight1.setStyleSheet(self.btnStyle)
            self.btnEarlyMorning1.setStyleSheet(self.btnStyleSelected)
            self.SetSelectedData(5)

    def SetSelectedData(self,type):

        # Morning
        if type == 0:
            cursor = myDb.getSpecificSlotTimings(MyConst.MORNING_KEY,None)
            tempRow = myDb.getSpecificSlotTimings(MyConst.EARLY_MORNING_KEY,MyConst.AFTER_FOOD_KEY)
            tempRow2 = myDb.getSpecificSlotTimings(MyConst.NOON_KEY, MyConst.BEFORE_FOOD_KEY)
        elif type == 1:
            cursor = myDb.getSpecificSlotTimings(MyConst.NOON_KEY, None)
            tempRow = myDb.getSpecificSlotTimings(MyConst.MORNING_KEY,MyConst.AFTER_FOOD_KEY)
            tempRow2 = myDb.getSpecificSlotTimings(MyConst.EVENING_KEY, MyConst.BEFORE_FOOD_KEY)
        elif type == 2:
            cursor = myDb.getSpecificSlotTimings(MyConst.EVENING_KEY, None)
            tempRow = myDb.getSpecificSlotTimings(MyConst.NOON_KEY,MyConst.AFTER_FOOD_KEY)
            tempRow2 = myDb.getSpecificSlotTimings(MyConst.LATE_NIGHT_KEY, MyConst.BEFORE_FOOD_KEY)
        elif type == 3:
            cursor = myDb.getSpecificSlotTimings(MyConst.MID_NIGHT_KEY, None)
            tempRow = myDb.getSpecificSlotTimings(MyConst.LATE_NIGHT_KEY,MyConst.AFTER_FOOD_KEY)
            tempRow2 = myDb.getSpecificSlotTimings(MyConst.EARLY_MORNING_KEY, MyConst.BEFORE_FOOD_KEY)
        elif type == 4:
            cursor = myDb.getSpecificSlotTimings(MyConst.LATE_NIGHT_KEY, None)
            tempRow = myDb.getSpecificSlotTimings(MyConst.EVENING_KEY,MyConst.AFTER_FOOD_KEY)
            tempRow2 = myDb.getSpecificSlotTimings(MyConst.MID_NIGHT_KEY, MyConst.BEFORE_FOOD_KEY)
        elif type == 5:
            cursor = myDb.getSpecificSlotTimings(MyConst.EARLY_MORNING_KEY, None)
            tempRow = myDb.getSpecificSlotTimings(MyConst.MID_NIGHT_KEY,MyConst.AFTER_FOOD_KEY)
            tempRow2 = myDb.getSpecificSlotTimings(MyConst.MORNING_KEY, MyConst.BEFORE_FOOD_KEY)


        lowerTimings = Util.addSubMinutes(Util.get12HourFormatTime(str(tempRow[3]),False),30,True)
        # print(Util.addSubMinutes(lowerTimings,30,True))
        upperTimings = Util.addSubMinutes(Util.get12HourFormatTime(str(tempRow2[3]),False),30,False)
        # print(Util.addSubMinutes(upperTimings,30,False))
        self.lowerTimeLimit = (lowerTimings[0]*60) + lowerTimings[1]
        self.upperTimeLimit = (upperTimings[0]*60) + upperTimings[1]


        print(str(self.lowerTimeLimit))
        print(str(self.upperTimeLimit))

        for row in cursor:
            temp = tuple(row)
            time = str(temp[3]).split(":")

            hour = int(time[0])
            min = int(time[1])
            isPm = False
            if hour>=12:
                isPm = True
                if hour>12:
                    hour = hour-12
            if temp[2]==MyConst.BEFORE_FOOD_KEY:
                self.bfHour = hour
                self.bfMin = min
                self.lblBfHour.setText(str(self.bfHour))
                self.lblBfMin.setText(str(self.bfMin))
                self.isBfPm = isPm
                if self.isBfPm:
                    self.lblBfAmPm.setText("pm")
                else:
                    self.lblBfAmPm.setText("am")
            else:
                self.afHour = hour
                self.afMin = min
                self.lblAfHour.setText(str(self.afHour))
                self.lblAfMin.setText(str(self.afMin))
                self.isAfPm = isPm
                if self.isAfPm:
                    self.lblAfAmPm.setText("pm")
                else:
                    self.lblAfAmPm.setText("am")

if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = ChangeTime(QMainWindow)

    window.show()

# start the app
    sys.exit(App.exec())

