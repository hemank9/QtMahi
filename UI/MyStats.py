from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Utility.MahiUtility as Util

import UI.MyStatsDetailed as statsDetailed
# importing packages
# import matplotlib.pyplot as plt
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg



class MyStats(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Stats")
        # setting geometry
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setStyleSheet("background-color:#FEC32E")
        self.label.setGeometry(0, 0, 1220, 39)

        self.UiComponents()

        # showing all the widgets
        self.show()

    def UiComponents(self):
        backBtn = QPushButton(self)
        backBtn.setGeometry(21, 61, 107, 47)
        backBtn.setStyleSheet("border-radius: 8; background-color: #F0F0F3")
        backBtn.setIcon(QtGui.QIcon('..\Resources\\backButton.png'))
        backBtn.setIconSize(QtCore.QSize(112, 52))
        backBtn.setGraphicsEffect(Util.getNeuShadow(0))
        backBtn.clicked.connect(self.close)

        addReadingsBtn = QPushButton(self)
        addReadingsBtn.setStyleSheet("border-radius: 10;")
        addReadingsBtn.setGeometry(800, 57, 260, 50)
        addReadingsBtn.setGraphicsEffect(Util.getNeuShadow(0))
        addReadingsBtn1 = QPushButton(self)
        addReadingsBtn1.setStyleSheet("border-radius: 10;")
        addReadingsBtn1.setGeometry(800, 57, 260, 50)
        addReadingsBtn1.setIcon(QtGui.QIcon('..\Resources\\addReadings.png'))
        addReadingsBtn1.setIconSize(QtCore.QSize(260, 50))
        addReadingsBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        # addReadingsBtn1.clicked.connect(self.)

        self.vitalsCombo1 = QComboBox(self)
        self.vitalsCombo1.setGeometry(187, 57, 214, 50)
        self.vitalsCombo1.setStyleSheet("border-radius: 10; color: #00A0B5 ")
        self.vitalsCombo1.setGraphicsEffect(Util.getNeuShadow(1))

        self.vitalsCombo = QComboBox(self)
        self.vitalsCombo.setGeometry(187, 57, 214, 50)
        self.vitalsCombo.setStyleSheet("border-radius: 10; color: #00A0B5; ")
        self.vitalsCombo.setGraphicsEffect(Util.getNeuShadow(0))
        self.vitalsCombo.addItem("HBA1C")
        self.vitalsCombo.addItem("Blood Pressure")
        self.vitalsCombo.addItem("Heart Rate")
        self.vitalsCombo.addItem("Haemoglobin")
        self.vitalsCombo.addItem("BMI")
        self.vitalsCombo.addItem("Sugar")
        self.vitalsCombo.addItem("Cholesterol")
        self.vitalsCombo.addItem("Pt/INR")
        self.vitalsCombo.addItem("Temperature")

        normalBtn = QPushButton("Normal", self)
        normalBtn.setStyleSheet("border-radius: 6; background-color: #7ACEDA; color: #FFFFFF")
        normalBtn.setGeometry(414, 57, 120, 50)
        normalBtn.setGraphicsEffect(Util.getNeuShadow(0))

        borderBtn = QPushButton("Border", self)
        borderBtn.setStyleSheet("border-radius: 6; background-color: #FEC32E; color: #FFFFFF")
        borderBtn.setGeometry(544, 57, 120, 50)
        borderBtn.setGraphicsEffect(Util.getNeuShadow(0))

        highLowBtn = QPushButton("High/Low", self)
        highLowBtn.setStyleSheet("border-radius: 6; background-color: #FE4343; color: #FFFFFF")
        highLowBtn.setGeometry(674, 57, 120, 50)
        highLowBtn.setGraphicsEffect(Util.getNeuShadow(0))


        self.normalBtnStyle = "border-radius: 10; background-color: #7ACEDA;"
        self.labelSmallStyle = "background-color:#00AAAAAA; color:white; font-size:15px; font:bold"
        self.labelHeaderStyle = "background-color:#00AAAAAA; color:#727376; font-size:15px"
        self.labelBigStyle = "background-color:#00AAAAAA; color:white; font-size:23px; font:bold"

        lblBpHeader = QLabel(self)
        lblBpHeader.setGeometry(68,125,132,20)
        lblBpHeader.setAlignment(Qt.AlignCenter)
        lblBpHeader.setStyleSheet(self.labelHeaderStyle)
        lblBpHeader.setText("Blood Pressure")
        lblBpHeader.setStyleSheet("color:#555; font-size:15px")

        lblHeartHeader = QLabel(self)
        lblHeartHeader.setGeometry(258,125,106,20)
        lblHeartHeader.setAlignment(Qt.AlignCenter)
        lblHeartHeader.setStyleSheet(self.labelHeaderStyle)
        lblHeartHeader.setText("Heart Rate")
        lblHeartHeader.setStyleSheet("color:#555; font-size:15px")

        lblBmiHeader = QLabel(self)
        lblBmiHeader.setGeometry(258+118,125,106,20)
        lblBmiHeader.setAlignment(Qt.AlignCenter)
        lblBmiHeader.setStyleSheet(self.labelHeaderStyle)
        lblBmiHeader.setText("BMI")
        lblBmiHeader.setStyleSheet("color:#555; font-size:15px")

        lblHaemoHeader = QLabel(self)
        lblHaemoHeader.setGeometry(258+(118*2),125,106,20)
        lblHaemoHeader.setAlignment(Qt.AlignCenter)
        lblHaemoHeader.setStyleSheet(self.labelHeaderStyle)
        lblHaemoHeader.setText("Haemoglobin")
        lblHaemoHeader.setStyleSheet("color:#555; font-size:15px")

        lblHba1cHeader = QLabel(self)
        lblHba1cHeader.setGeometry(258+(118*3),125,106,20)
        lblHba1cHeader.setAlignment(Qt.AlignCenter)
        lblHba1cHeader.setStyleSheet(self.labelHeaderStyle)
        lblHba1cHeader.setText("HBA1C")
        lblHba1cHeader.setStyleSheet("color:#555; font-size:15px")

        lblSugarHeader = QLabel(self)
        lblSugarHeader.setGeometry(258+(118*4),125,106,20)
        lblSugarHeader.setAlignment(Qt.AlignCenter)
        lblSugarHeader.setStyleSheet(self.labelHeaderStyle)
        lblSugarHeader.setText("Sugar")
        lblSugarHeader.setStyleSheet("color:#555; font-size:15px")

        lblCholesHeader = QLabel(self)
        lblCholesHeader.setGeometry(258+(118*5),125,106,20)
        lblCholesHeader.setAlignment(Qt.AlignCenter)
        lblCholesHeader.setStyleSheet(self.labelHeaderStyle)
        lblCholesHeader.setText("Cholestrol")
        lblCholesHeader.setStyleSheet("color:#555; font-size:15px")

        lblPtnrHeader = QLabel(self)
        lblPtnrHeader.setGeometry(258+(118*6),125,106,20)
        lblPtnrHeader.setAlignment(Qt.AlignCenter)
        lblPtnrHeader.setStyleSheet(self.labelHeaderStyle)
        lblPtnrHeader.setText("Pt/Nr")
        lblPtnrHeader.setStyleSheet("color:#555; font-size:15px")

        lblTempHeader = QLabel(self)
        lblTempHeader.setGeometry(258+(118*7),125,106,20)
        lblTempHeader.setAlignment(Qt.AlignCenter)
        lblTempHeader.setStyleSheet(self.labelHeaderStyle)
        lblTempHeader.setText("Temperature")
        lblTempHeader.setStyleSheet("color:#555; font-size:15px")




        self.bpBtnList = []
        self.bpLblValueList = []
        self.bpLblDateList = []
        self.bpLblUnitList = []
        self.heartBtnList = []
        self.heartLblValueList = []
        self.heartLblDateList = []
        self.heartLblUnitList = []
        self.bmiBtnList = []
        self.bmiLblValueList = []
        self.bmiLblDateList = []
        self.bmiLblUnitList = []
        self.HaemoBtnList = []
        self.HaemoLblValueList = []
        self.HaemoLblDateList = []
        self.HaemoLblUnitList = []
        self.Hba1cBtnList = []
        self.Hba1cLblValueList = []
        self.Hba1cLblDateList = []
        self.Hba1cLblUnitList = []
        self.SugarBtnList = []
        self.SugarLblValueList = []
        self.SugarLblDateList = []
        self.SugarLblUnitList = []
        self.CholesBtnList = []
        self.CholesLblValueList = []
        self.CholesLblDateList = []
        self.CholesLblUnitList = []
        self.PtnrBtnList = []
        self.PtnrLblValueList = []
        self.PtnrLblDateList = []
        self.PtnrLblUnitList = []
        self.TemperatureBtnList = []
        self.TemperatureLblValueList = []
        self.TemperatureLblDateList = []
        self.TemperatureLblUnitList = []

        startBpx = 21
        startBpy = 150
        startBpw = 222
        startBph = 90

        startLblx =137
        startLbly = 155
        startLblw = 100
        startLblh = 16

        startHeartx = 258
        startHearty = 150
        startHeartw = 106
        startHearth = 90

        for i in range(5):

            if i>0:
                startBpy= startBpy+100
                startLbly= startLbly+100
                startHearty= startHearty+100

            btnBp1 = QPushButton(self)
            btnBp1.setGeometry(startBpx,startBpy,startBpw,startBph)
            btnBp1.setStyleSheet(self.normalBtnStyle)

            lblBpDate1 = QLabel(self)
            lblBpDate1.setGeometry(startLblx,startLbly,startLblw,startLblh)
            lblBpDate1.setAlignment(Qt.AlignRight)
            lblBpDate1.setStyleSheet(self.labelSmallStyle)
            lblBpDate1.setText("10-05-21")

            lblBpUnit1 = QLabel(self)
            lblBpUnit1.setGeometry(startLblx,startLbly+60,startLblw,startLblh+10)
            lblBpUnit1.setAlignment(Qt.AlignRight)
            lblBpUnit1.setStyleSheet(self.labelSmallStyle)
            lblBpUnit1.setText("mm/hg")

            lblBpValue = QLabel(self)
            lblBpValue.setGeometry(startBpx+10,startBpy+30,startBpw-20,startBph-65)
            lblBpValue.setAlignment(Qt.AlignRight)
            lblBpValue.setStyleSheet(self.labelBigStyle)
            lblBpValue.setText('<font color="#FFF">100 </font><font color="#006CB5">SYS</font>'
                                    '<font color="#FFF">   85 </font><font color="#006CB5">DIA</font>')

            btnBp = QPushButton(self)
            btnBp.setGeometry(startBpx,startBpy,startBpw,startBph)
            btnBp.setStyleSheet("background-color:#00AAAAAA")
            btnBp.clicked.connect(lambda: self.VitalClicked("Blood Pressure"))


            self.bpBtnList.append(btnBp)
            self.bpLblValueList.append(lblBpValue)
            self.bpLblDateList.append(lblBpDate1)
            self.bpLblUnitList.append(lblBpUnit1)


            #HeartRate

            btnHeart = QPushButton(self)
            btnHeart.setGeometry(startHeartx, startHearty, startHeartw, startHearth)
            btnHeart.setStyleSheet(self.normalBtnStyle)

            lblHeartDate = QLabel(self)
            lblHeartDate.setGeometry(startHeartx+2,startHearty+5,startHeartw-6,startHearth-74)
            lblHeartDate.setAlignment(Qt.AlignRight)
            lblHeartDate.setStyleSheet(self.labelSmallStyle)
            lblHeartDate.setText("10-05-21")

            lblHeartUnit = QLabel(self)
            lblHeartUnit.setGeometry(startHeartx-1,startHearty + 64,startHeartw-6,startHearth-70)
            lblHeartUnit.setAlignment(Qt.AlignRight)
            lblHeartUnit.setStyleSheet(self.labelSmallStyle)
            lblHeartUnit.setText("bpm")

            lblHeartValue = QLabel(self)
            lblHeartValue.setGeometry(startHeartx+15,startHearty +30,startHeartw-15, startHearth-57)
            lblHeartValue.setAlignment(Qt.AlignLeft)
            lblHeartValue.setStyleSheet(self.labelBigStyle)
            lblHeartValue.setText('90')


            btnHeartT = QPushButton(self)
            btnHeartT.setGeometry(startHeartx, startHearty, startHeartw, startHearth)
            btnHeartT.setStyleSheet("background-color:#00AAAAAA")
            btnHeartT.clicked.connect(lambda: self.VitalClicked("Heart Rate"))



            self.heartBtnList.append(btnHeartT)
            self.heartLblValueList.append(lblHeartValue)
            self.heartLblDateList.append(lblHeartDate)
            self.heartLblUnitList.append(lblHeartUnit)


            #BMI 258 150 106 90

            btnBmi = QPushButton(self)
            btnBmi.setGeometry(startHeartx+118, startHearty, startHeartw, startHearth)
            btnBmi.setStyleSheet(self.normalBtnStyle)

            lblBmiDate = QLabel(self)
            lblBmiDate.setGeometry(startHeartx+120,startHearty+5,startHeartw-6,startHearth-74)
            lblBmiDate.setAlignment(Qt.AlignRight)
            lblBmiDate.setStyleSheet(self.labelSmallStyle)
            lblBmiDate.setText("08-05-21")

            lblBmiUnit = QLabel(self)
            lblBmiUnit.setGeometry(startHeartx+117,startHearty + 64,startHeartw-6,startHearth-70)
            lblBmiUnit.setAlignment(Qt.AlignRight)
            lblBmiUnit.setStyleSheet(self.labelSmallStyle)
            lblBmiUnit.setText("kg/m2")

            lblBmiValue = QLabel(self)
            lblBmiValue.setGeometry(startHeartx+133,startHearty +30,startHeartw-15, startHearth-57)
            lblBmiValue.setAlignment(Qt.AlignLeft)
            lblBmiValue.setStyleSheet(self.labelBigStyle)
            lblBmiValue.setText('18.5')


            btnBmiT = QPushButton(self)
            btnBmiT.setGeometry(startHeartx+118, startHearty, startHeartw, startHearth)
            btnBmiT.setStyleSheet("background-color:#00AAAAAA")
            btnBmiT.clicked.connect(lambda: self.VitalClicked("BMI"))

            self.bmiBtnList.append(btnBmiT)
            self.bmiLblDateList.append(lblBmiDate)
            self.bmiLblUnitList.append(lblBmiUnit)
            self.bmiLblValueList.append(lblBmiValue)


            #Haemoglobin 258 150 106 90

            btnHaemo = QPushButton(self)
            btnHaemo.setGeometry(startHeartx+(118*2), startHearty, startHeartw, startHearth)
            btnHaemo.setStyleSheet(self.normalBtnStyle)

            lblHaemoDate = QLabel(self)
            lblHaemoDate.setGeometry(startHeartx+(118*2 + 2),startHearty+5,startHeartw-6,startHearth-74)
            lblHaemoDate.setAlignment(Qt.AlignRight)
            lblHaemoDate.setStyleSheet(self.labelSmallStyle)
            lblHaemoDate.setText("08-05-21")

            lblHaemoUnit = QLabel(self)
            lblHaemoUnit.setGeometry(startHeartx+(118*2 - 1),startHearty + 64,startHeartw-6,startHearth-70)
            lblHaemoUnit.setAlignment(Qt.AlignRight)
            lblHaemoUnit.setStyleSheet(self.labelSmallStyle)
            lblHaemoUnit.setText("g/dl")

            lblHaemoValue = QLabel(self)
            lblHaemoValue.setGeometry(startHeartx+(118*2+15),startHearty +30,startHeartw-15, startHearth-57)
            lblHaemoValue.setAlignment(Qt.AlignLeft)
            lblHaemoValue.setStyleSheet(self.labelBigStyle)
            lblHaemoValue.setText('13.93')


            btnHaemoT = QPushButton(self)
            btnHaemoT.setGeometry(startHeartx+(118*2), startHearty, startHeartw, startHearth)
            btnHaemoT.setStyleSheet("background-color:#00AAAAAA")
            btnHaemoT.clicked.connect(lambda: self.VitalClicked("Haemoglobin"))

            self.HaemoBtnList.append(btnHaemoT)
            self.HaemoLblDateList.append(lblHaemoDate)
            self.HaemoLblUnitList.append(lblHaemoUnit)
            self.HaemoLblValueList.append(lblHaemoValue)


            #HBA1C 258 150 106 90

            btnHba1c = QPushButton(self)
            btnHba1c.setGeometry(startHeartx+(118*3), startHearty, startHeartw, startHearth)
            btnHba1c.setStyleSheet(self.normalBtnStyle)

            lblHba1cDate = QLabel(self)
            lblHba1cDate.setGeometry(startHeartx+(118*3 + 2),startHearty+5,startHeartw-6,startHearth-74)
            lblHba1cDate.setAlignment(Qt.AlignRight)
            lblHba1cDate.setStyleSheet(self.labelSmallStyle)
            lblHba1cDate.setText("21-01-21")

            lblHba1cUnit = QLabel(self)
            lblHba1cUnit.setGeometry(startHeartx+(118*3 - 1),startHearty + 64,startHeartw-6,startHearth-70)
            lblHba1cUnit.setAlignment(Qt.AlignRight)
            lblHba1cUnit.setStyleSheet(self.labelSmallStyle)
            lblHba1cUnit.setText("mmol/mol")

            lblHba1cValue = QLabel(self)
            lblHba1cValue.setGeometry(startHeartx+(118*3+15),startHearty +30,startHeartw-15, startHearth-57)
            lblHba1cValue.setAlignment(Qt.AlignLeft)
            lblHba1cValue.setStyleSheet(self.labelBigStyle)
            lblHba1cValue.setText('16.8')


            btnHba1cT = QPushButton(self)
            btnHba1cT.setGeometry(startHeartx+(118*3), startHearty, startHeartw, startHearth)
            btnHba1cT.setStyleSheet("background-color:#00AAAAAA")
            btnHba1cT.clicked.connect(lambda: self.VitalClicked("HBA1C"))

            self.Hba1cBtnList.append(btnHba1cT)
            self.Hba1cLblDateList.append(lblHba1cDate)
            self.Hba1cLblUnitList.append(lblHba1cUnit)
            self.Hba1cLblValueList.append(lblHba1cValue)


            #Sugar

            btnSugar = QPushButton(self)
            btnSugar.setGeometry(startHeartx+(118*4), startHearty, startHeartw, startHearth)
            btnSugar.setStyleSheet(self.normalBtnStyle)

            lblSugarDate = QLabel(self)
            lblSugarDate.setGeometry(startHeartx+(118*4 + 2),startHearty+5,startHeartw-6,startHearth-74)
            lblSugarDate.setAlignment(Qt.AlignRight)
            lblSugarDate.setStyleSheet(self.labelSmallStyle)
            lblSugarDate.setText("15-03-21")

            lblSugarUnit = QLabel(self)
            lblSugarUnit.setGeometry(startHeartx+(118*4 - 1),startHearty + 64,startHeartw-6,startHearth-70)
            lblSugarUnit.setAlignment(Qt.AlignRight)
            lblSugarUnit.setStyleSheet(self.labelSmallStyle)
            lblSugarUnit.setText("mmol/mol")

            lblSugarValue = QLabel(self)
            lblSugarValue.setGeometry(startHeartx+(118*4+15),startHearty +30,startHeartw-15, startHearth-57)
            lblSugarValue.setAlignment(Qt.AlignLeft)
            lblSugarValue.setStyleSheet(self.labelBigStyle)
            lblSugarValue.setText('110')


            btnSugarT = QPushButton(self)
            btnSugarT.setGeometry(startHeartx+(118*4), startHearty, startHeartw, startHearth)
            btnSugarT.setStyleSheet("background-color:#00AAAAAA")
            btnSugarT.clicked.connect(lambda: self.VitalClicked("Sugar"))

            self.SugarBtnList.append(btnSugarT)
            self.SugarLblDateList.append(lblSugarDate)
            self.SugarLblUnitList.append(lblSugarUnit)
            self.SugarLblValueList.append(lblSugarValue)


            #Cholestrol

            btnCholes = QPushButton(self)
            btnCholes.setGeometry(startHeartx+(118*5), startHearty, startHeartw, startHearth)
            btnCholes.setStyleSheet(self.normalBtnStyle)

            lblCholesDate = QLabel(self)
            lblCholesDate.setGeometry(startHeartx+(118*5 + 2),startHearty+5,startHeartw-6,startHearth-74)
            lblCholesDate.setAlignment(Qt.AlignRight)
            lblCholesDate.setStyleSheet(self.labelSmallStyle)
            lblCholesDate.setText("12-02-21")

            lblCholesUnit = QLabel(self)
            lblCholesUnit.setGeometry(startHeartx+(118*5 - 1),startHearty + 64,startHeartw-6,startHearth-70)
            lblCholesUnit.setAlignment(Qt.AlignRight)
            lblCholesUnit.setStyleSheet(self.labelSmallStyle)
            lblCholesUnit.setText("mg/dl")

            lblCholesValue = QLabel(self)
            lblCholesValue.setGeometry(startHeartx+(118*5+15),startHearty +30,startHeartw-15, startHearth-57)
            lblCholesValue.setAlignment(Qt.AlignLeft)
            lblCholesValue.setStyleSheet(self.labelBigStyle)
            lblCholesValue.setText('3.32')


            btnCholesT = QPushButton(self)
            btnCholesT.setGeometry(startHeartx+(118*5), startHearty, startHeartw, startHearth)
            btnCholesT.setStyleSheet("background-color:#00AAAAAA")
            btnCholesT.clicked.connect(lambda: self.VitalClicked("Cholestrol"))

            self.CholesBtnList.append(btnCholesT)
            self.CholesLblDateList.append(lblCholesDate)
            self.CholesLblUnitList.append(lblCholesUnit)
            self.CholesLblValueList.append(lblCholesValue)

            #Pt/Nr

            btnPtnr = QPushButton(self)
            btnPtnr.setGeometry(startHeartx+(118*6), startHearty, startHeartw, startHearth)
            btnPtnr.setStyleSheet(self.normalBtnStyle)

            lblPtnrDate = QLabel(self)
            lblPtnrDate.setGeometry(startHeartx+(118*6 + 2),startHearty+5,startHeartw-6,startHearth-74)
            lblPtnrDate.setAlignment(Qt.AlignRight)
            lblPtnrDate.setStyleSheet(self.labelSmallStyle)
            lblPtnrDate.setText("06-08-20")

            lblPtnrUnit = QLabel(self)
            lblPtnrUnit.setGeometry(startHeartx+(118*6 - 1),startHearty + 64,startHeartw-6,startHearth-70)
            lblPtnrUnit.setAlignment(Qt.AlignRight)
            lblPtnrUnit.setStyleSheet(self.labelSmallStyle)
            lblPtnrUnit.setText("bpm")

            lblPtnrValue = QLabel(self)
            lblPtnrValue.setGeometry(startHeartx+(118*6+15),startHearty +30,startHeartw-15, startHearth-57)
            lblPtnrValue.setAlignment(Qt.AlignLeft)
            lblPtnrValue.setStyleSheet(self.labelBigStyle)
            lblPtnrValue.setText('98')


            btnPtnrT = QPushButton(self)
            btnPtnrT.setGeometry(startHeartx+(118*6), startHearty, startHeartw, startHearth)
            btnPtnrT.setStyleSheet("background-color:#00AAAAAA")
            btnPtnrT.clicked.connect(lambda: self.VitalClicked("Pt/Nr"))

            self.PtnrBtnList.append(btnPtnrT)
            self.PtnrLblDateList.append(lblPtnrDate)
            self.PtnrLblUnitList.append(lblPtnrUnit)
            self.PtnrLblValueList.append(lblPtnrValue)

            #Temperature

            btnTemperature = QPushButton(self)
            btnTemperature.setGeometry(startHeartx+(118*7), startHearty, startHeartw, startHearth)
            btnTemperature.setStyleSheet(self.normalBtnStyle)

            lblTemperatureDate = QLabel(self)
            lblTemperatureDate.setGeometry(startHeartx+(118*7 + 2),startHearty+5,startHeartw-6,startHearth-74)
            lblTemperatureDate.setAlignment(Qt.AlignRight)
            lblTemperatureDate.setStyleSheet(self.labelSmallStyle)
            lblTemperatureDate.setText("14-06-21")

            lblTemperatureUnit = QLabel(self)
            lblTemperatureUnit.setGeometry(startHeartx+(118*7 - 1),startHearty + 64,startHeartw-6,startHearth-70)
            lblTemperatureUnit.setAlignment(Qt.AlignRight)
            lblTemperatureUnit.setStyleSheet(self.labelSmallStyle)
            lblTemperatureUnit.setText("f")

            lblTemperatureValue = QLabel(self)
            lblTemperatureValue.setGeometry(startHeartx+(118*7+15),startHearty +30,startHeartw-15, startHearth-57)
            lblTemperatureValue.setAlignment(Qt.AlignLeft)
            lblTemperatureValue.setStyleSheet(self.labelBigStyle)
            lblTemperatureValue.setText('99.13')


            btnTemperatureT = QPushButton(self)
            btnTemperatureT.setGeometry(startHeartx+(118*7), startHearty, startHeartw, startHearth)
            btnTemperatureT.setStyleSheet("background-color:#00AAAAAA")
            btnTemperatureT.clicked.connect(lambda: self.VitalClicked("Temperature"))

            self.TemperatureBtnList.append(btnTemperatureT)
            self.TemperatureLblDateList.append(lblTemperatureDate)
            self.TemperatureLblUnitList.append(lblTemperatureUnit)
            self.TemperatureLblValueList.append(lblTemperatureValue)

    def VitalClicked(self,vital):
        print(vital)
        self.x = statsDetailed.MyStatsDetailed(vital)
        self.x.show()



if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = MyStats()

    window.show()

    # start the app
    sys.exit(App.exec_())