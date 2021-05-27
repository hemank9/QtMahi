from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class ExtraDosage(QWidget):                           # <===
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setStyleSheet("background-color:#FEC32E")
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
