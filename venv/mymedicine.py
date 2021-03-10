from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 700)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('Resources\Group 45.png'))
        self.label.setGeometry(0, 0, 1220, 195)


        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        # three buttons on the my medicine page
        # prescriptions
        btn_pre = QPushButton("", self)
        btn_pre.setGeometry(39, 48, 215, 67)
        btn_pre.setStyleSheet("border-radius : 30; background-color : #F0F0F3; text-align:top ; text-align:left; focus:pressed")
        btn_pre.setIcon(QtGui.QIcon('Resources\prescriptions.png'))
        btn_pre.setIconSize(QtCore.QSize(215, 67))
        # btn_pre.clicked.connect(self.clickme)

        # medicine time
        btn_mt = QPushButton("", self)
        btn_mt.setGeometry(269, 48, 215, 67)
        btn_mt.setStyleSheet("border-radius : 30; background-color : #F0F0F3; text-align:top ; text-align:left; focus:mtssed")
        btn_mt.setIcon(QtGui.QIcon('Resources\medicinetime.png'))
        btn_mt.setIconSize(QtCore.QSize(215, 67))
        # btn_mt.clicked.connect(self.clickme)

        # analytics
        btn_analytics = QPushButton("", self)
        btn_analytics.setGeometry(498, 48, 215, 67)
        btn_analytics.setStyleSheet("border-radius : 30; background-color : #F0F0F3; text-align:top ; text-align:left; focus:analyticsssed")
        btn_analytics.setIcon(QtGui.QIcon('Resources\manalytics.png'))
        btn_analytics.setIconSize(QtCore.QSize(215, 67))
        # btn_analytics.clicked.connect(self.clickme)

        btn_return = QPushButton("", self)
        btn_return.setGeometry(40, 130, 173, 61)
        btn_return.setStyleSheet("border-radius : 10; background-color : #F0F0F3")
        btn_return.setIcon(QtGui.QIcon('Resources\Group 34.png'))
        btn_return.setIconSize(QtCore.QSize(195, 101))
        btn_return.clicked.connect(self.close)

        btn_cylinder = QPushButton("", self)
        btn_cylinder.setGeometry(269, 130, 216, 83)
        btn_cylinder.setStyleSheet("border-radius : 10; background-color : #F0F0F3")
        btn_cylinder.setIcon(QtGui.QIcon('Resources\cylinder.png'))
        btn_cylinder.setIconSize(QtCore.QSize( 216, 83))
        # btn_cylinder.clicked.connect(self.close)

        # lbl_pic1 = QLabel(self)
        # lbl_pic1.setPixmap(QPixmap('Resources\mahi_ui_popart-01 2.png'))
        # lbl_pic1.setGeometry(797, 20, 271, 161)
        #
        # lbl_pic2 = QLabel(self)
        # lbl_pic2.setPixmap(QPixmap('Resources\pic2.png'))
        # lbl_pic2.setGeometry(1016, 94, 143, 101)

        lbl_txt1 = QLabel("* click on the buttons to see the medicine details",self)
        lbl_txt1.setGeometry(43, 197, 471, 29)

        lbl_txt = QLabel("97", self)
        lbl_txt.setGeometry(840, 60, 130, 80)
        lbl_txt.setFont(QFont('Arial', 40))
        lbl_txt.setAlignment(QtCore.Qt.AlignRight)
        lbl_txt.setStyleSheet("background-color : #fff9ea; color : #FEC32E; font-weight: bold")

        # creating a label widget
        # by default label will display at top left corner
        # lbl_txt1 = QLabel('Times font', self)
        # lbl_txt1.setFont(QFont('Times font', 100))
        # lbl_txt1.setGeometry(960, 100, 471, 29)



        # making of 96 buttons
        # w = QWidget(self)
        # grid = QGridLayout(w)
        #
        # for i in range(3):
        #     for j in range(3):
        #         grid.addWidget(QPushButton("Button", self), i, j)
        #

        # # w.show()

        btn1 = QPushButton("", self)
        btn1.setGeometry(39, 250, 86, 40)
        btn1.setStyleSheet("border-radius : 10; background-color : #006CB5")
        btn1.clicked.connect(self.clickme)

        btn2 = QPushButton("", self)
        btn2.setGeometry(39, 300, 86, 40)
        btn2.setStyleSheet("border-radius : 10; background-color : #006CB5")
        btn2.clicked.connect(self.clickme)

        btn3 = QPushButton("", self)
        btn3.setGeometry(39, 350, 86, 40)
        btn3.setStyleSheet("border-radius : 10; background-color : #006CB5")
        btn3.clicked.connect(self.clickme)

        btn4 = QPushButton("", self)
        btn4.setGeometry(39, 400, 86, 40)
        btn4.setStyleSheet("border-radius : 10; background-color : #006CB5")
        btn4.clicked.connect(self.clickme)

        btn5 = QPushButton("", self)
        btn5.setGeometry(39, 450, 86, 40)
        btn5.setStyleSheet("border-radius : 10; background-color : #006CB5")
        btn5.clicked.connect(self.clickme)

        btn6 = QPushButton("", self)
        btn6.setGeometry(39, 500, 86, 40)
        btn6.setStyleSheet("border-radius : 10; background-color : #006CB5")
        btn6.clicked.connect(self.clickme)

        btn7 = QPushButton("", self)
        btn7.setGeometry(39, 550, 86, 40)
        btn7.setStyleSheet("border-radius : 10; background-color : #006CB5")
        btn7.clicked.connect(self.clickme)

        btn8 = QPushButton("", self)
        btn8.setGeometry(39, 600, 86, 40)
        btn8.setStyleSheet("border-radius : 10; background-color : #006CB5")
        btn8.clicked.connect(self.clickme)

        btn9 = QPushButton("", self)
        btn9.setGeometry(39, 650, 86, 40)
        btn9.setStyleSheet("border-radius : 10; background-color : #006CB5")
        btn9.clicked.connect(self.clickme)

        btn11 = QPushButton("", self)
        btn11.setGeometry(133, 250, 86, 40)
        btn11.setStyleSheet("border-radius : 10; background-color : #004D80")
        btn11.clicked.connect(self.clickme)

        btn21 = QPushButton("", self)
        btn21.setGeometry(133, 300, 86, 40)
        btn21.setStyleSheet("border-radius : 10; background-color : #004D80")
        btn21.clicked.connect(self.clickme)

        btn31 = QPushButton("", self)
        btn31.setGeometry(133, 350, 86, 40)
        btn31.setStyleSheet("border-radius : 10; background-color : #004D80")
        btn31.clicked.connect(self.clickme)

        btn41 = QPushButton("", self)
        btn41.setGeometry(133, 400, 86, 40)
        btn41.setStyleSheet("border-radius : 10; background-color : #004D80")
        btn41.clicked.connect(self.clickme)

        btn51 = QPushButton("", self)
        btn51.setGeometry(133, 450, 86, 40)
        btn51.setStyleSheet("border-radius : 10; background-color : #004D80")
        btn51.clicked.connect(self.clickme)

        btn61 = QPushButton("", self)
        btn61.setGeometry(133, 500, 86, 40)
        btn61.setStyleSheet("border-radius : 10; background-color : #004D80")
        btn61.clicked.connect(self.clickme)

        btn71 = QPushButton("", self)
        btn71.setGeometry(133, 550, 86, 40)
        btn71.setStyleSheet("border-radius : 10; background-color : #004D80")
        btn71.clicked.connect(self.clickme)

        btn81 = QPushButton("", self)
        btn81.setGeometry(133, 600, 86, 40)
        btn81.setStyleSheet("border-radius : 10; background-color : #004D80")
        btn81.clicked.connect(self.clickme)

        btn91 = QPushButton("", self)
        btn91.setGeometry(133, 650, 86, 40)
        btn91.setStyleSheet("border-radius : 10; background-color : #004D80")
        btn91.clicked.connect(self.clickme)

        btn12 = QPushButton("", self)
        btn12.setGeometry(227, 250, 86, 40)
        btn12.setStyleSheet("border-radius : 10; background-color : #274E6F")
        btn12.clicked.connect(self.clickme)

        btn22 = QPushButton("", self)
        btn22.setGeometry(227, 300, 86, 40)
        btn22.setStyleSheet("border-radius : 10; background-color : #274E6F")
        btn22.clicked.connect(self.clickme)

        btn32 = QPushButton("", self)
        btn32.setGeometry(227, 350, 86, 40)
        btn32.setStyleSheet("border-radius : 10; background-color : #274E6F")
        btn32.clicked.connect(self.clickme)

        btn42 = QPushButton("", self)
        btn42.setGeometry(227, 400, 86, 40)
        btn42.setStyleSheet("border-radius : 10; background-color : #274E6F")
        btn42.clicked.connect(self.clickme)

        btn52 = QPushButton("", self)
        btn52.setGeometry(227, 450, 86, 40)
        btn52.setStyleSheet("border-radius : 10; background-color : #274E6F")
        btn52.clicked.connect(self.clickme)

        btn62 = QPushButton("", self)
        btn62.setGeometry(227, 500, 86, 40)
        btn62.setStyleSheet("border-radius : 10; background-color : #274E6F")
        btn62.clicked.connect(self.clickme)

        btn72 = QPushButton("", self)
        btn72.setGeometry(227, 550, 86, 40)
        btn72.setStyleSheet("border-radius : 10; background-color : #274E6F")
        btn72.clicked.connect(self.clickme)

        btn82 = QPushButton("", self)
        btn82.setGeometry(227, 600, 86, 40)
        btn82.setStyleSheet("border-radius : 10; background-color : #274E6F")
        btn82.clicked.connect(self.clickme)

        btn92 = QPushButton("", self)
        btn92.setGeometry(227, 650, 86, 40)
        btn92.setStyleSheet("border-radius : 10; background-color : #274E6F")
        btn92.clicked.connect(self.clickme)

        btn13 = QPushButton("", self)
        btn13.setGeometry(321, 250, 86, 40)
        btn13.setStyleSheet("border-radius : 10; background-color : #274257")
        btn13.clicked.connect(self.clickme)

        btn23 = QPushButton("", self)
        btn23.setGeometry(321, 300, 86, 40)
        btn23.setStyleSheet("border-radius : 10; background-color : #274257")
        btn23.clicked.connect(self.clickme)

        btn33 = QPushButton("", self)
        btn33.setGeometry(321, 350, 86, 40)
        btn33.setStyleSheet("border-radius : 10; background-color : #274257")
        btn33.clicked.connect(self.clickme)

        btn43 = QPushButton("", self)
        btn43.setGeometry(321, 400, 86, 40)
        btn43.setStyleSheet("border-radius : 10; background-color : #274257")
        btn43.clicked.connect(self.clickme)

        btn53 = QPushButton("", self)
        btn53.setGeometry(321, 450, 86, 40)
        btn53.setStyleSheet("border-radius : 10; background-color : #274257")
        btn53.clicked.connect(self.clickme)

        btn63 = QPushButton("", self)
        btn63.setGeometry(321, 500, 86, 40)
        btn63.setStyleSheet("border-radius : 10; background-color : #274257")
        btn63.clicked.connect(self.clickme)

        btn73 = QPushButton("", self)
        btn73.setGeometry(321, 550, 86, 40)
        btn73.setStyleSheet("border-radius : 10; background-color : #274257")
        btn73.clicked.connect(self.clickme)

        btn83 = QPushButton("", self)
        btn83.setGeometry(321, 600, 86, 40)
        btn83.setStyleSheet("border-radius : 10; background-color : #274257")
        btn83.clicked.connect(self.clickme)

        btn93 = QPushButton("", self)
        btn93.setGeometry(321, 650, 86, 40)
        btn93.setStyleSheet("border-radius : 10; background-color : #274257")
        btn93.clicked.connect(self.clickme)

        btn14 = QPushButton("", self)
        btn14.setGeometry(415, 250, 86, 40)
        btn14.setStyleSheet("border-radius : 10; background-color : #ED478D")
        btn14.clicked.connect(self.clickme)

        btn24 = QPushButton("", self)
        btn24.setGeometry(415, 300, 86, 40)
        btn24.setStyleSheet("border-radius : 10; background-color : #ED478D")
        btn24.clicked.connect(self.clickme)

        btn34 = QPushButton("", self)
        btn34.setGeometry(415, 350, 86, 40)
        btn34.setStyleSheet("border-radius : 10; background-color : #ED478D")
        btn34.clicked.connect(self.clickme)

        btn44 = QPushButton("", self)
        btn44.setGeometry(415, 400, 86, 40)
        btn44.setStyleSheet("border-radius : 10; background-color : #ED478D")
        btn44.clicked.connect(self.clickme)

        btn54 = QPushButton("", self)
        btn54.setGeometry(415, 450, 86, 40)
        btn54.setStyleSheet("border-radius : 10; background-color : #ED478D")
        btn54.clicked.connect(self.clickme)

        btn64 = QPushButton("", self)
        btn64.setGeometry(415, 500, 86, 40)
        btn64.setStyleSheet("border-radius : 10; background-color : #ED478D")
        btn64.clicked.connect(self.clickme)

        btn74 = QPushButton("", self)
        btn74.setGeometry(415, 550, 86, 40)
        btn74.setStyleSheet("border-radius : 10; background-color : #ED478D")
        btn74.clicked.connect(self.clickme)

        btn84 = QPushButton("", self)
        btn84.setGeometry(415, 600, 86, 40)
        btn84.setStyleSheet("border-radius : 10; background-color : #ED478D")
        btn84.clicked.connect(self.clickme)

        btn94 = QPushButton("", self)
        btn94.setGeometry(415, 650, 86, 40)
        btn94.setStyleSheet("border-radius : 10; background-color : #ED478D")
        btn94.clicked.connect(self.clickme)

        btn15 = QPushButton("", self)
        btn15.setGeometry(509, 250, 86, 40)
        btn15.setStyleSheet("border-radius : 10; background-color : #B86C87")
        btn15.clicked.connect(self.clickme)

        btn25 = QPushButton("", self)
        btn25.setGeometry(509, 300, 86, 40)
        btn25.setStyleSheet("border-radius : 10; background-color : #B86C87")
        btn25.clicked.connect(self.clickme)

        btn35 = QPushButton("", self)
        btn35.setGeometry(509, 350, 86, 40)
        btn35.setStyleSheet("border-radius : 10; background-color : #B86C87")
        btn35.clicked.connect(self.clickme)

        btn45 = QPushButton("", self)
        btn45.setGeometry(509, 400, 86, 40)
        btn45.setStyleSheet("border-radius : 10; background-color : #B86C87")
        btn45.clicked.connect(self.clickme)

        btn55 = QPushButton("", self)
        btn55.setGeometry(509, 450, 86, 40)
        btn55.setStyleSheet("border-radius : 10; background-color : #B86C87")
        btn55.clicked.connect(self.clickme)

        btn65 = QPushButton("", self)
        btn65.setGeometry(509, 500, 86, 40)
        btn65.setStyleSheet("border-radius : 10; background-color : #B86C87")
        btn65.clicked.connect(self.clickme)

        btn75 = QPushButton("", self)
        btn75.setGeometry(509, 550, 86, 40)
        btn75.setStyleSheet("border-radius : 10; background-color : #B86C87")
        btn75.clicked.connect(self.clickme)

        btn85 = QPushButton("", self)
        btn85.setGeometry(509, 600, 86, 40)
        btn85.setStyleSheet("border-radius : 10; background-color : #B86C87")
        btn85.clicked.connect(self.clickme)

        btn95 = QPushButton("", self)
        btn95.setGeometry(509, 650, 86, 40)
        btn95.setStyleSheet("border-radius : 10; background-color : #B86C87")
        btn95.clicked.connect(self.clickme)

        btn16 = QPushButton("", self)
        btn16.setGeometry(603, 250, 86, 40)
        btn16.setStyleSheet("border-radius : 10; background-color : #7A2548")
        btn16.clicked.connect(self.clickme)

        btn26 = QPushButton("", self)
        btn26.setGeometry(603, 300, 86, 40)
        btn26.setStyleSheet("border-radius : 10; background-color : #7A2548")
        btn26.clicked.connect(self.clickme)

        btn36 = QPushButton("", self)
        btn36.setGeometry(603, 350, 86, 40)
        btn36.setStyleSheet("border-radius : 10; background-color : #7A2548")
        btn36.clicked.connect(self.clickme)

        btn46 = QPushButton("", self)
        btn46.setGeometry(603, 400, 86, 40)
        btn46.setStyleSheet("border-radius : 10; background-color : #7A2548")
        btn46.clicked.connect(self.clickme)

        btn56 = QPushButton("", self)
        btn56.setGeometry(603, 450, 86, 40)
        btn56.setStyleSheet("border-radius : 10; background-color : #7A2548")
        btn56.clicked.connect(self.clickme)

        btn66 = QPushButton("", self)
        btn66.setGeometry(603, 500, 86, 40)
        btn66.setStyleSheet("border-radius : 10; background-color : #7A2548")
        btn66.clicked.connect(self.clickme)

        btn76 = QPushButton("", self)
        btn76.setGeometry(603, 550, 86, 40)
        btn76.setStyleSheet("border-radius : 10; background-color : #7A2548")
        btn76.clicked.connect(self.clickme)

        btn86 = QPushButton("", self)
        btn86.setGeometry(603, 600, 86, 40)
        btn86.setStyleSheet("border-radius : 10; background-color : #7A2548")
        btn86.clicked.connect(self.clickme)

        btn96 = QPushButton("", self)
        btn96.setGeometry(603, 650, 86, 40)
        btn96.setStyleSheet("border-radius : 10; background-color : #7A2548")
        btn96.clicked.connect(self.clickme)

        btn17 = QPushButton("", self)
        btn17.setGeometry(697, 250, 86, 40)
        btn17.setStyleSheet("border-radius : 10; background-color : #713B49")
        btn17.clicked.connect(self.clickme)

        btn27 = QPushButton("", self)
        btn27.setGeometry(697, 300, 86, 40)
        btn27.setStyleSheet("border-radius : 10; background-color : #713B49")
        btn27.clicked.connect(self.clickme)

        btn37 = QPushButton("", self)
        btn37.setGeometry(697, 350, 86, 40)
        btn37.setStyleSheet("border-radius : 10; background-color : #713B49")
        btn37.clicked.connect(self.clickme)

        btn47 = QPushButton("", self)
        btn47.setGeometry(697, 400, 86, 40)
        btn47.setStyleSheet("border-radius : 10; background-color : #713B49")
        btn47.clicked.connect(self.clickme)

        btn57 = QPushButton("", self)
        btn57.setGeometry(697, 450, 86, 40)
        btn57.setStyleSheet("border-radius : 10; background-color : #713B49")
        btn57.clicked.connect(self.clickme)

        btn67 = QPushButton("", self)
        btn67.setGeometry(697, 500, 86, 40)
        btn67.setStyleSheet("border-radius : 10; background-color : #713B49")
        btn67.clicked.connect(self.clickme)

        btn77 = QPushButton("", self)
        btn77.setGeometry(697, 550, 86, 40)
        btn77.setStyleSheet("border-radius : 10; background-color : #713B49")
        btn77.clicked.connect(self.clickme)

        btn87 = QPushButton("", self)
        btn87.setGeometry(697, 600, 86, 40)
        btn87.setStyleSheet("border-radius : 10; background-color : #713B49")
        btn87.clicked.connect(self.clickme)

        btn97 = QPushButton("", self)
        btn97.setGeometry(697, 650, 86, 40)
        btn97.setStyleSheet("border-radius : 10; background-color : #713B49")
        btn97.clicked.connect(self.clickme)

        btn18 = QPushButton("", self)
        btn18.setGeometry(791, 250, 86, 40)
        btn18.setStyleSheet("border-radius : 10; background-color : #009FB5")
        btn18.clicked.connect(self.clickme)

        btn28 = QPushButton("", self)
        btn28.setGeometry(791, 300, 86, 40)
        btn28.setStyleSheet("border-radius : 10; background-color : #009FB5")
        btn28.clicked.connect(self.clickme)

        btn38 = QPushButton("", self)
        btn38.setGeometry(791, 350, 86, 40)
        btn38.setStyleSheet("border-radius : 10; background-color : #009FB5")
        btn38.clicked.connect(self.clickme)

        btn48 = QPushButton("", self)
        btn48.setGeometry(791, 400, 86, 40)
        btn48.setStyleSheet("border-radius : 10; background-color : #009FB5")
        btn48.clicked.connect(self.clickme)

        btn58 = QPushButton("", self)
        btn58.setGeometry(791, 450, 86, 40)
        btn58.setStyleSheet("border-radius : 10; background-color : #009FB5")
        btn58.clicked.connect(self.clickme)

        btn68 = QPushButton("", self)
        btn68.setGeometry(791, 500, 86, 40)
        btn68.setStyleSheet("border-radius : 10; background-color : #009FB5")
        btn68.clicked.connect(self.clickme)

        btn78 = QPushButton("", self)
        btn78.setGeometry(791, 550, 86, 40)
        btn78.setStyleSheet("border-radius : 10; background-color : #009FB5")
        btn78.clicked.connect(self.clickme)

        btn88 = QPushButton("", self)
        btn88.setGeometry(791, 600, 86, 40)
        btn88.setStyleSheet("border-radius : 10; background-color : #009FB5")
        btn88.clicked.connect(self.clickme)

        btn98 = QPushButton("", self)
        btn98.setGeometry(791, 650, 86, 40)
        btn98.setStyleSheet("border-radius : 10; background-color : #009FB5")
        btn98.clicked.connect(self.clickme)

        btn19 = QPushButton("", self)
        btn19.setGeometry(885, 250, 86, 40)
        btn19.setStyleSheet("border-radius : 10; background-color : #007180")
        btn19.clicked.connect(self.clickme)

        btn29 = QPushButton("", self)
        btn29.setGeometry(885, 300, 86, 40)
        btn29.setStyleSheet("border-radius : 10; background-color : #007180")
        btn29.clicked.connect(self.clickme)

        btn39 = QPushButton("", self)
        btn39.setGeometry(885, 350, 86, 40)
        btn39.setStyleSheet("border-radius : 10; background-color : #007180")
        btn39.clicked.connect(self.clickme)

        btn49 = QPushButton("", self)
        btn49.setGeometry(885, 400, 86, 40)
        btn49.setStyleSheet("border-radius : 10; background-color : #007180")
        btn49.clicked.connect(self.clickme)

        btn59 = QPushButton("", self)
        btn59.setGeometry(885, 450, 86, 40)
        btn59.setStyleSheet("border-radius : 10; background-color : #007180")
        btn59.clicked.connect(self.clickme)

        btn69 = QPushButton("", self)
        btn69.setGeometry(885, 500, 86, 40)
        btn69.setStyleSheet("border-radius : 10; background-color : #007180")
        btn69.clicked.connect(self.clickme)

        btn79 = QPushButton("", self)
        btn79.setGeometry(885, 550, 86, 40)
        btn79.setStyleSheet("border-radius : 10; background-color : #007180")
        btn79.clicked.connect(self.clickme)

        btn89 = QPushButton("", self)
        btn89.setGeometry(885, 600, 86, 40)
        btn89.setStyleSheet("border-radius : 10; background-color : #007180")
        btn89.clicked.connect(self.clickme)

        btn99 = QPushButton("", self)
        btn99.setGeometry(885, 650, 86, 40)
        btn99.setStyleSheet("border-radius : 10; background-color : #007180")
        btn99.clicked.connect(self.clickme)

        btn1a = QPushButton("", self)
        btn1a.setGeometry(979, 250, 86, 40)
        btn1a.setStyleSheet("border-radius : 10; background-color : #308781")
        btn1a.clicked.connect(self.clickme)

        btn2a = QPushButton("", self)
        btn2a.setGeometry(979, 300, 86, 40)
        btn2a.setStyleSheet("border-radius : 10; background-color : #308781")
        btn2a.clicked.connect(self.clickme)

        btn3a = QPushButton("", self)
        btn3a.setGeometry(979, 350, 86, 40)
        btn3a.setStyleSheet("border-radius : 10; background-color : #308781")
        btn3a.clicked.connect(self.clickme)

        btn4a = QPushButton("", self)
        btn4a.setGeometry(979, 400, 86, 40)
        btn4a.setStyleSheet("border-radius : 10; background-color : #308781")
        btn4a.clicked.connect(self.clickme)

        btn5a = QPushButton("", self)
        btn5a.setGeometry(979, 450, 86, 40)
        btn5a.setStyleSheet("border-radius : 10; background-color : #308781")
        btn5a.clicked.connect(self.clickme)

        btn6a = QPushButton("", self)
        btn6a.setGeometry(979, 500, 86, 40)
        btn6a.setStyleSheet("border-radius : 10; background-color : #308781")
        btn6a.clicked.connect(self.clickme)

        btn7a = QPushButton("", self)
        btn7a.setGeometry(979, 550, 86, 40)
        btn7a.setStyleSheet("border-radius : 10; background-color : #308781")
        btn7a.clicked.connect(self.clickme)

        btn8a = QPushButton("", self)
        btn8a.setGeometry(979, 600, 86, 40)
        btn8a.setStyleSheet("border-radius : 10; background-color : #308781")
        btn8a.clicked.connect(self.clickme)

        btn9a = QPushButton("", self)
        btn9a.setGeometry(979, 650, 86, 40)
        btn9a.setStyleSheet("border-radius : 10; background-color : #308781")
        btn9a.clicked.connect(self.clickme)

        btn1b = QPushButton("", self)
        btn1b.setGeometry(1073, 250, 86, 40)
        btn1b.setStyleSheet("border-radius : 10; background-color : #15625F")
        btn1b.clicked.connect(self.clickme)

        btn2b = QPushButton("", self)
        btn2b.setGeometry(1073, 300, 86, 40)
        btn2b.setStyleSheet("border-radius : 10; background-color : #15625F")
        btn2b.clicked.connect(self.clickme)

        btn3b = QPushButton("", self)
        btn3b.setGeometry(1073, 350, 86, 40)
        btn3b.setStyleSheet("border-radius : 10; background-color : #15625F")
        btn3b.clicked.connect(self.clickme)

        btn4b = QPushButton("", self)
        btn4b.setGeometry(1073, 400, 86, 40)
        btn4b.setStyleSheet("border-radius : 10; background-color : #15625F")
        btn4b.clicked.connect(self.clickme)

        btn5b = QPushButton("", self)
        btn5b.setGeometry(1073, 450, 86, 40)
        btn5b.setStyleSheet("border-radius : 10; background-color : #15625F")
        btn5b.clicked.connect(self.clickme)

        btn6b = QPushButton("", self)
        btn6b.setGeometry(1073, 500, 86, 40)
        btn6b.setStyleSheet("border-radius : 10; background-color : #15625F")
        btn6b.clicked.connect(self.clickme)

        btn7b = QPushButton("", self)
        btn7b.setGeometry(1073, 550, 86, 40)
        btn7b.setStyleSheet("border-radius : 10; background-color : #15625F")
        btn7b.clicked.connect(self.clickme)

        btn8b = QPushButton("", self)
        btn8b.setGeometry(1073, 600, 86, 40)
        btn8b.setStyleSheet("border-radius : 10; background-color : #15625F")
        btn8b.clicked.connect(self.clickme)

        btn9b = QPushButton("", self)
        btn9b.setGeometry(1073, 650, 86, 40)
        btn9b.setStyleSheet("border-radius : 10; background-color : #15625F")
        btn9b.clicked.connect(self.clickme)

    def clickme(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("DONT KNOW ABOUT THIS MEDICINE MAYBE CROCINE")
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.exec()
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec())
