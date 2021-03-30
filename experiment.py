import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Utility.MahiUtility as MahiUtil
import Custom.AppointmentListItem as appoi
import API.api_calls as MyApis
import json
class LoadingGif(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.lblAnimation = QLabel(self)
        self.lblAnimation.setGeometry(0,0,200,200)
        self.movie = QMovie('Resources\loading.gif')
        self.lblAnimation.setMovie(self.movie)

        # timer = QTimer(self)
        # self.startAnimation()
        # timer.singleShot(3000,self.stopAnimation)
        # self.show()
    # Start Animation
    def startAnimation(self):
        self.show()
        self.movie.start()
    # Stop Animation(According to need)
    def stopAnimation(self):
        self.movie.stop()
        self.close()

if __name__ == '__main__':
    App = QApplication(sys.argv)
    # create the instance of our Window
    window = LoadingGif()
    window.startAnimation()
    # start the app
    sys.exit(App.exec())