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
        self.cylinderNo = 1
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
        openBtn.clicked.connect(lambda : self.popup(1))

        # settingiconLbl = QLabel(self)
        # settingiconLbl.setGeometry(29, 26, 36, 36)
        # self.pixmap = QPixmap('\Resources\Settings.png')
        # self.label.setPixmap(self.pixmap)

        self.popupLbl1 = QLabel(self)
        self.popupLbl1.setGeometry(343, 205, 533, 275)
        self.popupLbl1.setStyleSheet("background-color: #F0F0F3; border-radius: 15")
        self.popupLbl1.setGraphicsEffect(Util.getNeuShadow(0))
        self.popupLbl = QLabel(self)
        self.popupLbl.setGeometry(343, 205, 533, 275)
        self.popupLbl.setStyleSheet("background-color: #F0F0F3; border-radius: 15")
        self.popupLbl.setGraphicsEffect(Util.getNeuShadow(1))

        self.cylinderLbl = QLabel("Cylinder " + str(self.cylinderNo), self)
        self.cylinderLbl.setGeometry(386, 269, 258, 75)
        self.cylinderLbl.setStyleSheet("color: #00A0B5; font-size:50px")

        self.doneBtn1 = QPushButton("Done", self)
        self.doneBtn1.setGeometry(386, 370, 169, 75)
        self.doneBtn1.setStyleSheet("background-color: #F0F0F3; color: #00A0B5; border-radius:5")
        self.doneBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        self.doneBtn = QPushButton("Done", self)
        self.doneBtn.setGeometry(386, 370, 169, 75)
        self.doneBtn.setStyleSheet("background-color: #F0F0F3; color: #00A0B5; border-radius:5; font-size: 35px")
        self.doneBtn.setGraphicsEffect(Util.getNeuShadow(1))

        self.nextBtn1 = QPushButton("next", self)
        self.nextBtn1.setGeometry(664, 370, 169, 75)
        self.nextBtn1.setStyleSheet("background-color: #F0F0F3; color: #00A0B5; border-radius:5")
        self.nextBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        self.nextBtn = QPushButton("Next", self)
        self.nextBtn.setGeometry(664, 370, 169, 75)
        self.nextBtn.setStyleSheet("background-color: #F0F0F3; color: #00A0B5; border-radius:5; font-size: 35px")
        self.nextBtn.setGraphicsEffect(Util.getNeuShadow(1))
        self.nextBtn.clicked.connect(self.nextClicked)

        self.popup(2)

    def popup(self, type):

        if type == 1:
            self.popupLbl1.show()
            self.popupLbl.show()
            self.cylinderLbl.show()
            self.doneBtn1.show()
            self.doneBtn.show()
            self.nextBtn1.show()
            self.nextBtn.show()
        else:
            self.popupLbl1.hide()
            self.popupLbl.hide()
            self.cylinderLbl.hide()
            self.doneBtn1.hide()
            self.doneBtn.hide()
            self.nextBtn1.hide()
            self.nextBtn.hide()

    def nextClicked(self):

        if self.cylinderNo<8:
            self.cylinderNo = self.cylinderNo + 1

            self.cylinderLbl.setText("Cylinder " + str(self.cylinderNo))



if __name__ == '__main__':

    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Inject()

    # start the app
    sys.exit(App.exec())