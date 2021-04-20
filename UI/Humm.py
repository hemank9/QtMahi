from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Utility.MahiUtility as Util
import requests
import MyDatabase.my_database as db
import json
import constants as myConst
import Utility.MahiUtility as MahiUtil
import API.api_calls as MyApis


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

        self.currentPage = 0
        self.loadingDialog = MahiUtil.LoadingGif()
        # self.fetchHummFeeds()
        self.showFullImage(False)
        self.showTextImage(False)
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
        btnPrevious1.clicked.connect(self.prevClicked)

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
        btnNext1.clicked.connect(self.nextClicked)




        self.lblImage = QLabel(self)
        self.lblImage.setGeometry(18,55,607,607)

        self.lblTitle = QLabel(self)
        self.lblTitle.setGeometry(642,72,550,65)
        self.lblTitle.setWordWrap(True)
        self.lblTitle.setStyleSheet("font:bold; color:#333; font-size:23px")

        self.lblDesc = QLabel(self)
        self.lblDesc.setGeometry(642,150,447,400)
        self.lblDesc.setAlignment(Qt.AlignTop)
        self.lblDesc.setWordWrap(True)
        self.lblDesc.setStyleSheet("font:normal; color:#555; font-size:22px;")



        self.lblFullImage = QLabel(self)
        self.lblFullImage.setGeometry(428,40,363,645)

        self.showFullImage(False)

    def fetchHummFeeds(self):

    # try:
        if MahiUtil.isInternetOn():
            self.loadingDialog.startAnimation()
            temp1 = MyApis.fetchHummFeeds(self.currentPage,"","1")
            self.loadingDialog.stopAnimation()

            if temp1 != None:
                # temp = json.loads(temp1, strict=False)
                self.hummFeeds = list(temp1["data"])
                self.ParseHummFeed()

            else:
                print("Humm data not available")


        # except Exception as e:
        #     print(e.__class__)

    def ParseHummFeed(self):
        hummFeed = self.hummFeeds[self.currentPage]

        pageType = int(hummFeed["PageType"])
        # Image + Text
        if  pageType == myConst.HUMM_IMAGE_TEXT:
            self.showTextImage(True)
            self.showFullImage(False)

        elif pageType == myConst.HUMM_FULL_IMAGE:
            self.showTextImage(False)
            self.showFullImage(True)
        else:
            print(str(pageType))
            self.showTextImage(False)
            self.showFullImage(False)


    def showTextImage(self,show):
        if show:

            hummFeed = self.hummFeeds[self.currentPage]
            self.lblImage.show()
            self.lblDesc.show()
            self.lblTitle.show()

            url_image = hummFeed["ImageName"]
            image = QImage()
            image.loadFromData(requests.get(url_image).content)

            pixmap = QtGui.QPixmap(image)
            scaledImage = pixmap.scaled(607, 607)
            self.lblImage.setPixmap(scaledImage)
            self.lblTitle.setText(hummFeed["Title"])
            self.lblDesc.setText(hummFeed["Description"])
        else :
            self.lblImage.hide()
            self.lblDesc.hide()
            self.lblTitle.hide()

    def showFullImage(self, show):
        if show:

            hummFeed = self.hummFeeds[self.currentPage]
            self.lblFullImage.show()

            full_image = hummFeed["ImageName"]

            image1 = QImage()
            image1.loadFromData(requests.get(full_image).content)

            pixmap1 = QtGui.QPixmap(image1)
            scaledImage1 = pixmap1.scaled(363, 645)
            self.lblFullImage.setPixmap(scaledImage1)

        else:
            self.lblFullImage.hide()

    def nextClicked(self):
        if self.currentPage < len(self.hummFeeds)-1:
            self.currentPage = self.currentPage+1
            self.ParseHummFeed()

    def prevClicked(self):
        if self.currentPage > 0:
            self.currentPage = self.currentPage-1
            self.ParseHummFeed()

if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Humm()

    window.show()

    # start the app
    sys.exit(App.exec())
