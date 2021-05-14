from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from UI.MyFileList import FileList
import MyDatabase.my_database as db
import API.api_calls as my_apis
import Utility.MahiUtility as Util
import json
import API.my_urls as urls
import requests
import math


class MyProfile(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        # setting title
        self.setWindowTitle("Python ")
        # setting geometry
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setStyleSheet("background-color:#FEC32E")
        self.label.setGeometry(0, 0, 1220, 39)

        self.UiComponents()

        # showing all the widgets
        self.show()

        # try :
        temp = db.fetchProfileDetails()
        if temp!=None:
            self.profileResponse = json.loads(temp)
            self.setProfileData()
        else :
            print("Profile data not available in database")


        # except Exception as E:
        #     print(E.__class__)
        #     print("Something went wrong in fetching profile data from database")

        # try:
        temp = my_apis.fetchProfileDetailsAPI()
        if temp!=None:
            self.profileResponse = json.loads(temp)
            self.setProfileData()
        else:
            print("Profile data not available in API")

        # except Exception as E:
        #     print(E.__class__)
        #     print("Something went wrong in fetching profile data from API")
        # method for widgets

    def UiComponents(self):

        label_pic = QLabel(self)
        label_pic.setPixmap(QPixmap('..\Resources\Group 41.png'))
        label_pic.setGeometry(34, 48, 1164, 469)

        # NAME PROFILE
        self.label1_pic = QLabel(self)
        self.label1_pic.setGeometry(370, 58, 180, 180)
        self.label1_pic.setStyleSheet(" border-radius : 15")


        self.lblName = QLabel(self)
        self.lblName.setGeometry(105,55,243,38)
        self.lblName.setAlignment(Qt.AlignRight)
        self.lblName.setStyleSheet("color:#ee488d; font-size:30px;")


        self.lblAgeGender = QLabel(self)
        self.lblAgeGender.setGeometry(174,89,174,31)
        self.lblAgeGender.setAlignment(Qt.AlignRight)
        self.lblAgeGender.setStyleSheet("color:#373435; font-size:18px;")


        self.lblEmail = QLabel(self)
        self.lblEmail.setGeometry(155,116,193,31)
        self.lblEmail.setAlignment(Qt.AlignRight)
        self.lblEmail.setStyleSheet("color:#373435; font-size:18px;")


        self.lblMobile = QLabel(self)
        self.lblMobile.setGeometry(162,147,186,31)
        self.lblMobile.setAlignment(Qt.AlignRight)
        self.lblMobile.setStyleSheet("color:#373435; font-size:18px;")


        self.lblDob = QLabel(self)
        self.lblDob.setGeometry(227,176,124,31)
        self.lblDob.setAlignment(Qt.AlignRight)
        self.lblDob.setStyleSheet("color:#373435; font-size:18px;")


        self.lblBloodGroup= QLabel(self)
        self.lblBloodGroup.setGeometry(298,208,60,37)
        self.lblBloodGroup.setAlignment(Qt.AlignCenter)
        self.lblBloodGroup.setStyleSheet("color:#373435; font-size:23px; border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")


        self.lblAddress = QLabel(self)
        self.lblAddress.setGeometry(70,253,477,50)
        self.lblAddress.setAlignment(Qt.AlignRight)
        self.lblAddress.setStyleSheet("color:#373435; font-size:18px;")
        self.lblAddress.setWordWrap(True)


        self.lblPharmaNumber = QLabel(self)
        self.lblPharmaNumber.setGeometry(272,303,275,30)
        self.lblPharmaNumber.setAlignment(Qt.AlignRight)
        self.lblPharmaNumber.setStyleSheet("color:#373435; font-size:18px;")



        # Medical History
        l2 = QLabel("Medical History", self)
        l2.setGeometry(573, 40, 150, 29)
        l2.setStyleSheet("color:#EE488D; font: 21px; background-color: #F0F0F3")
        # l2.setStyleSheet("color:#EE488D; font: 21px")

        # Emergency contact
        self.lblEmergency = QLabel("Emergency : 9988776655\n\nCare Taker : 9988776655", self)
        self.lblEmergency.setGeometry(881, 112, 307, 82)
        self.lblEmergency.setAlignment(Qt.AlignCenter)
        self.lblEmergency.setStyleSheet("border-radius : 10; background-color : #00A0B5; color:white; font-size:18px; font-weight:bold")
        self.lblEmergency.setWordWrap(True)

        self.lblDiseaseHistory = QLabel(self)
        self.lblDiseaseHistory.setWordWrap(True)
        self.lblDiseaseHistory.setGeometry(596,98,250,200)
        self.lblDiseaseHistory.setAlignment(Qt.AlignTop)
        self.lblDiseaseHistory.setStyleSheet("font-size:18px;")

        self.btnDiseasePrev = QPushButton("<", self)
        self.btnDiseasePrev.setGeometry(640, 305, 40, 25)
        self.btnDiseasePrev.setStyleSheet(
            "border-radius:10; font:bold; font-size:13px; background-color : #7ACEDA; color:#FFFFFF;text-align: center;")
        self.btnDiseasePrev.clicked.connect(lambda : self.diseaseChanged(0))

        self.btnDiseaseNext = QPushButton(">", self)
        self.btnDiseaseNext.setGeometry(755, 305, 40, 25)
        self.btnDiseaseNext.setStyleSheet(
            "border-radius:10; font:bold; font-size:13px; background-color : #7ACEDA; color:#FFFFFF;text-align: center;")
        self.btnDiseaseNext.clicked.connect(lambda : self.diseaseChanged(1))

        self.lblDiseasePage = QLabel(self)
        self.lblDiseasePage.setGeometry(710, 305, 40, 25)
        self.lblDiseasePage.setStyleSheet("font:normal; font-size:13px; text-align: center; text-color:#373435;")


        # Allergies
        self.lblAllergies = QLabel( self)
        self.lblAllergies.setGeometry(54, 393, 254, 114)
        self.lblAllergies.setStyleSheet("background-color : #F0F0F3; border-radius : 15;  font-size:18px; color:#373435;")
        self.lblAllergies.setWordWrap(True)
        self.lblAllergies.setAlignment(Qt.AlignTop)
        l4 = QLabel("Allergies", self)
        l4.setGeometry(35, 345, 87, 29)
        l4.setStyleSheet("color:#EE488D; font: 21px; background-color: #F0F0F3")


        # Family history

        self.lblFamHistory = QLabel(self)
        self.lblFamHistory.setGeometry(345,395,195,75)
        self.lblFamHistory.setAlignment(Qt.AlignTop)
        self.lblFamHistory.setStyleSheet("background-color : #F0F0F3; border-radius : 15;  font-size:18px; color:#373435;")
        self.lblFamHistory.setWordWrap(True)

        l5 = QLabel("Family History", self)
        l5.setGeometry(325, 345, 139, 29)
        l5.setStyleSheet("color:#EE488D; font: 21px; background-color: #F0F0F3")
        self.btnFamilyPrev = QPushButton("<", self)
        self.btnFamilyPrev.setGeometry(372, 475, 40, 25)
        self.btnFamilyPrev.setStyleSheet(
            "border-radius:10; font:bold; font-size:13px; background-color : #7ACEDA; color:#FFFFFF;text-align: center;")
        self.btnFamilyPrev.clicked.connect(lambda : self.famHistoryChanged(0))
        self.btnFamilyNext = QPushButton(">", self)
        self.btnFamilyNext.setGeometry(472, 475, 40, 25)
        self.btnFamilyNext.setStyleSheet(
            "border-radius:10; font:bold; font-size:13px; background-color : #7ACEDA; color:#FFFFFF;text-align: center;")
        self.btnFamilyNext.clicked.connect(lambda : self.famHistoryChanged(1))

        self.lblFamilyPage = QLabel(self)
        self.lblFamilyPage.setGeometry(432, 475, 40, 25)
        self.lblFamilyPage.setStyleSheet("font:normal; font-size:13px; text-align: center; text-color:#373435;")

        # Birth History
        self.lblGestation = QLabel( self)
        self.lblGestation.setGeometry(593, 393, 176, 30)
        self.lblGestation.setStyleSheet("background-color : #F0F0F3; border-radius : 15;  font-size:18px;")
        self.lblGestation.setAlignment(Qt.AlignLeft)
        self.lblGestation.setWordWrap(True)

        self.lblBirthOrder = QLabel('<font color="#ee488d">Birth Order: </font><font color="#373435">2nd Born</font>', self)
        self.lblBirthOrder.setGeometry(593, 423, 176, 30)
        self.lblBirthOrder.setStyleSheet("background-color : #F0F0F3; border-radius : 15;  font-size:18px;")
        self.lblBirthOrder.setAlignment(Qt.AlignLeft)
        self.lblBirthOrder.setWordWrap(True)

        self.lblDelivery = QLabel('<font color="#ee488d">Delivery: </font><font color="#373435">Normal</font>', self)
        self.lblDelivery.setGeometry(593, 453, 176, 30)
        self.lblDelivery.setStyleSheet("background-color : #F0F0F3; border-radius : 15;  font-size:18px;")
        self.lblDelivery.setAlignment(Qt.AlignLeft)
        self.lblDelivery.setWordWrap(True)

        self.lblBirthWeight= QLabel('<font color="#ee488d">Birth Weight: </font><font color="#373435">2.5kg</font>', self)
        self.lblBirthWeight.setGeometry(593, 483, 176, 30)
        self.lblBirthWeight.setStyleSheet("background-color : #F0F0F3; border-radius : 15;  font-size:18px;")
        self.lblBirthWeight.setAlignment(Qt.AlignLeft)
        self.lblBirthWeight.setWordWrap(True)
        l6 = QLabel("Birth History", self)
        l6.setGeometry(575, 345, 124, 29)
        l6.setStyleSheet("color:#EE488D; font: 21px; background-color: #F0F0F3")

        # medical procedure

        l7 = QLabel("Medical Procedure", self)
        l7.setGeometry(888, 202, 177, 29)
        l7.setStyleSheet("color:#EE488D; font: 21px; background-color: #F0F0F3")

        self.lblProcedureName= QLabel('<font color="#ee488d">Name: </font><font color="#373435">Shalini Mehra</font>', self)
        self.lblProcedureName.setGeometry(900, 258, 198, 30)
        self.lblProcedureName.setStyleSheet("background-color : #F0F0F3; border-radius : 15;  font-size:18px;")
        self.lblProcedureName.setAlignment(Qt.AlignLeft)
        self.lblProcedureName.setWordWrap(True)

        self.lblIcd= QLabel('<font color="#ee488d">ICD: </font><font color="#373435">Code : 6109</font>', self)
        self.lblIcd.setGeometry(900, 283, 198, 30)
        self.lblIcd.setStyleSheet("background-color : #F0F0F3; border-radius : 15;  font-size:18px;")
        self.lblIcd.setAlignment(Qt.AlignLeft)
        self.lblIcd.setWordWrap(True)

        self.lblProcedureDate= QLabel('<font color="#ee488d">Date: </font><font color="#373435">25/12/2020</font>', self)
        self.lblProcedureDate.setGeometry(900, 308, 198, 30)
        self.lblProcedureDate.setStyleSheet("background-color : #F0F0F3; border-radius : 15;  font-size:18px;")
        self.lblProcedureDate.setAlignment(Qt.AlignLeft)
        self.lblProcedureDate.setWordWrap(True)

        self.lblHospital= QLabel('<font color="#ee488d">Hospital: </font><font color="#373435">CIMS</font>', self)
        self.lblHospital.setGeometry(900, 333, 198, 30)
        self.lblHospital.setStyleSheet("background-color : #F0F0F3; border-radius : 15;  font-size:18px;")
        self.lblHospital.setAlignment(Qt.AlignLeft)
        self.lblHospital.setWordWrap(True)

        self.lblDoctor= QLabel('<font color="#ee488d">Dr. </font><font color="#373435">Dhiren Shah</font>', self)
        self.lblDoctor.setGeometry(900, 358, 198, 30)
        self.lblDoctor.setStyleSheet("background-color : #F0F0F3; border-radius : 15;  font-size:18px;")
        self.lblDoctor.setAlignment(Qt.AlignLeft)
        self.lblDoctor.setWordWrap(True)

        self.lblRecovery= QLabel('<font color="#ee488d">Recovery: </font><font color="#373435">Complications</font>', self)
        self.lblRecovery.setGeometry(900, 383, 198, 30)
        self.lblRecovery.setStyleSheet("background-color : #F0F0F3; border-radius : 15;  font-size:18px;")
        self.lblRecovery.setAlignment(Qt.AlignLeft)
        self.lblRecovery.setWordWrap(True)

        self.lblComments= QLabel('There was zero to no post-operative complication, however I got diagnosed with chronic hypertension after surgery.', self)
        self.lblComments.setGeometry(900, 413, 285, 54)
        self.lblComments.setStyleSheet("background-color : #F0F0F3; border-radius : 15;text-color:#373435;  font-size:15px;")
        self.lblComments.setAlignment(Qt.AlignLeft)
        self.lblComments.setWordWrap(True)

        self.btnProcedurePrev = QPushButton("<",self)
        self.btnProcedurePrev.setGeometry(960,475,40,25)
        self.btnProcedurePrev.setStyleSheet("border-radius:10; font:bold; font-size:13px; background-color : #7ACEDA; color:#FFFFFF;text-align: center;")
        self.btnProcedurePrev.clicked.connect(self.prevProcedureClicked)
        self.btnProcedureNext = QPushButton(">",self)
        self.btnProcedureNext.setGeometry(1060,475,40,25)
        self.btnProcedureNext.setStyleSheet("border-radius:10; font:bold; font-size:13px; background-color : #7ACEDA; color:#FFFFFF;text-align: center;")
        self.btnProcedureNext.clicked.connect(self.nextProcedureClicked)

        self.lblProcedurePage = QLabel(self)
        self.lblProcedurePage.setGeometry(1018,475,40,25)
        self.lblProcedurePage.setStyleSheet("font:normal; font-size:13px; text-align: center; text-color:#373435;")


        # Buttons on My Profile
        lbmi = QLabel("BMI", self)
        lbmi.setGeometry(71, 634, 34, 26)
        lbmi.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")

        self.btn_bmi = QPushButton( self)
        self.btn_bmi.setGeometry(35, 544, 106, 90)
        self.btn_bmi.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; font:bold; font-size:24px; text-align: center;")
        self.btn_bmi.setGraphicsEffect(Util.getNeuShadow(0))

        self.lblBmiDate = QLabel(self)
        self.lblBmiDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblBmiDate.setGeometry(65,549,70,16)
        self.lblBmiDate.setAlignment(Qt.AlignRight)

        self.lblBmiUnit = QLabel(self)
        self.lblBmiUnit.setStyleSheet("color:white;font-size:15px; background-color : #7ACEDA")
        self.lblBmiUnit.setGeometry(65,608,70,20)
        self.lblBmiUnit.setAlignment(Qt.AlignRight)

        btn_bmiT = QPushButton(self)
        btn_bmiT.setGeometry(35, 544, 106, 90)
        btn_bmiT.setStyleSheet("border-radius : 10; background-color : #007ACEDA")
        btn_bmiT.setGraphicsEffect(Util.getNeuShadow(0))
        btn_bmiT.clicked.connect(self.clickme)



        lbp = QLabel("Blood Pressure", self)
        lbp.setGeometry(198, 634, 132, 20)
        lbp.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")

        btn_bp = QPushButton(self)
        btn_bp.setGeometry(151, 544, 222, 90)
        btn_bp.setGraphicsEffect(Util.getNeuShadow(0))
        btn_bp.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; font:bold; font-size:24px; text-align: center;")

        self.lblBpValue = QLabel(self)
        self.lblBpValue.setStyleSheet("font:bold; font-size:24px; text-align: center; background-color:#00AAAAAA")
        self.lblBpValue.setGeometry(163,572,200,33)

        self.lblBpDate = QLabel(self)
        self.lblBpDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblBpDate.setGeometry(295,549,70,16)
        self.lblBpDate.setAlignment(Qt.AlignRight)

        self.lblBpUnit = QLabel(self)
        self.lblBpUnit.setStyleSheet("color:white;font-size:15px; background-color : #7ACEDA")
        self.lblBpUnit.setGeometry(295,608,70,20)
        self.lblBpUnit.setAlignment(Qt.AlignRight)

        btn_bpT = QPushButton(self)
        btn_bpT.setGeometry(151, 544, 222, 90)
        btn_bpT.setStyleSheet("border-radius : 10; background-color : #007ACEDA")
        btn_bpT.setGraphicsEffect(Util.getNeuShadow(0))
        btn_bpT.clicked.connect(self.clickme)



        lhr = QLabel("Heart Rate", self)
        lhr.setGeometry(389, 634, 110, 29)
        lhr.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")
        self.btn_hr = QPushButton( self)
        self.btn_hr.setGeometry(383, 544, 107, 90)
        self.btn_hr.setGraphicsEffect(Util.getNeuShadow(0))
        self.btn_hr.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; font:bold; font-size:24px; text-align: center;")

        self.lblHrDate = QLabel(self)
        self.lblHrDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblHrDate.setGeometry(412,549,70,16)
        self.lblHrDate.setAlignment(Qt.AlignRight)

        self.lblHrUnit = QLabel(self)
        self.lblHrUnit.setStyleSheet("color:white;font-size:15px; background-color : #7ACEDA")
        self.lblHrUnit.setGeometry(412,608,70,20)
        self.lblHrUnit.setAlignment(Qt.AlignRight)

        btn_hrT = QPushButton("", self)
        btn_hrT.setGeometry(383, 544, 107, 90)
        btn_hrT.setStyleSheet(
            "border-radius : 10; background-color : #007ACEDA; ")
        btn_hrT.setGraphicsEffect(Util.getNeuShadow(0))
        btn_hrT.clicked.connect(self.clickme)



        lhg = QLabel("Haemoglobin", self)
        lhg.setGeometry(500, 634, 139, 29)
        lhg.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")
        self.btn_hg = QPushButton("", self)
        self.btn_hg.setGeometry(500, 544, 106, 90)
        self.btn_hg.setGraphicsEffect(Util.getNeuShadow(0))
        self.btn_hg.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; font:bold; font-size:24px; text-align: center;")

        self.lblHgDate = QLabel(self)
        self.lblHgDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblHgDate.setGeometry(526,549,70,16)
        self.lblHgDate.setAlignment(Qt.AlignRight)

        self.lblHgUnit = QLabel(self)
        self.lblHgUnit.setStyleSheet("color:white;font-size:15px; background-color : #7ACEDA")
        self.lblHgUnit.setGeometry(526,608,70,20)
        self.lblHgUnit.setAlignment(Qt.AlignRight)

        btn_hgT = QPushButton("", self)
        btn_hgT.setGeometry(500, 544, 106, 90)
        btn_hgT.setStyleSheet(
            "border-radius : 10; background-color : #007ACEDA;")
        btn_hgT.setGraphicsEffect(Util.getNeuShadow(0))
        btn_hgT.clicked.connect(self.clickme)



        lhba = QLabel("HBA1C", self)
        lhba.setGeometry(639, 634, 71, 29)
        lhba.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")
        self.btn_hba = QPushButton("", self)
        self.btn_hba.setGeometry(616, 544, 106, 90)
        self.btn_hba.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; font:bold; font-size:24px; text-align: center;")
        self.btn_hba.setGraphicsEffect(Util.getNeuShadow(0))

        self.lblHba1cDate = QLabel(self)
        self.lblHba1cDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblHba1cDate.setGeometry(645,549,70,16)
        self.lblHba1cDate.setAlignment(Qt.AlignRight)

        self.lblHba1cUnit = QLabel(self)
        self.lblHba1cUnit.setStyleSheet("color:white;font-size:15px; background-color : #7ACEDA")
        self.lblHba1cUnit.setGeometry(645,608,70,20)
        self.lblHba1cUnit.setAlignment(Qt.AlignRight)

        btn_hba = QPushButton("", self)
        btn_hba.setGeometry(616, 544, 106, 90)
        btn_hba.setStyleSheet(
            "border-radius : 10; background-color : #007ACEDA;")
        btn_hba.setGraphicsEffect(Util.getNeuShadow(0))
        btn_hba.clicked.connect(self.clickme)



        lsugar = QLabel("Weight", self)
        lsugar.setGeometry(756, 634, 59, 29)
        lsugar.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")
        self.btn_sugar = QPushButton("", self)
        self.btn_sugar.setGeometry(732, 544, 106, 90)
        self.btn_sugar.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; font:bold; font-size:24px; text-align: center;")
        self.btn_sugar.setGraphicsEffect(Util.getNeuShadow(0))

        self.lblSugarDate = QLabel(self)
        self.lblSugarDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblSugarDate.setGeometry(762,549,70,16)
        self.lblSugarDate.setAlignment(Qt.AlignRight)

        self.lblSugarUnit = QLabel(self)
        self.lblSugarUnit.setStyleSheet("color:white;font-size:15px; background-color : #7ACEDA")
        self.lblSugarUnit.setGeometry(762,608,70,20)
        self.lblSugarUnit.setAlignment(Qt.AlignRight)

        btn_sugarT = QPushButton("", self)
        btn_sugarT.setGeometry(732, 544, 106, 90)
        btn_sugarT.setStyleSheet(
            "border-radius : 10; background-color : #007ACEDA;")
        btn_sugarT.setGraphicsEffect(Util.getNeuShadow(0))
        btn_sugarT.clicked.connect(self.clickme)



        lcho = QLabel("Cholesterol", self)
        lcho.setGeometry(858, 634, 105, 29)
        lcho.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")
        self.btn_choles = QPushButton("", self)
        self.btn_choles.setGeometry(849, 544, 106, 90)
        self.btn_choles.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; font:bold; font-size:24px; text-align: center;")
        self.btn_choles.setGraphicsEffect(Util.getNeuShadow(0))

        self.lblCholDate = QLabel(self)
        self.lblCholDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblCholDate.setGeometry(879,549,70,16)
        self.lblCholDate.setAlignment(Qt.AlignRight)

        self.lblCholUnit = QLabel(self)
        self.lblCholUnit.setStyleSheet("color:white;font-size:15px; background-color : #7ACEDA")
        self.lblCholUnit.setGeometry(879,608,70,20)
        self.lblCholUnit.setAlignment(Qt.AlignRight)

        btn_cholesT = QPushButton("", self)
        btn_cholesT.setGeometry(849, 544, 106, 90)
        btn_cholesT.setStyleSheet(
            "border-radius : 10; background-color : #007ACEDA;")
        btn_cholesT.setGraphicsEffect(Util.getNeuShadow(0))
        btn_cholesT.clicked.connect(self.clickme)



        lpt = QLabel("Pt/INR", self)
        lpt.setGeometry(992, 634, 57, 29)
        lpt.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")
        self.btn_pt = QPushButton("", self)
        self.btn_pt.setGeometry(965, 544, 106, 90)
        self.btn_pt.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; font:bold; font-size:24px; text-align: center;")
        self.btn_pt.setGraphicsEffect(Util.getNeuShadow(0))

        self.lblPtDate = QLabel(self)
        self.lblPtDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblPtDate.setGeometry(994,549,70,16)
        self.lblPtDate.setAlignment(Qt.AlignRight)

        self.lblPtUnit = QLabel(self)
        self.lblPtUnit.setStyleSheet("color:white;font-size:15px; background-color : #7ACEDA")
        self.lblPtUnit.setGeometry(994,608,70,20)
        self.lblPtUnit.setAlignment(Qt.AlignRight)

        btn_ptT = QPushButton("", self)
        btn_ptT.setGeometry(965, 544, 106, 90)
        btn_ptT.setStyleSheet(
            "border-radius : 10; background-color : #007ACEDA;")
        btn_ptT.setGraphicsEffect(Util.getNeuShadow(0))
        btn_ptT.clicked.connect(self.clickme)



        ltemp = QLabel("Temparature", self)
        ltemp.setGeometry(1084, 634, 109, 29)
        ltemp.setStyleSheet("color:#006CB5; font: 19px; background-color: #F0F0F3")
        self.btn_temp = QPushButton("", self)
        self.btn_temp.setGeometry(1081, 544, 106, 90)
        self.btn_temp.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; font:bold; font-size:24px; text-align: center;")
        self.btn_temp.setGraphicsEffect(Util.getNeuShadow(0))

        self.lblTempDate = QLabel(self)
        self.lblTempDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblTempDate.setGeometry(1109,549,70,16)
        self.lblTempDate.setAlignment(Qt.AlignRight)

        self.lblTempUnit = QLabel(self)
        self.lblTempUnit.setStyleSheet("color:white;font-size:15px; background-color : #7ACEDA")
        self.lblTempUnit.setGeometry(1109,608,70,20)
        self.lblTempUnit.setAlignment(Qt.AlignRight)

        btn_tempT = QPushButton("", self)
        btn_tempT.setGeometry(1081, 544, 106, 90)
        btn_tempT.setStyleSheet(
            "border-radius : 10; background-color : #007ACEDA;")
        btn_tempT.setGraphicsEffect(Util.getNeuShadow(0))
        btn_tempT.clicked.connect(self.clickme)



        btn_back = QPushButton("", self)
        btn_back.setGeometry(879, 55, 112, 41)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('..\Resources\\backButton.png'))
        btn_back.setIconSize(QtCore.QSize(112, 41))
        btn_back.clicked.connect(self.close)

        syncBtn = QPushButton(self)
        syncBtn.setGeometry(1002, 55, 45, 41)
        syncBtn.setStyleSheet("border-radius: 8; background-color: #F0F0F3")
        syncBtn.setIcon(QtGui.QIcon('..\Resources\\syncBtn.png'))
        syncBtn.setIconSize(QtCore.QSize(45, 41))
        syncBtn.setGraphicsEffect(Util.getNeuShadow(0))
        syncBtn.clicked.connect(self.close)

        btn_files = QPushButton("", self)
        btn_files.setGeometry(1064, 55, 122, 41)
        btn_files.setStyleSheet("border-radius : 8; background-color: #00A0B5; text-align:left")
        btn_files.setIcon(QtGui.QIcon('..\Resources\medFiles.png'))
        btn_files.setIconSize(QtCore.QSize(122, 41))
        btn_files.clicked.connect(self.medfiles)

    def clickme(self):
        # printing pressed
        print("pressed")

    def medfiles(self):
        self.m = FileList()
        self.m.show()
        # self.hide()

    def setProfileData(self):
        print("")

        # Personalized data
        personalize_data = self.profileResponse["personalize_data"][0]
        name = personalize_data["firstName"] + personalize_data["lastName"]
        user_img = urls.BASE_URL + personalize_data["user_image"]  # profile image url
        # age = str(self.profileResponse["age"])
        gender = personalize_data["gender"]
        contact_num = str(personalize_data["userContactNumber"])
        email = personalize_data["userEmail"]
        dob = personalize_data["dob"]
        address = personalize_data["address1"]
        bgroup = personalize_data["blood_group"]
        pharmacyNumber = personalize_data["pharmacy_number"]

        self.lblName.setText(name)
        self.lblAgeGender.setText(gender)
        self.lblMobile.setText(contact_num)
        self.lblEmail.setText(email)
        self.lblDob.setText(dob)
        self.lblAddress.setText(address)
        self.lblBloodGroup.setText(bgroup)
        self.lblPharmaNumber.setText(pharmacyNumber)

        image = QImage()
        image.loadFromData(requests.get(user_img).content)

        pixmap = QtGui.QPixmap(image)
        scaledImage = pixmap.scaled(180, 180)
        self.label1_pic.setPixmap(scaledImage)

        # Allergies
        allergies = ""
        i = 0
        for allergy in self.profileResponse["allergy_data"]:
            allergies = allergies + allergy["allergy_name"]
            if i < len(self.profileResponse["allergy_data"])-1:
                allergies = allergies+", "
            i = i+1

        self.lblAllergies.setText(allergies)

        # Birth History
        birth_history = self.profileResponse["birth_history_data"]

        self.lblGestation.setText('<font color="#ee488d">Gestation: </font><font color="#373435">'+birth_history["gstation"]+'</font>')
        self.lblBirthOrder.setText('<font color="#ee488d">Birth Order: </font><font color="#373435">'+birth_history["birth_order"]+'</font>')
        self.lblDelivery.setText('<font color="#ee488d">Delivery: </font><font color="#373435">'+birth_history["delivery"]+'</font>')
        self.lblBirthWeight.setText('<font color="#ee488d">Birth Weight: </font><font color="#373435">'+birth_history["birth_weight"]+'kg</font>')

        # Medical Procedure
        medical_procedures = self.profileResponse["medical_procedure_data"]
        self.totalProcedures = 0
        self.procedurePage = -1

        if len(medical_procedures)>0:
            self.procedurePage = 0
            self.totalProcedures = len(medical_procedures)
            self.setMedicalProcedure()

        # Family History
        family_history = self.profileResponse["famliy_disease_data"]
        self.totalFamilyMembers = 0
        self.familyHistoryPage = -1
        if len(family_history)>0:
            self.familyHistoryPage = 0
            self.totalFamilyMembers = len(family_history)
            self.setFamHistory()

        # My Disease
        disease_history = self.profileResponse["disease_data"]["my_disease"]

        self.totalDieases = 0
        self.diseasePage = -1
        self.diseaseList = []
        if len(disease_history)>0:
            self.diseasePage = 0
            for i in disease_history:
                self.totalDieases = self.totalDieases+len(i)

                for disease in i:
                    self.diseaseList.append(disease)

            self.setDiseaseData()


        # Vital Data

        vital_data = self.profileResponse["vital_data"]

        self.lblBmiDate.setText(str(vital_data["WEIGHT"]["latest_measured_on"]).split(" ")[0])
        height = float(str(vital_data["HEIGHT"]["latest_value"]).split(" ")[0])/100
        weight = float(str(vital_data["WEIGHT"]["latest_value"]).split(" ")[0])
        bmiValue = weight/(height*height)
        self.btn_bmi.setText(str(round(bmiValue,1)))
        self.lblBmiUnit.setText("Kg/m2")

        temp = str(vital_data["BLOOD PRESSURE"]["latest_value"]).split(" ")[0].split("/")
        bpValue = '<font color="#fff">'+temp[0]+'</font><font color="#006CB5"> SYS</font>   <font color="#fff">' \
                    ''+temp[1]+'</font><font color="#006CB5"> DIA</font>'
        self.lblBpValue.setText(bpValue)
        self.lblBpDate.setText(str(vital_data["BLOOD PRESSURE"]["latest_measured_on"]).split(" ")[0])
        self.lblBpUnit.setText(str(vital_data["BLOOD PRESSURE"]["vital_measured"]))

        self.btn_hr.setText(str(vital_data["HEART RATE"]["latest_value"]).split(" ")[0])
        self.lblHrDate.setText(str(vital_data["HEART RATE"]["latest_measured_on"]).split(" ")[0])
        self.lblHrUnit.setText(str(vital_data["HEART RATE"]["vital_measured"]))


        self.btn_hg.setText(str(vital_data["HAEMOGLOBIN"]["latest_value"]).split(" ")[0])
        self.lblHgDate.setText(str(vital_data["HAEMOGLOBIN"]["latest_measured_on"]).split(" ")[0])
        self.lblHgUnit.setText(str(vital_data["HAEMOGLOBIN"]["vital_measured"]))


        self.btn_hba.setText(str(vital_data["HBA1C"]["latest_value"]).split(" ")[0])
        self.lblHba1cDate.setText(str(vital_data["HBA1C"]["latest_measured_on"]).split(" ")[0])
        self.lblHba1cUnit.setText(str(vital_data["HBA1C"]["vital_measured"]))


        self.btn_choles.setText(str(vital_data["CHOLESTEROL"]["latest_value"]).split(" ")[0])
        self.lblCholDate.setText(str(vital_data["CHOLESTEROL"]["latest_measured_on"]).split(" ")[0])
        self.lblCholUnit.setText(str(vital_data["CHOLESTEROL"]["vital_measured"]))


        self.btn_pt.setText(str(vital_data["PT/INR"]["latest_value"]).split(" ")[0])
        self.lblPtDate.setText(str(vital_data["PT/INR"]["latest_measured_on"]).split(" ")[0])
        self.lblPtUnit.setText(str(vital_data["PT/INR"]["vital_measured"]))


        self.btn_temp.setText(str(vital_data["TEMPERATURE"]["latest_value"]).split(" ")[0])
        self.lblTempDate.setText(str(vital_data["TEMPERATURE"]["latest_measured_on"]).split(" ")[0])
        self.lblTempUnit.setText(str(vital_data["TEMPERATURE"]["vital_measured"]))



        self.btn_sugar.setText(str(vital_data["WEIGHT"]["latest_value"]).split(" ")[0])
        self.lblSugarDate.setText(str(vital_data["WEIGHT"]["latest_measured_on"]).split(" ")[0])
        self.lblSugarUnit.setText(str(vital_data["WEIGHT"]["vital_measured"]))

        # self.btn_sugar.setText("N.A.")




    def setDiseaseData(self):
        print("")

        self.lblDiseasePage.setText(str(self.diseasePage+1)+"/"+str(math.ceil(self.totalDieases/3)))
        index = self.diseasePage*3
        loop = self.totalDieases-index
        if loop>3:
            loop = 3

        diseaseString = ""
        for i in range(loop):
            diseaseString = diseaseString+'<font color="#ee488d">' + self.diseaseList[index+i]["disease_name"] + '<br/></font>'
            diseaseString = diseaseString+'<font color="#373435">'+self.diseaseList[index+i]["start_date"]+\
                            ' - '+self.diseaseList[index+i]["end_date"]+'<br/><br/></font>'

        self.lblDiseaseHistory.setText(diseaseString)

    def diseaseChanged(self,type):
        if type == 0:
            if self.diseasePage > 0:
                self.diseasePage = self.diseasePage-1
                self.setDiseaseData()

        elif type == 1:
            if (self.diseasePage+1)*3 < self.totalDieases :
                self.diseasePage = self.diseasePage + 1
                self.setDiseaseData()

    def setFamHistory(self):
        famHistory = self.profileResponse["famliy_disease_data"][self.familyHistoryPage]
        self.lblFamilyPage.setText(str(self.familyHistoryPage+1)+"/"+str(self.totalFamilyMembers))
        diseases = ""
        j = 1
        for i in famHistory['disease_histry']:
            diseases = diseases+i["disease_name"]
            if j < len(famHistory['disease_histry']):
                diseases = diseases+", "
            j = j+1

        self.lblFamHistory.setText('<font color="#ee488d">' + str(famHistory['relation']) + ': </font><font color="#373435">'+diseases+'</font>')

    def famHistoryChanged(self,type):

        if type == 0:
            if self.familyHistoryPage > 0:
                self.familyHistoryPage = self.familyHistoryPage-1
                self.setFamHistory()

        elif type == 1:

            if self.familyHistoryPage < self.totalFamilyMembers -1:
                self.familyHistoryPage = self.familyHistoryPage + 1
                self.setFamHistory()

    def setMedicalProcedure(self):

        medical_procedure = self.profileResponse["medical_procedure_data"][self.procedurePage]
        self.lblProcedureName.setText(
            '<font color="#ee488d">Name: </font><font color="#373435">' + medical_procedure["p_name"] + '</font>')
        self.lblIcd.setText('<font color="#ee488d">ICD: </font><font color="#373435">' + medical_procedure[
            "icd_code"] + '</font>')
        self.lblProcedureDate.setText(
            '<font color="#ee488d">Date: </font><font color="#373435">' + medical_procedure[
                "date_of_p"] + '</font>')
        self.lblHospital.setText(
            '<font color="#ee488d">Hospital: </font><font color="#373435">' + medical_procedure[
                "where_p"] + '</font>')
        self.lblDoctor.setText(
            '<font color="#ee488d">By: </font><font color="#373435">' + medical_procedure["by_whom"] + '</font>')
        self.lblRecovery.setText('<font color="#ee488d">Recovery: </font><font color="#373435">' + medical_procedure["recovery"] + '</font>')
        self.lblComments.setText(medical_procedure["special_cmt"])

        self.lblProcedurePage.setText(str(self.procedurePage+1)+"/"+str(self.totalProcedures))

    def nextProcedureClicked(self):
        if self.procedurePage < self.totalProcedures-1:
            self.procedurePage = self.procedurePage+1
            self.setMedicalProcedure()

    def prevProcedureClicked(self):
        if self.procedurePage > 0 :
            self.procedurePage = self.procedurePage-1
            self.setMedicalProcedure()

    def nextFamilyClicked(self):
        if self.procedurePage < self.totalProcedures-1:
            self.procedurePage = self.procedurePage+1
            self.setMedicalProcedure()

    def prevFamilyClicked(self):
        if self.procedurePage > 0:
            self.procedurePage = self.procedurePage-1
            self.setMedicalProcedure()


if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = MyProfile()

    window.show()

    # start the app
    sys.exit(App.exec_())
