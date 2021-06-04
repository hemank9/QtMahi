from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Utility.MahiUtility as Util


class PillboxListItem(QWidget):
    def __init__(self, parent=None):
        super(PillboxListItem, self).__init__(parent)

        frame1 = QFrame(self)
        frame1.setFixedWidth(800)
        # frame1.setGraphicsEffect(shadow)
        frame1.setStyleSheet("background-color:#f0f0f3")

        self.fixedSttyle = "border-radius : 10; background-color : ";
        self.btn1 = QPushButton("", self)
        # self.btn1.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn1.setFixedSize(86, 32)
        self.btn1.clicked.connect(self.oneClicked)

        self.btn2 = QPushButton("", self)
        # self.btn2.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn2.setFixedSize(86, 32)
        self.btn2.clicked.connect(self.twoClicked)

        self.btn3 = QPushButton("", self)
        # self.btn3.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn3.setFixedSize(86, 32)
        self.btn3.clicked.connect(self.threeClicked)

        self.btn4 = QPushButton("", self)
        # self.btn4.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn4.setFixedSize(86, 32)
        self.btn4.clicked.connect(self.fourClicked)

        self.btn5 = QPushButton("", self)
        # self.btn5.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn5.setFixedSize(86, 32)
        self.btn5.clicked.connect(self.fiveClicked)

        self.btn6 = QPushButton("", self)
        # self.btn6.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn6.setFixedSize(86, 32)
        self.btn6.clicked.connect(self.sixClicked)

        self.btn7 = QPushButton("", self)
        # self.btn7.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn7.setFixedSize(86, 32)
        self.btn7.clicked.connect(self.sevenClicked)

        self.btn8 = QPushButton("", self)
        # self.btn8.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn8.setFixedSize(86, 32)
        self.btn8.clicked.connect(self.eightClicked)


        self.allQHBoxLayout = QHBoxLayout()
        self.allQHBoxLayout.addWidget(self.btn1,1)
        self.allQHBoxLayout.addWidget(self.btn2,1)
        self.allQHBoxLayout.addWidget(self.btn3,1)
        self.allQHBoxLayout.addWidget(self.btn4,1)
        self.allQHBoxLayout.addWidget(self.btn5,1)
        self.allQHBoxLayout.addWidget(self.btn6,1)
        self.allQHBoxLayout.addWidget(self.btn7,1)
        self.allQHBoxLayout.addWidget(self.btn8,1)
        self.setLayout(self.allQHBoxLayout)
        self.allQHBoxLayout.setParent(frame1)

    def setButtonColor(self,type,color):
        t = int(type)
        print("")
        if t==1:
            self.btn1.setStyleSheet(self.fixedSttyle+str(color)+";")
        elif t==2:
            self.btn2.setStyleSheet(self.fixedSttyle + str(color) + ";")
        elif t==3:
            self.btn3.setStyleSheet(self.fixedSttyle + str(color) + ";")
        elif t==4:
            self.btn4.setStyleSheet(self.fixedSttyle + str(color) + ";")
        elif t==5:
            self.btn5.setStyleSheet(self.fixedSttyle + str(color) + ";")
        elif t==6:
            self.btn6.setStyleSheet(self.fixedSttyle + str(color) + ";")
        elif t==7:
            self.btn7.setStyleSheet(self.fixedSttyle + str(color) + ";")
        elif t==8:
            self.btn8.setStyleSheet(self.fixedSttyle + str(color) + ";")


    def oneClicked(self):
        print("one clicked")

    def twoClicked(self):
        print("two clicked")

    def threeClicked(self):
        print("three clicked")

    def fourClicked(self):
        print("four clicked")

    def fiveClicked(self):
        print("five clicked")

    def sixClicked(self):
        print("six clicked")

    def sevenClicked(self):
        print("seven clicked")

    def eightClicked(self):
        print("eight clicked")

class MyCylinders(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 700)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../Resources/Group 108.png'))
        self.label.setGeometry(0, -10, 1220, 195)


        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        # four buttons on the my medicine page
        #Medicine history
        btnMedHistory1 = QPushButton(self)
        btnMedHistory1.setGeometry(198, 57, 150, 70)
        btnMedHistory1.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        btnMedHistory1.setGraphicsEffect(Util.getNeuShadow(0))
        btnMedHistory = QPushButton("Medicine \n History",self)
        btnMedHistory.setGeometry(198, 57, 150, 70)
        btnMedHistory.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color: #00A0B5")
        btnMedHistory.setGraphicsEffect(Util.getNeuShadow(1))
        # btnMedHistory1.clicked.connect(self.)

        # analytics
        btn_analytics1 = QPushButton("", self)
        btn_analytics1.setGeometry(363, 57, 150, 70)
        btn_analytics1.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        btn_analytics1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_analytics = QPushButton("Analytics", self)
        btn_analytics.setGeometry(363, 57, 150, 70)
        btn_analytics.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color: #00A0B5")
        btn_analytics.setGraphicsEffect(Util.getNeuShadow(1))
        # btn_analytics.clicked.connect(self.clickme)

        # Extra Dosage
        btnExtraDosage1 = QPushButton("", self)
        btnExtraDosage1.setGeometry(528, 57, 150, 70)
        btnExtraDosage1.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        btnExtraDosage1.setGraphicsEffect(Util.getNeuShadow(0))
        btnExtraDosage = QPushButton("Extra Dosage", self)
        btnExtraDosage.setGeometry(528, 57, 150, 70)
        btnExtraDosage.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color: #00A0B5")
        btnExtraDosage.setGraphicsEffect(Util.getNeuShadow(1))
        # btnExtraDosage.clicked.connect(self.clickme)

        #Medicine Time
        btnMedTime1 = QPushButton("", self)
        btnMedTime1.setGeometry(693, 57, 150, 70)
        btnMedTime1.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        btnMedTime1.setGraphicsEffect(Util.getNeuShadow(0))
        btnMedTime = QPushButton("Extra Dosage", self)
        btnMedTime.setGeometry(693, 57, 150, 70)
        btnMedTime.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color: #00A0B5")
        btnMedTime.setGraphicsEffect(Util.getNeuShadow(1))
        # btnMedTime.clicked.connect(self.clickme)

        btn_return = QPushButton("", self)
        btn_return.setGeometry(16, 59, 112, 41)
        btn_return.setStyleSheet("border-radius : 10; background-color : #F0F0F3")
        btn_return.setIcon(QtGui.QIcon('../Resources/backButton.png'))
        btn_return.setIconSize(QtCore.QSize(112, 41))
        btn_return.setGraphicsEffect(Util.getNeuShadow(1))
        btn_return.clicked.connect(self.close)

        btnSync1 = QPushButton(self)
        btnSync1.setGeometry(143, 60, 39, 39)
        btnSync1.setStyleSheet("border-radius : 10; background-color : #F0F0F3")
        btnSync1.setIcon(QtGui.QIcon('../Resources/syncBtn.png'))
        btnSync1.setIconSize(QtCore.QSize(39, 39))
        btnSync1.setGraphicsEffect(Util.getNeuShadow(0))
        btnSync = QPushButton(self)
        btnSync.setGeometry(143, 60, 39, 39)
        btnSync.setStyleSheet("border-radius : 10; background-color : #F0F0F3")
        btnSync.setIcon(QtGui.QIcon('../Resources/syncBtn.png'))
        btnSync.setIconSize(QtCore.QSize(39, 39))
        btnSync.setGraphicsEffect(Util.getNeuShadow(1))


        btn_cylinder1 = QPushButton("", self)
        btn_cylinder1.setGeometry(16, 140, 168, 38)
        btn_cylinder1.setStyleSheet("border-radius : 10; background-color : #F0F0F3")
        btn_cylinder1.setIconSize(QtCore.QSize( 168, 38))
        btn_cylinder1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_cylinder = QPushButton("Cylinder View >", self)
        btn_cylinder.setGeometry(16, 140, 168, 38)
        btn_cylinder.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color :#EE488D")
        btn_cylinder.setIconSize(QtCore.QSize(168, 38))
        btn_cylinder.setGraphicsEffect(Util.getNeuShadow(1))
        # btn_cylinder.clicked.connect(self.close)

        # lbl_pic1 = QLabel(self)
        # lbl_pic1.setPixmap(QPixmap('Resources\mahi_ui_popart-01 2.png'))
        # lbl_pic1.setGeometry(797, 20, 271, 161)
        #
        # lbl_pic2 = QLabel(self)
        # lbl_pic2.setPixmap(QPixmap('Resources\pic2.png'))
        # lbl_pic2.setGeometry(1016, 94, 143, 101)

        lbl_txt1 = QLabel("* click on the buttons to see the medicine details",self)
        lbl_txt1.setGeometry(43, 197, 471, 29)

        # lbl_txt = QLabel("97", self)
        # lbl_txt.setGeometry(840, 60, 130, 80)
        # lbl_txt.setFont(QFont('Arial', 40))
        # lbl_txt.setAlignment(QtCore.Qt.AlignRight)
        # lbl_txt.setStyleSheet("background-color : #fff9ea; color : #FEC32E; font-weight: bold")

        self.myQListWidget = QListWidget(self)
        self.myQListWidget.setGeometry(40,236,830,450)

        for i in range(8):
            # Create QCustomQWidget
            myQCustomQWidget = PillboxListItem()
            myQListWidgetItem = QListWidgetItem(self.myQListWidget)
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())


            myQCustomQWidget.setButtonColor(1,"#FAD208")
            myQCustomQWidget.setButtonColor(2,"#F7941D")
            myQCustomQWidget.setButtonColor(3,"#BF2D93")
            myQCustomQWidget.setButtonColor(4,"#92278F")
            myQCustomQWidget.setButtonColor(5,"#009DF8")
            myQCustomQWidget.setButtonColor(6,"#08077C")
            myQCustomQWidget.setButtonColor(7,"#714D3F")
            myQCustomQWidget.setButtonColor(8,"#7A2548")

            if i == 0:
                myQCustomQWidget.setButtonColor(1, "#00FAD208")
                myQCustomQWidget.setButtonColor(2, "#00F7941D")
                myQCustomQWidget.setButtonColor(3, "#00BF2D93")
                myQCustomQWidget.setButtonColor(4, "#0092278F")
                myQCustomQWidget.setButtonColor(5, "#00009DF8")
                myQCustomQWidget.setButtonColor(6, "#0008077C")
                myQCustomQWidget.setButtonColor(7, "#00714D3F")
                myQCustomQWidget.setButtonColor(8, "#F00")

            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)



    def clickme(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("DONT KNOW ABOUT THIS MEDICINE MAYBE CROCINE")
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.exec()

#
# if __name__ == '__main__':
#     App = QApplication(sys.argv)
#
#     # create the instance of our Window
#     window = MyCylinders()
#
#     window.show()
#
#     # start the app
#     sys.exit(App.exec())
