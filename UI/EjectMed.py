import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Utility.MahiUtility as Util

class EjectMed(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Refill")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        # self.label = QLabel(self)
        # self.label.setPixmap(QPixmap('../Resources/Group 48.png'))
        # self.label.setGeometry(0, 0, 1220, 685)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        btn_back = QPushButton("X", self)
        btn_back.setGeometry(714, 207, 23, 23)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3; color: #C0C0C0")
        # btn_back.clicked.connect(self.close)

        self.ejectLbl = QLabel(self)
        self.ejectLbl.setGeometry(21, 23, 205, 33)
        self.ejectLbl.setPixmap(QPixmap('../Resources/ejectMedScreen.png'))

        massEjectBtn1 = QPushButton("Mass Ejection", self)
        massEjectBtn1.setGeometry(933, 24, 175, 41)
        massEjectBtn1.setStyleSheet("background-color: #F0F0F3; color: #00A0B5; border-radius: 7")
        massEjectBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        massEjectBtn = QPushButton("Mass Ejection", self)
        massEjectBtn.setGeometry(933, 24, 175, 41)
        massEjectBtn.setStyleSheet("background-color: #F0F0F3; color: #00A0B5; border-radius: 7")
        massEjectBtn.setGraphicsEffect(Util.getNeuShadow(1))

        EjectNow1 = QPushButton(self)
        EjectNow1.setGeometry(787, 151, 123, 41)
        EjectNow1.setStyleSheet("background-color: #F0F0F3; color: #00A0B5; border-radius: 7")
        EjectNow1.setGraphicsEffect(Util.getNeuShadow(0))
        EjectNow = QPushButton("Eject", self)
        EjectNow.setGeometry(787, 151, 123, 41)
        EjectNow.setStyleSheet("background-color: #F0F0F3; color: #00A0B5; border-radius: 7")
        EjectNow.setGraphicsEffect(Util.getNeuShadow(1))



        self.line = QLabel(self)
        self.line.setGeometry(0, 205, 2, 1220)
        self.line.setPixmap(QPixmap('../Resources/line.png'))

        self.MedLbl = QLabel(self)
        self.MedLbl.setText("Medicine Time Table (15/08/2021)")
        self.line.setGeometry(230, 159, 384, 35)


if __name__ == '__main__':

    App = QApplication(sys.argv)

    # create the instance of our Window
    window = EjectMed()

    window.show()

    # start the app
    sys.exit(App.exec())