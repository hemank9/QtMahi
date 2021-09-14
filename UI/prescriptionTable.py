import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
import Utility.MahiUtility as Util
from PyQt5.QtCore import *

class PrescriptionTable(QWidget):

    def __init__(self):
        super().__init__()
        # stylesheet = """
        #             QTableWidget {
        #                 background-color: black;
        #                 border-radius: 10px
        #             }
        #
        #             QTableWidget::item {
        #                 color: #222222;
        #                 border-radius: 5px;
        #                 border: 1px solid #999;
        #                 padding: 15px;
        #             }
        #
        #             # QTableWidget::item:selected {
        #             #     background-color: yellow;
        #             #     color: blue;
        #             # }
        #         """
        #
        # self.setStyleSheet(stylesheet)

        # App = QApplication(sys.argv)
        # App.setStyleSheet(stylesheet)

        self.setWindowTitle("Prescription")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        # self.label = QLabel(self)
        # self.label.setStyleSheet("background-color:#FEC32E")
        # self.label.setGeometry(0, 0, 1220, 39)

        self.UiComponents()
        self.show()

    def UiComponents(self):

        # btn_back = QPushButton("", self)
        # btn_back.setGeometry(40, 53, 173, 41)
        # btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        # btn_back.setIcon(QtGui.QIcon('../Resources/backButton.png'))
        # btn_back.setIconSize(QtCore.QSize(155, 71))
        # btn_back.clicked.connect(self.close)

        self.btnStyle = "border-radius : 15; background-color: #F0F03; color : #00A0B5;font:bold;font-size:16px"
        self.btnStyleSelected = "border-radius : 15; background-color: #BCE6EC; color : #00A0B5;font:bold;font-size:16px"

        btn_back = QPushButton("", self)
        btn_back.setGeometry(23, 21, 112, 41)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('../Resources/back.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)
        self.description = QLabel(self)
        self.description.setGeometry(415, 133, 287, 23)
        self.description.setText("*AF = After Food BF = Before Food")
        self.description.setStyleSheet("background-color: #F0F0F3; font-size: 18px")

        self.descripBtn1 = QPushButton(self)
        self.descripBtn1.setGeometry(720, 124, 91, 41)
        self.descripBtn1.setStyleSheet("background-color: #F0F0F3; border-radius: 3;")
        self.descripBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        self.descripBtn = QPushButton(self)
        self.descripBtn.setGeometry(720, 124, 91, 41)
        self.descripBtn.setStyleSheet("background-color: #F0F0F3; border-radius: 3;")
        self.descripBtn.setGraphicsEffect(Util.getNeuShadow(1))
        btnOnGoingPresc1 = QPushButton("", self)
        btnOnGoingPresc1.setGeometry(207, 20, 289, 41)
        btnOnGoingPresc1.setStyleSheet(self.btnStyleSelected)
        btnOnGoingPresc1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnOnGoingPresc = QPushButton("On Going Prescription", self)
        self.btnOnGoingPresc.setGeometry(207, 20, 289, 41)
        self.btnOnGoingPresc.setStyleSheet(self.btnStyleSelected)
        self.btnOnGoingPresc.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnOnGoingPresc.clicked.connect(lambda : self.headersClicked(2))

        btnNewPresc1 = QPushButton("", self)
        btnNewPresc1.setGeometry(509, 20, 289, 41)
        btnNewPresc1.setStyleSheet(self.btnStyle)
        btnNewPresc1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnNewPresc = QPushButton("New Prescription", self)
        self.btnNewPresc.setGeometry(509, 20, 289, 41)
        self.btnNewPresc.setStyleSheet(self.btnStyle)
        self.btnNewPresc.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnNewPresc.clicked.connect(lambda : self.headersClicked(1))

        btnRefill1 = QPushButton("", self)
        btnRefill1.setGeometry(811, 20, 154, 41)
        btnRefill1.setStyleSheet(self.btnStyle)
        btnRefill1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnRefill = QPushButton("New Prescription", self)
        self.btnRefill.setGeometry(811, 20, 154, 41)
        self.btnRefill.setStyleSheet(self.btnStyle)
        self.btnRefill.setGraphicsEffect(Util.getNeuShadow(1))


        # btnRefill = QPushButton("Refill Now", self)
        # btnRefill.setGeometry(889, 56, 301, 59)
        # btnRefill.setStyleSheet("background-color : #EE498D; border-radius : 6; font:semi-bold; font-size: 24px; color:white")
        # btnRefill.setGraphicsEffect(Util.getNeuShadow(0))
        # btnRefill.clicked.connect()

        # lblPres = QLabel(self)
        # lblPres.setGeometry(247, 54, 612, 64)
        # lblPres.setStyleSheet("border-radius : 10;")
        # lblPres.setGraphicsEffect(Util.getNeuShadow(0))
        #
        # lblPres1 = QLabel(self)
        # lblPres1.setGeometry(247, 54, 612, 64)
        # lblPres1.setStyleSheet("border-radius : 10;")
        # lblPres1.setGraphicsEffect(Util.getNeuShadow(1))
        #
        # lblDate = QLabel(self)
        # lblDate.setGeometry(486, 69, 138, 35)
        # lblDate.setStyleSheet("font : bold; font-size : 21px")
        # lblDate.setText("07.04.2021")
        #
        # lblDayTime = QLabel(self)
        # lblDayTime.setGeometry(666, 69, 170, 35)
        # lblDayTime.setStyleSheet("font : bold; font-size : 21px")
        # lblDayTime.setText("07.04.2021")
        #
        # btnUpdatedPresc = QPushButton(self)
        # btnUpdatedPresc.setGeometry(260, 59, 191, 52)
        # btnUpdatedPresc.setStyleSheet("background-color : #F0F0F3; border-radius: 10")
        # btnUpdatedPresc.setIcon(QtGui.QIcon('../Resources/Group 95.png'))
        # btnUpdatedPresc.setIconSize(QtCore.QSize(180, 110))
        #
        # btnUpdatedPreTrans = QPushButton(self)
        # btnUpdatedPreTrans.setGeometry(247, 54, 612, 64)
        # btnUpdatedPreTrans.setStyleSheet("background-color:#00F0F0F3;")


        self.frame = QFrame(self)
        self.frame.setGeometry(25,234,1169,450)
        self.vBox = QVBoxLayout(self)

        self.vBox.setParent(self.frame)

        self.tableWidget = QTableWidget()

        self.tableWidget.setShowGrid(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)

        # Row count
        self.tableWidget.setRowCount(7)

        # Column count
        self.tableWidget.setColumnCount(5)
        for i in range(7):
            medicineItem = QTableWidgetItem(str(i+1)+". Dolo")
            medicineItem.setFont(QFont("Arial",12))

            morningItem = QTableWidgetItem("1 AF")
            morningItem.setTextAlignment(Qt.AlignCenter)
            morningItem.setFont(QFont("Arial",12))

            afternoonItem = QTableWidgetItem("0.5 IOT")
            afternoonItem.setTextAlignment(Qt.AlignCenter)
            afternoonItem.setFont(QFont("Arial",12))

            eveItem = QTableWidgetItem("1 BF")
            eveItem.setTextAlignment(Qt.AlignCenter)
            eveItem.setFont(QFont("Arial",12))

            durationItem = QTableWidgetItem("20 days")
            durationItem.setTextAlignment(Qt.AlignCenter)
            durationItem.setFont(QFont("Arial",12))

            self.tableWidget.setItem(i,0,medicineItem)
            self.tableWidget.setItem(i,1,morningItem)
            self.tableWidget.setItem(i,2,afternoonItem)
            self.tableWidget.setItem(i,3,eveItem)
            self.tableWidget.setItem(i,4,durationItem)


        # self.tableWidget.setItem(0, 0, QTableWidgetItem("Name"))
        # self.tableWidget.setItem(0, 1, QTableWidgetItem("City"))
        # self.tableWidget.setItem(1, 0, QTableWidgetItem("Aloysius"))
        # self.tableWidget.setItem(1, 1, QTableWidgetItem("Indore"))
        # self.tableWidget.setItem(2, 0, QTableWidgetItem("Alan"))
        # self.tableWidget.setItem(2, 1, QTableWidgetItem("Bhopal"))
        # self.tableWidget.setItem(3, 0, QTableWidgetItem("Arnavi"))
        # self.tableWidget.setItem(3, 1, QTableWidgetItem("Mandsaur"))

        # Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        # self.tableWidget.show()
        self.vBox.addWidget(self.tableWidget)



        #table headers
        lblTableMedicine = QLabel("Medicine",self)
        lblTableMedicine.setAlignment(Qt.AlignCenter)
        lblTableMedicine.setGeometry(33,178,232,63)
        lblTableMedicine.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:20px")

        lblTableDosage = QLabel("Dosage",self)
        lblTableDosage.setAlignment(Qt.AlignCenter)
        lblTableDosage.setGeometry(266,178,690,31)
        lblTableDosage.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:18px")

        lblTableMorning = QLabel("Morning",self)
        lblTableMorning.setAlignment(Qt.AlignCenter)
        lblTableMorning.setGeometry(266,210,229,31)
        lblTableMorning.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:18px")

        lblTableAfternoon = QLabel("Afternoon",self)
        lblTableAfternoon.setAlignment(Qt.AlignCenter)
        lblTableAfternoon.setGeometry(496,210,229,31)
        lblTableAfternoon.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:18px")



        self.newPrescBkg = QLabel(self)
        self.newPrescBkg.setGeometry(0, 120, 1220, 685)
        self.newPrescBkg.setStyleSheet("background-color: #F0F0F3")
        self.newPrescBkg.hide()

        self.lblNewPrescTitle = QLabel("Upload the latest prescription through the mobile app ",self)
        self.lblNewPrescTitle.setGeometry(252,300,400,90)
        self.lblNewPrescTitle.setWordWrap(True)
        self.lblNewPrescTitle.setStyleSheet("color:black; font-size:20px")
        self.lblNewPrescTitle.hide()

        self.lblQrImage = QLabel(self)
        self.lblQrImage.setGeometry(700,240,230,230)
        self.lblQrImage.setPixmap(QPixmap('../Resources/mahi_qr.png'))
        self.lblQrImage.hide()

    def headersClicked(self,type):

        if type == 1:
            self.btnNewPresc.setStyleSheet(self.btnStyleSelected)
            self.btnOnGoingPresc.setStyleSheet(self.btnStyle)
            self.NewPrescriptionClicked()
        else :
            self.btnNewPresc.setStyleSheet(self.btnStyle)
            self.btnOnGoingPresc.setStyleSheet(self.btnStyleSelected)
            self.OnGoingPrescClicked()

    def NewPrescriptionClicked(self):
        print('')
        self.newPrescBkg.show()
        self.lblNewPrescTitle.show()
        self.lblQrImage.show()

    def OnGoingPrescClicked(self):
        print('')
        self.newPrescBkg.hide()
        self.lblNewPrescTitle.hide()
        self.lblQrImage.hide()

    def Refill(self):
        # self.tableWidget.hide()
        # self.frame.hide()
        # self.btnRefill.hide()
        # self.btnRefill1.hide()
        # self.descripBtn.hide()
        # self.descripBtn1.hide()
        # self.description.hide()
        # self.btn_back.hide()
        # self.btnOnGoingPresc.hide()
        # self.btnOnGoingPresc1.hide()
        # self.btnNewPresc.hide()
        # self.btnNewPresc1.hide()
        self.quesRefillLbl.show()
        self.yesBtn.show()
        self.yesBtn1.show()
        self.screenLbl.show()
        self.btn_back.show()
        self.btn_back1.show()

    def XBtn(self):
        self.quesRefillLbl.hide()
        self.yesBtn.hide()
        self.yesBtn1.hide()
        self.screenLbl.hide()
        self.btn_back.hide()
        self.btn_back1.hide()

if __name__ == '__main__':

    App = QApplication(sys.argv)
    # App.setStyleSheet()

    # create the instance of our Window
    window = PrescriptionTable()

    window.show()

    # start the app
    sys.exit(App.exec())



