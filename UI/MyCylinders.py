from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5 import QtCore
import Utility.MahiUtility as Util

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

class PrescriptionTable(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setStyleSheet("background-color:#FEC32E")
        self.label.setGeometry(0, 0, 1220, 39)

        self.cylinderVisible = True
        self.UiComponents()
    #
    #     # showing all the widgets
        self.show()
    #
    def UiComponents(self):
        # four buttons on the my medicine page
        # Medicine history
        btnMedHistory1 = QPushButton(self)
        btnMedHistory1.setGeometry(198, 57, 150, 70)
        btnMedHistory1.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        btnMedHistory1.setGraphicsEffect(Util.getNeuShadow(0))
        btnMedHistory = QPushButton("Medicine \n History", self)
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

        # Medicine Time
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
        btn_cylinder1.setIconSize(QtCore.QSize(168, 38))
        btn_cylinder1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btn_cylinder = QPushButton("Cylinder View >", self)
        self.btn_cylinder.setGeometry(16, 140, 168, 38)
        self.btn_cylinder.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color :#EE488D")
        self.btn_cylinder.setIconSize(QtCore.QSize(168, 38))
        self.btn_cylinder.setGraphicsEffect(Util.getNeuShadow(1))
        self.btn_cylinder.clicked.connect(self.cylinderClicked)

        self.lbl_txt1 = QLabel("* click on the buttons to see the medicine details", self)
        self.lbl_txt1.setGeometry(43, 190, 471, 29)

        self.myQListWidget = QListWidget(self)
        self.myQListWidget.setStyleSheet("border:None;")
        self.myQListWidget.setGeometry(40,220,830,450)

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



        self.frame = QFrame(self)
        self.frame.setGeometry(25,256,1169,450)
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



        # Table will fit the screen horizontally
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        # self.tableWidget.show()
        self.vBox.addWidget(self.tableWidget)

        # table headers
        self.lblTableMedicine = QLabel("Medicine", self)
        self.lblTableMedicine.setAlignment(Qt.AlignCenter)
        self.lblTableMedicine.setGeometry(33, 200, 232, 63)
        self.lblTableMedicine.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:20px")

        self.lblTableDosage = QLabel("Dosage", self)
        self.lblTableDosage.setAlignment(Qt.AlignCenter)
        self.lblTableDosage.setGeometry(266, 200, 690, 31)
        self.lblTableDosage.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:18px")

        self.lblTableMorning = QLabel("Morning", self)
        self.lblTableMorning.setAlignment(Qt.AlignCenter)
        self.lblTableMorning.setGeometry(266, 232, 229, 31)
        self.lblTableMorning.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:18px")

        self.lblTableAfternoon = QLabel("Afternoon", self)
        self.lblTableAfternoon.setAlignment(Qt.AlignCenter)
        self.lblTableAfternoon.setGeometry(496, 232, 229, 31)
        self.lblTableAfternoon.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:18px")

        self.lblTableEvening = QLabel("Evening", self)
        self.lblTableEvening.setAlignment(Qt.AlignCenter)
        self.lblTableEvening.setGeometry(726, 232, 230, 31)
        self.lblTableEvening.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:18px")

        self.lblTableDuration = QLabel("Duration", self)
        self.lblTableDuration.setAlignment(Qt.AlignCenter)
        self.lblTableDuration.setGeometry(957, 200, 228, 63)
        self.lblTableDuration.setStyleSheet("border-radius:5;border:0.8px solid #AAA; font-size:20px")

        # self.frame.hide()
        # self.lblTableDuration.hide()
        # self.lblTableEvening.hide()
        # self.lblTableAfternoon.hide()
        # self.lblTableMorning.hide()
        # self.lblTableMedicine.hide()
        # self.lblTableDosage.hide()

        self.viewChanged()

    def cylinderClicked(self):
        if(self.cylinderVisible):
            self.cylinderVisible = False
            self.btn_cylinder.setText("Prescription View >")
        else:
            self.cylinderVisible = True
            self.btn_cylinder.setText("Cylinder View >")

        self.viewChanged()

    def viewChanged(self):
        if self.cylinderVisible:
            self.frame.hide()
            self.lblTableEvening.hide()
            self.lblTableAfternoon.hide()
            self.lblTableDuration.hide()
            self.lblTableMorning.hide()
            self.lblTableDosage.hide()
            self.lblTableMedicine.hide()
            self.myQListWidget.show()
            self.lbl_txt1.show()
        else:
            self.frame.show()
            self.lblTableEvening.show()
            self.lblTableAfternoon.show()
            self.lblTableDuration.show()
            self.lblTableMorning.show()
            self.lblTableDosage.show()
            self.lblTableMedicine.show()
            self.myQListWidget.hide()
            self.lbl_txt1.hide()



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



