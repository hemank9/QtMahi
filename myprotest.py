from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        # setting title
        self.setWindowTitle("Python ")
        # setting geometry
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\yellow.png'))
        self.label.setGeometry(0, 0, 1220, 39)

        self.UiComponents()

        # showing all the widgets
        self.show()

        # method for widgets

    def UiComponents(self):
        label1_pic = QLabel(self)
        label1_pic.setPixmap(QPixmap('Resources\Group 41.png'))
        label1_pic.setGeometry(34, 48, 1164, 469)

        # NAME PROFILE

        label1_pic = QLabel(self)
        label1_pic.setPixmap(QPixmap('Resources\pic.png'))
        label1_pic.setGeometry(370, 51, 184, 180)
        label1_pic.setStyleSheet(" border-radius : 15")

        # Medical History
        l2 = QLabel("Medical History", self)
        l2.setGeometry(573, 40, 150, 29)
        l2.setStyleSheet("color:#EE488D; font: 21px; background-color: #F0F0F3")
        label2 = QLabel("Multi label i.e With multi line", self)
        label2.setGeometry(600, 100, 250, 220)
        label2.setStyleSheet(" background-color : #F0F0F3")
        # making it multi line
        label2.setWordWrap(True)
        # l2.setStyleSheet("color:#EE488D; font: 21px")

        # Emergency contact
        label3 = QLabel("Emergency", self)
        label3.setGeometry(881, 112, 307, 82)
        label3.setStyleSheet("border-radius : 10; background-color : #00A0B5 ")
        label3.setWordWrap(True)

        # Allergies
        label4 = QLabel("Multi label i.e With multi line", self)
        label4.setGeometry(54, 393, 254, 114)
        label4.setStyleSheet("background-color : #F0F0F3; border-radius : 15")
        label4.setWordWrap(True)
        l4 = QLabel("Allergies", self)
        l4.setGeometry(35, 345, 87, 29)
        l4.setStyleSheet("color:#EE488D; font: 21px; background-color: #F0F0F3")

        # Family history
        label5 = QLabel("Multi label i.e With multi line", self)
        label5.setGeometry(344, 393, 213, 119)
        label5.setStyleSheet("background-color : #F0F0F3; border-radius : 15")
        label5.setWordWrap(True)
        l5 = QLabel("Family History", self)
        l5.setGeometry(325, 345, 139, 29)
        l5.setStyleSheet("color:#EE488D; font: 21px; background-color: #F0F0F3")

        # Birth History
        label6 = QLabel("Multi label i.e With multi line", self)
        label6.setGeometry(595, 393, 270, 119)
        label6.setStyleSheet("background-color : #F0F0F3; border-radius : 15")
        label6.setWordWrap(True)
        l6 = QLabel("Birth History", self)
        l6.setGeometry(575, 345, 124, 29)
        l6.setStyleSheet("color:#EE488D; font: 21px; background-color: #F0F0F3")

        # medical procedure
        label7 = QLabel("Multi label i.e With multi line", self)
        label7.setGeometry(900, 255, 277, 252)
        label7.setStyleSheet("background-color : #F0F0F3; border-radius : 15")
        label7.setWordWrap(True)
        l7 = QLabel("Medical Procedure", self)
        l7.setGeometry(888, 202, 177, 29)
        l7.setStyleSheet("color:#EE488D; font: 21px; background-color: #F0F0F3")

        # Buttons on My Profile

        btn_bmi = QPushButton("", self)
        btn_bmi.setGeometry(35, 544, 106, 90)
        btn_bmi.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_bmi.clicked.connect(self.clickme)
        lbmi = QLabel("BMI", self)
        lbmi.setGeometry(71, 634, 34, 26)
        lbmi.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")

        btn_bp = QPushButton("", self)
        btn_bp.setGeometry(151, 544, 222, 90)
        btn_bp.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_bp.clicked.connect(self.clickme)
        lbp = QLabel("Blood Pressure", self)
        lbp.setGeometry(198, 634, 132, 20)
        lbp.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")

        btn_hr = QPushButton("", self)
        btn_hr.setGeometry(383, 544, 107, 90)
        btn_hr.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_hr.clicked.connect(self.clickme)
        lhr = QLabel("Heart Rate", self)
        lhr.setGeometry(389, 634, 110, 29)
        lhr.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")

        btn_hg = QPushButton("", self)
        btn_hg.setGeometry(500, 544, 106, 90)
        btn_hg.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_hg.clicked.connect(self.clickme)
        lhg = QLabel("Haemoglobin", self)
        lhg.setGeometry(500, 634, 139, 29)
        lhg.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")

        btn_hba = QPushButton("", self)
        btn_hba.setGeometry(616, 544, 106, 90)
        btn_hba.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_hba.clicked.connect(self.clickme)
        lhba = QLabel("HBA1C", self)
        lhba.setGeometry(639, 634, 71, 29)
        lhba.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")

        btn_sugar = QPushButton("", self)
        btn_sugar.setGeometry(732, 544, 106, 90)
        btn_sugar.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_sugar.clicked.connect(self.clickme)
        lsugar = QLabel("Sugar", self)
        lsugar.setGeometry(756, 634, 59, 29)
        lsugar.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")

        btn_choles = QPushButton("", self)
        btn_choles.setGeometry(849, 544, 106, 90)
        btn_choles.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_choles.clicked.connect(self.clickme)
        lcho = QLabel("Cholesterol", self)
        lcho.setGeometry(858, 634, 105, 29)
        lcho.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")

        btn_pt = QPushButton("", self)
        btn_pt.setGeometry(965, 544, 106, 90)
        btn_pt.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_pt.clicked.connect(self.clickme)
        lpt = QLabel("Pt/INR", self)
        lpt.setGeometry(992, 634, 57, 29)
        lpt.setStyleSheet("color:#006CB5; font: 18px; background-color: #F0F0F3")

        btn_temp = QPushButton("", self)
        btn_temp.setGeometry(1081, 544, 106, 90)
        btn_temp.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_temp.clicked.connect(self.clickme)
        ltemp = QLabel("Temparature", self)
        ltemp.setGeometry(1084, 634, 109, 29)
        ltemp.setStyleSheet("color:#006CB5; font: 19px; background-color: #F0F0F3")

        btn_back = QPushButton("", self)
        btn_back.setGeometry(881, 50, 135, 50)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('Resources\Group 27.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)

        btn_files = QPushButton("", self)
        btn_files.setGeometry(999, 50, 189, 50)
        btn_files.setStyleSheet("border-radius : 20; background-color: #F0F0F3; text-align:left")
        btn_files.setIcon(QtGui.QIcon('Resources\medfiles.png'))
        btn_files.setIconSize(QtCore.QSize(189, 71))
        btn_files.clicked.connect(self.medfiles)

    def clickme(self):
        # printing pressed
        print("pressed")

    def medfiles(self):
        self.m = Window2()
        self.m.show()
        # self.hide()

    # def file(self):
    #     self.m = Window3()
    #     self.m.show()
    #     self.hide()


App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec_())
