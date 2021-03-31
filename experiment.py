from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

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

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 700)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\Group 45.png'))
        self.label.setGeometry(0, 0, 1220, 195)


        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        # three buttons on the my medicine page
        # prescriptions
        btn_pre = QPushButton("", self)
        btn_pre.setGeometry(39, 48, 215, 67)
        btn_pre.setStyleSheet("border-radius : 30; background-color : #F0F0F3; text-align:top ; text-align:left; focus:pressed")
        btn_pre.setIcon(QtGui.QIcon('Resources\prescriptions.png'))
        btn_pre.setIconSize(QtCore.QSize(215, 67))
        # btn_pre.clicked.connect(self.clickme)

        # medicine time
        btn_mt = QPushButton("", self)
        btn_mt.setGeometry(269, 48, 215, 67)
        btn_mt.setStyleSheet("border-radius : 30; background-color : #F0F0F3; text-align:top ; text-align:left; focus:mtssed")
        btn_mt.setIcon(QtGui.QIcon('Resources\medicinetime.png'))
        btn_mt.setIconSize(QtCore.QSize(215, 67))
        # btn_mt.clicked.connect(self.clickme)

        # analytics
        btn_analytics = QPushButton("", self)
        btn_analytics.setGeometry(498, 48, 215, 67)
        btn_analytics.setStyleSheet("border-radius : 30; background-color : #F0F0F3; text-align:top ; text-align:left; focus:analyticsssed")
        btn_analytics.setIcon(QtGui.QIcon('Resources\manalytics.png'))
        btn_analytics.setIconSize(QtCore.QSize(215, 67))
        # btn_analytics.clicked.connect(self.clickme)

        btn_return = QPushButton("", self)
        btn_return.setGeometry(40, 130, 173, 61)
        btn_return.setStyleSheet("border-radius : 10; background-color : #F0F0F3")
        btn_return.setIcon(QtGui.QIcon('Resources\Group 34.png'))
        btn_return.setIconSize(QtCore.QSize(195, 101))
        btn_return.clicked.connect(self.close)

        btn_cylinder = QPushButton("", self)
        btn_cylinder.setGeometry(269, 130, 216, 83)
        btn_cylinder.setStyleSheet("border-radius : 10; background-color : #F0F0F3")
        btn_cylinder.setIcon(QtGui.QIcon('Resources\cylinder.png'))
        btn_cylinder.setIconSize(QtCore.QSize( 216, 83))
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

        lbl_txt = QLabel("97", self)
        lbl_txt.setGeometry(840, 60, 130, 80)
        lbl_txt.setFont(QFont('Arial', 40))
        lbl_txt.setAlignment(QtCore.Qt.AlignRight)
        lbl_txt.setStyleSheet("background-color : #fff9ea; color : #FEC32E; font-weight: bold")

        self.myQListWidget = QListWidget(self)
        self.myQListWidget.setGeometry(40,236,800,450)

        for i in range(8):
            # Create QCustomQWidget
            myQCustomQWidget = PillboxListItem()
            myQListWidgetItem = QListWidgetItem(self.myQListWidget)
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())


            myQCustomQWidget.setButtonColor(1,"#006CB5")
            myQCustomQWidget.setButtonColor(2,"#004D80")
            myQCustomQWidget.setButtonColor(3,"#274E6F")
            myQCustomQWidget.setButtonColor(4,"#274257")
            myQCustomQWidget.setButtonColor(5,"#ED478D")
            myQCustomQWidget.setButtonColor(6,"#B86C87")
            myQCustomQWidget.setButtonColor(7,"#7A2548")
            myQCustomQWidget.setButtonColor(8,"#713B49")

            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)


    def clickme(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("DONT KNOW ABOUT THIS MEDICINE MAYBE CROCINE")
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.exec()


if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    window.show()

    # start the app
    sys.exit(App.exec())
