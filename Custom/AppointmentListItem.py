
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import colors as Colors

class AppointmentListItem(QWidget):
    def __init__(self, parent=None):

        super(AppointmentListItem, self).__init__(parent)


        style = "background-color: #F0F0F3; border-radius : 15; margin-top : 10; margin-bottom : 10; margin-left : 10; margin-right : 10; "
        frame1 = QFrame(self)
        # frame1.setGraphicsEffect(shadow)
        frame1.setFixedWidth(1151)
        frame1.setFixedHeight(120)
        # frame1.setContentsMargins(10, 10, 10, 10)
        frame1.setStyleSheet(style)


        frame2 = QFrame(self)
        # frame1.setGraphicsEffect(shadow)
        frame2.setFixedWidth(1151)
        frame2.setFixedHeight(120)
        # frame2.setContentsMargins(10, 10, 10, 10)
        frame2.setStyleSheet(style)
        # frame1.setFrameStyle(QFrame.Raised)
        # frame1.setGeometry(567, 459, 200, 200)
        # frame1.setFrameStyle(QFrame.Panel |
        #                     QFrame.Plain)
        # frame1.setLayout(self.allQHBoxLayout)
        # frame1.setFrameShape(QFrame.StyledPanel)
        self.textQVBoxLayout = QVBoxLayout()
        self.textUpQLabel = QLabel()
        self.textUpQLabel.setFixedWidth(400)
        self.textDownQLabel = QLabel()
        self.textDownQLabel.setWordWrap(True)

        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout = QHBoxLayout()
        self.iconQLabel = QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)

        # setStyleSheet
        self.textUpQLabel.setStyleSheet("font: bold; color:" + Colors.DarkBlue+"; background-color:#F0F0F3")
        self.textDownQLabel.setStyleSheet("color:" + Colors.Grey8+"; background-color:#F0F0F3")

        self.lblAddress = QLabel()
        self.lblAddress.setStyleSheet("color: #EE488D; overflow: hidden; font: bold; text-overflow: ellipsis; display: -webkit-box; "
                                                               "-webkit-line-clamp: 2; -webkit-box-orient: vertical;"
                                                               +"; background-color:#F0F0F3")
        # self.lblAddress.setGeometry(589, 142, 276, 69)
        self.lblAddress.setWordWrap(True)
        # self.lblAddress.setMinimumHeight(99)
        self.lblAddress.setMinimumWidth(376)
        self.allQHBoxLayout.addWidget(self.lblAddress, 0)
        # self.allQHBoxLayout.setGeometry(QRect(589, 142, 276, 69))

        self.btnSelectTime = QPushButton("", self)
        # self.btnSelectTime.setGeometry(996, 138, 65, 65)
        self.btnSelectTime.setStyleSheet("background-color : #F0F0F3; border-radius : 10")
        self.btnSelectTime.setIcon(QtGui.QIcon('Resources\Group 88.png'))
        self.btnSelectTime.setIconSize(QtCore.QSize(70, 70))
        self.allQHBoxLayout.addWidget(self.btnSelectTime, 1)



        self.btnLocation = QPushButton(self)
        self.btnLocation.setStyleSheet("background-color : #F0F0F3; border-radius : 10")
        self.btnLocation.setIcon(QtGui.QIcon('Resources\Group 88.png'))
        self.btnLocation.setIconSize(QtCore.QSize(70, 70))
        self.allQHBoxLayout.addWidget(self.btnLocation, 1)
        # self.allQHBoxLayout.setContentsMargins(5, 10, 30, 10)


        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(15)
        shadow1.setColor(Qt.lightGray)
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(15)
        shadow2.setColor(Qt.white)
        frame1.setGraphicsEffect(shadow1)
        frame2.setGraphicsEffect(shadow2)
        shadow2.setXOffset(-5)
        shadow2.setYOffset(-5)
        self.allQHBoxLayout.setParent(frame2)



    imagePath = "Resources\emorning.png"

    def setTextUp(self, text):
        self.textUpQLabel.setText(text)

    def setTextDown(self, text):
        self.textDownQLabel.setText(text)

    def setAddress(self, text):
        # imagePath = "Resources\emorning.png"
        self.lblAddress.setText(text)