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
import math



class DocAppScreen(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 700)
        self.setStyleSheet("background-color: #F0F0F3")
        # self.label = QLabel(self)
        # self.label.setStyleSheet("background-color:#FEC32E")
        # self.label.setGeometry(0, 0, 1220, 165)
        self.btnStyle = "border-radius : 10; background-color : #F0F03; color : #006CB5; font : bold "
        self.btnStyleSelected = "border-radius : 10; background-color : #C4DBF0; color : #006CB5; font : bold "
        self.fontObj = QFont('Arial', 9)
        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

        self.appo_type = "0"
        self.page = 1
        self.total = 0;
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
        btnBack.setIcon(QtGui.QIcon('../Resources/backButton.png'))
        btnBack.setIconSize(QtCore.QSize(115, 41))
        btnBack.clicked.connect(self.close)

        btnPageBack = QPushButton(self)
        btnPageBack.setGeometry(500, 619, 70, 70)
        btnPageBack.setStyleSheet("border-radius : 10; background-color: #F0F03")
        btnPageBack.setGraphicsEffect(MahiUtil.getNeuShadow(0))


        btnPageBack1 = QPushButton(self)
        btnPageBack1.setGeometry(500, 619, 70, 70)
        btnPageBack1.setStyleSheet("border-radius : 10; background-color: #F0F03")
        btnPageBack1.setIcon(QtGui.QIcon('../Resources/pageBack.png'))
        btnPageBack1.setIconSize(QtCore.QSize(115, 41))
        btnPageBack1.setGraphicsEffect(MahiUtil.getNeuShadow(1))
        btnPageBack1.clicked.connect(self.PageBack)

        btnPageNext = QPushButton(self)
        btnPageNext.setGeometry(680, 619, 70, 70)
        btnPageNext.setStyleSheet("border-radius : 10; background-color: #F0F03 ")
        btnPageNext.setGraphicsEffect(MahiUtil.getNeuShadow(0))


        btnPageNext1 = QPushButton(self)
        btnPageNext1.setGeometry(680, 619, 70, 70)
        btnPageNext1.setStyleSheet("border-radius : 10; background-color: #F0F03 ")
        btnPageNext1.setIcon(QtGui.QIcon('../Resources/pageNext.png'))
        btnPageNext1.setIconSize(QtCore.QSize(115, 41))
        btnPageNext1.setGraphicsEffect(MahiUtil.getNeuShadow(1))
        btnPageNext1.clicked.connect(self.PageNext)

        self.lblPageNo = QLabel("", self)
        self.lblPageNo.setGeometry(602, 631, 50, 50)
        self.lblPageNo.setStyleSheet("border-radius : 10; background-color: pink")
        self.lblPageNo.setAlignment(Qt.AlignCenter)


        self.myQListWidget = QListWidget(self)
        self.myQListWidget.setGeometry(16, 125, 1191, 475)
        # self.myQListWidget.setContentsMargins(0, 0, 0, 0)
        # self.myQListWidget.setStyleSheet(("QListWidget:item{height: 40px;border-left: 4px solid red;}QListWidget::item:selected {background-color: white; color: black}"))

        # self.myQListWidget.

        self.loadingDialog = MahiUtil.LoadingGif()
        self.myQListWidget.setStyleSheet("border:None;")


    def UpcominClick(self):
        self.btnAppHistory2.setStyleSheet(self.btnStyle)
        self.btnUpComnin2.setStyleSheet(self.btnStyleSelected)
        self.appo_type = "0"
        self.page = 1
        self.total = 0
        self.myQListWidget.clear()
        self.SetAppointmentList()


    def HistoryClicked(self):
        self.btnAppHistory2.setStyleSheet(self.btnStyleSelected)
        self.btnUpComnin2.setStyleSheet(self.btnStyle)
        self.appo_type = "1"
        self.page = 1
        self.total = 0
        self.myQListWidget.clear()
        self.SetAppointmentList()


    def SetAppointmentList(self):


        try:

            if MahiUtil.isInternetOn():
                self.loadingDialog.startAnimation()

                self.appo_response = MyApis.fetchAppointments(self.appo_type, self.page)

                self.loadingDialog.stopAnimation()

                if self.appo_response != None:
                    self.json_array = self.appo_response["data"]

                    if self.page == 1:
                        total_rec = int(self.appo_response["total_records"])

                        if total_rec != 0:
                            temp = len(self.json_array)
                            self.total = math.ceil(total_rec/temp)
                            self.lblPageNo.setText(str(self.page)+"/"+str(self.total))
                        else:
                            self.lblPageNo.setText("0")

                    self.myQListWidget.clear()
                    for appo in self.json_array:
                        # Create QCustomQWidget
                        myQCustomQWidget = appoi.AppointmentListItem()
                        myQCustomQWidget.setTextUp(appo["doctor_name"])
                        myQCustomQWidget.setTextDown(appo["id"])
                        myQCustomQWidget.setAddress(appo["appointment_date"])
                        myQCustomQWidget.setAppoStatus(appo["appointment_status_flag"])
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

            else:
                # no internet screen
                print("internet off")

        except Exception as e:
            print(e.__class__)
            self.loadingDialog.stopAnimation()


    def PageBack(self):
        if self.page >1:
            self.page -=1
            self.lblPageNo.setText(str(self.page) + "/" + str(self.total))
            self.SetAppointmentList()

    def PageNext(self):
        if self.page<self.total:
            self.page +=1
            self.lblPageNo.setText(str(self.page) + "/" + str(self.total))
            self.SetAppointmentList()


# if __name__ == '__main__':
#     App = QApplication(sys.argv)
#
#     # create the instance of our Window
#     window = Window()
#
#     window.show()
#
#     # start the app
#     sys.exit(App.exec())
