from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Utility.MahiUtility as Util


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
        addReadingsBtn1 = QPushButton("Add readings", self)
        addReadingsBtn1.setStyleSheet("border-radius: 10;")
        addReadingsBtn1.setGeometry(800, 57, 260, 50)
        addReadingsBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        # addReadingsBtn1.clicked.connect(self.)

        filterBtn = QPushButton(self)
        filterBtn.setStyleSheet("border-radius: 10;")
        filterBtn.setGeometry(1082, 135, 110, 50)
        filterBtn.setGraphicsEffect(Util.getNeuShadow(0))
        filterBtn1 = QPushButton("FILTER", self)
        filterBtn1.setStyleSheet("border-radius: 10;")
        filterBtn1.setGeometry(1082, 135, 110, 50)
        filterBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        # filterBtn1.clicked.connect(self.)

        tableBtn = QPushButton(self)
        tableBtn.setStyleSheet("border-radius: 15;")
        tableBtn.setGeometry(1082, 213, 110, 130)
        tableBtn.setGraphicsEffect(Util.getNeuShadow(0))
        tableBtn1 = QPushButton("TABLE ", self)
        tableBtn1.setStyleSheet("border-radius: 15;")
        tableBtn1.setGeometry(1082, 213, 110, 130)
        tableBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        # tableBtn1.clicked.connect(self.)

        graphBtn = QPushButton(self)
        graphBtn.setStyleSheet("border-radius: 15;")
        graphBtn.setGeometry(1082, 371, 110, 130)
        graphBtn.setGraphicsEffect(Util.getNeuShadow(0))
        graphBtn1 = QPushButton("GRAPH ", self)
        graphBtn1.setStyleSheet("border-radius: 15;")
        graphBtn1.setGeometry(1082, 371, 110, 130)
        graphBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        # graphBtn1.clicked.connect(self.)

        helpBtn = QPushButton(self)
        helpBtn.setStyleSheet("border-radius: 15;")
        helpBtn.setGeometry(1082, 529, 110, 130)
        helpBtn.setGraphicsEffect(Util.getNeuShadow(0))
        helpBtn1 = QPushButton("HELP ", self)
        helpBtn1.setStyleSheet("border-radius: 15;")
        helpBtn1.setGeometry(1082, 529, 110, 130)
        helpBtn1.setGraphicsEffect(Util.getNeuShadow(1))
        # helpBtn1.clicked.connect(self.)

        self.vitalsCombo = QComboBox(self)
        self.vitalsCombo.setGeometry(142, 57, 192, 50)
        self.vitalsCombo.setStyleSheet("border-radius: 10; ")
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

        label11 = QLabel("Hello how are you??", self)
        label11.setGeometry(200, 300, 500, 100)
        label11.setFont((QFont("Arial", 18)))
        label11.setStyleSheet("color:red")

        label12 = QLabel("Hello how are you??", self)
        label12.setGeometry(200, 500, 500, 300)
        label12.setFont((QFont("Nunito", 18)))
        label12.setStyleSheet("color:red")

if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = MyStats()

    window.show()

    # start the app
    sys.exit(App.exec_())
