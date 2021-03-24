import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import colors as Colors


class QCustomQWidget(QWidget):
    def __init__(self, parent=None):

        super(QCustomQWidget, self).__init__(parent)


        style = "background-color: #eee; border-radius : 15; margin-top : 10; margin-bottom : 30; margin-left : 10; margin-right : 10; "
        frame1 = QFrame(self)
        # frame1.setGraphicsEffect(shadow)
        frame1.setFixedWidth(1210)
        frame1.setFixedHeight(120)
        # frame1.setContentsMargins(10, 10, 10, 10)
        frame1.setStyleSheet(style)


        frame2 = QFrame(self)
        # frame1.setGraphicsEffect(shadow)
        frame2.setFixedWidth(1210)
        frame2.setFixedHeight(120)
        # frame2.setContentsMargins(10, 10, 10, 10)
        frame2.setStyleSheet(style)
        # frame1.setFrameStyle(QFrame.Raised)
        # frame1.setGeometry(567, 459, 200, 200)
        # frame1.setFrameStyle(QFrame.Panel |
        #                     QFrame.Plain)
        # frame1.setLayout(self.allQHBoxLayout)
        # frame1.setFrameShape(QFrame.StyledPanel)
        self.textQVBoxLayout = QVBoxLayout()
        self.textUpQLabel = QLabel()
        self.textUpQLabel.setFixedWidth(400)
        self.textDownQLabel = QLabel()
        self.textDownQLabel.setWordWrap(True)

        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout = QHBoxLayout()
        self.iconQLabel = QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)

        # setStyleSheet
        self.textUpQLabel.setStyleSheet("font: bold; color:" + Colors.DarkBlue)
        self.textDownQLabel.setStyleSheet("color:" + Colors.Grey8)

        self.lblAddress = QLabel()
        self.lblAddress.setStyleSheet("color:" + Colors.Grey8 +";overflow: hidden; text-overflow: ellipsis; display: -webkit-box; "
                                                               "-webkit-line-clamp: 2; -webkit-box-orient: vertical;")
        # self.lblAddress.setGeometry(589, 142, 276, 69)
        self.lblAddress.setWordWrap(True)
        # self.lblAddress.setMinimumHeight(99)
        self.lblAddress.setMinimumWidth(376)
        self.allQHBoxLayout.addWidget(self.lblAddress, 0)
        # self.allQHBoxLayout.setGeometry(QRect(589, 142, 276, 69))

        self.btnSelectTime = QPushButton("Select Time", self)
        self.allQHBoxLayout.addWidget(self.btnSelectTime, 1)

        self.btnNavigate = QPushButton("Navigate", self)
        self.allQHBoxLayout.addWidget(self.btnNavigate, 1)

        self.btnFavorite = QPushButton("Favorite", self)
        self.allQHBoxLayout.addWidget(self.btnFavorite, 1)
        self.allQHBoxLayout.setContentsMargins(5, 10, 30, 10)


        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(15)
        shadow1.setColor(Qt.lightGray)
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(15)
        shadow2.setColor(Qt.white)
        frame1.setGraphicsEffect(shadow1)
        frame2.setGraphicsEffect(shadow2)
        shadow2.setXOffset(-5)
        shadow2.setYOffset(-5)
        self.allQHBoxLayout.setParent(frame2)



    imagePath = "Resources\emorning.png"

    def setTextUp(self, text):
        self.textUpQLabel.setText(text)

    def setTextDown(self, text):
        self.textDownQLabel.setText(text)

    def setAddress(self, text):
        # imagePath = "Resources\emorning.png"
        self.lblAddress.setText(text)


class exampleQMainWindow(QMainWindow):
    def __init__(self):
        super(exampleQMainWindow, self).__init__()
        # Create QListWidget
        self.setGeometry(0, 0, 1220, 700)

        self.label2 = QLabel(self)
        self.label2.setPixmap(QPixmap('Resources\yellow.png'))
        self.label2.setGeometry(0, 0, 1220, 39)

        self.show()
        self.setStyleSheet("background-color: #F0F0F3")


        self.myQListWidget = QListWidget(self)
        self.myQListWidget.setGeometry(0, 41, 600, 1200)

        for index, name, Address in [
            ('Dr. Dhaval Naik', 'Cardiovascular, Thoraic Surgeon',
             'CIMS Hospital,Near Shukan Mall,Opp. Science CityRoad, Shukan Mall,'
             'Science City Road'),
            ('No.2', 'Nyaruko', 'icon.png'),
            ('No.3', 'Louise', 'icon.png')]:
            # Create QCustomQWidget
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp(index)
            myQCustomQWidget.setTextDown(name)
            myQCustomQWidget.setAddress(Address)
            # self.lblm.setGeometry(589, 142, 276, 69)
            # Create QListWidgetItem
            myQListWidgetItem = QListWidgetItem(self.myQListWidget)
            # Set size hint
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            # Add QListWidgetItem into QListWidget
            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)
            self.myQListWidget.clear()
        for index, name, Address in [
            ('Dr. Swappy', 'Cardiscular, Thoraic Surgeon',
             'CIMS Hospital,Near Shukan Mall,Opp. Science CityRoad, Shukan Mall,'
             'Science City Road'),
            ('No.2', 'Sansuko', 'icon.png'),
            ('No.2', 'Sansuko', 'icon.png'),
            ('No.2', 'Sansuko', 'icon.png'),
            ('No.2', 'Sansuko', 'icon.png'),
            ('No.2', 'Sansuko', 'icon.png'),
            ('No.3', 'Ljosdyse', 'icon.png')]:
            # Create QCustomQWidget
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setTextUp(index)
            myQCustomQWidget.setTextDown(name)
            myQCustomQWidget.setAddress(Address)
            # self.lblm.setGeometry(589, 142, 276, 69)
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
