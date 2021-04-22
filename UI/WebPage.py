from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWebEngineCore
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

class WebPage(QWidget):
    def __init__(self,link):
        super().__init__()
        self.setWindowTitle("Humm")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.link = link
        #
        #
        # self.label = QLabel(self)
        # self.label.setPixmap(QPixmap('../Resources/yellow.png'))
        # self.label.setGeometry(0, 0, 1220, 39)
        #
        # btn_back = QPushButton("", self)
        # btn_back.setGeometry(15, 40, 135, 50)
        # btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        # btn_back.setIcon(QtGui.QIcon('..\Resources\Group 27.png'))
        # btn_back.setIconSize(QtCore.QSize(155, 71))
        # btn_back.clicked.connect(self.close)

        vbox = QVBoxLayout(self)
        self.webview= QtWebEngineWidgets.QWebEngineView()
        self.webview.load(QUrl(self.link))

        vbox.addWidget(self.webview)
        self.setLayout(vbox)
        # self.webview.show()


# if __name__ == '__main__':
#     App = QApplication(sys.argv)
#
#     # create the instance of our Window
#     link = "https://www.medicalnewstoday.com/articles/can-a-common-food-preservative-harm-the-immune-system"
#     window = WebPage(link)
#
#     window.show()
#
#     # start the app
#     sys.exit(App.exec())