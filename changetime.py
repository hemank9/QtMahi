import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 700)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\mtry.png'))
        self.label.setGeometry(0, 0, 1220, 700)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        btn_bck = QPushButton("", self)
        btn_bck.setGeometry(43, 48, 150, 75)
        btn_bck.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_bck.setIcon(QtGui.QIcon('Resources\Group 34.png'))
        btn_bck.setIconSize(QtCore.QSize(160, 90))
        btn_bck.clicked.connect(self.close)

        lblt = QLabel("Morning", self)
        lblt.setGeometry(354, 70, 105, 40)

        lblbf = QLabel("Before Food", self)
        lblbf.setGeometry(354, 143, 115, 29)

        lblaf = QLabel("After Food", self)
        lblaf.setGeometry(651, 143, 105, 40)

        lblnt = QLabel("IOT", self)
        lblnt.setGeometry(954, 143, 105, 40)

        # Buttons for Morning Before Food

        btnbfHourAdd = QPushButton("", self)
        btnbfHourAdd.setGeometry(354, 211, 45, 33)
        btnbfHourAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnbfHourAdd.setIcon(QtGui.QIcon('Resources\mAddTime.png'))
        btnbfHourAdd.setIconSize(QtCore.QSize(160, 90))
        btnbfHourAdd.clicked.connect(self.close)

        btnbfHourSub = QPushButton("", self)
        btnbfHourSub.setGeometry(354, 296, 45, 33)
        btnbfHourSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnbfHourSub.setIcon(QtGui.QIcon('Resources\mSubTime.png'))
        btnbfHourSub.setIconSize(QtCore.QSize(160, 90))
        btnbfHourSub.clicked.connect(self.close)

        btnbfMinAdd = QPushButton("", self)
        btnbfMinAdd.setGeometry(430, 211, 45, 33)
        btnbfMinAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnbfMinAdd.setIcon(QtGui.QIcon('Resources\mAddTime.png'))
        btnbfMinAdd.setIconSize(QtCore.QSize(160, 90))
        btnbfMinAdd.clicked.connect(self.close)

        btnbfMinSub = QPushButton("", self)
        btnbfMinSub.setGeometry(430, 296, 45, 33)
        btnbfMinSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnbfMinSub.setIcon(QtGui.QIcon('Resources\mSubTime.png'))
        btnbfMinSub.setIconSize(QtCore.QSize(160, 90))
        btnbfMinSub.clicked.connect(self.close)

        btnBfAmPm = QPushButton("", self)
        btnBfAmPm.setGeometry(506, 253, 45, 33)
        btnBfAmPm.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnBfAmPm.setIcon(QtGui.QIcon('Resources\pmbtn.png'))
        btnBfAmPm.setIconSize(QtCore.QSize(160, 90))
        btnBfAmPm.clicked.connect(self.close)

        lblAmPm = QLabel("am", self)
        lblAmPm.setGeometry(514, 253, 25, 25)

        display_lbl = QLabel(self)
        display_lbl.setPixmap(QPixmap('Resources\mBkg.png'))
        display_lbl.setGeometry(354, 253, 45, 33)
        lblBfHour = QLabel("10", self)
        lblBfHour.setGeometry(360, 260, 30, 21)
        lblBfHour.setAlignment(QtCore.Qt.AlignCenter)
        lblBfHour.setStyleSheet("background-color : #0000")

        display2_lbl = QLabel(self)
        display2_lbl.setPixmap(QPixmap('Resources\mBkg.png'))
        display2_lbl.setGeometry(430, 253, 45, 33)
        lblBfMin = QLabel("10", self)
        lblBfMin.setGeometry(436, 260, 30, 21)
        lblBfMin.setAlignment(QtCore.Qt.AlignCenter)
        lblBfMin.setStyleSheet("background-color : #0000")

        # Buttons for Morning After Food

        btnAfHourAdd = QPushButton("", self)
        btnAfHourAdd.setGeometry(651, 211, 45, 33)
        btnAfHourAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAfHourAdd.setIcon(QtGui.QIcon('Resources\mAddTime.png'))
        btnAfHourAdd.setIconSize(QtCore.QSize(160, 90))
        btnAfHourAdd.clicked.connect(self.close)

        btnAfHourSub = QPushButton("", self)
        btnAfHourSub.setGeometry(651, 296, 45, 33)
        btnAfHourSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAfHourSub.setIcon(QtGui.QIcon('Resources\mSubTime.png'))
        btnAfHourSub.setIconSize(QtCore.QSize(160, 90))
        btnAfHourSub.clicked.connect(self.close)

        btnAfMinAdd = QPushButton("", self)
        btnAfMinAdd.setGeometry(727, 211, 45, 33)
        btnAfMinAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAfMinAdd.setIcon(QtGui.QIcon('Resources\mAddTime.png'))
        btnAfMinAdd.setIconSize(QtCore.QSize(160, 90))
        btnAfMinAdd.clicked.connect(self.close)

        btnAfMinSub = QPushButton("", self)
        btnAfMinSub.setGeometry(727, 296, 45, 33)
        btnAfMinSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAfMinSub.setIcon(QtGui.QIcon('Resources\mSubTime.png'))
        btnAfMinSub.setIconSize(QtCore.QSize(160, 90))
        btnAfMinSub.clicked.connect(self.close)

        btnAfAmPm = QPushButton("", self)
        btnAfAmPm.setGeometry(803, 253, 45, 33)
        btnAfAmPm.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnAfAmPm.setIcon(QtGui.QIcon('Resources\pmbtn.png'))
        btnAfAmPm.setIconSize(QtCore.QSize(160, 90))
        btnAfAmPm.clicked.connect(self.close)

        lblAfAmPm = QLabel("am", self)
        lblAfAmPm.setGeometry(811, 253, 25, 25)

        display3_lbl = QLabel(self)
        display3_lbl.setPixmap(QPixmap('Resources\mBkg.png'))
        display3_lbl.setGeometry(651, 253, 45, 33)
        lblAfHour = QLabel("10", self)
        lblAfHour.setGeometry(657, 260, 30, 21)
        lblAfHour.setAlignment(QtCore.Qt.AlignCenter)
        lblAfHour.setStyleSheet("background-color : #0000")

        display4_lbl = QLabel(self)
        display4_lbl.setPixmap(QPixmap('Resources\mBkg.png'))
        display4_lbl.setGeometry(727, 253, 45, 33)
        lblAfMin = QLabel("10", self)
        lblAfMin.setGeometry(733, 260, 30, 21)
        lblAfMin.setAlignment(QtCore.Qt.AlignCenter)
        lblAfMin.setStyleSheet("background-color : #0000")

        # Buttons for IOT

        btnItHourAdd = QPushButton("", self)
        btnItHourAdd.setGeometry(954, 211, 45, 33)
        btnItHourAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnItHourAdd.setIcon(QtGui.QIcon('Resources\mAddTime.png'))
        btnItHourAdd.setIconSize(QtCore.QSize(160, 90))
        btnItHourAdd.clicked.connect(self.close)

        btnItHourSub = QPushButton("", self)
        btnItHourSub.setGeometry(954, 296, 45, 33)
        btnItHourSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnItHourSub.setIcon(QtGui.QIcon('Resources\mSubTime.png'))
        btnItHourSub.setIconSize(QtCore.QSize(160, 90))
        btnItHourSub.clicked.connect(self.close)

        btnItMinAdd = QPushButton("", self)
        btnItMinAdd.setGeometry(1030, 211, 45, 33)
        btnItMinAdd.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnItMinAdd.setIcon(QtGui.QIcon('Resources\mAddTime.png'))
        btnItMinAdd.setIconSize(QtCore.QSize(160, 90))
        btnItMinAdd.clicked.connect(self.close)

        btnItMinSub = QPushButton("", self)
        btnItMinSub.setGeometry(1030, 296, 45, 33)
        btnItMinSub.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnItMinSub.setIcon(QtGui.QIcon('Resources\mSubTime.png'))
        btnItMinSub.setIconSize(QtCore.QSize(160, 90))
        btnItMinSub.clicked.connect(self.close)

        btnItAmPm = QPushButton("", self)
        btnItAmPm.setGeometry(1106, 253, 45, 33)
        btnItAmPm.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btnItAmPm.setIcon(QtGui.QIcon('Resources\pmbtn.png'))
        btnItAmPm.setIconSize(QtCore.QSize(160, 90))
        btnItAmPm.clicked.connect(self.close)

        lblItAmPm = QLabel("am", self)
        lblItAmPm.setGeometry(1114, 253, 25, 25)

        display5_lbl = QLabel(self)
        display5_lbl.setPixmap(QPixmap('Resources\mBkg.png'))
        display5_lbl.setGeometry(954, 253, 45, 33)
        lblItHour = QLabel("10", self)
        lblItHour.setGeometry(960, 260, 30, 21)
        lblItHour.setAlignment(QtCore.Qt.AlignCenter)
        lblItHour.setStyleSheet("background-color : #0000")

        display6_lbl = QLabel(self)
        display6_lbl.setPixmap(QPixmap('Resources\mBkg.png'))
        display6_lbl.setGeometry(1030, 253, 45, 33)
        lblItMin = QLabel("10", self)
        lblItMin.setGeometry(1036, 260, 30, 21)
        lblItMin.setAlignment(QtCore.Qt.AlignCenter)
        lblItMin.setStyleSheet("background-color : #0000")

        # Buttons of Morning, Evening, Afternoon

        # lbl99 = QLabel("",self)
        # lbl99.setGeometry(35, 202, 200, 80)
        # lbl99.setStyleSheet("border-radius : 15;background-color : white")

        btnMorning = QPushButton("Morning", self)
        btnMorning.setGeometry(41, 217, 200, 80)
        btnMorning.setStyleSheet("border-radius : 15; background-color: #F0F0F3; color : #00A0B5")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(Qt.red)
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.3)
        btnMorning.setGraphicsEffect(shadow)
        # shadow.setGraphicsEffect(self.opacity_effect)

        # btnMorning.setIcon(QtGui.QIcon('Resources\mAddTime.png'))
        # btnMorning.setIconSize(QtCore.QSize(160, 90))
        btnMorning.clicked.connect(self.close)

        # lbl91 = QLabel("", self)
        # lbl91.setGeometry(37, 320, 200, 80)
        # lbl91.setStyleSheet("border-radius : 15;background-color : white")


        btnAfternoon = QPushButton("Afternoon", self)
        btnAfternoon.setGeometry(41, 326, 200, 80)
        btnAfternoon.setStyleSheet("border-radius : 15; background-color: #F0F03; color : #00A0B5")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        btnAfternoon.setGraphicsEffect(shadow)
        shadow.setColor(Qt.lightGray)
        # btnAfternoon.setIcon(QtGui.QIcon('Resources\mAddTime.png'))
        # btnAfternoon.setIconSize(QtCore.QSize(160, 90))
        btnAfternoon.clicked.connect(self.close)

        btnEvening = QPushButton("Evening", self)
        btnEvening.setGeometry(41, 435, 200, 80)
        btnEvening.setStyleSheet("border-radius : 15; background-color: #f0f03; color : #00A0B5")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setXOffset(-5)
        shadow.setYOffset(-5)
        shadow.setColor(Qt.white)
        btnEvening.setGraphicsEffect(shadow)
        # btnEvening.setIcon(QtGui.QIcon('Resources\mAddTime.png'))
        # btnEvening.setIconSize(QtCore.QSize(160, 90))
        btnEvening.clicked.connect(self.close)

        btnEvening = QPushButton("Evening", self)
        btnEvening.setGeometry(41, 435, 200, 80)
        btnEvening.setStyleSheet("border-radius : 15; background-color: #EEE; color : #00A0B5")
        # shadow = QGraphicsDropShadowEffect("{"  "width:350px;height:200px;"
        #                                         "border: solid 1px #555;"
        #                                         "background-color: #eed;"
        #                                         "box-shadow: 0 0 10px rgba(0,0,0,0.6);"
        #                                         "-moz-box-shadow: 0 0 10px rgba(0,0,0,0.6);"
        #                                         "-webkit-box-shadow: 0 0 10px rgba(0,0,0,0.6);"
        #
        #                                          "-o-box-shadow: 0 0 10px rgba(0,0,0,0.6);" "}")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(Qt.lightGray)
        btnEvening.setGraphicsEffect(shadow)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        # btnEvening.setIcon(QtGui.QIcon('Resources\mAddTime.png'))
        # btnEvening.setIconSize(QtCore.QSize(160, 90))
        btnEvening.clicked.connect(self.close)

        btnOk = QPushButton("", self)
        btnOk.setGeometry(967, 459, 158, 92)
        btnOk.setStyleSheet("border-radius : 15; background-color: #F0F0F3; color : #00A0B5")
        btnOk.setIcon(QtGui.QIcon('Resources\mOk.png'))
        btnOk.setIconSize(QtCore.QSize(180, 110))
        btnOk.clicked.connect(self.close)


App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec())
