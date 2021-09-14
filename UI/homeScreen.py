# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime
# from PyQt5 import QLa
# from myprofile import MyProfile

import sys
# from test import *
import UI.myprofile as myPro
import UI.medicinetime as myMeds
import UI.docAppScreen as myAppo
import UI.settings as settings
import UI.Humm as humm
import UI.MyCylinders as myCylinder
import UI.prescriptionTable as myPrescription
import UI.MyStats as myStats
import UI.power as pwr
import Utility.MahiUtility as Util
import time
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time
import datetime


class WorkerThread(QThread):
    update_progress = pyqtSignal(int)
    def run(self):
        i = 0
        while True:
            # slowing down the loop
            current_time = QTime.currentTime()

            # converting QTime object to string
            label_time = current_time.toString('ss')
            print(label_time)
            i = i+1
            if int(label_time)%10 == 0:
                temp = current_time.toString("hh:mm:ss ap")
                print(temp)

                self.update_progress.emit(i)
                # self.ShowBox()


            time.sleep(1)

class HomeScreen(QMainWindow):
    def __init__(self, parent = None):
        super().__init__()
        self.doAction()
        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 685)

        # calling method
        self.UiComponents()
        self.setStyleSheet("background-color: #F0F0F3")
        font = QFont('Arial', 40, QFont.Bold)
        layout = QVBoxLayout()
        self.lblTime = QLabel(self)
        self.lblTime.setGeometry(476, 312, 340, 81)
        layout.addWidget(self.lblTime)
        self.lblTime.setFont(font)
        self.lblTime.setStyleSheet("color: #00A0B5")
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        # lblTime.setPixmap(QPixmap('../Resources/Time.png'))

        # showing all the widgets
        self.show()

        # method for widgets
    def showTime(self):
        # getting current time
        current_time = QTime.currentTime()

        # converting QTime object to string
        label_time = current_time.toString('hh:mm ap')

        # showing it to the label
        self.lblTime.setText(label_time)

    def UiComponents(self):

        # creating a push button
        btn_cal1 = QPushButton("", self)
        btn_cal1.setGeometry(24, 561, 194, 100)
        btn_cal1.setStyleSheet("border-radius : 15; background-color : #F0F0F3; color:#00A0B5")
        btn_cal1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_cal = QPushButton("", self)
        btn_cal.setGeometry(24, 561, 194, 100)
        btn_cal.setStyleSheet("border-radius : 15; background-color : #F0F0F3;  color:#00A0B5")
        btn_cal.setIcon(QtGui.QIcon('../Resources/MyCalendar.png'))
        btn_cal.setIconSize(QtCore.QSize(194, 100))
        btn_cal.setGraphicsEffect(Util.getNeuShadow(1))
        btn_cal.clicked.connect(self.Calendar)

        #profilebutton
        btn_pro1 = QPushButton("", self)
        btn_pro1.setGeometry(756, 561, 194, 100)
        btn_pro1.setStyleSheet("border-radius : 15; background-color : #F0F0F3; color:#00A0B5; ")
        btn_pro1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_pro = QPushButton("", self)
        btn_pro.setGeometry(756, 561, 194, 100)
        btn_pro.setStyleSheet("border-radius : 15; background-color : #F0F0F3; color:#00A0B5; ")
        btn_pro.setIcon(QtGui.QIcon('../Resources/MyProfile.png'))
        btn_pro.setIconSize(QtCore.QSize(194, 100))
        btn_pro.setGraphicsEffect(Util.getNeuShadow(1))
        btn_pro.clicked.connect(self.profileClicked)

        # mymedcicinebutton
        btn_med1 = QPushButton("", self)
        btn_med1.setGeometry(1003, 561, 194, 100)
        btn_med1.setStyleSheet("border-radius : 15; background-color : #F0F0F3;  ")
        btn_med1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_med = QPushButton("", self)
        btn_med.setGeometry(1003, 561, 194, 100)
        btn_med.setStyleSheet("border-radius : 15; background-color : #F0F0F3;  ;color:#00A0B5; ")
        btn_med.setIcon(QtGui.QIcon('../Resources/MyMedicine.png'))
        btn_med.setIconSize(QtCore.QSize(194, 100))
        btn_med.setGraphicsEffect(Util.getNeuShadow(1))
        btn_med.clicked.connect(self.myCylinderClicked)

        # mystatsbutton
        btn_stat1 = QPushButton("", self)
        btn_stat1.setGeometry(512, 561, 194, 100)
        btn_stat1.setStyleSheet("border-radius : 15; background-color : #F0F0F3; color:#00A0B5;")
        btn_stat1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_stat = QPushButton("", self)
        btn_stat.setGeometry(512, 561, 194, 100)
        btn_stat.setStyleSheet("border-radius : 15; background-color : #F0F0F3; color:#00A0B5;")
        btn_stat.setIcon(QtGui.QIcon('../Resources/MyStats.png'))
        btn_stat.setIconSize(QtCore.QSize(194, 100))
        btn_stat.setGraphicsEffect(Util.getNeuShadow(1))
        btn_stat.clicked.connect(self.myStatsClicked)

        # settingsbutton    background-image : Resources(setm.png)  background-color : #F5A5BF  color:#FFFFFF
        btn_sett1 = QPushButton("", self)
        btn_sett1.setGeometry(329, 86, 54, 54)
        btn_sett1.setStyleSheet("border-radius : 5; background-color : #F0F0F3;")
        btn_sett1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_sett = QPushButton("", self)
        btn_sett.setGeometry(329, 86, 54, 54)
        btn_sett.setStyleSheet("border-radius : 5; background-color : #F0F0F3; ")
        btn_sett.setIcon(QtGui.QIcon('../Resources/Settings.png'))
        btn_sett.setIconSize(QtCore.QSize(54, 54))
        btn_sett.setGraphicsEffect(Util.getNeuShadow(1))
        btn_sett.clicked.connect(self.settingsClicked)

        btn_power1 = QPushButton("", self)
        btn_power1.setGeometry(24, 86, 54, 54)
        btn_power1.setStyleSheet("border-radius : 5; background-color : #F0F0F3;")
        btn_power1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_power = QPushButton("", self)
        btn_power.setGeometry(24, 86, 54, 54)
        btn_power.setStyleSheet("border-radius : 5; background-color : #F0F0F3; ")
        btn_power.setIcon(QtGui.QIcon('../Resources/PowerM.png/'))
        btn_power.setIconSize(QtCore.QSize(54, 54))
        btn_power.setGraphicsEffect(Util.getNeuShadow(1))
        btn_power.clicked.connect(self.powerClicked)

        btn_Notif1 = QPushButton("", self)
        btn_Notif1.setGeometry(98, 86, 54, 54)
        btn_Notif1.setStyleSheet("border-radius : 5; background-color : #F0F0F3; ")
        btn_Notif1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_Notif = QPushButton("", self)
        btn_Notif.setGeometry(98, 86, 54, 54)
        btn_Notif.setStyleSheet("border-radius : 5; background-color : #F0F0F3; ")
        btn_Notif.setIcon(QtGui.QIcon('../Resources/Notif.png'))
        btn_Notif.setIconSize(QtCore.QSize(54, 54))
        btn_Notif.setGraphicsEffect(Util.getNeuShadow(1))
        btn_Notif.clicked.connect(self.settingsClicked)

        btn_wifi1 = QPushButton("", self)
        btn_wifi1.setGeometry(172, 86, 54, 54)
        btn_wifi1.setStyleSheet("border-radius : 5; background-color : #F0F0F3;")
        btn_wifi1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_wifi = QPushButton("", self)
        btn_wifi.setGeometry(172, 86, 54, 54)
        btn_wifi.setStyleSheet("border-radius : 5; background-color : #F0F0F3; ")
        btn_wifi.setIcon(QtGui.QIcon('../Resources/wifi.png'))
        btn_wifi.setIconSize(QtCore.QSize(54, 54))
        btn_wifi.setGraphicsEffect(Util.getNeuShadow(1))
        btn_wifi.clicked.connect(self.settingsClicked)

        btn_Bluetooth1 = QPushButton("", self)
        btn_Bluetooth1.setGeometry(246, 86, 54, 54)
        btn_Bluetooth1.setStyleSheet("border-radius : 5; background-color : #F0F0F3;")
        btn_Bluetooth1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_Bluetooth = QPushButton("", self)
        btn_Bluetooth.setGeometry(246, 86, 54, 54)
        btn_Bluetooth.setStyleSheet("border-radius : 5; background-color : #F0F0F3;")
        btn_Bluetooth.setIcon(QtGui.QIcon('../Resources/bluetooth.png'))
        btn_Bluetooth.setIconSize(QtCore.QSize(54, 54))
        btn_Bluetooth.setGraphicsEffect(Util.getNeuShadow(1))
        btn_Bluetooth.clicked.connect(self.settingsClicked)

        # Refill Button
        btn_Refill = QPushButton("", self)
        btn_Refill.setGeometry(690, 86, 140, 58)
        btn_Refill.setStyleSheet("border-radius : 15; background-color : #F0F0F3; color:#FFFFFF;")
        btn_Refill.setGraphicsEffect(Util.getNeuShadow(0))
        btn_Refill = QPushButton("", self)
        btn_Refill.setGeometry(690, 86, 140, 58)
        btn_Refill.setStyleSheet("border-radius : 15; background-color : #F0F0F3; color:#FFFFFF;")
        btn_Refill.setIcon(QtGui.QIcon('../Resources/Refill.png'))
        btn_Refill.setIconSize(QtCore.QSize(140, 58))
        btn_Refill.setGraphicsEffect(Util.getNeuShadow(1))
        btn_Refill.clicked.connect(self.refillClicked)

        # Inject Button
        btn_Inject1 = QPushButton("", self)
        btn_Inject1.setGeometry(871, 86, 140, 58)
        btn_Inject1.setStyleSheet("border-radius : 15; background-color : #F0F0F3; color:#FFFFFF;")
        btn_Inject1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_Inject = QPushButton("", self)
        btn_Inject.setGeometry(871, 86, 140, 58)
        btn_Inject.setStyleSheet("border-radius : 15; background-color : #F0F0F3; color:#FFFFFF;")
        btn_Inject.setIcon(QtGui.QIcon('../Resources/InjectBox.png'))
        btn_Inject.setIconSize(QtCore.QSize(140, 58))
        btn_Inject.setGraphicsEffect(Util.getNeuShadow(1))
        # btn_Inject.clicked.connect(self.refillClicked)

        # Eject Button
        btn_Eject1 = QPushButton("", self)
        btn_Eject1.setGeometry(1056, 86, 140, 58)
        btn_Eject1.setStyleSheet("border-radius : 15; background-color : #F0F0F3; color:#FFFFFF;")
        btn_Eject1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_Eject = QPushButton("", self)
        btn_Eject.setGeometry(1056, 86, 140, 58)
        btn_Eject.setStyleSheet("border-radius : 15; background-color : #F0F0F3; color:#FFFFFF;")
        btn_Eject.setIcon(QtGui.QIcon('../Resources/InjectBox.png'))
        btn_Eject.setIconSize(QtCore.QSize(140, 58))
        btn_Eject.setGraphicsEffect(Util.getNeuShadow(1))
        # btn_Eject.clicked.connect(self.refillClicked)


        # hummbutton
        btn_humm1 = QPushButton("", self)
        btn_humm1.setGeometry(268, 561, 200, 100)
        btn_humm1.setStyleSheet("border-radius : 15; background-color : #F0F0F3; color:#FFFFFF; ")
        btn_humm1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_humm = QPushButton("", self)
        btn_humm.setGeometry(268, 561, 200, 100)
        btn_humm.setStyleSheet("border-radius : 15; background-color : #F0F0F3; color:#FFFFFF;")
        btn_humm.setIcon(QtGui.QIcon('../Resources/humm.png'))
        btn_humm.setIconSize(QtCore.QSize(200, 100))
        btn_humm.setGraphicsEffect(Util.getNeuShadow(1))
        btn_humm.clicked.connect(self.hummClicked)


        # SOS
        btn_sos1 = QPushButton("", self)
        btn_sos1.setGeometry(1122, 24, 74, 41)
        btn_sos1.setStyleSheet("border-radius : 10; background-color : #00A0B5; color:#FFFFFF;")
        btn_sos1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_sos = QPushButton("SOS", self)
        btn_sos.setGeometry(1122, 24, 74, 41)
        btn_sos.setStyleSheet("border-radius : 10; background-color : #00A0B5; color:#FFFFFF;")
        btn_sos.setGraphicsEffect(Util.getNeuShadow(1))
        # btn_sos.setIcon(QtGui.QIcon('../Resources/menubar.png'))
        # btn_sos.setIconSize(QtCore.QSize(767, 83))
        btn_sos.clicked.connect(self.clickme)


        # refillBar
        btn_refillbar1 = QPushButton("", self)
        btn_refillbar1.setGeometry(690, 24, 420, 38)
        btn_refillbar1.setStyleSheet("border-radius : 20; background-color : #E5E5E5; ")
        btn_refillbar1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_refillbar = QPushButton("", self)
        btn_refillbar.setGeometry(690, 24, 420, 38)
        btn_refillbar.setStyleSheet("border-radius : 20; background-color : #E5E5E5;")
        btn_refillbar.setGraphicsEffect(Util.getNeuShadow(1))
        btn_refillbar.setIcon(QtGui.QIcon('../Resources/RefillBar.png'))
        btn_refillbar.setIconSize(QtCore.QSize(420, 38))
        # btn_refillbar.clicked.connect(self.refillClicked)


        # doc_appointment_button
        btn_doc1 = QPushButton("", self)
        btn_doc1.setGeometry(24, 24, 611, 38)
        btn_doc1.setStyleSheet("border-radius : 5; background-color : #F0F0F3; color:#FFFFFF; text-align:left")
        btn_doc1.setGraphicsEffect(Util.getNeuShadow(0))
        btn_doc = QPushButton("", self)
        btn_doc.setGeometry(24, 24, 611, 38)
        btn_doc.setStyleSheet("border-radius : 5; background-color : #F0F0F3; color:#FFFFFF; text-align:left")
        btn_doc.setIcon(QtGui.QIcon('../Resources/DocAppoint.png'))
        btn_doc.setIconSize(QtCore.QSize(611, 38))
        btn_doc.setGraphicsEffect(Util.getNeuShadow(1))
        btn_doc.clicked.connect(self.docAppoClicked)

        #btn_doc.setFrameShadow(QFrame.Sunken)



    def clickme(self):
        # printing pressed
        print("pressed")

    def hummClicked(self):
        self.x = humm.Humm()
        self.x.show()

    def medTimeClicked(self):
        self.x = myMeds.MyMedicines()
        self.x.show()

    def profileClicked(self):
        self.x = myPro.MyProfile()
        self.x.show()

    def myCylinderClicked(self):
        self.x = myCylinder.PrescriptionTable()
        self.x.show()

    def docAppoClicked(self):
        self.x = myAppo.DocAppScreen()
        self.x.show()

    def settingsClicked(self):
        self.x = settings.Settings(self)
        self.x.show()

    # calendar function
    def Calendar(self):
        vbox = QVBoxLayout()
        self.calendar = QCalendarWidget()

        vbox.addWidget(self.calendar)

        self.setLayout(vbox)

    def refillClicked(self):
        self.x = myPrescription.PrescriptionTable()
        self.x.show()

    def myStatsClicked(self):
        self.x = myStats.MyStats(0)
        self.x.show()

    def powerClicked(self):
        self.x = pwr.Power()
        self.x.show()

    def evt_update_progress(self):
        # current_time = QTime.currentTime()
        # temp = current_time.toString("hh:mm:ss ap")
        # QMessageBox.information(self,"Done",temp)
        # self.hummClicked()
        print(" ")

    def doAction(self):
        # setting for loop to set value of progress bar
        self.worker = WorkerThread()
        self.worker.start()
        # self.worker.finished.connect(self.evt_worker_finished)
        self.worker.update_progress.connect(self.evt_update_progress)

    def StopAction(self):
        # setting for loop to set value of progress bar
        print("clicked")
        # self.worker = WorkerThread()
        self.worker.terminate()
    # # create pyqt5 app
    # def mypro(self):
    #     self.pro = MyProfile()
    #     self.pro.show()


if __name__ == '__main__':

    App = QApplication(sys.argv)

    # create the instance of our Window
    window = HomeScreen()

    # start the app
    sys.exit(App.exec())