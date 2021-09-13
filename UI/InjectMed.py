import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Utility.MahiUtility as Util

class Inject(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Refill")
        self.setGeometry(0, 0, 1220, 685)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: #F0F0F3")
        # self.label = QLabel(self)
        # self.label.setPixmap(QPixmap('../Resources/Group 48.png'))
        # self.label.setGeometry(0, 0, 1220, 685)
        self.UiComponents()
        self.show()


    def UiComponents(self):

        btn_back1 = QPushButton("X", self)
        btn_back1.setGeometry(1131, 24, 65, 65)
        btn_back1.setStyleSheet("border-radius : 10; background-color: #F0F0F3; color: #C0C0C0")
        btn_back1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_back = QPushButton("X", self)
        btn_back.setGeometry(1131, 24, 65, 65)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3; color: #C0C0C0; font-size: 40px")
        btn_back.setGraphicsEffect(Util.getNeuShadow(1))
        btn_back.clicked.connect(self.close)

        injectlbl = QLabel("Inject Medicine", self)
        injectlbl.setGeometry(29, 21, 315, 48)
        injectlbl.setStyleSheet("color: #00A0B5; background-color: #F0F0F3; font-size: 32px")

        openBtn = QPushButton("Open Cylinder", self)
        openBtn.setGeometry(29, 106, 288, 40)
        openBtn.setStyleSheet("background-color: #BCE6EC; color: #00A0B5; border-radius : 8")
        openBtn.setGraphicsEffect(Util.getNeuShadow(0))
        openBtn.clicked.connect(self.popup)

        settingiconLbl = QLabel(self)
        settingiconLbl.setGeometry(29, 26, 36, 36)
        self.pixmap = QPixmap('\Resources\Settings.png')
        self.label.setPixmap(self.pixmap)

    def popup(self):

        popupLbl1 = QLabel(self)
        popupLbl1.setGeometry(343, 205, 533, 275)
        popupLbl1.setStyleSheet("background-color: #F0F0F3; border-radius: 15")
        popupLbl1.setGraphicsEffect(Util.getNeuShadow(0))
        popupLbl = QLabel("Cylinder", self)
        popupLbl.setGeometry(343, 205, 533, 275)
        popupLbl.setStyleSheet("background-color: #F0F0F3; border-radius: 15")
        popupLbl.setGraphicsEffect(Util.getNeuShadow(1))

        cylinderLbl = QLabel("Cylinder", self)
        cylinderLbl.setGeometry(386, 269, 258, 75)
        cylinderLbl.setStyleSheet("color: #00A0B5; font-size:50")

        doneBtn1 = QPushButton("Done", self)
        doneBtn1.setGeometry(386, 370, 169, 75)
        doneBtn1.setStyleSheet("background-color: #F0F0F3; color: #00A0B5; border-radius:5")
        doneBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        doneBtn = QPushButton("Done", self)
        doneBtn.setGeometry(386, 370, 169, 75)
        doneBtn.setStyleSheet("background-color: #F0F0F3; color: #00A0B5; border-radius:5; font-size: 35px")
        doneBtn.setGraphicsEffect(Util.getNeuShadow(1))

        nextBtn1 = QPushButton("next", self)
        nextBtn1.setGeometry(664, 370, 169, 75)
        nextBtn1.setStyleSheet("background-color: #F0F0F3; color: #00A0B5; border-radius:5")
        nextBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        nextBtn = QPushButton("Next", self)
        nextBtn.setGeometry(664, 370, 169, 75)
        nextBtn.setStyleSheet("background-color: #F0F0F3; color: #00A0B5; border-radius:5; font-size: 35px")
        nextBtn.setGraphicsEffect(Util.getNeuShadow(1))





if __name__ == '__main__':

    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Inject()

    # start the app
    sys.exit(App.exec())