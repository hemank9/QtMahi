from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Utility.MahiUtility as Util

import sys



class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")



        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('..\Resources\\notif1.png'))
        self.label.setGeometry(0, 0, 680, 685)

        self.firstLabel = QLabel("Its time for your medicines",self)
        self.firstLabel.setStyleSheet("color: #00A0B5; font-size:30px")
        self.firstLabel.setGeometry(728, 303, 402, 45)

        self.timeLabel = QLabel(self)
        self.timeLabel.setGeometry(728, 351, 264, 30)
        self.timeLabel.setText("4:30 pm | After Lunch Dose")
        self.timeLabel.setStyleSheet("color: #707070; font-size:20px ")

        self.continueButton = QPushButton("Continue", self)
        self.continueButton.setGeometry(720, 410, 120, 40)
        self.continueButton.setStyleSheet("background-color: #00A0B5; border-radius: 8px; color : white; font-size: 20px")
        self.continueButton.setGraphicsEffect(Util.getNeuShadow(0))
        self.continueButton.clicked.connect(self.goToNotif2)

        self.snoozeButton = QPushButton("Snooze", self)
        self.snoozeButton.setGeometry(864, 422, 58, 24)
        self.snoozeButton.setStyleSheet("background-color: #0000A0B5; color: #707070; font-size: 18px")

        cancelButton = QPushButton(self)
        cancelButton.setGeometry(1164, 24, 32, 32)
        cancelButton.setStyleSheet("background-color: #0000a0b5")
        cancelButton.setIcon(QtGui.QIcon('../Resources/cancel.png'))
        cancelButton.setIconSize(QtCore.QSize(32, 32))
        cancelButton.clicked.connect(self.close)

        #NOTIF 2



        self.label1 = QLabel(self)
        self.label1.setPixmap(QPixmap('..\Resources\\notif2.png'))
        self.label1.setGeometry(0, 0, 680, 685)

        self.YourMedsLabel = QLabel("Your Medicines", self)
        self.YourMedsLabel.setStyleSheet("color: #00A0B5; font-size:30px")
        self.YourMedsLabel.setGeometry(720, 100, 232, 45)

        self.infoStep1Label = QLabel(
            "your pills have been placed into the pillbox,    click on eject to remove it from the machine", self)
        self.infoStep1Label.setStyleSheet("color: #707070; font-size:16px")
        self.infoStep1Label.setWordWrap(True)
        self.infoStep1Label.setGeometry(720, 152, 353, 48)

        self.doseBkg1List = []
        self.doseBkg2List = []
        self.doseNameList = []
        self.doseImageList = []
        self.doseVolList = []

        self.startX = 720
        self.starty = 220
        self.startw = 100

        yCount = -1

        for i in range(12):
            xVar = i%4
            if xVar == 0:
                yCount=yCount+1

            medLabel11 = QLabel(self)
            medLabel11.setGeometry(self.startX + (xVar*115), self.starty + (yCount*115), self.startw, self.startw)
            medLabel11.setStyleSheet("border-radius:14; background-color: #ECEDF1")
            medLabel11.setGraphicsEffect(Util.getNeuShadow(1))

            medLabel1 = QLabel(self)
            medLabel1.setGeometry(self.startX + (xVar*115), self.starty + (yCount*115), self.startw, self.startw)
            medLabel1.setStyleSheet("border-radius:14; background-color: #ECEDF1")
            medLabel1.setGraphicsEffect(Util.getNeuShadow(0))
            self.doseBkg1List.append(medLabel1)
            self.doseBkg2List.append(medLabel11)

            doseImage = QLabel(self)
            doseImage.setGeometry(self.startX + 36  + (xVar*115), self.starty + 9+ (yCount*115), 32, 32)
            doseImage.setPixmap(QPixmap('..\Resources\meds.png'))
            self.doseImageList.append(doseImage)

            doseName = QLabel(self)
            doseName.setGeometry(self.startX + 13  + (xVar*115), self.starty + 48+ (yCount*115), 76, 24)
            doseName.setStyleSheet("color: #00A0B5; font-size: 12px; font: bold")
            doseName.setText("DOLO- 650")
            doseName.setWordWrap(True)
            doseName.setAlignment(Qt.AlignCenter)
            self.doseNameList.append(doseName)

            doseVol = QLabel(self)
            doseVol.setGeometry(self.startX + 6  + (xVar*115), self.starty + 72+ (yCount*115), 89, 18)
            doseVol.setStyleSheet("color:#707070; font-size: 10px; font: bold")
            doseVol.setText("2 capsules")
            doseVol.setAlignment(Qt.AlignCenter)
            self.doseVolList.append(doseVol)


        self.ejectButton = QPushButton("Eject", self)
        self.ejectButton.setGeometry(720, 586, 120, 40)
        self.ejectButton.setStyleSheet("background-color: #00A0B5; color: white; border-radius: 8; font-size:20px")
        self.ejectButton.setGraphicsEffect(Util.getNeuShadow(0))
        self.ejectButton.clicked.connect(self.goToNotif3)

        #NOTIF 3

        self.label3 = QLabel(self)
        self.label3.setPixmap(QPixmap('..\Resources\\notif3.png'))
        self.label3.setGeometry(0, 0, 680, 685)

        self.PlaceLabel = QLabel("Place the Pill Box", self)
        self.PlaceLabel.setStyleSheet("color: #00A0B5; font-size:30px")
        self.PlaceLabel.setGeometry(720, 250, 247, 45)

        self.infoStep2Label = QLabel("Put the Pill Box in the machine as shown in the image on the left ", self)
        self.infoStep2Label.setStyleSheet("color: #707070; font-size:16px")
        self.infoStep2Label.setWordWrap(True)
        self.infoStep2Label.setGeometry(720, 320, 331, 60)

        self.openButton = QPushButton("Open", self)
        self.openButton.setGeometry(720, 413, 120, 40)
        self.openButton.setStyleSheet("background-color: #00A0B5; color: white; border-radius: 8; font-size:20px")
        self.openButton.setGraphicsEffect(Util.getNeuShadow(0))

        self.setLayout(1, True)

    def goToNotif2(self):
        print("pressed")
        # self.x = noti2.Notif2()
        # self.x.show()
        self.setLayout(2, True)

    def goToNotif3(self):
        self.setLayout(3, True)


    def setLayout(self, type, show):
        if type==1:
            if show:
                self.snoozeButton.show()
                self.continueButton.show()
                self.firstLabel.show()
                self.timeLabel.show()
                self.label.show()
                self.setLayout(2, False)
                self.setLayout(3, False)
            else:
                self.snoozeButton.hide()
                self.continueButton.hide()
                self.firstLabel.hide()
                self.timeLabel.hide()
                self.label.hide()
        elif type == 2:
            if show:
                self.ejectButton.show()
                self.YourMedsLabel.show()
                self.infoStep1Label.show()
                for i in range(len(self.doseImageList)):
                    self.doseBkg1List[i].show()
                    self.doseBkg2List[i].show()
                    self.doseNameList[i].show()
                    self.doseVolList[i].show()
                    self.doseImageList[i].show()

                self.label1.show()
                self.setLayout(1, False)
                self.setLayout(3, False)
            else:
                self.ejectButton.hide()
                self.YourMedsLabel.hide()
                self.infoStep1Label.hide()
                for i in range(len(self.doseImageList)):
                    self.doseBkg1List[i].hide()
                    self.doseBkg2List[i].hide()
                    self.doseNameList[i].hide()
                    self.doseVolList[i].hide()
                    self.doseImageList[i].hide()
                self.label1.hide()
                print("helllo")

        elif type == 3:
            if show:
                self.label3.show()
                self.PlaceLabel.show()
                self.infoStep2Label.show()
                self.openButton.show()
                self.setLayout(1, False)
                self.setLayout(2, False)
            else:
                self.label3.hide()
                self.PlaceLabel.hide()
                self.infoStep2Label.hide()
                self.openButton.hide()





App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec())
