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


class MyStats(QMainWindow):

    def __init__(self, parent=None):
        super().__init__()
        # setting title
        self.setWindowTitle("Python ")
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
        # plt.plot([2, 8, 7, 4, 7, 6, 2, 5, 9], marker='D')
        # plt.show()

        # self.graph = pg.PlotWidget()
        # self.setCentralWidget(self.graph)
        # hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        # temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]
        #
        # self.graph.setBackground('w')
        # self.graph.plot(hour, temperature)

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
        addReadingsBtn1 = QPushButton( self)
        addReadingsBtn1.setStyleSheet("border-radius: 10;")
        addReadingsBtn1.setGeometry(800, 57, 260, 50)
        addReadingsBtn1.setIcon(QtGui.QIcon('..\Resources\\addReadings.png'))
        addReadingsBtn1.setIconSize(QtCore.QSize(260, 50))
        addReadingsBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        # addReadingsBtn1.clicked.connect(self.)

        filterBtn =  QComboBox(self)
        filterBtn.setStyleSheet("border-radius: 10;")
        filterBtn.setGeometry(1082, 135, 110, 50)
        filterBtn.setGraphicsEffect(Util.getNeuShadow(0))
        self.filterBtn1 = QComboBox(self)
        self.filterBtn1.setStyleSheet("border-radius: 10; color: #00A0B5")
        self.filterBtn1.setGeometry(1082, 135, 110, 50)
        self.filterBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        self.filterBtn1.addItem("Weekly")
        self.filterBtn1.addItem("Monthly")
        self.filterBtn1.addItem("Yearly")
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
        # graphBtn1.clicked.connect(self.)

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


        label11 = QLabel("Hello how are you??", self)
        label11.setGeometry(200, 300, 500, 100)
        label11.setFont((QFont("Arial", 18)))
        label11.setStyleSheet("color:red")

        label12 = QLabel("Hello how are you??", self)
        label12.setGeometry(200, 500, 500, 300)
        label12.setFont((QFont("Nunito", 18)))
        label12.setStyleSheet("color:red")

    def tableClick(self):
        self.lblTable = QLabel(self)
        self.lblTable.setGeometry(21, 133, 1043, 523)
        self.lblTable.setStyleSheet("background-color: #FFFFFF")

        btnClose = QPushButton(self)
        btnClose.setGeometry(30, 143, 45, 45)
        btnClose.setStyleSheet("background-color: #F0F0F3; border-radius:5")
        btnClose.setGraphicsEffect(Util.getNeuShadow(0))
        btnClose1 = QPushButton(self)
        btnClose1.setGeometry(30, 143, 45, 45)
        btnClose1.setStyleSheet("background-color: #F0F0F3; border-radius:5")
        btnClose1.setGraphicsEffect(Util.getNeuShadow(1))
        btnClose1.setIcon(QtGui.QIcon('..\Resources\\close.png'))
        btnClose1.setIconSize(QtCore.QSize(45, 45))
        btnClose1.clicked.connect(self.close)

    def helpClick(self):

        # qlabel = QLabel(self)
        # qlabel.setGeometry(50, 100, 50, 50)
        print("pressed")


if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = MyStats()

    window.show()

    # start the app
    sys.exit(App.exec_())
