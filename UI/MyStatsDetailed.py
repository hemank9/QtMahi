from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Utility.MahiUtility as Util
# importing packages
# import matplotlib.pyplot as plt
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg


class MyStatsDetailed(QMainWindow):

    def __init__(self, vital):
        super().__init__()
        # setting title
        self.setWindowTitle("Python ")
        # setting geometry
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        # self.label = QLabel(self)
        # self.label.setStyleSheet("background-color:#FEC32E")
        # self.label.setGeometry(0, 0, 1220, 39)

        self.vital = vital

        self.UiComponents()

        # showing all the widgets
        self.show()

    def UiComponents(self):
        # plt.plot([2, 8, 7, 4, 7, 6, 2, 5, 9], marker='D')
        # plt.show()



        #Graph View

        self.lblTable = QLabel(self)
        self.lblTable.setGeometry(21, 133, 1043, 530)
        self.lblTable.setStyleSheet("background-color: #FFFFFF")
        self.lblTable.hide()

        startx = 60
        starty = 210
        startw = 122
        starth =86
        rowcount = 1

        vitalsBtn = QComboBox(self)
        vitalsBtn.setStyleSheet("QComboBox {border-radius: 10; color: #00A0B5; }"
                                       "QComboBox::drop-down { background:rgb(255,255,255,0);padding-right:20px}")
        vitalsBtn.setGeometry(890, 145, 130, 40)
        vitalsBtn.setGraphicsEffect(Util.getNeuShadow(0))
        self.vitalsBtn1 = QComboBox(self)
        self.vitalsBtn1.setStyleSheet("QComboBox {border-radius: 10; color: #00A0B5;padding-left:15px;font-size:18px }"
                                       "QComboBox::drop-down { background:rgb(255,255,255,0);padding-right:20px}"
                                       "QComboBox::down-arrow{image: url(../Resources/dropDown.png)}")
        self.vitalsBtn1.setGeometry(890, 145, 130, 40)
        self.vitalsBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        self.vitalsBtn1.addItem("FPG")
        self.vitalsBtn1.addItem("OTGG")
        self.vitalsBtn1.addItem("RGT")
        # self.filterBtn1.addItem("Haemoglobin")
        # filterBtn1.clicked.connect(self.)

        btnPageBack = QPushButton(self)
        btnPageBack.setGeometry(459,595,50,50)
        btnPageBack.setStyleSheet("border-radius : 10; background-color: #F0F03")
        btnPageBack.setGraphicsEffect(Util.getNeuShadow(0))

        btnPageBack1 = QPushButton(self)
        btnPageBack1.setGeometry(459,595,50,50)
        btnPageBack1.setStyleSheet("border-radius : 10; background-color: #F0F03;font-size:20px;color:#777")
        btnPageBack1.setText("<")
        btnPageBack1.setIconSize(QtCore.QSize(115, 41))
        btnPageBack1.setGraphicsEffect(Util.getNeuShadow(1))
        # btnPageBack1.clicked.connect(self.PageBack)

        btnPageNext = QPushButton(self)
        btnPageNext.setGeometry(639,595,50,50)
        btnPageNext.setStyleSheet("border-radius : 10; background-color: #F0F03 ")
        btnPageNext.setGraphicsEffect(Util.getNeuShadow(0))

        btnPageNext1 = QPushButton(self)
        btnPageNext1.setGeometry(639,595,50,50)
        btnPageNext1.setStyleSheet("border-radius : 10; background-color: #F0F03;font-size:20px;color:#777 ")
        btnPageNext1.setText(">")
        btnPageNext1.setIconSize(QtCore.QSize(115, 41))
        btnPageNext1.setGraphicsEffect(Util.getNeuShadow(1))
        # btnPageNext1.clicked.connect(self.PageNext)

        self.lblPageNo = QLabel("", self)
        self.lblPageNo.setGeometry(551,608,50,31)
        self.lblPageNo.setStyleSheet("border-radius : 10; background-color: pink")
        self.lblPageNo.setAlignment(Qt.AlignCenter)

        for i in range(28):

            if(i>0):
                startx = startx+140

            if i>0 and (i)%7==0:
                startx = 60
                starty = starty+95
                # rowcount = rowcount+1

            lblBkg = QLabel(self)
            pixmap = QtGui.QPixmap('../Resources/graphBkg.png')
            scaledImage = pixmap.scaled(startw, starth)
            lblBkg.setPixmap(QPixmap(scaledImage))
            lblBkg.setGeometry(startx,starty,startw,starth)
            lblBkg.setStyleSheet("background-color:#00AAAAAA")

            lblDate = QLabel(self)
            lblDate.setGeometry(startx+16,starty+9,89,29)
            lblDate.setText("20/03/21")
            lblDate.setAlignment(Qt.AlignCenter)
            lblDate.setStyleSheet("color:#727376; font-size:18px; background-color:#00FFFFFF")

            lblValue = QLabel(self)
            lblValue.setGeometry(startx+16,starty+39,89,29)
            lblValue.setText("16.8")
            lblValue.setAlignment(Qt.AlignCenter)
            lblValue.setStyleSheet("color:white; font-size:22px; background-color:#00FFFFFF")

            lblUnit = QLabel(self)
            lblUnit.setGeometry(startx+16,starty+59,89,29)
            lblUnit.setText("mmol/mol")
            lblUnit.setAlignment(Qt.AlignCenter)
            lblUnit.setStyleSheet("color:white; font-size:15px; background-color:#00FFFFFF")


        # self.btnClose = QPushButton(self)
        # self.btnClose.setGeometry(30, 143, 45, 45)
        # self.btnClose.setStyleSheet("background-color: #F0F0F3; border-radius:5")
        # self.btnClose.setGraphicsEffect(Util.getNeuShadow(0))
        # self.btnClose.hide()
        # self.btnClose1 = QPushButton(self)
        # self.btnClose1.setGeometry(30, 143, 45, 45)
        # self.btnClose1.setStyleSheet("background-color: #F0F0F3; border-radius:5")
        # self.btnClose1.setGraphicsEffect(Util.getNeuShadow(1))
        # self.btnClose1.setIcon(QtGui.QIcon('..\Resources\\close.png'))
        # self.btnClose1.setIconSize(QtCore.QSize(45, 45))
        # self.btnClose1.clicked.connect(self.GraphViewClicked)
        # self.btnClose1.hide()

        syncBtn = QPushButton(self)
        syncBtn.setGeometry(133, 63, 45, 45)
        syncBtn.setStyleSheet("border-radius: 8; background-color: #F0F0F3")
        syncBtn.setIcon(QtGui.QIcon('..\Resources\\syncBtn.png'))
        syncBtn.setIconSize(QtCore.QSize(112, 52))
        syncBtn.setGraphicsEffect(Util.getNeuShadow(0))
        syncBtn.clicked.connect(self.close)


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

        filterBtn = QComboBox(self)
        filterBtn.setStyleSheet("QComboBox {border-radius: 10; color: #00A0B5 }"
                                       "QComboBox::drop-down { background:rgb(255,255,255,0);padding-right:20px}")
        filterBtn.setGeometry(1082, 135, 110, 50)
        filterBtn.setGraphicsEffect(Util.getNeuShadow(0))
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

        tableBtn = QPushButton(self)
        tableBtn.setStyleSheet("border-radius: 15;")
        tableBtn.setGeometry(1082, 213, 110, 130)
        tableBtn.setGraphicsEffect(Util.getNeuShadow(0))
        tableBtn1 = QPushButton(self)
        tableBtn1.setStyleSheet("border-radius: 15;")
        tableBtn1.setGeometry(1082, 213, 110, 130)
        tableBtn1.setIcon(QtGui.QIcon('..\Resources\\table.png'))
        tableBtn1.setIconSize(QtCore.QSize(110, 130))
        tableBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        tableBtn1.clicked.connect(self.tableClick)

        graphBtn = QPushButton(self)
        graphBtn.setStyleSheet("border-radius: 15;")
        graphBtn.setGeometry(1082, 371, 110, 130)
        graphBtn.setGraphicsEffect(Util.getNeuShadow(0))
        graphBtn1 = QPushButton(self)
        graphBtn1.setStyleSheet("border-radius: 15;")
        graphBtn1.setGeometry(1082, 371, 110, 130)
        graphBtn1.setIcon(QtGui.QIcon('..\Resources\\graph.png'))
        graphBtn1.setIconSize(QtCore.QSize(110, 130))
        graphBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        graphBtn1.clicked.connect(self.GraphViewClicked)

        helpBtn = QPushButton(self)
        helpBtn.setStyleSheet("border-radius: 15;")
        helpBtn.setGeometry(1082, 529, 110, 130)
        helpBtn.setGraphicsEffect(Util.getNeuShadow(0))
        helpBtn1 = QPushButton(self)
        helpBtn1.setStyleSheet("border-radius: 15;")
        helpBtn1.setGeometry(1082, 529, 110, 130)
        helpBtn1.setIcon(QtGui.QIcon('..\Resources\\helpStats.png'))
        helpBtn1.setIconSize(QtCore.QSize(110, 130))
        helpBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        helpBtn1.clicked.connect(self.helpClick)

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
        self.vitalsCombo.addItem("HBA1C")
        self.vitalsCombo.addItem("Blood Pressure")
        self.vitalsCombo.addItem("Heart Rate")
        self.vitalsCombo.addItem("Haemoglobin")
        self.vitalsCombo.addItem("BMI")
        self.vitalsCombo.addItem("Sugar")
        self.vitalsCombo.addItem("Cholesterol")
        self.vitalsCombo.addItem("Pt/INR")
        self.vitalsCombo.addItem("Temperature")
        self.vitalsCombo.currentIndexChanged.connect(self.vitalChanged)

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

        self.graph = PlotWidget()
        # self.setCentralWidget(self.graph)
        hour1 = ["20/03/21","08/09/20","05/11/20","28/10/20","01/07/20","08/03/21","18/01/21","16/03/21","11/03/21","19/04/21"]
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
        # self.graphWidget.showGrid(x=True, y=True)


    def tableClick(self):
        # self.lblTable = QLabel(self)
        # self.lblTable.setGeometry(21, 133, 1043, 523)
        # self.lblTable.setStyleSheet("background-color: #FFFFFF")
        self.lblTable.show()
        self.gridLayoutWidget.hide()
        print("pressed")

    def helpClick(self):
        # qlabel = QLabel(self)
        # qlabel.setGeometry(50, 100, 50, 50)
        print("pressed")

    def GraphViewClicked(self):
        self.lblTable.hide()
        self.gridLayoutWidget.show()

    def vitalChanged(self,i):
        print(i)




if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = MyStatsDetailed("")

    window.show()

    # start the app
    sys.exit(App.exec_())
