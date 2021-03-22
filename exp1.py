import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import colors as Colors


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    def initUI(self):
        frame = QFrame()
        frame.setFrameStyle(QFrame.Panel |
                QFrame.Plain)
        label = QLabel('This is random text')
        dockWidget = QDockWidget('Main', self)
        # set the widget to non-movable, non-floatable and non-closable
        dockWidget.setFeatures(dockWidget.NoDockWidgetFeatures)
        dockWidget.setWidget(label)
        # add the QDockWidget to the QLayout
        hbox = QHBoxLayout()
        hbox.addWidget(dockWidget)
        # set the layout of the QFrame
        frame.setLayout(hbox)
        # create another QLayout to add QFrame
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(frame)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Test')
def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()