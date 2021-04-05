from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Custom.FileListItem as myFile

class FileList(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\yellow.png'))
        self.label.setGeometry(0, 0, 1220, 39)

        self.UiComponents()
        #
        #     # showing all the widgets
        # self.show()
    #
    def UiComponents(self):
        self.myQListWidget = QListWidget(self)
        self.myQListWidget.setGeometry(16, 125, 1191, 475)

        for i in range(5):
            myQCustomQWidget = myFile.FileListItem()
            myQCustomQWidget.setTextFileName('X-Ray')
            myQCustomQWidget.setTextDateDoctor('24/12/2021 Dr.Mobihealth')
            myQCustomQWidget.setExtension(".jpeg")
            myQListWidgetItem = QListWidgetItem(self.myQListWidget)
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())

            self.myQListWidget.addItem(myQListWidgetItem)
            self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)

if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = FileList()

    window.show()

    # start the app
    sys.exit(App.exec_())