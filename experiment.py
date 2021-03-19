import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python ")
        self.setGeometry(0, 0, 1220, 700)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):
        listWidget = QListWidget(self)

        item_1 = QListWidgetItem("Item 1");
        # Resize width and height
        listWidget.resize(300, 120)
        listWidget.addItem(item_1);
        listWidget.addItem("Item 2");
        listWidget.addItem("Item 3");
        listWidget.addItem("Item 4");

        listWidget.setWindowTitle('PyQT QListwidget Demo')
        listWidget.show()

if __name__ == '__main__':

    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Window()

    window.show()

    # start the app
    sys.exit(App.exec())