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
            print("Profile data not available in database")

        # except Exception as E:
        #     print(E.__class__)
        #     print("Something went wrong in fetching profile data from API")
        # method for widgets

    def UiComponents(self):
        label1_pic = QLabel(self)
        label1_pic.setPixmap(QPixmap('..\Resources\Group 41.png'))
        label1_pic.setGeometry(34, 48, 1164, 469)

        # NAME PROFILE
        label1_pic = QLabel(self)
        label1_pic.setPixmap(QPixmap('..\Resources\pic.png'))
        label1_pic.setGeometry(370, 51, 184, 180)
        label1_pic.setStyleSheet(" border-radius : 15")


        self.lblName = QLabel("Shalini Mehra",self)
        self.lblName.setGeometry(105,55,243,38)
        self.lblName.setAlignment(Qt.AlignRight)
        self.lblName.setStyleSheet("color:#ee488d; font-size:30px;")


        self.lblAgeGender = QLabel("30 Years    Female",self)
        self.lblAgeGender.setGeometry(174,89,174,31)
        self.lblAgeGender.setAlignment(Qt.AlignRight)
        self.lblAgeGender.setStyleSheet("color:#373435; font-size:18px;")


        self.lblEmail = QLabel("shalinimehra@gmail.com",self)
        self.lblEmail.setGeometry(155,116,193,31)
        self.lblEmail.setAlignment(Qt.AlignRight)
        self.lblEmail.setStyleSheet("color:#373435; font-size:18px;")


        self.lblMobile = QLabel("9988776655",self)
        self.lblMobile.setGeometry(162,147,186,31)
        self.lblMobile.setAlignment(Qt.AlignRight)
        self.lblMobile.setStyleSheet("color:#373435; font-size:18px;")


        self.lblDob = QLabel("25/09/1992",self)
        self.lblDob.setGeometry(227,176,124,31)
        self.lblDob.setAlignment(Qt.AlignRight)
        self.lblDob.setStyleSheet("color:#373435; font-size:18px;")


        self.lblBloodGroup= QLabel("AB+",self)
        self.lblBloodGroup.setGeometry(298,208,60,37)
        self.lblBloodGroup.setAlignment(Qt.AlignCenter)
        self.lblBloodGroup.setStyleSheet("color:#373435; font-size:23px; border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")


        self.lblAddress = QLabel("423,Iscon Emporio, Near Star Bazar, Jodhpur Cross Road,Satellite Ahmedabad, Gujarat, 380009",self)
        self.lblAddress.setGeometry(70,253,477,50)
        self.lblAddress.setAlignment(Qt.AlignRight)
        self.lblAddress.setStyleSheet("color:#373435; font-size:18px;")
        self.lblAddress.setWordWrap(True)


        self.lblPharmaNumber = QLabel("9887776655",self)
        self.lblPharmaNumber.setGeometry(272,303,275,30)
        self.lblPharmaNumber.setAlignment(Qt.AlignRight)
        self.lblPharmaNumber.setStyleSheet("color:#373435; font-size:18px;")



        # Medical History
        l2 = QLabel("Medical History", self)
        l2.setGeometry(573, 40, 150, 29)
        l2.setStyleSheet("color:#EE488D; font: 21px; background-color: #F0F0F3")
        lblMedHistory = QLabel("Multi label i.e With multi line", self)
        lblMedHistory.setGeometry(600, 100, 250, 220)
        lblMedHistory.setStyleSheet(" background-color : #F0F0F3")
        # making it multi line
        lblMedHistory.setWordWrap(True)
        # l2.setStyleSheet("color:#EE488D; font: 21px")

        # Emergency contact
        label3 = QLabel("Emergency", self)
        label3.setGeometry(881, 112, 307, 82)
        label3.setStyleSheet("border-radius : 10; background-color : #00A0B5 ")
        label3.setWordWrap(True)

        # Allergies
        self.lblAllergies = QLabel("lactose intolerent, Peanuts, Preservatives", self)
        self.lblAllergies.setGeometry(54, 393, 254, 114)
        self.lblAllergies.setStyleSheet("background-color : #F0F0F3; border-radius : 15;  font-size:18px; color:#373435;")
        self.lblAllergies.setWordWrap(True)
        self.lblAllergies.setAlignment(Qt.AlignTop)
        l4 = QLabel("Allergies", self)
        l4.setGeometry(35, 345, 87, 29)
        l4.setStyleSheet("color:#EE488D; font: 21px; background-color: #F0F0F3")


        # Family history
        lblFamilyHistory = QLabel("Multi label i.e With multi line", self)
        lblFamilyHistory.setGeometry(344, 393, 213, 119)
        lblFamilyHistory.setStyleSheet("background-color : #F0F0F3; border-radius : 15")
        lblFamilyHistory.setWordWrap(True)
        l5 = QLabel("Family History", self)
        l5.setGeometry(325, 345, 139, 29)
        l5.setStyleSheet("color:#EE488D; font: 21px; background-color: #F0F0F3")

        # Birth History
        self.lblGestation = QLabel('<font color="#ee488d">Gestation: </font><font color="#373435">Full Term</font>', self)
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

        self.lblDate= QLabel('<font color="#ee488d">Date: </font><font color="#373435">25/12/2020</font>', self)
        self.lblDate.setGeometry(900, 308, 198, 30)
        self.lblDate.setStyleSheet("background-color : #F0F0F3; border-radius : 15;  font-size:18px;")
        self.lblDate.setAlignment(Qt.AlignLeft)
        self.lblDate.setWordWrap(True)

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

        self.btnProcedureNext = QPushButton(">",self)
        self.btnProcedureNext.setGeometry(1060,475,40,25)
        self.btnProcedureNext.setStyleSheet("border-radius:10; font:bold; font-size:13px; background-color : #7ACEDA; color:#FFFFFF;text-align: center;")

        self.lblProcedurePage = QLabel("1/6",self)
        self.lblProcedurePage.setGeometry(1018,475,40,25)
        self.lblProcedurePage.setStyleSheet("font:normal; font-size:13px; text-align: center; text-color:#373435;")


        # Buttons on My Profile
        lbmi = QLabel("BMI", self)
        lbmi.setGeometry(71, 634, 34, 26)
        lbmi.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")

        self.btn_bmi = QPushButton("18.5", self)
        self.btn_bmi.setGeometry(35, 544, 106, 90)
        self.btn_bmi.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; font:bold; font-size:24px; text-align: center;")
        self.btn_bmi.setGraphicsEffect(Util.getNeuShadow(0))

        self.lblBmiDate = QLabel("25/09/2020",self)
        self.lblBmiDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblBmiDate.setGeometry(65,549,70,16)
        self.lblBmiDate.setAlignment(Qt.AlignRight)

        self.lblBmiUnit = QLabel("kg/m2",self)
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

        self.btn_bp = QPushButton(self)
        self.btn_bp.setGeometry(151, 544, 222, 90)
        self.btn_bp.setGraphicsEffect(Util.getNeuShadow(0))
        self.btn_bp.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; font:bold; font-size:24px; text-align: center;")

        self.lblBpDate = QLabel("25/09/2020",self)
        self.lblBpDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblBpDate.setGeometry(295,549,70,16)
        self.lblBpDate.setAlignment(Qt.AlignRight)

        self.lblBpUnit = QLabel("mm/hg",self)
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
        self.btn_hr = QPushButton("", self)
        self.btn_hr.setGeometry(383, 544, 107, 90)
        self.btn_hr.setGraphicsEffect(Util.getNeuShadow(0))
        self.btn_hr.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; font:bold; font-size:24px; text-align: center;")

        self.lblHrDate = QLabel("25/09/2020",self)
        self.lblHrDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblHrDate.setGeometry(412,549,70,16)
        self.lblHrDate.setAlignment(Qt.AlignRight)

        self.lblHrUnit = QLabel("bpm",self)
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

        self.lblHgDate = QLabel("25/09/2020",self)
        self.lblHgDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblHgDate.setGeometry(526,549,70,16)
        self.lblHgDate.setAlignment(Qt.AlignRight)

        self.lblHgUnit = QLabel("g/dl",self)
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

        self.lblHba1cDate = QLabel("25/09/2020",self)
        self.lblHba1cDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblHba1cDate.setGeometry(645,549,70,16)
        self.lblHba1cDate.setAlignment(Qt.AlignRight)

        self.lblHba1cUnit = QLabel("mmol/mol",self)
        self.lblHba1cUnit.setStyleSheet("color:white;font-size:15px; background-color : #7ACEDA")
        self.lblHba1cUnit.setGeometry(645,608,70,20)
        self.lblHba1cUnit.setAlignment(Qt.AlignRight)

        btn_hba = QPushButton("", self)
        btn_hba.setGeometry(616, 544, 106, 90)
        btn_hba.setStyleSheet(
            "border-radius : 10; background-color : #007ACEDA;")
        btn_hba.setGraphicsEffect(Util.getNeuShadow(0))
        btn_hba.clicked.connect(self.clickme)



        lsugar = QLabel("Sugar", self)
        lsugar.setGeometry(756, 634, 59, 29)
        lsugar.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")
        self.btn_sugar = QPushButton("", self)
        self.btn_sugar.setGeometry(732, 544, 106, 90)
        self.btn_sugar.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; font:bold; font-size:24px; text-align: center;")
        self.btn_sugar.setGraphicsEffect(Util.getNeuShadow(0))

        self.lblSugarDate = QLabel("25/09/2020",self)
        self.lblSugarDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblSugarDate.setGeometry(762,549,70,16)
        self.lblSugarDate.setAlignment(Qt.AlignRight)

        self.lblSugarUnit = QLabel("mmol/mol",self)
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

        self.lblCholDate = QLabel("25/09/2020",self)
        self.lblCholDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblCholDate.setGeometry(879,549,70,16)
        self.lblCholDate.setAlignment(Qt.AlignRight)

        self.lblCholUnit = QLabel("mg/dl",self)
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

        self.lblPtDate = QLabel("25/09/2020",self)
        self.lblPtDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblPtDate.setGeometry(994,549,70,16)
        self.lblPtDate.setAlignment(Qt.AlignRight)

        self.lblPtUnit = QLabel("bpm",self)
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

        self.lblTempDate = QLabel("25/09/2020",self)
        self.lblTempDate.setStyleSheet("color:white;font-size:12px; background-color : #7ACEDA")
        self.lblTempDate.setGeometry(1109,549,70,16)
        self.lblTempDate.setAlignment(Qt.AlignRight)

        self.lblTempUnit = QLabel("f",self)
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
        btn_back.setGeometry(865, 50, 135, 50)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('..\Resources\\backButton.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)

        btn_files = QPushButton("", self)
        btn_files.setGeometry(999, 50, 189, 50)
        btn_files.setStyleSheet("border-radius : 20; background-color: #F0F0F3; text-align:left")
        btn_files.setIcon(QtGui.QIcon('..\Resources\medfiles.png'))
        btn_files.setIconSize(QtCore.QSize(189, 71))
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
        name = self.profileResponse["profile"]["firstname"] + self.profileResponse["profile"]["lastname"]
        user_img = self.profileResponse["profile"]["user_img"]  # profile image url
        age = str(self.profileResponse["profile"]["age"])
        gender = self.profileResponse["profile"]["gender"]
        contact_num = str(self.profileResponse["profile"]["contact_num"])
        email = self.profileResponse["profile"]["email"]
        dob = self.profileResponse["profile"]["dob"]
        address = self.profileResponse["profile"]["address1"]
        bgroup = self.profileResponse["profile"]["blood_group"]

        self.lblName.setText(name)
        self.lblAgeGender.setText(age+" "+gender)
        self.lblMobile.setText(contact_num)
        self.lblEmail.setText(email)
        self.lblDob.setText(dob)
        self.lblAddress.setText(address)
        self.lblBloodGroup.setText(bgroup)


# if __name__ == '__main__':
#     App = QApplication(sys.argv)
#
#     # create the instance of our Window
#     window = MyProfile()
#
#     window.show()
#
#     # start the app
#     sys.exit(App.exec_())
