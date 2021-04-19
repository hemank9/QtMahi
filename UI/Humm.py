from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Utility.MahiUtility as Util
import requests


class Humm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Humm")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../Resources/yellow.png'))
        self.label.setGeometry(0, 0, 1220, 39)

        self.UiComponents()
        self.show()

    def UiComponents(self):

        # BUTTONS FOR HUMM

        btnBackToTop = QPushButton(self)
        btnBackToTop.setGeometry(1136, 254, 61, 61)
        btnBackToTop.setStyleSheet("border-radius:10")
        btnBackToTop.setGraphicsEffect(Util.getNeuShadow(0))

        btnBackToTop1 = QPushButton(self)
        btnBackToTop1.setGeometry(1136, 254, 61, 61)
        btnBackToTop1.setGraphicsEffect(Util.getNeuShadow(1))
        btnBackToTop1.setStyleSheet("border-radius:10")
        btnBackToTop1.setIcon(QtGui.QIcon('../Resources/backToTop.png'))
        btnBackToTop1.setIconSize(QtCore.QSize(60, 40))

        btnRefresh = QPushButton(self)
        btnRefresh.setGeometry(1136, 340, 61, 61)
        btnRefresh.setStyleSheet("border-radius:10")
        btnRefresh.setGraphicsEffect(Util.getNeuShadow(0))

        btnRefresh1 = QPushButton(self)
        btnRefresh1.setGeometry(1136, 340, 61, 61)
        btnRefresh1.setGraphicsEffect(Util.getNeuShadow(1))
        btnRefresh1.setStyleSheet("border-radius:10")
        btnRefresh1.setIcon(QtGui.QIcon('../Resources/Refresh.png'))
        btnRefresh1.setIconSize(QtCore.QSize(60, 40))

        btnHome = QPushButton(self)
        btnHome.setGeometry(1136, 426, 61, 61)
        btnHome.setStyleSheet("border-radius:10")
        btnHome.setGraphicsEffect(Util.getNeuShadow(0))

        btnHome1 = QPushButton(self)
        btnHome1.setGeometry(1136, 426, 61, 61)
        btnHome1.setGraphicsEffect(Util.getNeuShadow(1))
        btnHome1.setStyleSheet("border-radius:10")
        btnHome1.setIcon(QtGui.QIcon('../Resources/Home.png'))
        btnHome1.setIconSize(QtCore.QSize(60, 40))

        btnPrevious = QPushButton(self)
        btnPrevious.setGeometry(1136, 512, 61, 61)
        btnPrevious.setStyleSheet("border-radius:10")
        btnPrevious.setGraphicsEffect(Util.getNeuShadow(0))

        btnPrevious1 = QPushButton(self)
        btnPrevious1.setGeometry(1136, 512, 61, 61)
        btnPrevious1.setGraphicsEffect(Util.getNeuShadow(1))
        btnPrevious1.setStyleSheet("border-radius:10")
        btnPrevious1.setIcon(QtGui.QIcon('../Resources/Previous.png'))
        btnPrevious1.setIconSize(QtCore.QSize(60, 40))

        btnNext = QPushButton(self)
        btnNext.setGeometry(1136, 598, 61, 61)
        btnNext.setStyleSheet("border-radius:10")
        btnNext.setGraphicsEffect(Util.getNeuShadow(0))

        btnNext1 = QPushButton(self)
        btnNext1.setGeometry(1136, 598, 61, 61)
        btnNext1.setGraphicsEffect(Util.getNeuShadow(1))
        btnNext1.setStyleSheet("border-radius:10")
        btnNext1.setIcon(QtGui.QIcon('../Resources/Next.png'))
        btnNext1.setIconSize(QtCore.QSize(60, 40))



        url_image= "https://mobihealth.in//upload/health_feed/607b1f0aa40591618681610672.png"
        image = QImage()
        image.loadFromData(requests.get(url_image).content)

        pixmap = QtGui.QPixmap(image)
        scaledImage = pixmap.scaled(607, 607)
        self.lblImage = QLabel(self)
        self.lblImage.setGeometry(18,55,607,607)
        self.lblImage.setPixmap(scaledImage)

        self.lblTitle = QLabel(self)
        self.lblTitle.setGeometry(642,72,550,65)
        self.lblTitle.setWordWrap(True)
        self.lblTitle.setText("Holistic approach to measuring outcomes in children with autism "
                              "spectrum disorder (ASD).")
        self.lblTitle.setStyleSheet("font:bold; color:#333; font-size:23px")

        self.lblDesc = QLabel(self)
        self.lblDesc.setGeometry(642,150,447,400)
        self.lblDesc.setAlignment(Qt.AlignTop)
        self.lblDesc.setWordWrap(True)
        self.lblDesc.setText("A nervous system disorder that affects the cognitive,"
                             " emotional, social, and physical development of an individual mostly "
                             "in early childhood. It is estimated that 1 in every 54 kids in the US"
                             " are on autism spectrum. The older approach based on the criteria of"
                             " “Doing Well” does not completely satisfies the spectrum. Peer relationship"
                             " and other skills are to be considered as well, read more.")
        self.lblDesc.setStyleSheet("font:normal; color:#555; font-size:22px;")



if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Humm()

    window.show()

    # start the app
    sys.exit(App.exec())
