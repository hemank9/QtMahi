import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class uiControlTest(QMainWindow):
    def __init__(self):
        super(uiControlTest, self).__init__()
        # self.ui = uic.loadUi('uiControlTest.ui')
        self.show()

        for i in range(0,300):
            wid = animItemWidget()
            wid.label_2.setText('Last edited by chrise @2014.06.21:23:17')
            wid.label.setText('Animation ' + str(i) + '       ')

            wid2 = QListWidgetItem()
            wid2.setSizeHint(QtCore.QSize(100, 40))
            self.ui.list.addItem(wid2)
            self.ui.list.setItemWidget(wid2, wid)

        def awesomeButtonPressed():
            print ('awesome!')

class animItemWidget(QWidget):

    def __init__(self, parent=None):
        super(animItemWidget, self).__init__()
        self.horizontalLayout_4 = QHBoxLayout(self)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setMargin(3)
        self.horizontalLayout_4.setObjectName(QtCore.QString.fromUtf8("horizontalLayout_4"))
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(QtCore.QString.fromUtf8("verticalLayout_2"))
        self.label = QLabel(self)
        font = QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName(QtCore.QString.fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.pixMap02 = QLabel(self)
        self.pixMap02.setText(QtCore.QString.fromUtf8(""))
        self.pixMap02.setObjectName(QtCore.QString.fromUtf8("pixMap02"))
        self.verticalLayout_2.addWidget(self.pixMap02)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(QtCore.QString.fromUtf8("verticalLayout"))
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(QtCore.QString.fromUtf8("horizontalLayout"))
        self.pixMap01 = QLabel(self)
        self.pixMap01.setText(QtCore.QString.fromUtf8(""))
        self.pixMap01.setObjectName(QtCore.QString.fromUtf8("pixMap01"))
        self.horizontalLayout.addWidget(self.pixMap01)
        spacerItem = QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.button02 = QPushButton(self)
        self.button02.setMaximumSize(QtCore.QSize(24, 24))
        self.button02.setText(QtCore.QString.fromUtf8(""))
        self.button02.setObjectName(QtCore.QString.fromUtf8("button02"))
        self.horizontalLayout.addWidget(self.button02)
        self.button01 = QPushButton(self)
        self.button01.setMaximumSize(QtCore.QSize(24, 24))
        self.button01.setText(QtCore.QString.fromUtf8(""))
        self.button01.setObjectName(QtCore.QString.fromUtf8("button01"))
        self.horizontalLayout.addWidget(self.button01)
        self.button04 = QPushButton(self)
        self.button04.setMaximumSize(QtCore.QSize(24, 24))
        self.button04.setText(QtCore.QString.fromUtf8(""))
        self.button04.setObjectName(QtCore.QString.fromUtf8("button04"))
        self.horizontalLayout.addWidget(self.button04)
        self.button03 = QPushButton(self)
        self.button03.setMaximumSize(QtCore.QSize(24, 24))
        self.button03.setText(QtCore.QString.fromUtf8(""))
        self.button03.setObjectName(QtCore.QString.fromUtf8("button03"))
        self.horizontalLayout.addWidget(self.button03)
        self.button05 = QPushButton(self)
        self.button05.setMaximumSize(QtCore.QSize(24, 24))
        self.button05.setText(QtCore.QString.fromUtf8(""))
        self.button05.setObjectName(QtCore.QString.fromUtf8("button05"))
        self.horizontalLayout.addWidget(self.button05)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(QtCore.QString.fromUtf8("horizontalLayout_3"))
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(QtCore.QString.fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.connect(self.button02, QtCore.SIGNAL("clicked()"), self.awesome)

    def awesome(self):
        print  (self.label.text() + ' is awesome!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = uiControlTest()
    sys.exit(app.exec_())