from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Utility.MahiUtility as Util
import math
import UI.MyStatsDetailed as statsDetailed
# importing packages
# import matplotlib.pyplot as plt
from pyqtgraph import PlotWidget, plot
import API.api_calls as myApis
import pyqtgraph as pg
import UI.AddMyStats as addStats

class MyStats(QMainWindow):

    def __init__(self,type):
        super().__init__()
        self.setWindowTitle("My Stats")
        # setting geometry
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setStyleSheet("background-color:#FEC32E")
        self.label.setGeometry(0, 0, 1220, 39)

        self.pageInit = type

        self.UiComponents()

        # showing all the widgets
        self.show()

    def UiComponents(self):

        self.initVitals()

        self.lblHideVitals = QLabel(self)
        self.lblHideVitals.setGeometry(0,120,1500,1000)
        self.lblHideVitals.setStyleSheet("background-color:#F0F0F3")
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
        addReadingsBtn1.clicked.connect(self.AddReadingsClicked)

        self.vitalsCombo1 = QComboBox(self)
        self.vitalsCombo1.setGeometry(187, 57, 214, 50)
        self.vitalsCombo1.setStyleSheet("QComboBox {border-radius: 10; color: #00A0B5; }"
                                        "QComboBox::drop-down { background:rgb(255,255,255,0)}")
        self.vitalsCombo1.setGraphicsEffect(Util.getNeuShadow(1))

        self.vitalsCombo = QComboBox(self)
        self.vitalsCombo.setGeometry(187, 57, 214, 50)
        self.vitalsCombo.setStyleSheet("QComboBox {border-radius: 10; color: #00A0B5; padding-left:15px;font-size:18px}"
                                       "QComboBox::drop-down { background:rgb(255,255,255,0);padding-right:20px}"
                                       "QComboBox::down-arrow{image: url(../Resources/dropDown.png)}")
        self.vitalsCombo.setGraphicsEffect(Util.getNeuShadow(0))
        self.vitalsCombo.addItem("All Vitals")
        self.vitalsCombo.currentIndexChanged.connect(self.vitalChanged)

        syncBtn = QPushButton(self)
        syncBtn.setGeometry(133, 63, 45, 45)
        syncBtn.setStyleSheet("border-radius: 8; background-color: #F0F0F3")
        syncBtn.setIcon(QtGui.QIcon('..\Resources\\syncBtn.png'))
        syncBtn.setIconSize(QtCore.QSize(112, 52))
        syncBtn.setGraphicsEffect(Util.getNeuShadow(0))
        syncBtn.clicked.connect(self.close)

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

        self.filterBtn = QComboBox(self)
        self.filterBtn.setStyleSheet("QComboBox {border-radius: 10; color: #00A0B5 }"
                                "QComboBox::drop-down { background:rgb(255,255,255,0);padding-right:20px}")
        self.filterBtn.setGeometry(1082, 135, 110, 50)
        self.filterBtn.setGraphicsEffect(Util.getNeuShadow(0))
        self.filterBtn1 = QComboBox(self)
        self.filterBtn1.setGeometry(1082, 135, 110, 50)
        self.filterBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        self.filterBtn1.addItem("Weekly")
        self.filterBtn1.addItem("Monthly")
        self.filterBtn1.addItem("Yearly")
        self.filterBtn1.setStyleSheet("QComboBox {border-radius: 10; color: #00A0B5;padding-left:15px;font-size:18px }"
                                      "QComboBox::drop-down { background:rgb(255,255,255,0);padding-right:20px}"
                                      "QComboBox::down-arrow{image: url(../Resources/dropDown.png)}")
        # self.filterBtn1.addItem("Haemoglobin")
        # filterBtn1.clicked.connect(self.)

        self.tableBtn = QPushButton(self)
        self.tableBtn.setStyleSheet("border-radius: 15;")
        self.tableBtn.setGeometry(1082, 213, 110, 130)
        self.tableBtn.setGraphicsEffect(Util.getNeuShadow(0))
        self.tableBtn1 = QPushButton(self)
        self.tableBtn1.setStyleSheet("border-radius: 15;")
        self.tableBtn1.setGeometry(1082, 213, 110, 130)
        self.tableBtn1.setIcon(QtGui.QIcon('..\Resources\\table.png'))
        self.tableBtn1.setIconSize(QtCore.QSize(110, 130))
        self.tableBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        self.tableBtn1.clicked.connect(self.tableClick)

        self.graphBtn = QPushButton(self)
        self.graphBtn.setStyleSheet("border-radius: 15;")
        self.graphBtn.setGeometry(1082, 371, 110, 130)
        self.graphBtn.setGraphicsEffect(Util.getNeuShadow(0))
        self.graphBtn1 = QPushButton(self)
        self.graphBtn1.setStyleSheet("border-radius: 15;")
        self.graphBtn1.setGeometry(1082, 371, 110, 130)
        self.graphBtn1.setIcon(QtGui.QIcon('..\Resources\\graph.png'))
        self.graphBtn1.setIconSize(QtCore.QSize(110, 130))
        self.graphBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        self.graphBtn1.clicked.connect(self.GraphViewClicked)

        self.helpBtn = QPushButton(self)
        self.helpBtn.setStyleSheet("border-radius: 15;")
        self.helpBtn.setGeometry(1082, 529, 110, 130)
        self.helpBtn.setGraphicsEffect(Util.getNeuShadow(0))
        self.helpBtn1 = QPushButton(self)
        self.helpBtn1.setStyleSheet("border-radius: 15;")
        self.helpBtn1.setGeometry(1082, 529, 110, 130)
        self.helpBtn1.setIcon(QtGui.QIcon('..\Resources\\helpStats.png'))
        self.helpBtn1.setIconSize(QtCore.QSize(110, 130))
        self.helpBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        self.helpBtn1.clicked.connect(self.helpClick)

        self.initTableView()
        self.initGraph()

        if self.pageInit == 0:
            self.showAllVitals()
        else:
            self.vitalsCombo.setCurrentIndex(self.pageInit)


        self.fetchVitalsList()
        self.fetchLastVitalsData()

    def fetchVitalsList(self):
        try:
            if Util.isInternetOn():
                temp = myApis.fetchVitalList()
                if temp!= None:
                    self.vitalList = temp["details"]
                    for x in self.vitalList:
                        self.vitalsCombo.addItem(x["vital_name"])

        except Exception as e:
            print(e.__cause__)

    def fetchLastVitalsData(self):
        try:

            if Util.isInternetOn():
                temp = myApis.fetchLastVitalsData()

                if temp!= None:
                    self.allVitalsResponse = temp["response"]
                    self.bmiDataList1 = None
                    for vitals in self.allVitalsResponse:
                        self.setVitalsData(vitals["vital_name"], vitals["vital_data"], vitals["unit"])


        except Exception as e:
            print(e.__cause__)

    def setVitalsData(self, vitalName, vitalData, unit):

        try:

            if str(vitalName).upper() == "HAEMOGLOBIN":
                i = 0
                for data in vitalData:
                    self.HaemoLblValueList[i].setText(str(data["point"]))
                    self.HaemoLblDateList[i].setText(str(data["date"]))
                    self.HaemoLblUnitList[i].setText(str(unit))

                    if len(data["mahi_vital_color_code"])>0:
                        if data["mahi_vital_color_code"] == "blue":
                            self.HaemoBkgBtnList[i].setStyleSheet(self.normalBtnStyle)
                        elif data["mahi_vital_color_code"] == "red":
                            self.HaemoBkgBtnList[i].setStyleSheet(self.redBtnStyle)
                        else:
                            self.HaemoBkgBtnList[i].setStyleSheet(self.orangeBtnStyle)
                    else:
                        self.HaemoBkgBtnList[i].setStyleSheet(self.normalBtnStyle)
                    i = i+1

            elif str(vitalName).upper() == "CHOLESTEROL":
                i = 0
                for data in vitalData:
                    self.CholesLblValueList[i].setText(str(data["point"]))
                    self.CholesLblDateList[i].setText(str(data["date"]))
                    self.CholesLblUnitList[i].setText(str(unit))

                    if len(data["mahi_vital_color_code"])>0:
                        if data["mahi_vital_color_code"] == "blue":
                            self.CholesBkgBtnList[i].setStyleSheet(self.normalBtnStyle)
                        elif data["mahi_vital_color_code"] == "red":
                            self.CholesBkgBtnList[i].setStyleSheet(self.redBtnStyle)
                        else:
                            self.CholesBkgBtnList[i].setStyleSheet(self.orangeBtnStyle)
                    else:
                        self.CholesBkgBtnList[i].setStyleSheet(self.normalBtnStyle)

                    i = i + 1

            elif str(vitalName).upper() == "HBA1C":
                i = 0
                for data in vitalData:
                    self.Hba1cLblValueList[i].setText(str(data["point"]))
                    self.Hba1cLblDateList[i].setText(str(data["date"]))
                    self.Hba1cLblUnitList[i].setText(str(unit))

                    if len(data["mahi_vital_color_code"])>0:
                        if data["mahi_vital_color_code"] == "blue":
                            self.Hba1cBkgBtnList[i].setStyleSheet(self.normalBtnStyle)
                        elif data["mahi_vital_color_code"] == "red":
                            self.Hba1cBkgBtnList[i].setStyleSheet(self.redBtnStyle)
                        else:
                            self.Hba1cBkgBtnList[i].setStyleSheet(self.orangeBtnStyle)
                    else:
                        self.Hba1cBkgBtnList[i].setStyleSheet(self.normalBtnStyle)

                    i = i + 1

            elif str(vitalName).upper() == "PT/INR":
                i = 0
                for data in vitalData:
                    self.PtnrLblValueList[i].setText(str(data["point"]["PT"])+"/"+str(data["point"]["INR"]))
                    self.PtnrLblDateList[i].setText(str(data["date"]))
                    self.PtnrLblUnitList[i].setText(str(unit))

                    if len(data["mahi_vital_color_code"])>0:
                        if data["mahi_vital_color_code"] == "blue":
                            self.PtnrBkgBtnList[i].setStyleSheet(self.normalBtnStyle)
                        elif data["mahi_vital_color_code"] == "red":
                            self.PtnrBkgBtnList[i].setStyleSheet(self.redBtnStyle)
                        else:
                            self.PtnrBkgBtnList[i].setStyleSheet(self.orangeBtnStyle)
                    else:
                        self.PtnrBkgBtnList[i].setStyleSheet(self.normalBtnStyle)

                    i = i + 1

            elif str(vitalName).upper() == "HEART RATE":
                i = 0
                for data in vitalData:
                    self.heartLblValueList[i].setText(str(data["point"]))
                    self.heartLblDateList[i].setText(str(data["date"]))
                    self.heartLblUnitList[i].setText(str(unit))

                    if len(data["mahi_vital_color_code"])>0:
                        if data["mahi_vital_color_code"] == "blue":
                            self.heartBkgBtnList[i].setStyleSheet(self.normalBtnStyle)
                        elif data["mahi_vital_color_code"] == "red":
                            self.heartBkgBtnList[i].setStyleSheet(self.redBtnStyle)
                        else:
                            self.heartBkgBtnList[i].setStyleSheet(self.orangeBtnStyle)
                    else:
                        self.heartBkgBtnList[i].setStyleSheet(self.normalBtnStyle)

                    i = i + 1

            elif str(vitalName).upper() == "HEIGHT" or str(vitalName).upper() == "WEIGHT":
                if self.bmiDataList1 == None:
                    self.bmiDataList1 = vitalData
                else:
                    i = 0
                    for data in vitalData:
                        if(str(vitalName).upper() == "WEIGHT"):
                            tempHeight = float(self.bmiDataList1[i]["point"])/100
                            bmi = round(float(data["point"]) / (tempHeight*tempHeight) , 1)

                        self.bmiLblValueList[i].setText(str(bmi))
                        self.bmiLblDateList[i].setText(str(data["date"]))
                        self.bmiLblUnitList[i].setText("kg/m2")

                        if len(data["mahi_vital_color_code"])>0:
                            if data["mahi_vital_color_code"] == "blue":
                                self.bmiBkgBtnList[i].setStyleSheet(self.normalBtnStyle)
                            elif data["mahi_vital_color_code"] == "red":
                                self.bmiBkgBtnList[i].setStyleSheet(self.redBtnStyle)
                            else:
                                self.bmiBkgBtnList[i].setStyleSheet(self.orangeBtnStyle)
                        else:
                            self.bmiBkgBtnList[i].setStyleSheet(self.normalBtnStyle)

                        i = i + 1

            elif str(vitalName).upper() == "SUGAR":
                i = 0
                for data in vitalData:
                    self.SugarLblValueList[i].setText(str(data["point"]))
                    self.SugarLblDateList[i].setText(str(data["date"]))
                    self.SugarLblUnitList[i].setText(str(unit))

                    if len(data["mahi_vital_color_code"])>0:
                        if data["mahi_vital_color_code"] == "blue":
                            self.SugarBkgBtnList[i].setStyleSheet(self.normalBtnStyle)
                        elif data["mahi_vital_color_code"] == "red":
                            self.SugarBkgBtnList[i].setStyleSheet(self.redBtnStyle)
                        else:
                            self.SugarBkgBtnList[i].setStyleSheet(self.orangeBtnStyle)
                    else:
                        self.SugarBkgBtnList[i].setStyleSheet(self.normalBtnStyle)

                    i = i + 1

            elif str(vitalName).upper() == "TEMPERATURE":
                i = 0
                for data in vitalData:
                    self.TemperatureLblValueList[i].setText(str(data["point"]))
                    self.TemperatureLblDateList[i].setText(str(data["date"]))
                    self.TemperatureLblUnitList[i].setText(str(unit))

                    if len(data["mahi_vital_color_code"])>0:
                        if data["mahi_vital_color_code"] == "blue":
                            self.TemperatureBkgBtnList[i].setStyleSheet(self.normalBtnStyle)
                        elif data["mahi_vital_color_code"] == "red":
                            self.TemperatureBkgBtnList[i].setStyleSheet(self.redBtnStyle)
                        else:
                            self.TemperatureBkgBtnList[i].setStyleSheet(self.orangeBtnStyle)
                    else:
                        self.TemperatureBkgBtnList[i].setStyleSheet(self.normalBtnStyle)

                    i = i + 1

            elif str(vitalName).upper() == "BLOOD PRESSURE":
                i = 0
                for data in vitalData:
                    self.bpLblValueList[i].setText('<font color="#FFF">'+str(data["point"]["Systolic"])+' </font><font color="#006CB5">SYS</font>'
                                       '<font color="#FFF">   '+str(data["point"]["Diastolic"])+' </font><font color="#006CB5">DIA</font>')
                    # self.bpLblValueList[i].setText(str(data["point"]))
                    self.bpLblDateList[i].setText(str(data["date"]))
                    self.bpLblUnitList[i].setText(str(unit))

                    if len(data["mahi_vital_color_code"])>0:
                        if data["mahi_vital_color_code"] == "blue":
                            self.bpBkgBtnList[i].setStyleSheet(self.normalBtnStyle)
                        elif data["mahi_vital_color_code"] == "red":
                            self.bpBkgBtnList[i].setStyleSheet(self.redBtnStyle)
                        else:
                            self.bpBkgBtnList[i].setStyleSheet(self.orangeBtnStyle)
                    else:
                        self.bpBkgBtnList[i].setStyleSheet(self.normalBtnStyle)

                    i = i + 1

        except Exception as e:
            print(e.__cause__)

    def initVitals(self):

        self.normalBtnStyle = "border-radius: 10; background-color: #7ACEDA;"
        self.redBtnStyle = "border-radius: 10; background-color: #FE4343;"
        self.orangeBtnStyle = "border-radius: 10; background-color: #FEC32E;"
        self.labelSmallStyle = "background-color:#00AAAAAA; color:white; font-size:15px; font:bold"
        self.labelHeaderStyle = "background-color:#00AAAAAA; color:#727376; font-size:15px"
        self.labelBigStyle = "background-color:#00AAAAAA; color:white; font-size:22px; font:bold"

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




        self.bpBkgBtnList = []
        self.bpBtnList = []
        self.bpLblValueList = []
        self.bpLblDateList = []
        self.bpLblUnitList = []

        self.heartBkgBtnList = []
        self.heartBtnList = []
        self.heartLblValueList = []
        self.heartLblDateList = []
        self.heartLblUnitList = []

        self.bmiBkgBtnList = []
        self.bmiBtnList = []
        self.bmiLblValueList = []
        self.bmiLblDateList = []
        self.bmiLblUnitList = []

        self.HaemoBkgBtnList = []
        self.HaemoBtnList = []
        self.HaemoLblValueList = []
        self.HaemoLblDateList = []
        self.HaemoLblUnitList = []

        self.Hba1cBkgBtnList = []
        self.Hba1cBtnList = []
        self.Hba1cLblValueList = []
        self.Hba1cLblDateList = []
        self.Hba1cLblUnitList = []

        self.SugarBkgBtnList = []
        self.SugarBtnList = []
        self.SugarLblValueList = []
        self.SugarLblDateList = []
        self.SugarLblUnitList = []

        self.CholesBkgBtnList = []
        self.CholesBtnList = []
        self.CholesLblValueList = []
        self.CholesLblDateList = []
        self.CholesLblUnitList = []

        self.PtnrBkgBtnList = []
        self.PtnrBtnList = []
        self.PtnrLblValueList = []
        self.PtnrLblDateList = []
        self.PtnrLblUnitList = []

        self.TemperatureBkgBtnList = []
        self.TemperatureBtnList = []
        self.TemperatureLblValueList = []
        self.TemperatureLblDateList = []
        self.TemperatureLblUnitList = []

        self.blueBkg = "background-color:#00AAAAAA"

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

            lblBpUnit1 = QLabel(self)
            lblBpUnit1.setGeometry(startLblx,startLbly+60,startLblw,startLblh+10)
            lblBpUnit1.setAlignment(Qt.AlignRight)
            lblBpUnit1.setStyleSheet(self.labelSmallStyle)

            lblBpValue = QLabel(self)
            lblBpValue.setGeometry(startBpx+10,startBpy+30,startBpw-20,startBph-65)
            lblBpValue.setAlignment(Qt.AlignRight)
            lblBpValue.setStyleSheet(self.labelBigStyle)
            lblBpValue.setText('<font color="#FFF">100 </font><font color="#006CB5">SYS</font>'
                                    '<font color="#FFF">   85 </font><font color="#006CB5">DIA</font>')

            btnBp = QPushButton(self)
            btnBp.setGeometry(startBpx,startBpy,startBpw,startBph)
            btnBp.setStyleSheet(self.blueBkg)
            btnBp.clicked.connect(lambda: self.VitalClicked("Blood Pressure"))


            self.bpBkgBtnList.append(btnBp1)
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

            lblHeartUnit = QLabel(self)
            lblHeartUnit.setGeometry(startHeartx-1,startHearty + 64,startHeartw-6,startHearth-70)
            lblHeartUnit.setAlignment(Qt.AlignRight)
            lblHeartUnit.setStyleSheet(self.labelSmallStyle)

            lblHeartValue = QLabel(self)
            lblHeartValue.setGeometry(startHeartx+15,startHearty +30,startHeartw-15, startHearth-57)
            lblHeartValue.setAlignment(Qt.AlignLeft)
            lblHeartValue.setStyleSheet(self.labelBigStyle)


            btnHeartT = QPushButton(self)
            btnHeartT.setGeometry(startHeartx, startHearty, startHeartw, startHearth)
            btnHeartT.setStyleSheet(self.blueBkg)
            btnHeartT.clicked.connect(lambda: self.VitalClicked("Heart Rate"))



            self.heartBkgBtnList.append(btnHeart)
            self.heartBtnList.append(btnHeartT)
            self.heartLblValueList.append(lblHeartValue)
            self.heartLblDateList.append(lblHeartDate)
            self.heartLblUnitList.append(lblHeartUnit)


            #BMI

            btnBmi = QPushButton(self)
            btnBmi.setGeometry(startHeartx+118, startHearty, startHeartw, startHearth)
            btnBmi.setStyleSheet(self.normalBtnStyle)

            lblBmiDate = QLabel(self)
            lblBmiDate.setGeometry(startHeartx+120,startHearty+5,startHeartw-6,startHearth-74)
            lblBmiDate.setAlignment(Qt.AlignRight)
            lblBmiDate.setStyleSheet(self.labelSmallStyle)

            lblBmiUnit = QLabel(self)
            lblBmiUnit.setGeometry(startHeartx+117,startHearty + 64,startHeartw-6,startHearth-70)
            lblBmiUnit.setAlignment(Qt.AlignRight)
            lblBmiUnit.setStyleSheet(self.labelSmallStyle)

            lblBmiValue = QLabel(self)
            lblBmiValue.setGeometry(startHeartx+133,startHearty +30,startHeartw-15, startHearth-57)
            lblBmiValue.setAlignment(Qt.AlignLeft)
            lblBmiValue.setStyleSheet(self.labelBigStyle)


            btnBmiT = QPushButton(self)
            btnBmiT.setGeometry(startHeartx+118, startHearty, startHeartw, startHearth)
            btnBmiT.setStyleSheet(self.blueBkg)
            btnBmiT.clicked.connect(lambda: self.VitalClicked("BMI"))

            self.bmiBkgBtnList.append(btnBmi)
            self.bmiBtnList.append(btnBmiT)
            self.bmiLblDateList.append(lblBmiDate)
            self.bmiLblUnitList.append(lblBmiUnit)
            self.bmiLblValueList.append(lblBmiValue)


            #Haemoglobin

            btnHaemo = QPushButton(self)
            btnHaemo.setGeometry(startHeartx+(118*2), startHearty, startHeartw, startHearth)
            btnHaemo.setStyleSheet(self.normalBtnStyle)

            lblHaemoDate = QLabel(self)
            lblHaemoDate.setGeometry(startHeartx+(118*2 + 2),startHearty+5,startHeartw-6,startHearth-74)
            lblHaemoDate.setAlignment(Qt.AlignRight)
            lblHaemoDate.setStyleSheet(self.labelSmallStyle)

            lblHaemoUnit = QLabel(self)
            lblHaemoUnit.setGeometry(startHeartx+(118*2 - 1),startHearty + 64,startHeartw-6,startHearth-70)
            lblHaemoUnit.setAlignment(Qt.AlignRight)
            lblHaemoUnit.setStyleSheet(self.labelSmallStyle)

            lblHaemoValue = QLabel(self)
            lblHaemoValue.setGeometry(startHeartx+(118*2+15),startHearty +30,startHeartw-15, startHearth-57)
            lblHaemoValue.setAlignment(Qt.AlignLeft)
            lblHaemoValue.setStyleSheet(self.labelBigStyle)


            btnHaemoT = QPushButton(self)
            btnHaemoT.setGeometry(startHeartx+(118*2), startHearty, startHeartw, startHearth)
            btnHaemoT.setStyleSheet(self.blueBkg)
            btnHaemoT.clicked.connect(lambda: self.VitalClicked("Haemoglobin"))

            self.HaemoBkgBtnList.append(btnHaemo)
            self.HaemoBtnList.append(btnHaemoT)
            self.HaemoLblDateList.append(lblHaemoDate)
            self.HaemoLblUnitList.append(lblHaemoUnit)
            self.HaemoLblValueList.append(lblHaemoValue)


            #HBA1C

            btnHba1c = QPushButton(self)
            btnHba1c.setGeometry(startHeartx+(118*3), startHearty, startHeartw, startHearth)
            btnHba1c.setStyleSheet(self.normalBtnStyle)

            lblHba1cDate = QLabel(self)
            lblHba1cDate.setGeometry(startHeartx+(118*3 + 2),startHearty+5,startHeartw-6,startHearth-74)
            lblHba1cDate.setAlignment(Qt.AlignRight)
            lblHba1cDate.setStyleSheet(self.labelSmallStyle)

            lblHba1cUnit = QLabel(self)
            lblHba1cUnit.setGeometry(startHeartx+(118*3 - 1),startHearty + 64,startHeartw-6,startHearth-70)
            lblHba1cUnit.setAlignment(Qt.AlignRight)
            lblHba1cUnit.setStyleSheet(self.labelSmallStyle)

            lblHba1cValue = QLabel(self)
            lblHba1cValue.setGeometry(startHeartx+(118*3+15),startHearty +30,startHeartw-15, startHearth-57)
            lblHba1cValue.setAlignment(Qt.AlignLeft)
            lblHba1cValue.setStyleSheet(self.labelBigStyle)


            btnHba1cT = QPushButton(self)
            btnHba1cT.setGeometry(startHeartx+(118*3), startHearty, startHeartw, startHearth)
            btnHba1cT.setStyleSheet(self.blueBkg)
            btnHba1cT.clicked.connect(lambda: self.VitalClicked("HBA1C"))

            self.Hba1cBkgBtnList.append(btnHba1c)
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

            lblSugarUnit = QLabel(self)
            lblSugarUnit.setGeometry(startHeartx+(118*4 - 1),startHearty + 64,startHeartw-6,startHearth-70)
            lblSugarUnit.setAlignment(Qt.AlignRight)
            lblSugarUnit.setStyleSheet(self.labelSmallStyle)

            lblSugarValue = QLabel(self)
            lblSugarValue.setGeometry(startHeartx+(118*4+15),startHearty +30,startHeartw-15, startHearth-57)
            lblSugarValue.setAlignment(Qt.AlignLeft)
            lblSugarValue.setStyleSheet(self.labelBigStyle)


            btnSugarT = QPushButton(self)
            btnSugarT.setGeometry(startHeartx+(118*4), startHearty, startHeartw, startHearth)
            btnSugarT.setStyleSheet(self.blueBkg)
            btnSugarT.clicked.connect(lambda: self.VitalClicked("Sugar"))

            self.SugarBkgBtnList.append(btnSugar)
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

            lblCholesUnit = QLabel(self)
            lblCholesUnit.setGeometry(startHeartx+(118*5 - 1),startHearty + 64,startHeartw-6,startHearth-70)
            lblCholesUnit.setAlignment(Qt.AlignRight)
            lblCholesUnit.setStyleSheet(self.labelSmallStyle)

            lblCholesValue = QLabel(self)
            lblCholesValue.setGeometry(startHeartx+(118*5+15),startHearty +30,startHeartw-15, startHearth-57)
            lblCholesValue.setAlignment(Qt.AlignLeft)
            lblCholesValue.setStyleSheet(self.labelBigStyle)

            btnCholesT = QPushButton(self)
            btnCholesT.setGeometry(startHeartx+(118*5), startHearty, startHeartw, startHearth)
            btnCholesT.setStyleSheet(self.blueBkg)
            btnCholesT.clicked.connect(lambda: self.VitalClicked("Cholestrol"))

            self.CholesBkgBtnList.append(btnCholes)
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

            lblPtnrUnit = QLabel(self)
            lblPtnrUnit.setGeometry(startHeartx+(118*6 - 1),startHearty + 64,startHeartw-6,startHearth-70)
            lblPtnrUnit.setAlignment(Qt.AlignRight)
            lblPtnrUnit.setStyleSheet(self.labelSmallStyle)

            lblPtnrValue = QLabel(self)
            lblPtnrValue.setGeometry(startHeartx+(118*6+15),startHearty +30,startHeartw-15, startHearth-57)
            lblPtnrValue.setAlignment(Qt.AlignLeft)
            lblPtnrValue.setStyleSheet(self.labelBigStyle)

            btnPtnrT = QPushButton(self)
            btnPtnrT.setGeometry(startHeartx+(118*6), startHearty, startHeartw, startHearth)
            btnPtnrT.setStyleSheet(self.blueBkg)
            btnPtnrT.clicked.connect(lambda: self.VitalClicked("Pt/Nr"))

            self.PtnrBkgBtnList.append(btnPtnr)
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

            lblTemperatureUnit = QLabel(self)
            lblTemperatureUnit.setGeometry(startHeartx+(118*7 - 1),startHearty + 64,startHeartw-6,startHearth-70)
            lblTemperatureUnit.setAlignment(Qt.AlignRight)
            lblTemperatureUnit.setStyleSheet(self.labelSmallStyle)

            lblTemperatureValue = QLabel(self)
            lblTemperatureValue.setGeometry(startHeartx+(118*7+15),startHearty +30,startHeartw-15, startHearth-57)
            lblTemperatureValue.setAlignment(Qt.AlignLeft)
            lblTemperatureValue.setStyleSheet(self.labelBigStyle)


            btnTemperatureT = QPushButton(self)
            btnTemperatureT.setGeometry(startHeartx+(118*7), startHearty, startHeartw, startHearth)
            btnTemperatureT.setStyleSheet(self.blueBkg)
            btnTemperatureT.clicked.connect(lambda: self.VitalClicked("Temperature"))

            self.TemperatureBkgBtnList.append(btnTemperature)
            self.TemperatureBtnList.append(btnTemperatureT)
            self.TemperatureLblDateList.append(lblTemperatureDate)
            self.TemperatureLblUnitList.append(lblTemperatureUnit)
            self.TemperatureLblValueList.append(lblTemperatureValue)

    def initGraph(self):
        self.graph = PlotWidget()
        # self.setCentralWidget(self.graph)
        hour1 = ["20/03/21", "08/09/20", "05/11/20", "28/10/20", "01/07/20", "08/03/21", "18/01/21", "16/03/21",
                 "11/03/21", "19/04/21"]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        self.graph.setBackground('w')
        self.graph.plot(range(len(hour1)), temperature, symbol='o')
        xax = self.graph.getAxis('bottom')
        ticks = [list(zip(range(len(hour1)), hour1))]
        xax.setTicks(ticks)

        self.gridLayoutWidget = QWidget(self)
        rect = QtCore.QRect(21, 133, 1043, 530)
        self.gridLayoutWidget.setGeometry(rect)
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        # frame = QFrame(self)
        # frame.setGeometry(21, 133, 1043, 523)
        # frame.setStyleSheet("background-color:red")
        # self.gridLayout.setParent(frame)
        self.gridLayout.addWidget(self.graph, 0, 0, 1, 3)
        self.gridLayoutWidget.setStyleSheet("background-color:white")

    def initTableView(self):
        # Graph View

        self.lblTable = QLabel(self)
        self.lblTable.setGeometry(21, 133, 1043, 530)
        self.lblTable.setStyleSheet("background-color: #FFFFFF")

        startx = 60
        starty = 210
        startw = 122
        starth = 86
        rowcount = 1

        self.cbSubVitalsB = QComboBox(self)
        self.cbSubVitalsB.setStyleSheet("QComboBox {border-radius: 10; color: #00A0B5; }"
                                "QComboBox::drop-down { background:rgb(255,255,255,0);padding-right:20px}")
        self.cbSubVitalsB.setGeometry(890, 145, 130, 40)
        self.cbSubVitalsB.setGraphicsEffect(Util.getNeuShadow(0))
        self.cbSubVitals = QComboBox(self)
        self.cbSubVitals.setStyleSheet("QComboBox {border-radius: 10; color: #00A0B5;padding-left:15px;font-size:18px }"
                                      "QComboBox::drop-down { background:rgb(255,255,255,0);padding-right:20px}"
                                      "QComboBox::down-arrow{image: url(../Resources/dropDown.png)}")
        self.cbSubVitals.setGeometry(890, 145, 130, 40)
        self.cbSubVitals.setGraphicsEffect(Util.getNeuShadow(1))
        self.cbSubVitals.currentIndexChanged.connect(self.subVitalChanged)
        # self.filterBtn1.addItem("Haemoglobin")
        # filterBtn1.clicked.connect(self.)

        self.btnPageBack = QPushButton(self)
        self.btnPageBack.setGeometry(459, 595, 50, 50)
        self.btnPageBack.setStyleSheet("border-radius : 10; background-color: #F0F03")
        self.btnPageBack.setGraphicsEffect(Util.getNeuShadow(0))

        self.btnPageBack1 = QPushButton(self)
        self.btnPageBack1.setGeometry(459, 595, 50, 50)
        self.btnPageBack1.setStyleSheet("border-radius : 10; background-color: #F0F03;font-size:20px;color:#777")
        self.btnPageBack1.setText("<")
        self.btnPageBack1.setIconSize(QtCore.QSize(115, 41))
        self.btnPageBack1.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnPageBack1.clicked.connect(lambda : self.ChangeTablePage(False))

        self.btnPageNext = QPushButton(self)
        self.btnPageNext.setGeometry(639, 595, 50, 50)
        self.btnPageNext.setStyleSheet("border-radius : 10; background-color: #F0F03 ")
        self.btnPageNext.setGraphicsEffect(Util.getNeuShadow(0))

        self.btnPageNext1 = QPushButton(self)
        self.btnPageNext1.setGeometry(639, 595, 50, 50)
        self.btnPageNext1.setStyleSheet("border-radius : 10; background-color: #F0F03;font-size:20px;color:#777 ")
        self.btnPageNext1.setText(">")
        self.btnPageNext1.setIconSize(QtCore.QSize(115, 41))
        self.btnPageNext1.setGraphicsEffect(Util.getNeuShadow(1))
        self.btnPageNext1.clicked.connect(lambda : self.ChangeTablePage(True))

        self.lblPageNo = QLabel("", self)
        self.lblPageNo.setGeometry(551, 608, 50, 31)
        self.lblPageNo.setStyleSheet("border-radius : 10; background-color: pink")
        self.lblPageNo.setAlignment(Qt.AlignCenter)

        self.lblBkgList = []
        self.lblVitalDateList = []
        self.lblVitalValueList = []
        self.lblVitalUnitList = []

        for i in range(28):

            if (i > 0):
                startx = startx + 140

            if i > 0 and (i) % 7 == 0:
                startx = 60
                starty = starty + 95
                # rowcount = rowcount+1

            lblBkg = QLabel(self)
            pixmap = QtGui.QPixmap('../Resources/graphBkg.png')
            scaledImage = pixmap.scaled(startw, starth)
            lblBkg.setPixmap(QPixmap(scaledImage))
            lblBkg.setGeometry(startx, starty, startw, starth)
            lblBkg.setStyleSheet(self.blueBkg)

            lblDate = QLabel(self)
            lblDate.setGeometry(startx + 11, starty + 9, 99, 29)
            lblDate.setAlignment(Qt.AlignCenter)
            lblDate.setStyleSheet("color:#727376; font-size:17px; background-color:#00FF0000")

            lblValue = QLabel(self)
            lblValue.setGeometry(startx + 16, starty + 39, 89, 29)
            lblValue.setAlignment(Qt.AlignCenter)
            lblValue.setStyleSheet("color:white; font-size:22px; background-color:#00FFFFFF")

            lblUnit = QLabel(self)
            lblUnit.setGeometry(startx + 16, starty + 59, 89, 29)
            lblUnit.setAlignment(Qt.AlignCenter)
            lblUnit.setStyleSheet("color:white; font-size:15px; background-color:#00FFFFFF")

            self.lblBkgList.append(lblBkg)
            self.lblVitalDateList.append(lblDate)
            self.lblVitalUnitList.append(lblUnit)
            self.lblVitalValueList.append(lblValue)

        self.lblTable.hide()

    def ChangeTablePage(self, increase):

        if increase:
            if self.tablePage < self.tableTotalPage:
                self.tablePage = self.tablePage+1
        else:
            if self.tablePage > 1:
                self.tablePage = self.tablePage - 1

        self.SetTableData()

    def VitalClicked(self,vital):
        print(vital)
        self.x = statsDetailed.MyStatsDetailed(vital)
        self.x.show()

    def vitalChanged(self,i):
        print(i)
        self.pageInit = int(i)
        if i == 0:
            self.showAllVitals()
        else:
            self.tablePage = 1
            self.tableClick()
            self.fetchVitalDetails()

    def subVitalChanged(self):
        self.tablePage = 1
        self.SetTableData()

    def fetchVitalDetails(self):
        try:
            if Util.isInternetOn():
                vitalId = self.vitalList[self.pageInit-1]["main_vital_id"]
                temp = myApis.fetchVitalDetails(vitalId)
                if temp!= None:
                    self.vitalDomData = temp["details"]["dom_data"]

                    self.hasSubVitals = False
                    if isinstance(self.vitalDomData["sub_vitals"], (bool)):
                        self.cbSubVitals.hide()
                        self.cbSubVitalsB.hide()
                        self.hasSubVitals = False
                    else:
                        self.cbSubVitals.show()
                        self.cbSubVitalsB.show()
                        self.cbSubVitals.clear()
                        self.hasSubVitals = True

                        for sub in self.vitalDomData["sub_vitals"]:
                            self.cbSubVitals.addItem(sub)

                    print(self.vitalDomData["sub_vitals"])

                    self.fetchSpecificVitalData()

        except Exception as e:
            print(e.__cause__)

    def fetchSpecificVitalData(self):
        try:
            if Util.isInternetOn():
                vitalId = self.vitalList[self.pageInit-1]["main_vital_id"]
                print(vitalId)
                temp = myApis.fetchSpecificVitalData(vitalId)
                if temp!= None:
                    print(temp)
                    self.tableVitalData = temp["response"]
                    self.tableTotalPage = math.ceil(len(self.tableVitalData)/28)
                    self.SetTableData()

        except Exception as e:
            print(e.__cause__)

    def SetTableData(self):
        try:
            self.lblPageNo.setText(str(self.tablePage) + "/" + str(self.tableTotalPage))
            if self.tablePage == 1:
                start = 0
            else:
                start = (self.tablePage - 1 )*28

            if len(self.tableVitalData) > 28*self.tablePage:
                end = 28
            else:
                end = len(self.tableVitalData) - start

            print(str(start)+"|"+str(end))

            for i in range(28):

                if end>0:
                    date = str(self.tableVitalData[start]["date"]).split(" ")[0]
                    self.lblVitalDateList[i].setText(date)
                    self.lblVitalUnitList[i].setText(self.tableVitalData[start]["unit"])
                    end = end - 1

                    if self.hasSubVitals:
                        self.lblVitalValueList[i].setText(str(self.tableVitalData[start]["point"]
                                                              [str(self.cbSubVitals.currentText())]))
                    else:
                        self.lblVitalValueList[i].setText(str(self.tableVitalData[start]["point"]))

                else:
                    self.lblVitalDateList[i].setText("")
                    self.lblVitalUnitList[i].setText("")
                    self.lblVitalValueList[i].setText("")

                start = start+1

        except Exception as e:
            print(e.__cause__)

    def tableClick(self):
        self.toggleTable(True)
        self.gridLayoutWidget.hide()
        self.lblHideVitals.show()
        self.toggleSidePanel(True)

    def helpClick(self):
        print("pressed")

    def GraphViewClicked(self):
        self.toggleTable(False)
        self.gridLayoutWidget.show()
        self.lblHideVitals.show()
        self.toggleSidePanel(True)

    def showAllVitals(self):
        self.lblTable.hide()
        self.gridLayoutWidget.hide()
        self.lblHideVitals.hide()
        self.toggleSidePanel(False)
        self.toggleTable(False)

    def toggleSidePanel(self,show):

        if show:
            self.filterBtn.show()
            self.filterBtn1.show()
            self.graphBtn.show()
            self.graphBtn1.show()
            self.tableBtn.show()
            self.tableBtn1.show()
            self.helpBtn.show()
            self.helpBtn1.show()
        else:
            self.filterBtn.hide()
            self.filterBtn1.hide()
            self.graphBtn.hide()
            self.graphBtn1.hide()
            self.tableBtn.hide()
            self.tableBtn1.hide()
            self.helpBtn.hide()
            self.helpBtn1.hide()

    def toggleTable(self,show):

        if show:
            self.lblTable.show()
            self.cbSubVitalsB.show()
            self.cbSubVitals.show()
            self.btnPageBack.show()
            self.btnPageBack1.show()
            self.btnPageNext.show()
            self.btnPageNext1.show()
            self.lblPageNo.show()

            for i in range(28):
                self.lblBkgList[i].show()
                self.lblVitalDateList[i].show()
                self.lblVitalUnitList[i].show()
                self.lblVitalValueList[i].show()
        else:
            self.lblTable.hide()
            self.cbSubVitalsB.hide()
            self.cbSubVitals.hide()
            self.btnPageBack.hide()
            self.btnPageBack1.hide()
            self.btnPageNext.hide()
            self.btnPageNext1.hide()
            self.lblPageNo.hide()

            for i in range(28):
                self.lblBkgList[i].hide()
                self.lblVitalDateList[i].hide()
                self.lblVitalUnitList[i].hide()
                self.lblVitalValueList[i].hide()

    def AddReadingsClicked(self):

        if self.pageInit>0:
            vitalId = self.vitalList[self.pageInit-1]["main_vital_id"]

            self.x = addStats.AddMyStats(self,vitalId,self.vitalsCombo.currentText(), self.vitalDomData)
            self.x.show()

    def refreshData(self):
        self.tablePage = 1
        self.fetchSpecificVitalData()

if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = MyStats(0)

    window.show()

    # start the app
    sys.exit(App.exec_())