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

class LoadingGif(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(510, 242, 200, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)

        self.lblAnimation = QLabel("Please Wait.....",self)
        self.lblAnimation.setGeometry(0, 0, 200, 200)
        # self.movie = QMovie('Resources\loading.gif')
        # self.lblAnimation.setMovie(self.movie)


    def startAnimation(self):
        # self.movie.start()
        self.show()

    def stopAnimation(self):
        # self.movie.stop()
        self.close()



