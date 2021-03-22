import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import colors as Colors
class QCustomQWidget (QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQVBoxLayout = QVBoxLayout()
        self.textUpQLabel = QLabel()
        self.textDownQLabel = QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout = QHBoxLayout()
        self.iconQLabel = QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet("font: bold; color:"+Colors.DarkBlue)
        self.textDownQLabel.setStyleSheet("color:"+Colors.Grey8)

        self.lblAddress = QLabel()
        self.lblAddress.setStyleSheet("color:"+Colors.Grey8)
        self.allQHBoxLayout.addWidget(self.lblAddress,2)

        self.btnSelectTime = QPushButton("Select Time", self)
        self.allQHBoxLayout.addWidget(self.btnSelectTime,3)

        self.btnNavigate = QPushButton("Navigate", self)
        self.allQHBoxLayout.addWidget(self.btnNavigate,4)

        self.btnFavorite = QPushButton("Favorite", self)
        self.allQHBoxLayout.addWidget(self.btnFavorite,5)


    imagePath = "Resources\emorning.png"
    def setTextUp (self, text):
        self.textUpQLabel.setText(text)
    def setTextDown (self, text):
        self.textDownQLabel.setText(text)
    def setAddress (self, text):
        # imagePath = "Resources\emorning.png"
        self.lblAddress.setText(text)
class exampleQMainWindow (QMainWindow):
    def __init__ (self):
        super(exampleQMainWindow, self).__init__()
        # Create QListWidget
        self.setGeometry(0, 0, 1220, 700)

        self.myQListWidget = QListWidget(self)
        for index, name, Address in [
            ('Dr. Dhaval Naik', 'Cardiovascular, Thoraic Surgeon',  'CIMS Hospital,Near Shukan Mall,Opp. Science CityRoad,Shukan Mall,'
                                                                    'Science City Road, Ahmedabad'),
            ('No.2', 'Nyaruko', 'icon.png'),
            ('No.3', 'Louise',  'icon.png')]:
            # Create QCustomQWidget
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp(index)
            myQCustomQWidget.setTextDown(name)
            myQCustomQWidget.setAddress(Address)
            # Create QListWidgetItem
            myQListWidgetItem = QListWidgetItem(self.myQListWidget)
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
        self.setCentralWidget(self.myQListWidget)
app = QApplication([])
window = exampleQMainWindow()
window.show()
sys.exit(app.exec_())