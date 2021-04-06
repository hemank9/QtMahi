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

        btn_lnight = QPushButton("", self)
        btn_lnight.setGeometry(826, 100, 320, 320)
        btn_lnight.setStyleSheet("border-radius : 10; background-color: #0000")
        btn_lnight.setIcon(QtGui.QIcon('../Resources/lnight.png'))
        btn_lnight.setIconSize(QtCore.QSize(330, 330))
        btn_lnight.clicked.connect(self.close)

        btn_mnight = QPushButton("", self)
        btn_mnight.setGeometry(457, 100, 320, 320)
        btn_mnight.setStyleSheet("border-radius : 10; background-color: #0000")
        btn_mnight.setIcon(QtGui.QIcon('../Resources/mnight.png'))
        btn_mnight.setIconSize(QtCore.QSize(330, 330))
        btn_mnight.clicked.connect(self.close)

        btn_emorning = QPushButton("", self)
        btn_emorning.setGeometry(88, 100, 320, 320)
        btn_emorning.setStyleSheet("border-radius : 10; background-color: #0000")
        btn_emorning.setIcon(QtGui.QIcon('../Resources/emorning.png'))
        btn_emorning.setIconSize(QtCore.QSize(330, 330))
        btn_emorning.clicked.connect(self.close)

        frame = QFrame(self)
        frame.setFrameShape(QFrame.WinPanel)
        frame.setGeometry(115, 494, 270, 171)
        frame.setLineWidth(1)
        # frame.midLineWidth(3)
        frame.setStyleSheet("border-radius : 20; background-color: white ")


