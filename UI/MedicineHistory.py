from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import UI.repeatDosage as rDosage
import UI.extraDosage as extraDosage
import UI.datePickMassEjection as massEject
import UI.changetime as changeTime
import sys
import Utility.MahiUtility as Util
import UI.medPrescripHistory as presc


class MedicineHistory(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        # self.label = QLabel(self)
        # self.label.setStyleSheet("background-color:#FEC32E")
        # self.label.setGeometry(0, 0, 1220, 39)

        # self.cylinderVisible = True
        self.UiComponents()
    #
    #     # showing all the widgets
        self.show()
    #
    def UiComponents(self):
        # four buttons on the my medicine page
        self.btnStyle = "border-radius : 10; background-color : #F0F0F3; color: #00A0B5"
        self.btnStyleSelected = "border-radius : 10; background-color: #BCE6EC; color : #00A0B5"

        # Medicine history
        btnMedHistory1 = QPushButton(self)
        btnMedHistory1.setGeometry(198, 57, 150, 70)
        btnMedHistory1.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        btnMedHistory1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnMedHistory = QPushButton("Medicine \n History", self)
        self.btnMedHistory.setGeometry(198, 57, 150, 70)
        self.btnMedHistory.setStyleSheet(self.btnStyleSelected)
        self.btnMedHistory.setGraphicsEffect(Util.getNeuShadow(1))
        # self.btnMedHistory.clicked.connect(self.medHistoryClicked)

        # RX Change
        btnRxChange1 = QPushButton("", self)
        btnRxChange1.setGeometry(363, 57, 150, 70)
        btnRxChange1.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        btnRxChange1.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnRxChange = QPushButton("Analytics", self)
        self.btnRxChange.setGeometry(363, 57, 150, 70)
        self.btnRxChange.setStyleSheet("border-radius : 10; background-color : #F0F0F3; color: #00A0B5")
        self.btnRxChange.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnRxChange.clicked.connect(self.rxChangedClicked)

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

        #1ST TAB
        lblPrescription1 = QLabel(self)
        lblPrescription1.setGeometry(16, 188, 779, 67)
        lblPrescription1.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        lblPrescription1.setGraphicsEffect(Util.getNeuShadow(1))
        lblPrescription11 = QLabel(self)
        lblPrescription11.setGeometry(16, 188, 779, 67)
        lblPrescription11.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        lblPrescription11.setGraphicsEffect(Util.getNeuShadow(0))

        lblRefilled11 = QLabel(self)
        lblRefilled11.setGeometry(825, 188, 91, 67)
        lblRefilled11.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        lblRefilled11.setGraphicsEffect(Util.getNeuShadow(1))
        lblRefilled1 = QLabel(self)
        lblRefilled1.setGeometry(825, 188, 91, 67)
        lblRefilled1.setStyleSheet("border-radius : 10; background-color : #F0F0F3; font-size: 20px")
        lblRefilled1.setText("3")
        lblRefilled1.setAlignment(Qt.AlignCenter)
        lblRefilled1.setGraphicsEffect(Util.getNeuShadow(0))

        lblDrName = QLabel(self)
        lblDrName.setText("Dr.Mobihealth")
        lblDrName.setGeometry(39, 209, 146, 25)
        lblDrName.setStyleSheet("font-size: 15")

        lblDosage = QLabel(self)
        lblDosage.setText("3 dosage for 3 months")
        lblDosage.setGeometry(227, 209, 223, 25)
        lblDosage.setStyleSheet("font-size: 15")

        lblNoOfMeds = QLabel(self)
        lblNoOfMeds.setText("16")
        lblNoOfMeds.setGeometry(492, 209, 126, 25)
        lblNoOfMeds.setStyleSheet("font-size: 15")

        lblDate = QLabel(self)
        lblDate.setText("23/06/2021")
        lblDate.setGeometry(660, 209, 118, 25)
        lblDate.setStyleSheet("font-size: 15")

        btnPrescription111 = QPushButton(self)
        btnPrescription111.setGeometry(16, 188, 779, 67)
        btnPrescription111.setStyleSheet("border-radius : 10; background-color : #00F0F0F3;")
        btnPrescription111.clicked.connect(self.medHistoryClicked)

        #2ND TAB
        lblPrescription2 = QLabel(self)
        lblPrescription2.setGeometry(16, 270, 779, 67)
        lblPrescription2.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        lblPrescription2.setGraphicsEffect(Util.getNeuShadow(1))
        lblPrescription21 = QLabel(self)
        lblPrescription21.setGeometry(16, 270, 779, 67)
        lblPrescription21.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        lblPrescription21.setGraphicsEffect(Util.getNeuShadow(0))

        lblRefilled21 = QLabel(self)
        lblRefilled21.setGeometry(825, 270, 91, 67)
        lblRefilled21.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        lblRefilled21.setGraphicsEffect(Util.getNeuShadow(1))
        lblRefilled2 = QLabel(self)
        lblRefilled2.setGeometry(825, 270, 91, 67)
        lblRefilled2.setStyleSheet("border-radius : 10; background-color : #F0F0F3; font-size: 20px")
        lblRefilled2.setText("3")
        lblRefilled2.setAlignment(Qt.AlignCenter)
        lblRefilled2.setGraphicsEffect(Util.getNeuShadow(0))

        lblDrName2 = QLabel(self)
        lblDrName2.setText("Dr.Mobihealth")
        lblDrName2.setGeometry(39, 291, 146, 25)
        lblDrName2.setStyleSheet("font-size: 15")

        lblDosage2 = QLabel(self)
        lblDosage2.setText("3 dosage for 3 months")
        lblDosage2.setGeometry(227, 291, 223, 25)
        lblDosage2.setStyleSheet("font-size: 15")

        lblNoOfMeds2 = QLabel(self)
        lblNoOfMeds2.setText("16")
        lblNoOfMeds2.setGeometry(492, 291, 126, 25)
        lblNoOfMeds2.setStyleSheet("font-size: 15")

        lblDate2 = QLabel(self)
        lblDate2.setText("23/06/2021")
        lblDate2.setGeometry(660, 291, 118, 25)
        lblDate2.setStyleSheet("font-size: 15")

        btnPrescription2 = QPushButton(self)
        btnPrescription2.setGeometry(16, 270, 779, 67)
        btnPrescription2.setStyleSheet("border-radius : 10; background-color : #00F0F0F3;")
        btnPrescription2.clicked.connect(self.clickme)

        # 3RD TAB
        lblPrescription3 = QLabel(self)
        lblPrescription3.setGeometry(16, 352, 779, 67)
        lblPrescription3.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        lblPrescription3.setGraphicsEffect(Util.getNeuShadow(1))
        lblPrescription31 = QLabel(self)
        lblPrescription31.setGeometry(16, 352, 779, 67)
        lblPrescription31.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        lblPrescription31.setGraphicsEffect(Util.getNeuShadow(0))

        lblRefilled31 = QLabel(self)
        lblRefilled31.setGeometry(825, 352, 91, 67)
        lblRefilled31.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        lblRefilled31.setGraphicsEffect(Util.getNeuShadow(1))
        lblRefilled3 = QLabel(self)
        lblRefilled3.setGeometry(825, 352, 91, 67)
        lblRefilled3.setStyleSheet("border-radius : 10; background-color : #F0F0F3; font-size: 20px")
        lblRefilled3.setText("3")
        lblRefilled3.setAlignment(Qt.AlignCenter)
        lblRefilled3.setGraphicsEffect(Util.getNeuShadow(0))

        lblDrName3 = QLabel(self)
        lblDrName3.setText("Dr.Mobihealth")
        lblDrName3.setGeometry(39, 373, 146, 25)
        lblDrName3.setStyleSheet("font-size: 15")

        lblDosage3 = QLabel(self)
        lblDosage3.setText("3 dosage for 3 months")
        lblDosage3.setGeometry(227, 373, 223, 25)
        lblDosage3.setStyleSheet("font-size: 15")

        lblNoOfMeds3 = QLabel(self)
        lblNoOfMeds3.setText("16")
        lblNoOfMeds3.setGeometry(492, 373, 126, 25)
        lblNoOfMeds3.setStyleSheet("font-size: 15")

        lblDate3 = QLabel(self)
        lblDate3.setText("23/06/2021")
        lblDate3.setGeometry(660, 373, 118, 25)
        lblDate3.setStyleSheet("font-size: 15")

        btnPrescription3 = QPushButton(self)
        btnPrescription3.setGeometry(16, 352, 779, 67)
        btnPrescription3.setStyleSheet("border-radius : 10; background-color : #00F0F0F3;")
        btnPrescription3.clicked.connect(self.clickme)

        # 4TH TAB
        lblPrescription4 = QLabel(self)
        lblPrescription4.setGeometry(16, 434, 779, 67)
        lblPrescription4.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        lblPrescription4.setGraphicsEffect(Util.getNeuShadow(1))
        lblPrescription41 = QLabel(self)
        lblPrescription41.setGeometry(16, 434, 779, 67)
        lblPrescription41.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        lblPrescription41.setGraphicsEffect(Util.getNeuShadow(0))

        lblRefilled41 = QLabel(self)
        lblRefilled41.setGeometry(825, 434, 91, 67)
        lblRefilled41.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        lblRefilled41.setGraphicsEffect(Util.getNeuShadow(1))
        lblRefilled4 = QLabel(self)
        lblRefilled4.setGeometry(825, 434, 91, 67)
        lblRefilled4.setStyleSheet("border-radius : 10; background-color : #F0F0F3; font-size: 20px")
        lblRefilled4.setText("3")
        lblRefilled4.setAlignment(Qt.AlignCenter)
        lblRefilled4.setGraphicsEffect(Util.getNeuShadow(0))

        lblDrName4 = QLabel(self)
        lblDrName4.setText("Dr.Mobihealth")
        lblDrName4.setGeometry(39, 455, 146, 25)
        lblDrName4.setStyleSheet("font-size: 15")

        lblDosage4 = QLabel(self)
        lblDosage4.setText("3 dosage for 3 months")
        lblDosage4.setGeometry(227, 455, 223, 25)
        lblDosage4.setStyleSheet("font-size: 15")

        lblNoOfMeds4 = QLabel(self)
        lblNoOfMeds4.setText("16")
        lblNoOfMeds4.setGeometry(492, 455, 126, 25)
        lblNoOfMeds4.setStyleSheet("font-size: 15")

        lblDate4 = QLabel(self)
        lblDate4.setText("23/06/2021")
        lblDate4.setGeometry(660, 455, 118, 25)
        lblDate4.setStyleSheet("font-size: 15")

        btnPrescription4 = QPushButton(self)
        btnPrescription4.setGeometry(16, 434, 779, 67)
        btnPrescription4.setStyleSheet("border-radius : 10; background-color : #00F0F0F3;")
        btnPrescription4.clicked.connect(self.clickme)

        # 5TH TAB
        lblPrescription5 = QLabel(self)
        lblPrescription5.setGeometry(16, 516, 779, 67)
        lblPrescription5.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        lblPrescription5.setGraphicsEffect(Util.getNeuShadow(1))
        lblPrescription51 = QLabel(self)
        lblPrescription51.setGeometry(16, 516, 779, 67)
        lblPrescription51.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        lblPrescription51.setGraphicsEffect(Util.getNeuShadow(0))

        lblRefilled51 = QLabel(self)
        lblRefilled51.setGeometry(825, 516, 91, 67)
        lblRefilled51.setStyleSheet("border-radius : 10; background-color : #F0F0F3;")
        lblRefilled51.setGraphicsEffect(Util.getNeuShadow(1))
        lblRefilled5 = QLabel(self)
        lblRefilled5.setGeometry(825, 516, 91, 67)
        lblRefilled5.setStyleSheet("border-radius : 10; background-color : #F0F0F3; font-size: 20px")
        lblRefilled5.setText("3")
        lblRefilled5.setAlignment(Qt.AlignCenter)
        lblRefilled5.setGraphicsEffect(Util.getNeuShadow(0))

        lblDrName5 = QLabel(self)
        lblDrName5.setText("Dr.Mobihealth")
        lblDrName5.setGeometry(39, 537, 146, 25)
        lblDrName5.setStyleSheet("font-size: 15")

        lblDosage5 = QLabel(self)
        lblDosage5.setText("3 dosage for 3 months")
        lblDosage5.setGeometry(227, 537, 223, 25)
        lblDosage5.setStyleSheet("font-size: 15")

        lblNoOfMeds5 = QLabel(self)
        lblNoOfMeds5.setText("16")
        lblNoOfMeds5.setGeometry(492, 537, 126, 25)
        lblNoOfMeds5.setStyleSheet("font-size: 15")

        lblDate5 = QLabel(self)
        lblDate5.setText("23/06/2021")
        lblDate5.setGeometry(660, 537, 118, 25)
        lblDate5.setStyleSheet("font-size: 15")

        btnPrescription5 = QPushButton(self)
        btnPrescription5.setGeometry(16, 516, 779, 67)
        btnPrescription5.setStyleSheet("border-radius : 10; background-color : #00F0F0F3;")
        btnPrescription5.clicked.connect(self.clickme)

        self.btnPageBack = QPushButton(self)
        self.btnPageBack.setGeometry(513, 614, 50, 50)
        self.btnPageBack.setStyleSheet("border-radius : 10; background-color: #F0F03")
        self.btnPageBack.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnPageBack1 = QPushButton(self)
        self.btnPageBack1.setGeometry(513, 614, 50, 50)
        self.btnPageBack1.setStyleSheet("border-radius : 10; background-color: #F0F03;font-size:20px;color: black")
        self.btnPageBack1.setText("<")
        # self.btnPageBack1.setIconSize(QtCore.QSize(115, 41))
        self.btnPageBack1.setGraphicsEffect(Util.getNeuShadow(1))
        # btnPageBack1.clicked.connect(self.PageBack)

        self.btnPageNext = QPushButton(self)
        self.btnPageNext.setGeometry(693, 614, 50, 50)
        self.btnPageNext.setStyleSheet("border-radius : 10; background-color: #F0F03 ")
        self.btnPageNext.setGraphicsEffect(Util.getNeuShadow(0))

        self.btnPageNext1 = QPushButton(self)
        self.btnPageNext1.setGeometry(693, 614, 50, 50)
        self.btnPageNext1.setStyleSheet("border-radius : 10; background-color: #F0F03;font-size:20px;color:black ")
        self.btnPageNext1.setText(">")
        # self.btnPageNext1.setIconSize(QtCore.QSize(115, 41))
        self.btnPageNext1.setGraphicsEffect(Util.getNeuShadow(1))
        # btnPageNext1.clicked.connect(self.PageNext)

        self.lblPageNo = QLabel("1 / 1", self)
        self.lblPageNo.setGeometry(600, 621, 60, 41)
        self.lblPageNo.setStyleSheet("font:bold; font-size:16px")
        self.lblPageNo.setAlignment(Qt.AlignCenter)

    def clickme(self):
        print('pressed')

    def medHistoryClicked(self):
        # self.buttonSelected(1)
        self.m = presc.MedPrescriptionTable()
        self.m.show()

    def rxChangedClicked(self):
        self.buttonSelected(2)

    def buttonSelected(self, type):

        if type == 1:
            self.btnMedHistory.setStyleSheet(self.btnStyleSelected)
            self.btnRxChange.setStyleSheet((self.btnStyle))

        if type == 2:
            self.btnMedHistory.setStyleSheet(self.btnStyle)
            self.btnRxChange.setStyleSheet((self.btnStyleSelected))

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
    #     background-color: yellow;cli
    #     color: blue;
    # }
"""


if __name__ == '__main__':
    App = QApplication(sys.argv)
    App.setStyleSheet(stylesheet)
    # create the instance of our Window
    window = MedicineHistory()

    window.show()

# start the app
    sys.exit(App.exec())
