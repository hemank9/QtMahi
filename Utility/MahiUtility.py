import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import socket
from datetime import datetime

def printParams(params):
    for i,k in params.items():
        print(i+":"+k)

def getNeuShadow(type):
    shadow2 = QGraphicsDropShadowEffect()
    shadow2.setBlurRadius(15)
    if type == 0:
        shadow2.setColor(Qt.lightGray)
        shadow2.setXOffset(3)
        shadow2.setYOffset(3)
    else :
        shadow2.setColor(Qt.white)
        shadow2.setXOffset(-5)
        shadow2.setYOffset(-5)
    return shadow2

def getNeuShadow2(type, intensity,spread):
    shadow2 = QGraphicsDropShadowEffect()
    shadow2.setBlurRadius(int(intensity))
    if type == 0:
        shadow2.setColor(Qt.lightGray)
        shadow2.setXOffset(int(spread))
        shadow2.setYOffset(int(spread))
    else :
        shadow2.setColor(Qt.white)
        shadow2.setXOffset(int(spread))
        shadow2.setYOffset(int(spread))
    return shadow2

def convert24to12Time(oldTime):
    try:
        d = datetime.strptime(oldTime, "%H:%M")
        return d.strftime("%I:%M %p")
    except Exception as e:
        print(e.__cause__)
        return None

def get12HourFormatTime(t, convert):
    time = t.split(":")
    hour = int(time[0])
    min = int(time[1])
    isPm = False
    if convert:
        if hour >= 12:
            isPm = True
            if hour > 12:
                hour = hour - 12

        return [hour, min, isPm]
    else:
        return [hour, min]

def addSubMinutes(time, minsToAdd, isAdd):
    totalMins = (time[0]*60) + time[1]

    if minsToAdd<0:
        isAdd = False
        minsToAdd = minsToAdd*-1

    if isAdd:
        totalMins = totalMins+minsToAdd
    else:
        totalMins = totalMins - minsToAdd

        if totalMins<0:
            totalMins = totalMins + 1440

    hours = int(totalMins/60)
    mins = totalMins%60

    return [hours, mins]

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

class HummOptions():
    def __init__(self, value, AveragePercentage, SelectedOption):
        self.value = value
        self.AveragePercentage = AveragePercentage
        self.SelectedOption = SelectedOption

# class HummFeedModel():
#     def __init__(self, value, AveragePercentage, SelectedOption,):
#         self.value = value
#         self.AveragePercentage = AveragePercentage
#         self.SelectedOption = SelectedOption

def isInternetOn():
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname("www.google.com")
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False
