import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
import Utility.MahiUtility as Util
from PyQt5.QtCore import *
import UI.extraDosage as ed

class ExtraDose(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prescription")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        # self.label = QLabel(self)
        # self.label.setStyleSheet("background-color:#FEC32E")
        # self.label.setGeometry(0, 0, 1220, 39)

        self.UiComponents()
    #
    #     # showing all the widgets
        self.show()
    #
    def UiComponents(self):

        btn_back = QPushButton("", self)
        btn_back.setGeometry(16, 59, 112, 41)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('../Resources/backButton.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)

        self.titleBkg1List = []
        self.titleBkg2List = []
        self.medList = []
        self.medNameList = []
        self.buttonList = []

        self.startx = 25
        self.starty = 128

        for i in range(3):

            tileLabel1 = QLabel(self)
            tileLabel1.setGeometry(self.startx , self.starty + (i*75), 1159, 54)
            tileLabel1.setStyleSheet("border-radius: 7; background-color: #F0F0F3")
            tileLabel1.setGraphicsEffect(Util.getNeuShadow(0))
            tileLabel = QLabel(self)
            tileLabel.setGeometry(self.startx, self.starty + (i*75), 1159, 54)
            tileLabel.setStyleSheet("border-radius: 7; background-color: #F0F0F3")
            tileLabel.setGraphicsEffect(Util.getNeuShadow(1))
            self.titleBkg1List.append(tileLabel)
            self.titleBkg1List.append(tileLabel1)


            medLabel = QLabel("Medicine", self)
            medLabel.setGeometry(self.startx + 39, self.starty + (i*75) + 12, 84, 29)
            medLabel.setStyleSheet("backgorund-color: #00F0F0F3; font-size: 21px")
            self.medList.append(medLabel)

            medNameLabel = QLabel("DOLO-650", self)
            medNameLabel.setGeometry(self.startx + 157, self.starty + (i*75)  + 12, 150, 29)
            medNameLabel.setStyleSheet("backgorund-color: #00F0F0F3; font-size: 21px")
            self.medNameList.append(medNameLabel)

            tileButton = QPushButton(self)
            tileButton.setGeometry(self.startx, self.starty + (i*75) , 1159, 54)
            tileButton.setStyleSheet("background-color: #00F0F0F3; border-radius: 7")
            tileButton.clicked.connect(self.tileButtonClicked)
            self.buttonList.append(tileButton)


        self.popLabel = QLabel(self)
        self.popLabel.setGeometry(365, 200, 491, 262)
        self.popLabel.setStyleSheet("background-color: #F0F0F3; border-radius: 15; ")
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(30)
        shadow2.setColor(Qt.lightGray)
        shadow2.setXOffset(0)
        shadow2.setYOffset(0)
        self.popLabel.setGraphicsEffect(shadow2)

        self.extraDosePopLabel = QLabel("Extra Dosage",self)
        self.extraDosePopLabel.setGeometry(400, 211, 184, 41)
        self.extraDosePopLabel.setStyleSheet("color: #00A0B5; font-size:25px")

        self.mediLabel = QLabel("Medicine", self)
        self.mediLabel.setGeometry(400, 261, 94, 29)
        self.mediLabel.setStyleSheet("font-size: 21px")

        self.mediNameLabel = QLabel("DOLO SYRUP 60ML 120 ", self)
        self.mediNameLabel.setGeometry(554, 261, 266, 29)
        # self.mediNameLabel.setWordWrap(True)
        self.mediNameLabel.setStyleSheet("font-size: 21px")

        self.numLabel = QLabel("No. of doses", self)
        self.numLabel.setGeometry(400, 299, 128, 29)
        self.numLabel.setStyleSheet("font-size: 21px")

        self.numNoLabel = QLabel("12 Capsules", self)
        self.numNoLabel.setGeometry(554, 299, 123, 29)
        self.numNoLabel.setStyleSheet("font-size: 21px")

        self.timeLabel = QLabel("Time", self)
        self.timeLabel.setGeometry(400, 335, 113, 29)
        self.timeLabel.setStyleSheet("font-size: 21px")

        self.actualTimeLabel = QLabel("12 pm", self)
        self.actualTimeLabel.setGeometry(554, 335, 103, 29)
        self.actualTimeLabel.setStyleSheet("font-size: 21px")

        self.whenLabel = QLabel("When", self)
        self.whenLabel.setGeometry(400, 371, 123, 29)
        self.whenLabel.setStyleSheet("font-size: 21px")

        self.monthLabel = QLabel("12 months", self)
        self.monthLabel.setGeometry(554, 371, 113, 29)
        self.monthLabel.setStyleSheet("font-size: 21px")

        self.startDateLabel = QLabel("Start Date", self)
        self.startDateLabel.setGeometry(400, 407, 113, 29)
        self.startDateLabel.setStyleSheet("font-size: 21px")

        self.dateLabel = QLabel("12/07/2021", self)
        self.dateLabel.setGeometry(554, 407, 103, 29)
        self.dateLabel.setStyleSheet("font-size: 21px")

        self.backButton = QPushButton(self)
        self.backButton.setGeometry(737, 339, 83, 43)
        self.backButton.setStyleSheet("border-radius:7; background-color:#00A0B5")
        self.backButton.setIcon(QtGui.QIcon('../Resources/backk.png'))
        self.backButton.setIconSize(QtCore.QSize(83, 43))
        self.backButton.clicked.connect(self.popClose)

        self.editButton = QPushButton("Edit",self)
        self.editButton.setGeometry(737, 394, 83, 43)
        self.editButton.setStyleSheet("border-radius:7; background-color:#F0F0F3; color: #00A0B5; font-size: 25px")
        self.editButton.setGraphicsEffect(Util.getNeuShadow(0))
        self.editButton.clicked.connect(self.editClicked)

        self.editButton.hide()
        self.backButton.hide()
        self.dateLabel.hide()
        self.startDateLabel.hide()
        self.monthLabel.hide()
        self.whenLabel.hide()
        self.actualTimeLabel.hide()
        self.timeLabel.hide()
        self.mediNameLabel.hide()
        self.mediLabel.hide()
        self.numLabel.hide()
        self.numNoLabel.hide()
        self.popLabel.hide()
        self.extraDosePopLabel.hide()

    def popClose(self):
        self.editButton.hide()
        self.backButton.hide()
        self.dateLabel.hide()
        self.startDateLabel.hide()
        self.monthLabel.hide()
        self.whenLabel.hide()
        self.actualTimeLabel.hide()
        self.timeLabel.hide()
        self.mediNameLabel.hide()
        self.mediLabel.hide()
        self.numLabel.hide()
        self.numNoLabel.hide()
        self.popLabel.hide()
        self.extraDosePopLabel.hide()

    def tileButtonClicked(self):
        self.editButton.show()
        self.backButton.show()
        self.dateLabel.show()
        self.startDateLabel.show()
        self.monthLabel.show()
        self.whenLabel.show()
        self.actualTimeLabel.show()
        self.timeLabel.show()
        self.mediNameLabel.show()
        self.mediLabel.show()
        self.numLabel.show()
        self.numNoLabel.show()
        self.popLabel.show()
        self.extraDosePopLabel.show()

    def editClicked(self):
        self.x = ed.ExtraDosage()
        self.x.show()

#
# if __name__ == '__main__':
#     App = QApplication(sys.argv)
#
#     # create the instance of our Window
#     window = ExtraDose()
#
#     window.show()
#
# # start the app
#     sys.exit(App.exec())



