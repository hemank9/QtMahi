
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import colors as Colors

class FileListItem(QWidget):
    def __init__(self, parent=None):

        super(FileListItem, self).__init__(parent)


        style = "background-color: #F0F0F3; border-radius : 15; margin-top : 20; margin-bottom : 20; margin-left : 10; margin-right : 10; "

        fontObj = QFont('Arial',10)
        frame1 = QFrame(self)
        # frame1.setGraphicsEffect(shadow)
        frame1.setFixedWidth(1110)
        frame1.setFixedHeight(120)
        # frame1.setContentsMargins(10, 10, 10, 10)
        frame1.setStyleSheet(style)


        self.allQHBoxLayout = QHBoxLayout()
        frame2 = QFrame(self)
        # frame1.setGraphicsEffect(shadow)
        frame2.setFixedWidth(1110)
        frame2.setFixedHeight(120)
        frame2.setStyleSheet(style)
        self.lblFileName = QLabel()
        self.lblFileName.setFixedHeight(62)
        self.lblFileName.setStyleSheet("background-color: #F0F0F3;margin-left:20px;color:#006CB5; font:bold; font-size:25px;")
        self.lblDateDoctor = QLabel()
        self.lblDateDoctor.setWordWrap(True)
        self.lblDateDoctor.setStyleSheet("background-color: #F0F0F3;color:#006CB5; font-size:18px; margin-right:20;")

        self.lblExtension = QLabel()
        self.lblExtension.setWordWrap(True)
        self.lblExtension.setAlignment(Qt.AlignRight)
        self.lblExtension.setFixedWidth(200)
        self.lblExtension.setStyleSheet("background-color: #F0F0F3;color:#006CB5; font-size:18px; margin-right:20;")
        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.lblExtension)
        self.vBox.setAlignment(Qt.AlignVCenter)

        self.allQHBoxLayout.addWidget(self.lblFileName, 1)
        self.allQHBoxLayout.addWidget(self.lblDateDoctor, 1)
        self.allQHBoxLayout.addLayout(self.vBox)
        self.setLayout(self.allQHBoxLayout)
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

    def setTextFileName(self, text):
        self.lblFileName.setText(text)

    def setTextDateDoctor(self, text):
        self.lblDateDoctor.setText(text)

    def setExtension(self, text):
        self.lblExtension.setText(text)
