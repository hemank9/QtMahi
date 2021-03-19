# importing libraries 
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class MyProfile(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\yellow.png'))
        self.label.setGeometry(0, 0, 1220, 39)


        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        # shadow.set
        # creating label
        l2 = QLabel("Medical History", self)

        # l1.setText("Medical History")
        l2.setGeometry(573, 48, 150, 29)
        l2.setStyleSheet("color:#EE488D; font: 21px")

        label1 = QLabel("Normal label With out multi line", self)
        # label1.setGeometry(34, 48, 523, 295)
        # label1.setStyleSheet(" border-radius : 15; background-color : #FFFFFF")
        label1_pic = QLabel(self)
        label1_profile = QLabel(self)
        label1_pic.setPixmap(QPixmap('Resources\pic.png'))
        label1_profile.setPixmap(QPixmap('Resources\Rectangle 53.png'))

        label1_pic.setGeometry(370, 51, 184, 180)
        label1_profile.setGeometry(34, 48, 523, 300)

        label1_pic.setStyleSheet(" border-radius : 15")

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        # shadow.setColor(self, 'White')
        label1.setGraphicsEffect(shadow)

        # Medical History
        label2 = QLabel("Multi label i.e With multi line", self)
        label2.setGeometry(575, 75, 290, 268)
        label2.setStyleSheet("border-radius : 15, background-color : #FFFFFF")
        # making it multi line
        label2.setWordWrap(True)
        # l2.setStyleSheet("color:#EE488D; font: 21px")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        label2.setGraphicsEffect(shadow)

        # Emergency contact
        label3 = QLabel("Emergency", self)
        label3.setGeometry(881, 112, 307, 82)
        label3.setStyleSheet("border-radius : 10; background-color : #00A0B5 ")
        label3.setWordWrap(True)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        # label3.setFrameShape(QFrame.StyledPanel)
        # label3.setFrameShadow(QFrame.Raised)
        # label3.setFrameStyle("border-radius : 10")
        # label3.setLineWidth(3)

        # Allergies
        label4 = QLabel("Multi label i.e With multi line", self)
        label4.setGeometry(34, 388, 274, 139)
        label4.setStyleSheet("background-color : #FFFFFF; border-radius : 15")
        label4.setWordWrap(True)
        l4 = QLabel("Allergies", self)
        l4.setGeometry(35, 358, 87, 29)
        l4.setStyleSheet("color:#EE488D; font: 21px; background-color : #FFFFFF")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        label4.setGraphicsEffect(shadow)

        # Family history
        label5 = QLabel("Multi label i.e With multi line", self)
        label5.setGeometry(324, 388, 233, 139)
        label5.setStyleSheet("background-color : #FFFFFF; border-radius : 15")
        label5.setWordWrap(True)
        l5 = QLabel("Family History", self)
        l5.setGeometry(325, 358, 139, 29)
        l5.setStyleSheet("color:#EE488D; font: 21px")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        label5.setGraphicsEffect(shadow)

        # Birth History
        label6 = QLabel("Multi label i.e With multi line", self)
        label6.setGeometry(575, 388, 290, 139)
        label6.setStyleSheet("background-color : #FFFFFF; border-radius : 15")
        label6.setWordWrap(True)
        l6 = QLabel("Birth History", self)
        l6.setGeometry(575, 358, 124, 29)
        l6.setStyleSheet("color:#EE488D; font: 21px")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        label6.setGraphicsEffect(shadow)

        # medical procedure
        label7 = QLabel("Multi label i.e With multi line", self)
        label7.setGeometry(881, 235, 307, 282)
        label7.setStyleSheet("background-color : #FFFFFF; border-radius : 15")
        label7.setWordWrap(True)
        l7 = QLabel("Medical Procedure", self)
        l7.setGeometry(888, 202, 177, 29)
        l7.setStyleSheet("color:#EE488D; font: 21px; background-color: #E5E5E5")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        label7.setGraphicsEffect(shadow)

        # Buttons on My Profile

        btn_bmi = QPushButton("", self)
        btn_bmi.setGeometry(35, 544, 106, 90)
        btn_bmi.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_bmi.clicked.connect(self.clickme)
        lbmi = QLabel("BMI", self)
        lbmi.setGeometry(71, 634, 34, 26)
        lbmi.setStyleSheet("color:#006CB5; font: 18px; background-color: #E5E5E5")

        btn_bp = QPushButton("", self)
        btn_bp.setGeometry(151, 544, 222, 90)
        btn_bp.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_bp.clicked.connect(self.clickme)
        lbp = QLabel("Blood Pressure", self)
        lbp.setGeometry(198, 634, 132, 20)
        lbp.setStyleSheet("color:#006CB5; font: 18px; background-color: #E5E5E5")

        btn_hr = QPushButton("", self)
        btn_hr.setGeometry(383, 544, 107, 90)
        btn_hr.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_hr.clicked.connect(self.clickme)
        lhr = QLabel("Heart Rate", self)
        lhr.setGeometry(389, 634, 110, 29)
        lhr.setStyleSheet("color:#006CB5; font: 18px; background-color: #E5E5E5")

        btn_hg = QPushButton("", self)
        btn_hg.setGeometry(500, 544, 106, 90)
        btn_hg.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_hg.clicked.connect(self.clickme)
        lhg = QLabel("Haemoglobin", self)
        lhg.setGeometry(500, 634, 139, 29)
        lhg.setStyleSheet("color:#006CB5; font: 18px; background-color: #E5E5E5")

        btn_hba = QPushButton("", self)
        btn_hba.setGeometry(616, 544, 106, 90)
        btn_hba.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_hba.clicked.connect(self.clickme)
        lhba = QLabel("HBA1C", self)
        lhba.setGeometry(639, 634, 71, 29)
        lhba.setStyleSheet("color:#006CB5; font: 18px; background-color: #E5E5E5")

        btn_sugar = QPushButton("", self)
        btn_sugar.setGeometry(732, 544, 106, 90)
        btn_sugar.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_sugar.clicked.connect(self.clickme)
        lsugar = QLabel("Sugar", self)
        lsugar.setGeometry(756, 634, 59, 29)
        lsugar.setStyleSheet("color:#006CB5; font: 18px; background-color: #E5E5E5")

        btn_choles = QPushButton("", self)
        btn_choles.setGeometry(849, 544, 106, 90)
        btn_choles.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_choles.clicked.connect(self.clickme)
        lcho = QLabel("Cholesterol", self)
        lcho.setGeometry(858, 634, 105, 29)
        lcho.setStyleSheet("color:#006CB5; font: 18px; background-color: #E5E5E5")

        btn_pt = QPushButton("", self)
        btn_pt.setGeometry(965, 544, 106, 90)
        btn_pt.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_pt.clicked.connect(self.clickme)
        lpt = QLabel("Pt/INR", self)
        lpt.setGeometry(992, 634, 57, 29)
        lpt.setStyleSheet("color:#006CB5; font: 18px; background-color: #E5E5E5")

        btn_temp = QPushButton("", self)
        btn_temp.setGeometry(1081, 544, 106, 90)
        btn_temp.setStyleSheet("border-radius : 10; background-color : #7ACEDA; color:#FFFFFF; text-align:left")
        btn_temp.clicked.connect(self.clickme)
        ltemp = QLabel("Temparature", self)
        ltemp.setGeometry(1084, 634, 109, 29)
        ltemp.setStyleSheet("color:#006CB5; font: 19px; background-color: #E5E5E5")


        btn_back = QPushButton("", self)
        btn_back.setGeometry(881, 55, 135, 55)
        btn_back.setStyleSheet("border-radius : 10; background-color : #E5E5E5")
        btn_back.setIcon(QtGui.QIcon('Resources\Group 27.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)

        btn_files = QPushButton("", self)
        btn_files.setGeometry(999, 55, 189, 55)
        btn_files.setStyleSheet("border-radius : 20; background-color : #E5E5E5; text-align:left")
        btn_files.setIcon(QtGui.QIcon('Resources\medfiles.png'))
        btn_files.setIconSize(QtCore.QSize(189, 71))
        btn_files.clicked.connect(self.clickme)

    def clickme(self):
        # printing pressed
        print("pressed")


if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = MyProfile()

    window.show()

    # start the app
    sys.exit(App.exec())
