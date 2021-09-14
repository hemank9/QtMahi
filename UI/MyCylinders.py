from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5 import QtCore
import Utility.MahiUtility as Util
import MyDatabase.my_database as myDb
import constants as myConst
import json
import sys
import UI.MedicineHistory as medHist
import UI.medicinetime as medTime
import UI.medExtraDose as medDose

class PillboxListItem(QWidget):
    def __init__(self, parent=None):
        super(PillboxListItem, self).__init__(parent)


        frame1 = QFrame(self)
        frame1.setFixedWidth(800)
        # frame1.setGraphicsEffect(shadow)
        frame1.setStyleSheet("background-color:#f0f0f3")
        self.cylinderData = []

        self.fixedSttyle = "border-radius : 10; background-color : ";
        self.btn1 = QPushButton("", self)
        # self.btn1.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn1.setFixedSize(86, 32)
        self.btn1.clicked.connect(lambda: self.dosageClicked(0))

        self.btn2 = QPushButton("", self)
        # self.btn2.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn2.setFixedSize(86, 32)
        self.btn2.clicked.connect(lambda: self.dosageClicked(1))

        self.btn3 = QPushButton("", self)
        # self.btn3.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn3.setFixedSize(86, 32)
        self.btn3.clicked.connect(lambda: self.dosageClicked(2))

        self.btn4 = QPushButton("", self)
        # self.btn4.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn4.setFixedSize(86, 32)
        self.btn4.clicked.connect(lambda: self.dosageClicked(3))

        self.btn5 = QPushButton("", self)
        # self.btn5.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn5.setFixedSize(86, 32)
        self.btn5.clicked.connect(lambda: self.dosageClicked(4))

        self.btn6 = QPushButton("", self)
        # self.btn6.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn6.setFixedSize(86, 32)
        self.btn6.clicked.connect(lambda: self.dosageClicked(5))

        self.btn7 = QPushButton("", self)
        # self.btn7.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn7.setFixedSize(86, 32)
        self.btn7.clicked.connect(lambda: self.dosageClicked(6))

        self.btn8 = QPushButton("", self)
        # self.btn8.setStyleSheet("border-radius : 10; background-color : #006CB5;")
        self.btn8.setFixedSize(86, 32)
        self.btn8.clicked.connect(lambda: self.dosageClicked(7))


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

    def setJSONData(self,row):
        self.row = row

    def setCylinderData(self,cylinderData):
        self.cylinderData.append(cylinderData)


    def dosageClicked(self, position):
        print("clicked position : "+str(position)+" | Row:"+str(self.row))
        print(self.cylinderData[position])


class PrescriptionTable(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        # self.label = QLabel(self)
        # self.label.setStyleSheet("background-color:#FEC32E")
        # self.label.setGeometry(0, 0, 1220, 39)

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
        btnMedHistory.clicked.connect(lambda : self.buttonsClicked(1))

        # analytics
        btn_analytics1 = QPushButton("", self)
        btn_analytics1.setGeometry(363, 57, 150, 70)
        btn_analytics1.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        btn_analytics1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_analytics = QPushButton("Analytics", self)
        btn_analytics.setGeometry(363, 57, 150, 70)
        btn_analytics.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color: #00A0B5")
        btn_analytics.setGraphicsEffect(Util.getNeuShadow(1))

        # Extra Dosage
        btnExtraDosage1 = QPushButton("", self)
        btnExtraDosage1.setGeometry(528, 57, 150, 70)
        btnExtraDosage1.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        btnExtraDosage1.setGraphicsEffect(Util.getNeuShadow(0))
        btnExtraDosage = QPushButton("Extra Dosage", self)
        btnExtraDosage.setGeometry(528, 57, 150, 70)
        btnExtraDosage.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color: #00A0B5")
        btnExtraDosage.setGraphicsEffect(Util.getNeuShadow(1))
        btnExtraDosage.clicked.connect(lambda : self.buttonsClicked(3))

        # Medicine Time
        btnMedTime1 = QPushButton("", self)
        btnMedTime1.setGeometry(693, 57, 150, 70)
        btnMedTime1.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        btnMedTime1.setGraphicsEffect(Util.getNeuShadow(0))
        btnMedTime = QPushButton("Medicine Time", self)
        btnMedTime.setGeometry(693, 57, 150, 70)
        btnMedTime.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color: #00A0B5")
        btnMedTime.setGraphicsEffect(Util.getNeuShadow(1))
        btnMedTime.clicked.connect(lambda : self.buttonsClicked(2))

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

        cursor = myDb.getDosagesStatus(2)

        cylinder1 = []
        cylinder2 = []
        cylinder3 = []
        cylinder4 = []
        cylinder5 = []
        cylinder6 = []
        cylinder7 = []
        cylinder8 = []

        maxLen = 0

        for row in cursor:
            # print(str(row))

            if row[3] == myConst.cylinders[0]:
                cylinder1.append(row)
                if len(cylinder1)>maxLen:
                    maxLen = len(cylinder1)

            elif row[3] == myConst.cylinders[1]:
                cylinder2.append(row)
                if len(cylinder2)>maxLen:
                    maxLen = len(cylinder2)

            elif row[3] == myConst.cylinders[2]:
                cylinder3.append(row)
                if len(cylinder3)>maxLen:
                    maxLen = len(cylinder3)

            elif row[3] == myConst.cylinders[3]:
                cylinder4.append(row)
                if len(cylinder4)>maxLen:
                    maxLen = len(cylinder4)

            elif row[3] == myConst.cylinders[4]:
                cylinder5.append(row)
                if len(cylinder5)>maxLen:
                    maxLen = len(cylinder5)

            elif row[3] == myConst.cylinders[5]:
                cylinder6.append(row)
                if len(cylinder6)>maxLen:
                    maxLen = len(cylinder6)

            elif row[3] == myConst.cylinders[6]:
                cylinder7.append(row)
                if len(cylinder7)>maxLen:
                    maxLen = len(cylinder7)

            elif row[3] == myConst.cylinders[7]:
                cylinder8.append(row)
                if len(cylinder8)>maxLen:
                    maxLen = len(cylinder8)


        cylinder1 = self.cylinderInsertNone(cylinder1,maxLen)
        cylinder2 = self.cylinderInsertNone(cylinder2,maxLen)
        cylinder3 = self.cylinderInsertNone(cylinder3,maxLen)
        cylinder4 = self.cylinderInsertNone(cylinder4,maxLen)
        cylinder5 = self.cylinderInsertNone(cylinder5,maxLen)
        cylinder6 = self.cylinderInsertNone(cylinder6,maxLen)
        cylinder7 = self.cylinderInsertNone(cylinder7,maxLen)
        cylinder8 = self.cylinderInsertNone(cylinder8,maxLen)

        # for i in cylinder1:
        #     if i!=None:
        #         print(i[12])


        for i in range(maxLen):
            # Create QCustomQWidget
            myQCustomQWidget = PillboxListItem()
            myQListWidgetItem = QListWidgetItem(self.myQListWidget)
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())

            myQCustomQWidget.setJSONData(i)
            myQCustomQWidget.setCylinderData(cylinder1[i])
            myQCustomQWidget.setCylinderData(cylinder2[i])
            myQCustomQWidget.setCylinderData(cylinder3[i])
            myQCustomQWidget.setCylinderData(cylinder4[i])
            myQCustomQWidget.setCylinderData(cylinder5[i])
            myQCustomQWidget.setCylinderData(cylinder6[i])
            myQCustomQWidget.setCylinderData(cylinder7[i])
            myQCustomQWidget.setCylinderData(cylinder8[i])

            if(cylinder1[i]==None):
                myQCustomQWidget.setButtonColor(1,myConst.color_transparent)
            else:
                temp = str(cylinder1[i][12]).replace("'",'"')
                colors = json.loads(temp)

                status = cylinder1[i][9]
                if status == myConst.dosage_available:
                    myQCustomQWidget.setButtonColor(1,colors["filled_dosage"])
                elif status == myConst.dosage_missed:
                    myQCustomQWidget.setButtonColor(1, myConst.color_red)
                else:
                    myQCustomQWidget.setButtonColor(1, colors["empty_dosage"])

            if(cylinder2[i]==None):
                myQCustomQWidget.setButtonColor(2,myConst.color_transparent)
            else:
                temp = str(cylinder2[i][12]).replace("'", '"')
                colors = json.loads(temp)

                status = cylinder2[i][9]
                if status == myConst.dosage_available:
                    myQCustomQWidget.setButtonColor(2, colors["filled_dosage"])
                elif status == myConst.dosage_missed:
                    myQCustomQWidget.setButtonColor(2, myConst.color_red)
                else:
                    myQCustomQWidget.setButtonColor(2, colors["empty_dosage"])

            if(cylinder3[i]==None):
                myQCustomQWidget.setButtonColor(3,myConst.color_transparent)
            else:
                temp = str(cylinder3[i][12]).replace("'", '"')
                colors = json.loads(temp)

                status = cylinder3[i][9]
                if status == myConst.dosage_available:
                    myQCustomQWidget.setButtonColor(3, colors["filled_dosage"])
                elif status == myConst.dosage_missed:
                    myQCustomQWidget.setButtonColor(3, myConst.color_red)
                else:
                    myQCustomQWidget.setButtonColor(3, colors["empty_dosage"])

            if(cylinder4[i]==None):
                myQCustomQWidget.setButtonColor(4,myConst.color_transparent)
            else:
                temp = str(cylinder4[i][12]).replace("'", '"')
                colors = json.loads(temp)

                status = cylinder4[i][9]
                if status == myConst.dosage_available:
                    myQCustomQWidget.setButtonColor(4, colors["filled_dosage"])
                elif status == myConst.dosage_missed:
                    myQCustomQWidget.setButtonColor(4, myConst.color_red)
                else:
                    myQCustomQWidget.setButtonColor(4, colors["empty_dosage"])

            if(cylinder5[i]==None):
                myQCustomQWidget.setButtonColor(5,myConst.color_transparent)
            else:
                temp = str(cylinder5[i][12]).replace("'", '"')
                colors = json.loads(temp)

                status = cylinder5[i][9]
                if status == myConst.dosage_available:
                    myQCustomQWidget.setButtonColor(5, colors["filled_dosage"])
                elif status == myConst.dosage_missed:
                    myQCustomQWidget.setButtonColor(5, myConst.color_red)
                else:
                    myQCustomQWidget.setButtonColor(5, colors["empty_dosage"])

            if(cylinder6[i]==None):
                myQCustomQWidget.setButtonColor(6,myConst.color_transparent)
            else:
                temp = str(cylinder6[i][12]).replace("'", '"')
                colors = json.loads(temp)

                status = cylinder6[i][9]
                if status == myConst.dosage_available:
                    myQCustomQWidget.setButtonColor(6, colors["filled_dosage"])
                elif status == myConst.dosage_missed:
                    myQCustomQWidget.setButtonColor(6, myConst.color_red)
                else:
                    myQCustomQWidget.setButtonColor(6, colors["empty_dosage"])

            if(cylinder7[i]==None):
                myQCustomQWidget.setButtonColor(7,myConst.color_transparent)
            else:
                temp = str(cylinder7[i][12]).replace("'", '"')
                colors = json.loads(temp)

                status = cylinder7[i][9]
                if status == myConst.dosage_available:
                    myQCustomQWidget.setButtonColor(7, colors["filled_dosage"])
                elif status == myConst.dosage_missed:
                    myQCustomQWidget.setButtonColor(7, myConst.color_red)
                else:
                    myQCustomQWidget.setButtonColor(7, colors["empty_dosage"])

            if(cylinder8[i]==None):
                myQCustomQWidget.setButtonColor(8,myConst.color_transparent)
            else:
                temp = str(cylinder8[i][12]).replace("'", '"')
                colors = json.loads(temp)

                status = cylinder8[i][9]
                if status == myConst.dosage_available:
                    myQCustomQWidget.setButtonColor(8, colors["filled_dosage"])
                elif status == myConst.dosage_missed:
                    myQCustomQWidget.setButtonColor(8, myConst.color_red)
                else:
                    myQCustomQWidget.setButtonColor(8, colors["empty_dosage"])

            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)



        self.frame = QFrame(self)
        self.frame.setGeometry(25,256,1169,450)
        self.vBox = QVBoxLayout(self)

        self.vBox.setParent(self.frame)


        # Prescription View

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

    def cylinderInsertNone(self,cylinder, maxlen):
        diff = maxlen - len(cylinder)
        if (diff > 0):
            for i in range(diff):
                cylinder.insert(0, None)

        return cylinder

    def buttonsClicked(self,type):

        if type == 1:
            self.x = medHist.MedicineHistory()
            self.x.show()

        elif type == 2:
            self.x = medTime.MyMedicines()
            self.x.show()

        elif type == 3:
            self.x = medDose.ExtraDose()
            self.x.show()



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



