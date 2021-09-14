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
        stylesheet = """
                    QTableWidget {
                        background-color: black; 
                        border-radius: 10px
                    }

                    QTableWidget::item {
                        color: #222222;           
                        border-radius: 5px; 
                        border: 1px solid #999;
                        padding: 15px;
                    }

                    # QTableWidget::item:selected {
                    #     background-color: yellow;
                    #     color: blue;
                    # }
                """

        self.setStyleSheet(stylesheet)

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
        self.btnStyle = "border-radius : 5; background-color: #F0F03; color : #00A0B5;font:bold;font-size:16px"
        self.btnStyleSelected = "border-radius : 5; background-color: #BCE6EC; color : #00A0B5;font:bold;font-size:16px"

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

        self.btn_back = QPushButton("", self)
        self.btn_back.setGeometry(23, 21, 112, 41)
        self.btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        self.btn_back.setIcon(QtGui.QIcon('../Resources/back.png'))
        self.btn_back.setIconSize(QtCore.QSize(155, 71))
        self.btn_back.clicked.connect(self.close)

        self.btnOnGoingPresc1 = QPushButton("", self)
        self.btnOnGoingPresc1.setGeometry(207, 20, 289, 41)
        self.btnOnGoingPresc1.setStyleSheet(self.btnStyleSelected)
        self.btnOnGoingPresc1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnOnGoingPresc = QPushButton("On Going Prescription", self)
        self.btnOnGoingPresc.setGeometry(207, 20, 289, 41)
        self.btnOnGoingPresc.setStyleSheet(self.btnStyleSelected)
        self.btnOnGoingPresc.setGraphicsEffect(Util.getNeuShadow(1))

        self.btnNewPresc1 = QPushButton("", self)
        self.btnNewPresc1.setGeometry(509, 20, 289, 41)
        self.btnNewPresc1.setStyleSheet(self.btnStyle)
        self.btnNewPresc1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnNewPresc = QPushButton("New Prescription", self)
        self.btnNewPresc.setGeometry(509, 20, 289, 41)
        self.btnNewPresc.setStyleSheet(self.btnStyle)
        self.btnNewPresc.setGraphicsEffect(Util.getNeuShadow(1))

        self.btnRefill1 = QPushButton("", self)
        self.btnRefill1.setGeometry(811, 20, 154, 41)
        self.btnRefill1.setStyleSheet(self.btnStyle)
        self.btnRefill1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnRefill = QPushButton("Refill", self)
        self.btnRefill.setGeometry(811, 20, 154, 41)
        self.btnRefill.setStyleSheet(self.btnStyle)
        self.btnRefill.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnRefill.clicked.connect(self.Refill)

        self.quesRefillLbl = QLabel("Do you want to refill now?", self)
        self.quesRefillLbl.setGeometry(176, 142, 797, 400)
        self.quesRefillLbl.setPixmap(QPixmap('../Resources/refillnow.png'))
        self.quesRefillLbl.hide()

        self.yesBtn1 = QPushButton("Yes", self)
        self.yesBtn1.setGeometry(434, 374, 116, 56)
        self.yesBtn1.setStyleSheet("background-color: #F0F0F3; color: #00A0B5; border-radius: 5")
        self.yesBtn1.setGraphicsEffect(Util.getNeuShadow(0))
        self.yesBtn = QPushButton("Yes", self)
        self.yesBtn.setGeometry(434, 374, 116, 56)
        self.yesBtn.setStyleSheet("background-color: #F0F0F3; color: #00A0B5; border-radius: 5; font-size: 20px")
        self.yesBtn.setGraphicsEffect(Util.getNeuShadow(1))
        # self.yesBtn.clicked.connect(self.yes)
        self.yesBtn.hide()
        self.yesBtn1.hide()



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
        self.lblTableMedicine = QLabel("Medicine",self)
        self.lblTableMedicine.setAlignment(Qt.AlignCenter)
        self.lblTableMedicine.setGeometry(33,178,232,63)
        self.lblTableMedicine.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:20px")

        self.lblTableDosage = QLabel("Dosage",self)
        self.lblTableDosage.setAlignment(Qt.AlignCenter)
        self.lblTableDosage.setGeometry(266,178,690,31)
        self.lblTableDosage.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:18px")

        self.lblTableMorning = QLabel("Morning",self)
        self.lblTableMorning.setAlignment(Qt.AlignCenter)
        self.lblTableMorning.setGeometry(266,210,229,31)
        self.lblTableMorning.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:18px")

        self.lblTableAfternoon = QLabel("Afternoon",self)
        self.lblTableAfternoon.setAlignment(Qt.AlignCenter)
        self.lblTableAfternoon.setGeometry(496,210,229,31)
        self.lblTableAfternoon.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:18px")

        self.lblTableEvening = QLabel("Evening",self)
        self.lblTableEvening.setAlignment(Qt.AlignCenter)
        self.lblTableEvening.setGeometry(726,210,230,31)
        self.lblTableEvening.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:18px")

        self.lblTableDuration = QLabel("Duration",self)
        self.lblTableDuration.setAlignment(Qt.AlignCenter)
        self.lblTableDuration.setGeometry(957,178,228,63)
        self.lblTableDuration.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:20px")

        self.screenLbl = QLabel(self)
        self.screenLbl.setGeometry(0, 0, 1220, 685)
        self.screenLbl.setStyleSheet("background-color: #F0F0FF3")
        self.screenLbl.hide()

        self.btn_back1 = QPushButton("X", self)
        self.btn_back1.setGeometry(1131, 24, 65, 65)
        self.btn_back1.setStyleSheet("border-radius : 10; background-color: #F0F0F3; color: #C0C0C0; font-size:30px; font: bold")
        self.btn_back1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btn_back = QPushButton("X", self)
        self.btn_back.setGeometry(1131, 24, 65, 65)
        self.btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3; color: #C0C0C0; font-size:30px; font: bold")
        self.btn_back.setGraphicsEffect(Util.getNeuShadow(1))
        self.btn_back.clicked.connect(self.XBtn)
        self.btn_back.hide()
        self.btn_back1.hide()




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
    # App.setStyleSheet(stylesheet)

    # create the instance of our Window
    window = PrescriptionTable()

    window.show()

    # start the app
    sys.exit(App.exec())



