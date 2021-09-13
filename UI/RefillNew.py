import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import UI.prescriptionTable as preTable
import Utility.MahiUtility as Util


class RefillNew(QMainWindow):
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

        self.btnStyle = "border-radius : 15; background-color: #F0F03; color : #00A0B5;font:bold;font-size:16px"
        self.btnStyleSelected = "border-radius : 15; background-color: #BCE6EC; color : #00A0B5;font:bold;font-size:16px"

        btn_back = QPushButton("", self)
        btn_back.setGeometry(23, 21, 112, 41)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('../Resources/back.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)

        btnOnGoingPresc1 = QPushButton("", self)
        btnOnGoingPresc1.setGeometry(207, 20, 289, 41)
        btnOnGoingPresc1.setStyleSheet(self.btnStyleSelected)
        btnOnGoingPresc1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnOnGoingPresc = QPushButton("On Going Prescription", self)
        self.btnOnGoingPresc.setGeometry(207, 20, 289, 41)
        self.btnOnGoingPresc.setStyleSheet(self.btnStyleSelected)
        self.btnOnGoingPresc.setGraphicsEffect(Util.getNeuShadow(1))

        btnNewPresc1 = QPushButton("", self)
        btnNewPresc1.setGeometry(509, 20, 289, 41)
        btnNewPresc1.setStyleSheet(self.btnStyle)
        btnNewPresc1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnNewPresc = QPushButton("New Prescription", self)
        self.btnNewPresc.setGeometry(509, 20, 289, 41)
        self.btnNewPresc.setStyleSheet(self.btnStyle)
        self.btnNewPresc.setGraphicsEffect(Util.getNeuShadow(1))

        btnRefill1 = QPushButton("", self)
        btnRefill1.setGeometry(811, 20, 154, 41)
        btnRefill1.setStyleSheet(self.btnStyle)
        btnRefill1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnRefill = QPushButton("New Prescription", self)
        self.btnRefill.setGeometry(811, 20, 154, 41)
        self.btnRefill.setStyleSheet(self.btnStyle)
        self.btnRefill.setGraphicsEffect(Util.getNeuShadow(1))

        self.t = preTable.PrescriptionTable()
        self.t.show()




if __name__ == '__main__':

    App = QApplication(sys.argv)

    # create the instance of our Window
    window = RefillNew()

    # start the app
    sys.exit(App.exec())
