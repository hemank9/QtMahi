import json
import requests
import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import constants as constants
import MyDatabase.my_database as myDB
import Utility.MahiUtility as utility
import API.my_urls as myUrls
import API.api_calls as MyApis

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import Utility.MahiUtility as MahiUtil
import Custom.AppointmentListItem as appoi
import API.api_calls as MyApis
import json
import math

class DocAppScreen(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 700)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setStyleSheet("background-color:#FEC32E")
        self.label.setGeometry(0, 0, 1220, 165)
        self.btnStyle = "border-radius : 10; background-color : #F0F03; color : #006CB5; font : bold "
        self.btnStyleSelected = "border-radius : 10; background-color : #C4DBF0; color : #006CB5; font : bold "
        self.fontObj = QFont('Arial', 9)
        # calling method
        # self.UiComponents()
        self.lbl = QLabel(self)


        # showing all the widgets
        self.show()


        self.page = 1

        # self.SetAppointmentList()
        response = MyApis.fetchPrescriptionHistory(self.page)

        if response != None:
            prescriptionList = list(response['data'])

            # for prescription in prescriptionList:
            #     print(prescription['doctor_name'])
            if len(prescriptionList) > 0:
                presc  = prescriptionList[0]
                presc['patient_name']
                self.lbl.setStyleSheet("background-color: red")
                self.lbl.setText(presc['patient_name'])






if __name__ == "__main__":

    App = QApplication(sys.argv)

    # create the instance of our Window
    window = DocAppScreen()

    window.show()

    # start the app
    sys.exit(App.exec())
