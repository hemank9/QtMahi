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
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../Resources/yellow.png'))
        self.label.setGeometry(0, 0, 1220, 39)

        self.UiComponents()
    #
    #     # showing all the widgets
        self.show()
    #
    def UiComponents(self):

        btn_back = QPushButton("", self)
        btn_back.setGeometry(40, 53, 173, 41)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('../Resources/Group 49.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)

        btnRefill = QPushButton("Refill Now", self)
        btnRefill.setGeometry(889, 56, 301, 59)
        btnRefill.setStyleSheet("background-color : #EE498D; border-radius : 6; font:semi-bold; font-size: 24px; color:white")
        btnRefill.setGraphicsEffect(Util.getNeuShadow(0))
        # btnRefill.clicked.connect()

        lblPres = QLabel(self)
        lblPres.setGeometry(247, 54, 612, 64)
        lblPres.setStyleSheet("border-radius : 10;")
        lblPres.setGraphicsEffect(Util.getNeuShadow(0))

        lblPres1 = QLabel(self)
        lblPres1.setGeometry(247, 54, 612, 64)
        lblPres1.setStyleSheet("border-radius : 10;")
        lblPres1.setGraphicsEffect(Util.getNeuShadow(1))

        lblDate = QLabel(self)
        lblDate.setGeometry(486, 69, 138, 35)
        lblDate.setStyleSheet("font : bold; font-size : 21px")
        lblDate.setText("07.04.2021")

        lblDayTime = QLabel(self)
        lblDayTime.setGeometry(666, 69, 170, 35)
        lblDayTime.setStyleSheet("font : bold; font-size : 21px")
        lblDayTime.setText("07.04.2021")

        btnUpdatedPresc = QPushButton(self)
        btnUpdatedPresc.setGeometry(260, 59, 191, 52)
        btnUpdatedPresc.setStyleSheet("background-color : #F0F0F3; border-radius: 10")
        btnUpdatedPresc.setIcon(QtGui.QIcon('../Resources/Group 95.png'))
        btnUpdatedPresc.setIconSize(QtCore.QSize(180, 110))

        btnUpdatedPreTrans = QPushButton(self)
        btnUpdatedPreTrans.setGeometry(247, 54, 612, 64)
        btnUpdatedPreTrans.setStyleSheet("background-color:#00F0F0F3;")


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

        lblTableEvening = QLabel("Evening",self)
        lblTableEvening.setAlignment(Qt.AlignCenter)
        lblTableEvening.setGeometry(726,210,230,31)
        lblTableEvening.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:18px")

        lblTableDuration = QLabel("Duration",self)
        lblTableDuration.setAlignment(Qt.AlignCenter)
        lblTableDuration.setGeometry(957,178,228,63)
        lblTableDuration.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:20px")

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

if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyleSheet(stylesheet)

    # create the instance of our Window
    window = PrescriptionTable()

    window.show()

# start the app
    sys.exit(App.exec())



