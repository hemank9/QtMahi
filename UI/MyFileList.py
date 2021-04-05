from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Custom.FileListItem as myFile
import Utility.MahiUtility as Util

class FileList(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F5F5F5")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\yellow.png'))
        self.label.setGeometry(0, 0, 1220, 39)

        self.UiComponents()
        #
        #     # showing all the widgets
        # self.show()
    #
    def UiComponents(self):

        self.SortAscending = True
        self.btnStyle = "border-radius : 10; background-color : #FAFAFA; color:#006CB5; font:bold; font-size:22px; text-align: center;"
        self.btnStyleselected = "border-radius : 10; background-color : #C4DBF0; color:#006CB5; font:bold; font-size:22px; text-align: center;"
        self.btnAngio = QPushButton("Angiography", self)
        self.btnAngio.setGeometry(45, 128, 170, 50)
        self.btnAngio.setStyleSheet(
            self.btnStyleselected)
        self.btnAngio.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnAngio.clicked.connect(self.AngioClicked)

        self.btnXray = QPushButton("X-Ray", self)
        self.btnXray.setGeometry(236, 128, 170, 50)
        self.btnXray.setStyleSheet(
            self.btnStyle)
        self.btnXray.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnXray.clicked.connect(self.XrayClicked)

        self.btnEcg = QPushButton("ECG", self)
        self.btnEcg.setGeometry(427, 128, 170, 50)
        self.btnEcg.setStyleSheet(
            self.btnStyle)
        self.btnEcg.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnEcg.clicked.connect(self.EcgClicked)

        self.btnEcho = QPushButton("Eecho", self)
        self.btnEcho.setGeometry(618, 128, 170, 50)
        self.btnEcho.setStyleSheet(
            self.btnStyle)
        self.btnEcho.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnEcho.clicked.connect(self.EchoClicked)

        self.btnMri = QPushButton("MRI", self)
        self.btnMri.setGeometry(809, 128, 170, 50)
        self.btnMri.setStyleSheet(
            self.btnStyle)
        self.btnMri.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnMri.clicked.connect(self.MriClicked)

        self.btnBloodTest = QPushButton("Blood Test", self)
        self.btnBloodTest.setGeometry(1000, 128, 170, 50)
        self.btnBloodTest.setStyleSheet(
            self.btnStyle)
        self.btnBloodTest.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnBloodTest.clicked.connect(self.BloodTestClicked)

        self.btnAscending= QPushButton("Ascending", self)
        self.btnAscending.setGeometry(875, 58, 307, 43)
        self.btnAscending.setStyleSheet(self.btnStyleselected)
        self.btnAscending.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnAscending.clicked.connect(self.SortClicked)
        btn_back = QPushButton("", self)
        btn_back.setGeometry(41, 55, 135, 50)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F5F5F5")
        btn_back.setIcon(QtGui.QIcon('..\Resources\Group 87.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)

        self.myQListWidget = QListWidget(self)
        self.myQListWidget.setGeometry(41, 202, 1138, 405)

        btnPageBack = QPushButton(self)
        btnPageBack.setGeometry(475, 619, 70, 50)
        btnPageBack.setStyleSheet("border-radius : 10; background-color: #F0F03")
        btnPageBack.setGraphicsEffect(Util.getNeuShadow(0))

        btnPageBack1 = QPushButton("<",self)
        btnPageBack1.setGeometry(475, 619, 70, 50)
        btnPageBack1.setStyleSheet("border-radius : 10; background-color: #F0F03; font:bold; font-size:20px")
        btnPageBack1.setIcon(QtGui.QIcon('Resources\pageBack.png'))
        btnPageBack1.setIconSize(QtCore.QSize(115, 41))
        btnPageBack1.setGraphicsEffect(Util.getNeuShadow(1))

        btnPageNext = QPushButton(self)
        btnPageNext.setGeometry(655, 619, 70, 50)
        btnPageNext.setStyleSheet("border-radius : 10; background-color: #F0F03 ")
        btnPageNext.setGraphicsEffect(Util.getNeuShadow(0))

        btnPageNext1 = QPushButton(">",self)
        btnPageNext1.setGeometry(655, 619, 70, 50)
        btnPageNext1.setStyleSheet("border-radius : 10; background-color: #F0F03; font:bold; font-size:20px")
        btnPageNext1.setIcon(QtGui.QIcon('Resources\pageNext.png'))
        btnPageNext1.setIconSize(QtCore.QSize(115, 41))
        btnPageNext1.setGraphicsEffect(Util.getNeuShadow(1))

        self.lblPageNo = QLabel("", self)
        self.lblPageNo.setGeometry(577, 619, 50, 50)
        self.lblPageNo.setStyleSheet("border-radius : 10; background-color: pink")
        self.lblPageNo.setAlignment(Qt.AlignCenter)

        for i in range(5):
            myQCustomQWidget = myFile.FileListItem()
            myQCustomQWidget.setTextFileName('X-Ray')
            myQCustomQWidget.setTextDateDoctor('24/12/2021 Dr.Mobihealth')
            myQCustomQWidget.setExtension(".jpeg")
            myQListWidgetItem = QListWidgetItem(self.myQListWidget)
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())

            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)

        self.myQListWidget.set

    def SortClicked(self):
        if self.SortAscending:
            self.SortAscending = False
            self.btnAscending.setText("Descending")
        else:
            self.SortAscending = True
            self.btnAscending.setText("Ascending")

    def AngioClicked(self):
        self.SetFileTypeSelected(1)
    def EcgClicked(self):
        self.SetFileTypeSelected(2)
    def BloodTestClicked(self):
        self.SetFileTypeSelected(3)
    def MriClicked(self):
        self.SetFileTypeSelected(4)
    def EchoClicked(self):
        self.SetFileTypeSelected(5)
    def XrayClicked(self):
        self.SetFileTypeSelected(6)

    def SetFileTypeSelected(self,type):

        if type == 1:
            self.btnAngio.setStyleSheet(self.btnStyleselected)
            self.btnEcg.setStyleSheet(self.btnStyle)
            self.btnBloodTest.setStyleSheet(self.btnStyle)
            self.btnMri.setStyleSheet(self.btnStyle)
            self.btnEcho.setStyleSheet(self.btnStyle)
            self.btnXray.setStyleSheet(self.btnStyle)

        elif type == 2 :
            self.btnAngio.setStyleSheet(self.btnStyle)
            self.btnEcg.setStyleSheet(self.btnStyleselected)
            self.btnBloodTest.setStyleSheet(self.btnStyle)
            self.btnMri.setStyleSheet(self.btnStyle)
            self.btnEcho.setStyleSheet(self.btnStyle)
            self.btnXray.setStyleSheet(self.btnStyle)

        elif type == 3 :
            self.btnAngio.setStyleSheet(self.btnStyle)
            self.btnEcg.setStyleSheet(self.btnStyle)
            self.btnBloodTest.setStyleSheet(self.btnStyleselected)
            self.btnMri.setStyleSheet(self.btnStyle)
            self.btnEcho.setStyleSheet(self.btnStyle)
            self.btnXray.setStyleSheet(self.btnStyle)

        elif type == 4 :
            self.btnAngio.setStyleSheet(self.btnStyle)
            self.btnEcg.setStyleSheet(self.btnStyle)
            self.btnBloodTest.setStyleSheet(self.btnStyle)
            self.btnMri.setStyleSheet(self.btnStyleselected)
            self.btnEcho.setStyleSheet(self.btnStyle)
            self.btnXray.setStyleSheet(self.btnStyle)

        elif type == 5 :
            self.btnAngio.setStyleSheet(self.btnStyle)
            self.btnEcg.setStyleSheet(self.btnStyle)
            self.btnBloodTest.setStyleSheet(self.btnStyle)
            self.btnMri.setStyleSheet(self.btnStyle)
            self.btnEcho.setStyleSheet(self.btnStyleselected)
            self.btnXray.setStyleSheet(self.btnStyle)

        elif type == 6 :
            self.btnAngio.setStyleSheet(self.btnStyle)
            self.btnEcg.setStyleSheet(self.btnStyle)
            self.btnBloodTest.setStyleSheet(self.btnStyle)
            self.btnMri.setStyleSheet(self.btnStyle)
            self.btnEcho.setStyleSheet(self.btnStyle)
            self.btnXray.setStyleSheet(self.btnStyleselected)


if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = FileList()

    window.show()

    # start the app
    sys.exit(App.exec_())