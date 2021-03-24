import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import colors as Colors

class NeuButton(QWidget):
    def __init__(self, parent=None):

        super(NeuButton, self).__init__(parent)

        btnUpComnin1 = QPushButton("UPCOMING APPOINTMENT", self)
        btnUpComnin1.setGeometry(160, 57, 283, 52)
        btnUpComnin1.setFont(QFont('Arial', 10))
        btnUpComnin1.setStyleSheet("border-radius : 10; background-color : #F0F03; color : #006CB5; font : bold ")
        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(15)
        shadow1.setColor(Qt.lightGray)
        btnUpComnin1.setGraphicsEffect(shadow1)

        btnUpComnin2 = QPushButton("UPCOMING APPOINTMENT", self)
        btnUpComnin2.setGeometry(160, 57, 283, 52)
        btnUpComnin2.setFont(QFont('Arial', 10))
        btnUpComnin2.setStyleSheet("border-radius : 10; background-color : #F0F03; color : #006CB5; font : bold ")
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(15)
        shadow2.setColor(Qt.white)
        btnUpComnin2.setGraphicsEffect(shadow2)
        shadow2.setXOffset(-5)
        shadow2.setYOffset(-5)