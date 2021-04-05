import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import colors as Colors

class FileList(QMainWindow):
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
        # self.show()
    #
    def UiComponents(self):

        self.btnAngio = QPushButton("Angiography", self)
        self.btnAngio.setGeometry(45, 128, 170, 50)
        self.btnAngio.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color:#006CB5; font:bold; font-size:22px; text-align: center;")

        self.btnXray = QPushButton("X-Ray", self)
        self.btnXray.setGeometry(236, 128, 170, 50)
        self.btnXray.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color:#006CB5; font:bold; font-size:22px; text-align: center;")

        self.btnEcg = QPushButton("ECG", self)
        self.btnEcg.setGeometry(427, 128, 170, 50)
        self.btnEcg.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color:#006CB5; font:bold; font-size:22px; text-align: center;")

        self.btnEcho = QPushButton("Eecho", self)
        self.btnEcho.setGeometry(618, 128, 170, 50)
        self.btnEcho.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color:#006CB5; font:bold; font-size:22px; text-align: center;")

        self.btnMri = QPushButton("MRI", self)
        self.btnMri.setGeometry(809, 128, 170, 50)
        self.btnMri.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color:#006CB5; font:bold; font-size:22px; text-align: center;")

        self.btnBloodTest = QPushButton("Blood Test", self)
        self.btnBloodTest.setGeometry(1000, 128, 170, 50)
        self.btnBloodTest.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color:#006CB5; font:bold; font-size:22px; text-align: center;")

        self.btnBloodTest = QPushButton("Ascending", self)
        self.btnBloodTest.setGeometry(875, 58, 307, 43)
        self.btnBloodTest.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color:#006CB5; font:bold; font-size:22px; text-align: center;")

        btn_back = QPushButton("", self)
        btn_back.setGeometry(41, 55, 135, 50)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('..\Resources\Group 87.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)

