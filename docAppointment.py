import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QCustomQWidget (QWidget):

    def __init__(self, parent=None):
        super(QCustomQWidget, self).__init__(parent)

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 700)
        # self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\yellow.png'))
        self.label.setGeometry(0, 0, 1220, 700)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        textQVBoxLayout = QVBoxLayout()
        textUpQLabel = QLabel()
        textDownQLabel = QLabel()
        textQVBoxLayout.addWidget(textUpQLabel)
        textQVBoxLayout.addWidget(textDownQLabel)
        allQHBoxLayout = QHBoxLayout()
        iconQLabel = QLabel()
        allQHBoxLayout.addWidget(iconQLabel, 0)
        allQHBoxLayout.addLayout(textQVBoxLayout, 1)
        self.setLayout(allQHBoxLayout)

        textUpQLabel.setStyleSheet("background-color: white")
        textDownQLabel.setStyleSheet("background-color: white")

    def setTextUp (self, text):
        textUpQLabel = QLabel()
        textUpQLabel.setText(text)

    def setTextDown (self, text):
        textDownQLabel = QLabel()
        textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        # imagePath = "Resources\emorning.png"
        iconQLabel = QLabel()
        iconQLabel.setPixmap(QPixmap(imagePath))

class exampleQMainWindow (QMainWindow):
    def __init__ (self):
        super(exampleQMainWindow, self).__init__()
        self.setGeometry(0, 0, 1220, 700)

        # Create QListWidget
        self.myQListWidget = QListWidget(self)
        for index, name, icon in [
            ('No.1', 'Meyoko',  ''),
            ('No.2', 'Nyaruko', 'icon.png'),
            ('No.3', 'Louise',  'icon.png')]:
            # Create QCustomQWidget
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp(index)
            myQCustomQWidget.setTextDown(name)
            myQCustomQWidget.setIcon(icon)

            # Create QListWidgetItem
            myQListWidgetItem = QListWidgetItem(self.myQListWidget)
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
        self.setCentralWidget(self.myQListWidget)




App = QApplication(sys.argv)

# create the instance of our Window
window =exampleQMainWindow()

window.show()

# start the app
sys.exit(App.exec())


