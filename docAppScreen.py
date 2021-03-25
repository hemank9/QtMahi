import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Utility.MahiUtility as MahiUtil
import Custom.AppointmentListItem as appoi
import API.api_calls as MyApis
import json

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 700)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\docScreen.png'))
        self.label.setGeometry(0, 0, 1220, 165)
        self.btnStyle = "border-radius : 10; background-color : #F0F03; color : #006CB5; font : bold "
        self.btnStyleSelected = "border-radius : 10; background-color : #C4DBF0; color : #006CB5; font : bold "
        self.fontObj = QFont('Arial', 9)
        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

        self.appo_type = "0"
        self.SetAppointmentList()


    # method for widgets
    def UiComponents(self):
        btnUpComnin1 = QPushButton(self)
        btnUpComnin1.setGeometry(160, 57, 283, 52)
        btnUpComnin1.setStyleSheet(self.btnStyle)
        btnUpComnin1.setGraphicsEffect(MahiUtil.getNeuShadow(0))

        self.btnUpComnin2 = QPushButton("UPCOMING APPOINTMENT", self)
        self.btnUpComnin2.setGeometry(160, 57, 283, 52)
        self.btnUpComnin2.setFont(self.fontObj)
        self.btnUpComnin2.setStyleSheet(self.btnStyleSelected)
        self.btnUpComnin2.setGraphicsEffect(MahiUtil.getNeuShadow(1))
        self.btnUpComnin2.clicked.connect(self.UpcominClick)


        btnScan1 = QPushButton(self)
        btnScan1.setGeometry(467, 57, 190, 52)
        btnScan1.setStyleSheet(self.btnStyle)
        btnScan1.setGraphicsEffect(MahiUtil.getNeuShadow(0))

        btnScan2 = QPushButton("SCAN TO BOOK", self)
        btnScan2.setGeometry(467, 57, 190, 52)
        btnScan2.setFont(self.fontObj)
        btnScan2.setStyleSheet(self.btnStyle)
        btnScan2.setGraphicsEffect(MahiUtil.getNeuShadow(1))
        btnScan2.clicked.connect(self.close)

        btnAppHistory1 = QPushButton(self)
        btnAppHistory1.setGeometry(677, 57, 255, 52)
        btnAppHistory1.setStyleSheet(self.btnStyle)
        btnAppHistory1.setGraphicsEffect(MahiUtil.getNeuShadow(0))

        self.btnAppHistory2 = QPushButton("APPOINTMENT HISTORY",self)
        self.btnAppHistory2.setGeometry(677, 57, 255, 52)
        self.btnAppHistory2.setStyleSheet(self.btnStyle)
        self.btnAppHistory2.setFont(self.fontObj)
        self.btnAppHistory2.setGraphicsEffect(MahiUtil.getNeuShadow(1))
        self.btnAppHistory2.clicked.connect(self.HistoryClicked)

        btnBack = QPushButton("", self)
        btnBack.setGeometry(23, 62, 115, 41)
        btnBack.setStyleSheet("border-radius : 10; ")
        btnBack.setIcon(QtGui.QIcon('Resources\Group 87.png'))
        btnBack.setIconSize(QtCore.QSize(115, 41))
        btnBack.clicked.connect(self.close)

        btnPageBack = QPushButton(self)
        btnPageBack.setGeometry(364, 619, 115, 41)
        btnPageBack.setStyleSheet("border-radius : 10; background-color: black")
        # btnPageBack.setIcon(QtGui.QIcon('Resources\Group 87.png'))
        # btnPageBack.setIconSize(QtCore.QSize(115, 41))
        btnPageBack.clicked.connect(self.PageBack)

        btnPageNext = QPushButton(self)
        btnPageNext.setGeometry(685, 619, 115, 41)
        btnPageNext.setStyleSheet("border-radius : 10; background-color: black ")
        # btnPageNext.setIcon(QtGui.QIcon('Resources\Group 87.png'))
        # btnPageNext.setIconSize(QtCore.QSize(115, 41))
        btnPageNext.clicked.connect(self.PageNext)

        lblPageNo = QLabel("", self)
        lblPageNo.setGeometry(525, 619, 70, 70)
        lblPageNo.setStyleSheet("border-radius : 10; background-color: pink")


        self.myQListWidget = QListWidget(self)
        self.myQListWidget.setGeometry(16, 125, 1191, 475)

        # self.myQListWidget.


    def UpcominClick(self):
        self.btnAppHistory2.setStyleSheet(self.btnStyle)
        self.btnUpComnin2.setStyleSheet(self.btnStyleSelected)
        self.appo_type = "0"
        self.myQListWidget.clear()
        self.SetAppointmentList()


    def HistoryClicked(self):
        self.btnAppHistory2.setStyleSheet(self.btnStyleSelected)
        self.btnUpComnin2.setStyleSheet(self.btnStyle)
        self.appo_type = "1"
        self.myQListWidget.clear()
        self.SetAppointmentList()


    def SetAppointmentList(self):

        try:
            self.appo_response = MyApis.fetchAppointments(self.appo_type, "1")

            if self.appo_response != None:
                self.json_array = self.appo_response["data"]
                for appo in self.json_array:
                    # Create QCustomQWidget
                    myQCustomQWidget = appoi.AppointmentListItem()
                    myQCustomQWidget.setTextUp(appo["doctor_name"])
                    myQCustomQWidget.setTextDown(appo["id"])
                    myQCustomQWidget.setAddress(appo["appointment_date"])
                    # self.lblm.setGeometry(589, 142, 276, 69)
                    # Create QListWidgetItem
                    myQListWidgetItem = QListWidgetItem(self.myQListWidget)
                    # Set size hint
                    myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
                    # Add QListWidgetItem into QListWidget
                    self.myQListWidget.addItem(myQListWidgetItem)
                    self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)

            else:
                print("Error, please try again")

        except Exception as e:
            print(e.__class__)

        self.btnUpComnin2.setStyleSheet(self.btnStyle)



if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    window.show()

    # start the app
    sys.exit(App.exec())
