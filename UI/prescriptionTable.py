import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
import Utility.MahiUtility as Util
from PyQt5.QtCore import *

class PrescriptionTable(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../Resources/yellow.png'))
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
        btn_back.setIcon(QtGui.QIcon('../Resources/Group 49.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)

        btnRefill = QPushButton("Refill Now", self)
        btnRefill.setGeometry(889, 56, 301, 59)
        btnRefill.setStyleSheet("background-color : #EE498D; border-radius : 6; font:semi-bold; fond-size: 24")
        btnRefill.setGraphicsEffect(Util.getNeuShadow(0))
        # btnRefill.clicked.connect()

        lblPres = QLabel(self)
        lblPres.setGeometry(247, 54, 612, 64)
        lblPres.setStyleSheet("border-radius : 10;")
        lblPres.setGraphicsEffect(Util.getNeuShadow(0))

        lblPres1 = QLabel(self)
        lblPres1.setGeometry(247, 54, 612, 64)
        lblPres1.setStyleSheet("border-radius : 10;")
        lblPres1.setGraphicsEffect(Util.getNeuShadow(1))

        lblDate = QLabel(self)
        lblDate.setGeometry(486, 69, 138, 35)
        lblDate.setStyleSheet("font : bold; font-size : 26")
        lblDate.setText("07.04.2021")

        lblDayTime = QLabel(self)
        lblDayTime.setGeometry(666, 69, 170, 35)
        lblDayTime.setStyleSheet("font : bold; font-size : 26")
        lblDayTime.setText("07.04.2021")

        btnUpdatedPresc = QPushButton(self)
        btnUpdatedPresc.setGeometry(260, 59, 191, 52)
        btnUpdatedPresc.setStyleSheet("background-color : #F0F0F3; border-radius: 10")
        btnUpdatedPresc.setIcon(QtGui.QIcon('../Resources/Group 95.png'))
        btnUpdatedPresc.setIconSize(QtCore.QSize(180, 110))


if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = PrescriptionTable()

    window.show()

# start the app
    sys.exit(App.exec())



