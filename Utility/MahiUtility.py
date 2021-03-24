import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def printParams(params):
    for i,k in params.items():
        print(i+":"+k)

def getNeuShadow(type):
    shadow2 = QGraphicsDropShadowEffect()
    shadow2.setBlurRadius(15)
    if type == 0:
        shadow2.setColor(Qt.lightGray)
        shadow2.setXOffset(5)
        shadow2.setYOffset(5)
    else :
        shadow2.setColor(Qt.white)
        shadow2.setXOffset(-5)
        shadow2.setYOffset(-5)
    return shadow2