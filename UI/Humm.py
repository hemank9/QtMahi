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
import UI.WebPage as webPage


class Humm(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Humm")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        # self.label = QLabel(self)
        # self.label.setStyleSheet("background-color:#FEC32E")
        # self.label.setGeometry(0, 0, 1220, 39)

        self.UiComponents()

        self.currentPage = 0
        self.page = 1
        self.totalRecords = 0
        self.loadingDialog = MahiUtil.LoadingGif()
        self.fetchHummFeeds()
        # self.showFullImage(False)
        # self.showTextImage(False)
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
        btnBackToTop1.clicked.connect(self.backToTop)

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
        btnRefresh1.clicked.connect(self.refreshHumm)

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
        btnHome1.clicked.connect(self.close)

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

        self.lblImageQS = QLabel(self)
        self.lblImageQS.setGeometry(18,55,607,607)

        self.lblTitle = QLabel(self)
        self.lblTitle.setGeometry(642,72,550,65)
        self.lblTitle.setWordWrap(True)
        self.lblTitle.setStyleSheet("font:bold; color:#333; font-size:23px")

        self.lblDesc = QLabel(self)
        self.lblDesc.setGeometry(642,150,447,400)
        self.lblDesc.setAlignment(Qt.AlignTop)
        self.lblDesc.setWordWrap(True)
        self.lblDesc.setStyleSheet("font:normal; color:#555; font-size:22px;")

        self.lblQuestion = QLabel(self)
        self.lblQuestion.setGeometry(642,72,447,70)
        self.lblQuestion.setAlignment(Qt.AlignTop)
        self.lblQuestion.setWordWrap(True)
        self.lblQuestion.setStyleSheet("font:normal; color:#555; font-size:22px;")

        self.optionStyle = "border-radius: 8; text-align: left;padding-left:10px; font-size:15px"
        self.optionStyleCorrect = "border-radius: 8; text-align: left;padding-left:10px; font-size:15px;" \
                                  "background-color:#5500FF00"
        self.optionStyleIncorrect = "border-radius: 8; text-align: left;padding-left:10px; font-size:15px;" \
                                    "background-color:#55FF0000"
        self.optionStyleSurveySelected = "border-radius: 8; text-align: left;padding-left:10px; font-size:15px;" \
                                         "background-color:#FFD881"

        self.btnOption1s = QPushButton(self)
        self.btnOption1s.setGeometry(642, 151, 400, 62)
        self.btnOption1s.setStyleSheet("border-radius: 8")
        self.btnOption1s.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnOption1 = QPushButton(self)
        self.btnOption1.setGeometry(642, 151, 400, 62)
        self.btnOption1.setStyleSheet(self.optionStyle)
        self.btnOption1.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnOption1.clicked.connect(self.option1Clicked)

        self.btnOption2s = QPushButton(self)
        self.btnOption2s.setGeometry(642, 230, 400, 62)
        self.btnOption2s.setStyleSheet("border-radius: 8")
        self.btnOption2s.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnOption2 = QPushButton(self)
        self.btnOption2.setGeometry(642, 230, 400, 62)
        self.btnOption2.setStyleSheet(self.optionStyle)
        self.btnOption2.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnOption2.clicked.connect(self.option2Clicked)

        self.btnOption3s = QPushButton(self)
        self.btnOption3s.setGeometry(642, 309, 400, 62)
        self.btnOption3s.setStyleSheet("border-radius: 8")
        self.btnOption3s.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnOption3 = QPushButton(self)
        self.btnOption3.setGeometry(642, 309, 400, 62)
        self.btnOption3.setStyleSheet(self.optionStyle)
        self.btnOption3.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnOption3.clicked.connect(self.option3Clicked)

        self.btnOption4s = QPushButton(self)
        self.btnOption4s.setGeometry(642, 388, 400, 62)
        self.btnOption4s.setStyleSheet("border-radius: 8")
        self.btnOption4s.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnOption4 = QPushButton(self)
        self.btnOption4.setGeometry(642, 388, 400, 62)
        self.btnOption4.setStyleSheet(self.optionStyle)
        self.btnOption4.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnOption4.clicked.connect(self.option4Clicked)


        self.lblSurvey1 = QLabel(self)
        self.lblSurvey1.setGeometry(1050, 151, 62, 62)
        self.lblSurvey1.setAlignment(Qt.AlignCenter)
        self.lblSurvey1.setStyleSheet(self.optionStyle)
        self.lblSurvey1.setGraphicsEffect(Util.getNeuShadow(0))

        self.lblSurvey2 = QLabel(self)
        self.lblSurvey2.setGeometry(1050, 230, 62, 62)
        self.lblSurvey2.setAlignment(Qt.AlignCenter)
        self.lblSurvey2.setStyleSheet(self.optionStyle)
        self.lblSurvey2.setGraphicsEffect(Util.getNeuShadow(0))

        self.lblSurvey3 = QLabel(self)
        self.lblSurvey3.setGeometry(1050, 309, 62, 62)
        self.lblSurvey3.setAlignment(Qt.AlignCenter)
        self.lblSurvey3.setStyleSheet(self.optionStyle)
        self.lblSurvey3.setGraphicsEffect(Util.getNeuShadow(0))

        self.lblSurvey4 = QLabel(self)
        self.lblSurvey4.setGeometry(1050, 388, 62, 62)
        self.lblSurvey4.setAlignment(Qt.AlignCenter)
        self.lblSurvey4.setStyleSheet(self.optionStyle)
        self.lblSurvey4.setGraphicsEffect(Util.getNeuShadow(0))

        self.lblFullImage = QLabel(self)
        self.lblFullImage.setGeometry(428, 40, 363, 645)

        self.lblGoToLinks = QLabel(self)
        self.lblGoToLinks.setGeometry(642,622,150,40)
        self.lblGoToLinks.setStyleSheet("border-radius: 8;")
        self.lblGoToLinks.setGraphicsEffect(MahiUtil.getNeuShadow(0))
        self.lblGoToLink = QLabel(self)
        self.lblGoToLink.setGeometry(642,622,150,40)
        self.lblGoToLink.setStyleSheet("border-radius: 8;color:#0C6DB6; text-align: left;padding-left:10px; font-size:18px")
        self.lblGoToLink.setText("Read More")
        self.lblGoToLink.setGraphicsEffect(MahiUtil.getNeuShadow(1))

        self.btnGoTolink = QPushButton(self)
        self.btnGoTolink.setGeometry(642,622,150,40)
        self.btnGoTolink.setStyleSheet("background-color:#00FFFFFF")
        self.btnGoTolink.clicked.connect(self.goToLinkClicked)

        self.lblLinkIcon = QLabel(self)
        self.lblLinkIcon.setGeometry(755,622,22,40)

        pixmap = QtGui.QPixmap('../Resources/link.png')
        scaledImage = pixmap.scaled(20, 20)
        self.lblLinkIcon.setPixmap(scaledImage)

        #Full text UI components
        self.fullTextTitle = QLabel(self)
        self.fullTextTitle.setGeometry(31, 75, 1000, 66)
        self.fullTextTitle.setStyleSheet("font-size: 28px; font:bold; color: black;")
        self.fullTextTitle.setWordWrap(True)

        self.fullTextDescription = QLabel(self)
        self.fullTextDescription.setGeometry(31, 160, 1000, 450)
        self.fullTextDescription.setStyleSheet("color: black; font-size: 26px;")
        self.fullTextDescription.setWordWrap(True)
        self.fullTextDescription.setAlignment(Qt.AlignTop)

        #Full Text Survey

        self.FtsbtnOption1s = QPushButton(self)
        self.FtsbtnOption1s.setGeometry(31, 200, 700, 62)
        self.FtsbtnOption1s.setStyleSheet("border-radius: 8")
        self.FtsbtnOption1s.setGraphicsEffect(Util.getNeuShadow(0))
        self.FtsbtnOption1 = QPushButton(self)
        self.FtsbtnOption1.setGeometry(31, 200, 700, 62)
        self.FtsbtnOption1.setStyleSheet(self.optionStyle)
        self.FtsbtnOption1.setGraphicsEffect(Util.getNeuShadow(1))
        self.FtsbtnOption1.clicked.connect(lambda : self.FtsOptionClicked(1))

        self.FtsbtnOption2s = QPushButton(self)
        self.FtsbtnOption2s.setGeometry(31, 280, 700, 62)
        self.FtsbtnOption2s.setStyleSheet("border-radius: 8")
        self.FtsbtnOption2s.setGraphicsEffect(Util.getNeuShadow(0))
        self.FtsbtnOption2 = QPushButton(self)
        self.FtsbtnOption2.setGeometry(31, 280, 700, 62)
        self.FtsbtnOption2.setStyleSheet(self.optionStyle)
        self.FtsbtnOption2.setGraphicsEffect(Util.getNeuShadow(1))
        self.FtsbtnOption2.clicked.connect(lambda : self.FtsOptionClicked(2))

        self.FtsbtnOption3s = QPushButton(self)
        self.FtsbtnOption3s.setGeometry(31, 360, 700, 62)
        self.FtsbtnOption3s.setStyleSheet("border-radius: 8")
        self.FtsbtnOption3s.setGraphicsEffect(Util.getNeuShadow(0))
        self.FtsbtnOption3 = QPushButton(self)
        self.FtsbtnOption3.setGeometry(31, 360, 700, 62)
        self.FtsbtnOption3.setStyleSheet(self.optionStyle)
        self.FtsbtnOption3.setGraphicsEffect(Util.getNeuShadow(1))
        self.FtsbtnOption3.clicked.connect(lambda : self.FtsOptionClicked(3))

        self.FtsbtnOption4s = QPushButton(self)
        self.FtsbtnOption4s.setGeometry(31, 440, 700, 62)
        self.FtsbtnOption4s.setStyleSheet("border-radius: 8")
        self.FtsbtnOption4s.setGraphicsEffect(Util.getNeuShadow(0))
        self.FtsbtnOption4 = QPushButton(self)
        self.FtsbtnOption4.setGeometry(31, 440, 700, 62)
        self.FtsbtnOption4.setStyleSheet(self.optionStyle)
        self.FtsbtnOption4.setGraphicsEffect(Util.getNeuShadow(1))
        self.FtsbtnOption4.clicked.connect(lambda : self.FtsOptionClicked(4))

        self.FtslblSurvey1 = QLabel(self)
        self.FtslblSurvey1.setGeometry(750, 200, 62, 62)
        self.FtslblSurvey1.setAlignment(Qt.AlignCenter)
        self.FtslblSurvey1.setStyleSheet(self.optionStyle)
        self.FtslblSurvey1.setGraphicsEffect(Util.getNeuShadow(0))

        self.FtslblSurvey2 = QLabel(self)
        self.FtslblSurvey2.setGeometry(750, 280, 62, 62)
        self.FtslblSurvey2.setAlignment(Qt.AlignCenter)
        self.FtslblSurvey2.setStyleSheet(self.optionStyle)
        self.FtslblSurvey2.setGraphicsEffect(Util.getNeuShadow(0))

        self.FtslblSurvey3 = QLabel(self)
        self.FtslblSurvey3.setGeometry(750, 360, 62, 62)
        self.FtslblSurvey3.setAlignment(Qt.AlignCenter)
        self.FtslblSurvey3.setStyleSheet(self.optionStyle)
        self.FtslblSurvey3.setGraphicsEffect(Util.getNeuShadow(0))

        self.FtslblSurvey4 = QLabel(self)
        self.FtslblSurvey4.setGeometry(750, 440, 62, 62)
        self.FtslblSurvey4.setAlignment(Qt.AlignCenter)
        self.FtslblSurvey4.setStyleSheet(self.optionStyle)
        self.FtslblSurvey4.setGraphicsEffect(Util.getNeuShadow(0))

        self.toggleLinkButton(False)

        self.showFullImage(False)
        self.showQuizSurvey(False)
        self.showTextImage(False)
        self.optionList = []

    def fetchHummFeeds(self):

        try:
            if MahiUtil.isInternetOn():

                if self.page == 1:
                    self.loadingDialog.startAnimation()
                # temp1 = MyApis.fetchHummFeeds(self.page,"","1")
                temp1 = MyApis.fetchHummFeedsDummy()
                self.loadingDialog.stopAnimation()

                if temp1 != None:

                    if self.page == 1:
                        self.hummFeeds = list(temp1["data"])
                        self.ParseHummFeed()
                        self.totalRecords = int(temp1["total_records"])
                    elif self.page > 1:
                        self.hummFeeds = self.hummFeeds + list(temp1["data"])

            else:
                print("Humm data not available")


        except Exception as e:
            print(e.__class__)

    def refreshHumm(self):
        self.currentPage = 0
        self.hummFeeds = []
        self.optionList = []
        self.selectedOption = 0
        self.fetchHummFeeds()

    def goToLinkClicked(self):
        self.x = webPage.WebPage(self.link)
        self.x.show()

    def toggleLinkButton(self,show):

        if show:
            self.lblLinkIcon.show()
            self.lblGoToLink.show()
            self.lblGoToLinks.show()
            self.btnGoTolink.show()
        else:
            self.lblLinkIcon.hide()
            self.lblGoToLink.hide()
            self.lblGoToLinks.hide()
            self.btnGoTolink.hide()

    def backToTop(self):
        self.currentPage = 0
        self.optionList = []
        self.selectedOption = 0
        self.ParseHummFeed()

    def ParseHummFeed(self):

        if ((len(self.hummFeeds) - self.currentPage) == 10) and (len(self.hummFeeds) <= self.totalRecords):
            self.page = self.page+1
            self.fetchHummFeeds()

        hummFeed = self.hummFeeds[self.currentPage]

        pageType = int(hummFeed["PageType"])
        print(str(hummFeed))

        self.link = hummFeed.get("DetailUrl")

        if self.link!=None:
            if len(self.link)>7:
                self.toggleLinkButton(True)
            else:
                self.toggleLinkButton(False)
        else:
            self.toggleLinkButton(False)

        # Image + Text
        if  pageType == myConst.HUMM_IMAGE_TEXT:
            self.showFullImage(False)
            self.showQuizSurvey(False)
            self.showFullText(False)
            self.showFullTextSurvey(False)
            self.showTextImage(True)


        # Full Image
        elif pageType == myConst.HUMM_FULL_IMAGE:
            self.showTextImage(False)
            self.showQuizSurvey(False)
            self.showFullText(False)
            self.showFullTextSurvey(False)
            self.showFullImage(True)


        # Image + Quiz/Survey
        elif pageType == myConst.HUMM_IMAGE_QUIZ_SURVEY:
            self.showTextImage(False)
            self.showFullImage(False)
            self.showFullText(False)
            self.showFullTextSurvey(False)
            self.showQuizSurvey(True)


        # Full text
        elif pageType == myConst.HUMM_FULL_TEXT:
            self.showTextImage(False)
            self.showFullImage(False)
            self.showQuizSurvey(False)
            self.showFullTextSurvey(False)
            self.showFullText(True)

       #Full Text Survey
        elif pageType == myConst.HUMM_FULL_TEXT_SURVEY:
            self.showTextImage(False)
            self.showFullImage(False)
            self.showQuizSurvey(False)
            self.showFullText(False)
            self.showFullTextSurvey(True)

        else:
            self.showTextImage(False)
            self.showFullImage(False)
            self.showQuizSurvey(False)
            self.showFullText(False)
            self.showFullTextSurvey(False)



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

    def showFullText(self, show):

        if show:
            hummFeed = self.hummFeeds[self.currentPage]
            self.fullTextTitle.show()
            self.fullTextDescription.show()
            self.fullTextTitle.setText(hummFeed["Title"])
            self.fullTextDescription.setText(hummFeed["Description"])

        else:
            self.fullTextDescription.hide()
            self.fullTextTitle.hide()

    def showFullTextSurvey(self, show):

        if show:

            hummFeed = self.hummFeeds[self.currentPage]

            isSurvey = int(hummFeed["IsSurvey"]) == 1 # 1 for survey, 2 for quiz

            self.fullTextTitle.show()
            self.FtsbtnOption1.hide()
            self.FtsbtnOption1s.hide()
            self.FtsbtnOption2.hide()
            self.FtsbtnOption2s.hide()
            self.FtsbtnOption3.hide()
            self.FtsbtnOption3s.hide()
            self.FtsbtnOption4.hide()
            self.FtsbtnOption4s.hide()
            self.FtslblSurvey1.hide()
            self.FtslblSurvey2.hide()
            self.FtslblSurvey3.hide()
            self.FtslblSurvey4.hide()

            self.fullTextTitle.setText(hummFeed["Question"])

            optionArr = list(hummFeed["Options"])

            self.optionList = []
            self.selectedOption = 0
            for opt in optionArr:
                tempOtp = MahiUtil.HummOptions(opt["value"], opt["AveragePercentage"], opt["SelectedOption"]);
                self.optionList.append(tempOtp)
                if (len(self.optionList) == 1):
                    self.FtsbtnOption1.setText("1. " + self.optionList[0].value)
                    self.FtsbtnOption1.setStyleSheet(self.optionStyle)
                    self.FtsbtnOption1.show()
                    self.FtsbtnOption1s.show()

                elif (len(self.optionList) == 2):
                    self.FtsbtnOption2.setText("2. " +self.optionList[1].value)
                    self.FtsbtnOption2.setStyleSheet(self.optionStyle)
                    self.FtsbtnOption2.show()
                    self.FtsbtnOption2s.show()

                elif (len(self.optionList) == 3):
                    self.FtsbtnOption3.setText("3. " +self.optionList[2].value)
                    self.FtsbtnOption3.setStyleSheet(self.optionStyle)
                    self.FtsbtnOption3.show()
                    self.FtsbtnOption3s.show()

                elif (len(self.optionList) == 4):
                    self.FtsbtnOption4.setText("4. " +self.optionList[3].value)
                    self.FtsbtnOption4.setStyleSheet(self.optionStyle)
                    self.FtsbtnOption4.show()
                    self.FtsbtnOption4s.show()

                if int(tempOtp.SelectedOption) == 1:
                    self.selectedOption = len(self.optionList)

                # If it is quiz and option is selected
            if not isSurvey and int(hummFeed["isUserSelectedOption"]) == 1:
                correctOtp = int(hummFeed["CorrectOption"])
                if correctOtp == 1:
                    self.FtsbtnOption1.setStyleSheet(self.optionStyleCorrect)
                elif correctOtp == 2:
                    self.FtsbtnOption2.setStyleSheet(self.optionStyleCorrect)
                elif correctOtp == 3:
                    self.FtsbtnOption3.setStyleSheet(self.optionStyleCorrect)
                elif correctOtp == 4:
                    self.FtsbtnOption4.setStyleSheet(self.optionStyleCorrect)

                if self.selectedOption != int(hummFeed["CorrectOption"]):
                    if self.selectedOption == 1:
                        self.FtsbtnOption1.setStyleSheet(self.optionStyleIncorrect)
                    elif self.selectedOption == 2:
                        self.FtsbtnOption2.setStyleSheet(self.optionStyleIncorrect)
                    elif self.selectedOption == 3:
                        self.FtsbtnOption3.setStyleSheet(self.optionStyleIncorrect)
                    elif self.selectedOption == 4:
                        self.FtsbtnOption4.setStyleSheet(self.optionStyleIncorrect)

            # if survey and user option selected
            elif isSurvey and int(hummFeed["isUserSelectedOption"]) == 1:

                if self.selectedOption == 1:
                    self.FtsbtnOption1.setStyleSheet(self.optionStyleSurveySelected)
                elif self.selectedOption == 2:
                    self.FtsbtnOption2.setStyleSheet(self.optionStyleSurveySelected)
                elif self.selectedOption == 3:
                    self.FtsbtnOption3.setStyleSheet(self.optionStyleSurveySelected)
                elif self.selectedOption == 4:
                    self.FtsbtnOption4.setStyleSheet(self.optionStyleSurveySelected)

                i = 0
                for opt in self.optionList:
                    if i == 0:
                        self.FtslblSurvey1.show()
                        self.FtslblSurvey1.setText(str(opt.AveragePercentage).rstrip() + "%")
                        if self.selectedOption == i + 1:
                            self.FtslblSurvey1.setStyleSheet(self.optionStyleSurveySelected)
                    elif i == 1:
                        self.FtslblSurvey2.show()
                        self.FtslblSurvey2.setText(str(opt.AveragePercentage).rstrip() + "%")
                        if self.selectedOption == i + 1:
                            self.FtslblSurvey2.setStyleSheet(self.optionStyleSurveySelected)
                    elif i == 2:
                        self.FtslblSurvey3.show()
                        self.FtslblSurvey3.setText(str(opt.AveragePercentage).rstrip() + "%")
                        if self.selectedOption == i + 1:
                            self.FtslblSurvey3.setStyleSheet(self.optionStyleSurveySelected)
                    elif i == 3:
                        self.FtslblSurvey4.show()
                        self.FtslblSurvey4.setText(str(opt.AveragePercentage).rstrip() + "%")
                        if self.selectedOption == i + 1:
                            self.FtslblSurvey4.setStyleSheet(self.optionStyleSurveySelected)

                    i = i + 1

        else:
            self.fullTextTitle.hide()
            self.FtsbtnOption1.hide()
            self.FtsbtnOption1s.hide()
            self.FtsbtnOption2.hide()
            self.FtsbtnOption2s.hide()
            self.FtsbtnOption3.hide()
            self.FtsbtnOption3s.hide()
            self.FtsbtnOption4.hide()
            self.FtsbtnOption4s.hide()
            self.FtslblSurvey1.hide()
            self.FtslblSurvey2.hide()
            self.FtslblSurvey3.hide()
            self.FtslblSurvey4.hide()


    def showQuizSurvey(self, show):

        if show:

            self.showQuizSurvey(False)
            hummFeed = self.hummFeeds[self.currentPage]
            self.lblImageQS.show()
            self.lblQuestion.show()

            isSurvey = int(hummFeed["IsSurvey"]) == 1 # 1 for survey, 2 for quiz

            url_image = hummFeed["ImageName"]
            image = QImage()
            image.loadFromData(requests.get(url_image).content)

            pixmap = QtGui.QPixmap(image)
            scaledImage = pixmap.scaled(607, 607)
            self.lblImageQS.setPixmap(scaledImage)
            self.lblQuestion.setText(hummFeed["Question"])

            optionArr = list(hummFeed["Options"])

            self.optionList = []
            self.selectedOption = 0
            for opt in optionArr:
                tempOtp = MahiUtil.HummOptions(opt["value"],opt["AveragePercentage"],opt["SelectedOption"]);
                self.optionList.append(tempOtp)
                if(len(self.optionList) == 1):
                    self.btnOption1.setText(self.optionList[0].value)
                    self.btnOption1.setStyleSheet(self.optionStyle)
                    self.btnOption1.show()
                    self.btnOption1s.show()

                elif(len(self.optionList) == 2):
                    self.btnOption2.setText(self.optionList[1].value)
                    self.btnOption2.setStyleSheet(self.optionStyle)
                    self.btnOption2.show()
                    self.btnOption2s.show()

                elif(len(self.optionList) == 3):
                    self.btnOption3.setText(self.optionList[2].value)
                    self.btnOption3.setStyleSheet(self.optionStyle)
                    self.btnOption3.show()
                    self.btnOption3s.show()

                elif(len(self.optionList) == 4):
                    self.btnOption4.setText(self.optionList[3].value)
                    self.btnOption4.setStyleSheet(self.optionStyle)
                    self.btnOption4.show()
                    self.btnOption4s.show()

                if int(tempOtp.SelectedOption) == 1:
                    self.selectedOption = len(self.optionList)

            # If it is quiz and option is selected
            if not isSurvey and int(hummFeed["isUserSelectedOption"]) == 1:
                correctOtp = int(hummFeed["CorrectOption"])
                if correctOtp == 1:
                    self.btnOption1.setStyleSheet(self.optionStyleCorrect)
                elif correctOtp == 2:
                    self.btnOption2.setStyleSheet(self.optionStyleCorrect)
                elif correctOtp == 3:
                    self.btnOption3.setStyleSheet(self.optionStyleCorrect)
                elif correctOtp == 4:
                    self.btnOption4.setStyleSheet(self.optionStyleCorrect)

                if self.selectedOption != int(hummFeed["CorrectOption"]):
                    if self.selectedOption == 1:
                        self.btnOption1.setStyleSheet(self.optionStyleIncorrect)
                    elif self.selectedOption == 2:
                        self.btnOption2.setStyleSheet(self.optionStyleIncorrect)
                    elif self.selectedOption == 3:
                        self.btnOption3.setStyleSheet(self.optionStyleIncorrect)
                    elif self.selectedOption == 4:
                        self.btnOption4.setStyleSheet(self.optionStyleIncorrect)

            # if survey and user option selected
            elif isSurvey and int(hummFeed["isUserSelectedOption"]) == 1:

                if self.selectedOption == 1:
                    self.btnOption1.setStyleSheet(self.optionStyleSurveySelected)
                elif self.selectedOption == 2:
                    self.btnOption2.setStyleSheet(self.optionStyleSurveySelected)
                elif self.selectedOption == 3:
                    self.btnOption3.setStyleSheet(self.optionStyleSurveySelected)
                elif self.selectedOption == 4:
                    self.btnOption4.setStyleSheet(self.optionStyleSurveySelected)

                i = 0
                for opt in self.optionList:
                    if i == 0:
                        self.lblSurvey1.show()
                        self.lblSurvey1.setText(str(opt.AveragePercentage).rstrip()+"%")
                        if self.selectedOption == i+1:
                            self.lblSurvey1.setStyleSheet(self.optionStyleSurveySelected)
                    elif i == 1:
                        self.lblSurvey2.show()
                        self.lblSurvey2.setText(str(opt.AveragePercentage).rstrip()+"%")
                        if self.selectedOption == i+1:
                            self.lblSurvey2.setStyleSheet(self.optionStyleSurveySelected)
                    elif i == 2:
                        self.lblSurvey3.show()
                        self.lblSurvey3.setText(str(opt.AveragePercentage).rstrip()+"%")
                        if self.selectedOption == i+1:
                            self.lblSurvey3.setStyleSheet(self.optionStyleSurveySelected)
                    elif i == 3:
                        self.lblSurvey4.show()
                        self.lblSurvey4.setText(str(opt.AveragePercentage).rstrip()+"%")
                        if self.selectedOption == i+1:
                            self.lblSurvey4.setStyleSheet(self.optionStyleSurveySelected)

                    i=i+1

            # # if quiz and option not selected
            # elif not isSurvey and int(hummFeed["isUserSelectedOption"]) == 0:
            #     self.enableOptionClicks(True,1)
            # # if survey and option not selected
            # elif isSurvey and int(hummFeed["isUserSelectedOption"]) == 0:
            #     self.enableOptionClicks(True, 2)
        #hide all survey/quiz widgets
        else:
            self.lblImageQS.hide()
            self.lblQuestion.hide()
            self.btnOption1.hide()
            self.btnOption2.hide()
            self.btnOption3.hide()
            self.btnOption4.hide()
            self.btnOption1s.hide()
            self.btnOption2s.hide()
            self.btnOption3s.hide()
            self.btnOption4s.hide()
            self.lblSurvey1.hide()
            self.lblSurvey2.hide()
            self.lblSurvey3.hide()
            self.lblSurvey4.hide()

    def nextClicked(self):
        if self.currentPage < len(self.hummFeeds)-1:
            self.currentPage = self.currentPage+1
            self.ParseHummFeed()

    def prevClicked(self):
        if self.currentPage > 0:
            self.currentPage = self.currentPage-1
            self.ParseHummFeed()

    def option1Clicked(self):

        hummFeed = self.hummFeeds[self.currentPage]
        if int(hummFeed["isUserSelectedOption"]) == 0:
            self.selectedOption = 1
            self.SaveOptionApi(1)

    def option2Clicked(self):
        hummFeed = self.hummFeeds[self.currentPage]
        if int(hummFeed["isUserSelectedOption"]) == 0:
            self.selectedOption = 2
            self.SaveOptionApi(1)

    def option3Clicked(self):
        hummFeed = self.hummFeeds[self.currentPage]
        if int(hummFeed["isUserSelectedOption"]) == 0:
            self.selectedOption = 3
            self.SaveOptionApi(1)

    def option4Clicked(self):
        hummFeed = self.hummFeeds[self.currentPage]
        if int(hummFeed["isUserSelectedOption"]) == 0:
            self.selectedOption = 4
            self.SaveOptionApi(1)

    def FtsOptionClicked(self, opt):

        hummFeed = self.hummFeeds[self.currentPage]
        if int(hummFeed["isUserSelectedOption"]) == 0:
            self.selectedOption = opt
            self.SaveOptionApi(2)


    def SaveOptionApi(self, type):
        try:
            hummFeed = self.hummFeeds[self.currentPage]
            print("feed ID : "+str(hummFeed["Id"])+ "; Selected Option : "+str(self.selectedOption))

            self.loadingDialog.startAnimation()
            saveResponse = MyApis.saveHummSurveyQuizAns(self.selectedOption,str(hummFeed["Id"]))
            self.loadingDialog.stopAnimation()

            if saveResponse != None:

                self.hummFeeds[self.currentPage]["isUserSelectedOption"] = 1

                optionsArray = list(saveResponse["Options"])

                i = 0

                if len(optionsArray) > 0:
                    for opt in optionsArray:
                        self.hummFeeds[self.currentPage]["Options"][i]["AveragePercentage"] = opt["AveragePercentage"]
                        self.hummFeeds[self.currentPage]["Options"][i]["SelectedOption"] = opt["SelectedOption"]
                        print(str(self.hummFeeds[self.currentPage]["Options"][i]))


                        self.optionList[i].AveragePercentage = opt["AveragePercentage"]
                        i = i+1
                # Update manually
                else:
                    self.hummFeeds[self.currentPage]["Options"][self.selectedOption-1]["SelectedOption"] = 1

                hummFeed = self.hummFeeds[self.currentPage]
                # quiz
                if int(hummFeed["IsSurvey"]) == 2 :
                    correctOtp = int(hummFeed["CorrectOption"])
                    if type == 1:
                        if correctOtp == 1:
                            self.btnOption1.setStyleSheet(self.optionStyleCorrect)
                        elif correctOtp == 2:
                            self.btnOption2.setStyleSheet(self.optionStyleCorrect)
                        elif correctOtp == 3:
                            self.btnOption3.setStyleSheet(self.optionStyleCorrect)
                        elif correctOtp == 4:
                            self.btnOption4.setStyleSheet(self.optionStyleCorrect)


                        if self.selectedOption != int(hummFeed["CorrectOption"]):
                            if self.selectedOption == 1:
                                self.btnOption1.setStyleSheet(self.optionStyleIncorrect)
                            elif self.selectedOption == 2:
                                self.btnOption2.setStyleSheet(self.optionStyleIncorrect)
                            elif self.selectedOption == 3:
                                self.btnOption3.setStyleSheet(self.optionStyleIncorrect)
                            elif self.selectedOption == 4:
                                self.btnOption4.setStyleSheet(self.optionStyleIncorrect)

                    else:
                        if correctOtp == 1:
                            self.FtsbtnOption1.setStyleSheet(self.optionStyleCorrect)
                        elif correctOtp == 2:
                            self.FtsbtnOption2.setStyleSheet(self.optionStyleCorrect)
                        elif correctOtp == 3:
                            self.FtsbtnOption3.setStyleSheet(self.optionStyleCorrect)
                        elif correctOtp == 4:
                            self.FtsbtnOption4.setStyleSheet(self.optionStyleCorrect)

                        if self.selectedOption != int(hummFeed["CorrectOption"]):
                            if self.selectedOption == 1:
                                self.FtsbtnOption1.setStyleSheet(self.optionStyleIncorrect)
                            elif self.selectedOption == 2:
                                self.FtsbtnOption2.setStyleSheet(self.optionStyleIncorrect)
                            elif self.selectedOption == 3:
                                self.FtsbtnOption3.setStyleSheet(self.optionStyleIncorrect)
                            elif self.selectedOption == 4:
                                self.FtsbtnOption4.setStyleSheet(self.optionStyleIncorrect)


             # survey
                else:
                    if type == 1:

                        if self.selectedOption == 1:
                            self.btnOption1.setStyleSheet(self.optionStyleSurveySelected)
                        elif self.selectedOption == 2:
                            self.btnOption2.setStyleSheet(self.optionStyleSurveySelected)
                        elif self.selectedOption == 3:
                            self.btnOption3.setStyleSheet(self.optionStyleSurveySelected)
                        elif self.selectedOption == 4:
                            self.btnOption4.setStyleSheet(self.optionStyleSurveySelected)
                        i = 0
                        for opt in self.optionList:
                            if i == 0:
                                self.lblSurvey1.show()
                                self.lblSurvey1.setText(str(opt.AveragePercentage).rstrip() + "%")
                                if self.selectedOption == i + 1:
                                    self.lblSurvey1.setStyleSheet(self.optionStyleSurveySelected)
                            elif i == 1:
                                self.lblSurvey2.show()
                                self.lblSurvey2.setText(str(opt.AveragePercentage).rstrip() + "%")
                                if self.selectedOption == i + 1:
                                    self.lblSurvey2.setStyleSheet(self.optionStyleSurveySelected)
                            elif i == 2:
                                self.lblSurvey3.show()
                                self.lblSurvey3.setText(str(opt.AveragePercentage).rstrip() + "%")
                                if self.selectedOption == i + 1:
                                    self.lblSurvey3.setStyleSheet(self.optionStyleSurveySelected)
                            elif i == 3:
                                self.lblSurvey4.show()
                                self.lblSurvey4.setText(str(opt.AveragePercentage).rstrip() + "%")
                                if self.selectedOption == i + 1:
                                    self.lblSurvey4.setStyleSheet(self.optionStyleSurveySelected)

                            i = i + 1

                    else:
                        if self.selectedOption == 1:
                            self.FtsbtnOption1.setStyleSheet(self.optionStyleSurveySelected)
                        elif self.selectedOption == 2:
                            self.FtsbtnOption2.setStyleSheet(self.optionStyleSurveySelected)
                        elif self.selectedOption == 3:
                            self.FtsbtnOption3.setStyleSheet(self.optionStyleSurveySelected)
                        elif self.selectedOption == 4:
                            self.FtsbtnOption4.setStyleSheet(self.optionStyleSurveySelected)


                        i = 0
                        for opt in self.optionList:
                            if i == 0:
                                self.FtslblSurvey1.show()
                                self.FtslblSurvey1.setText(str(opt.AveragePercentage).rstrip() + "%")
                                if self.selectedOption == i + 1:
                                    self.FtslblSurvey1.setStyleSheet(self.optionStyleSurveySelected)
                            elif i == 1:
                                self.FtslblSurvey2.show()
                                self.FtslblSurvey2.setText(str(opt.AveragePercentage).rstrip() + "%")
                                if self.selectedOption == i + 1:
                                    self.FtslblSurvey2.setStyleSheet(self.optionStyleSurveySelected)
                            elif i == 2:
                                self.FtslblSurvey3.show()
                                self.FtslblSurvey3.setText(str(opt.AveragePercentage).rstrip() + "%")
                                if self.selectedOption == i + 1:
                                    self.FtslblSurvey3.setStyleSheet(self.optionStyleSurveySelected)
                            elif i == 3:
                                self.FtslblSurvey4.show()
                                self.FtslblSurvey4.setText(str(opt.AveragePercentage).rstrip() + "%")
                                if self.selectedOption == i + 1:
                                    self.FtslblSurvey4.setStyleSheet(self.optionStyleSurveySelected)

                            i = i + 1





        except Exception as e:
            print(e.__cause__)


if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Humm()

    window.show()

    # start the app
    sys.exit(App.exec())
