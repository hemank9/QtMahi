from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import UI.repeatDosage as rDosage
import UI.extraDosage as extraDosage
import UI.datePickMassEjection as massEject
import UI.changetime as changeTime
import sys
import Utility.MahiUtility as Util
import MyDatabase.my_database as myDb

class MyMedicines(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(0, 0, 1220, 700)
        self.setStyleSheet("background-color: #F0F0F3")
        # self.label = QLabel(self)
        # self.label.setStyleSheet("background-color:#FEC32E")
        # self.label.setGeometry(0, 0, 1220, 39)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        TitleStyle = "font-size:20px;"

        #Headers

        startX = 190
        startY = 242

        startX2 = 48
        startY2 = 282

        titles = ["Morning", "Noon", "Evening", "Early Morning", "Mid Night", "Late Night"]
        xCount = 0
        for i in range(6):

            lblBfTitle = QLabel("(BF)",self)
            lblBfTitle.setGeometry(startX + (xCount*380),startY,50,30)
            lblBfTitle.setStyleSheet(TitleStyle)
            lblAfTitle = QLabel("(AF)",self)
            lblAfTitle.setGeometry(startX + 120 + (xCount*380),startY,50,30)
            lblAfTitle.setStyleSheet(TitleStyle)

            lblTitle = QLabel(titles[i],self)
            lblTitle.setGeometry(startX2 + (xCount*380),startY2,90,60)
            lblTitle.setAlignment(Qt.AlignCenter)
            lblTitle.setWordWrap(True)
            lblTitle.setStyleSheet(TitleStyle)
            xCount = xCount+1
            if (i+1)%3==0:
                xCount=0;
                startY = startY+165
                startY2 = startY2+165


        borderColors = ["#FAD208","#BF2D93", "#009DF8", "#8CC63E", "#00A652", "#006733"]
        self.TextStyle = "text: bold; font-size:17px; border-radius : 7; border:4px solid "

        self.lblMorningBf = QLabel(self)
        self.lblMorningBf.setStyleSheet(self.TextStyle+borderColors[0])
        self.lblMorningBf.setGeometry(157, 285, 110, 55)
        self.lblMorningBf.setAlignment(Qt.AlignCenter)

        self.lblMorningAf = QLabel(self)
        self.lblMorningAf.setStyleSheet(self.TextStyle+borderColors[0])
        self.lblMorningAf.setGeometry(277, 285, 110, 55)
        self.lblMorningAf.setAlignment(Qt.AlignCenter)

        self.lblAfternoonBf = QLabel(self)
        self.lblAfternoonBf.setStyleSheet(self.TextStyle+borderColors[1])
        self.lblAfternoonBf.setGeometry(537, 285, 110, 55)
        self.lblAfternoonBf.setAlignment(Qt.AlignCenter)

        self.lblAfternoonAf = QLabel(self)
        self.lblAfternoonAf.setStyleSheet(self.TextStyle+borderColors[1])
        self.lblAfternoonAf.setGeometry(657, 285, 110, 55)
        self.lblAfternoonAf.setAlignment(Qt.AlignCenter)

        self.lblEveningBf = QLabel(self)
        self.lblEveningBf.setStyleSheet(self.TextStyle+borderColors[2])
        self.lblEveningBf.setGeometry(917, 285, 110, 55)
        self.lblEveningBf.setAlignment(Qt.AlignCenter)

        self.lblEveningAf = QLabel(self)
        self.lblEveningAf.setStyleSheet(self.TextStyle+borderColors[2])
        self.lblEveningAf.setGeometry(1037, 285, 110, 55)
        self.lblEveningAf.setAlignment(Qt.AlignCenter)

        self.lblEarlyMorningBf = QLabel(self)
        self.lblEarlyMorningBf.setStyleSheet(self.TextStyle+borderColors[3])
        self.lblEarlyMorningBf.setGeometry(157, 450, 110, 55)
        self.lblEarlyMorningBf.setText("7:30 pm")
        self.lblEarlyMorningBf.setAlignment(Qt.AlignCenter)

        self.lblEarlyMorningAf = QLabel(self)
        self.lblEarlyMorningAf.setStyleSheet(self.TextStyle+borderColors[3])
        self.lblEarlyMorningAf.setGeometry(277, 450, 110, 55)
        self.lblEarlyMorningAf.setText("8:30 pm")
        self.lblEarlyMorningAf.setAlignment(Qt.AlignCenter)

        self.lblMidNightBf = QLabel(self)
        self.lblMidNightBf.setStyleSheet(self.TextStyle+borderColors[4])
        self.lblMidNightBf.setGeometry(537, 450, 110, 55)
        self.lblMidNightBf.setText("7:30 pm")
        self.lblMidNightBf.setAlignment(Qt.AlignCenter)

        self.lblMidNightAf = QLabel(self)
        self.lblMidNightAf.setStyleSheet(self.TextStyle+borderColors[4])
        self.lblMidNightAf.setGeometry(657, 450, 110, 55)
        self.lblMidNightAf.setText("8:30 pm")
        self.lblMidNightAf.setAlignment(Qt.AlignCenter)

        self.lblLateNightBf = QLabel(self)
        self.lblLateNightBf.setStyleSheet(self.TextStyle+borderColors[5])
        self.lblLateNightBf.setGeometry(917, 450, 110, 55)
        self.lblLateNightBf.setText("7:30 pm")
        self.lblLateNightBf.setAlignment(Qt.AlignCenter)

        self.lblLateNightAf = QLabel(self)
        self.lblLateNightAf.setStyleSheet(self.TextStyle+borderColors[5])
        self.lblLateNightAf.setGeometry(1037, 450, 110, 55)
        self.lblLateNightAf.setText("8:30 pm")
        self.lblLateNightAf.setAlignment(Qt.AlignCenter)


        btn_adv1 = QPushButton("", self)
        btn_adv1.setGeometry(218, 55, 237, 105)
        btn_adv1.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_adv1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_adv = QPushButton("", self)
        btn_adv.setGeometry(218, 55, 237, 105)
        btn_adv.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_adv.setGraphicsEffect(Util.getNeuShadow(0))
        btn_adv.setIcon(QtGui.QIcon('../Resources/medAdv.png'))
        btn_adv.setIconSize(QtCore.QSize(237, 105))
        btn_adv.clicked.connect(self.massEjection)

        btn_changeTime1 = QPushButton("", self)
        btn_changeTime1.setGeometry(491, 55, 237, 105)
        btn_changeTime1.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_changeTime1.setGraphicsEffect(Util.getNeuShadow(1))
        btn_changeTime = QPushButton("", self)
        btn_changeTime.setGeometry(491, 55, 237, 105)
        btn_changeTime.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_changeTime.setIcon(QtGui.QIcon('../Resources/changeTime.png'))
        btn_changeTime.setIconSize(QtCore.QSize(237, 105))
        btn_changeTime.setGraphicsEffect(Util.getNeuShadow(0))
        btn_changeTime.clicked.connect(self.cTime)


        btn_extraDosage = QPushButton("", self)
        btn_extraDosage.setGeometry(765, 55, 237, 105)
        btn_extraDosage.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_extraDosage.setGraphicsEffect(Util.getNeuShadow(1))
        btn_extraDosage = QPushButton("", self)
        btn_extraDosage.setGeometry(765, 55, 237, 105)
        btn_extraDosage.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_extraDosage.setIcon(QtGui.QIcon('../Resources/extraDose.png'))
        btn_extraDosage.setIconSize(QtCore.QSize(237, 105))
        btn_extraDosage.setGraphicsEffect(Util.getNeuShadow(0))
        btn_extraDosage.clicked.connect(self.extraD)

        btn_bck = QPushButton("", self)
        btn_bck.setGeometry(43, 40, 150, 55)
        btn_bck.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_bck.setIcon(QtGui.QIcon('../Resources/backButton.png'))
        btn_bck.setIconSize(QtCore.QSize(160, 90))
        btn_bck.clicked.connect(self.close)

        self.SetCylinderData()

    def SetCylinderData(self):

        try:
            cursor = myDb.getSlotTimings()

            for row in cursor:
                print(row)

                time = Util.convert24to12Time(str(row[3]))

                if time == None:
                    time = "N.A."

                # Morning
                if str(row[1]).lower() == "morning":
                    if "before" in str(row[2]):
                        self.lblMorningBf.setText(time)
                    elif "after" in str(row[2]):
                        self.lblMorningAf.setText(time)

                # Afternoon
                elif str(row[1]).lower() == "afternoon" or str(row[1]).lower() == "noon":
                    if "before" in str(row[2]):
                        self.lblAfternoonBf.setText(time)
                    elif "after" in str(row[2]):
                        self.lblAfternoonAf.setText(time)

                # Evening
                elif str(row[1]).lower() == "evening":
                    if "before" in str(row[2]):
                        self.lblEveningBf.setText(time)
                    elif "after" in str(row[2]):
                        self.lblEveningAf.setText(time)

                # Early Morning
                elif str(row[1]).lower() == "early_morning":
                    if "before" in str(row[2]):
                        self.lblEarlyMorningBf.setText(time)
                    elif "after" in str(row[2]):
                        self.lblEarlyMorningAf.setText(time)

                # Mid Night
                elif str(row[1]).lower() == "mid_night":
                    if "before" in str(row[2]):
                        self.lblMidNightBf.setText(time)
                    elif "after" in str(row[2]):
                        self.lblMidNightAf.setText(time)

                # Late Night
                elif str(row[1]).lower() == "late_night":
                    if "before" in str(row[2]):
                        self.lblLateNightBf.setText(time)
                    elif "after" in str(row[2]):
                        self.lblLateNightAf.setText(time)


        except Exception as e:
            print(e.__cause__)


    # def afterNoonClicked(self):
    #     self.k = changeTime.ChangeTime(2)
    #     self.k.show()
    #
    # def morningClicked(self):
    #     self.k = changeTime.ChangeTime(1)
    #     self.k.show()
    #
    # def eveningClicked(self):
    #     self.k = changeTime.ChangeTime(3)
    #     self.k.show()


    def repeateD(self):
        self.l = rDosage.RepeatDosage()
        self.l.show()

    def massEjection(self):
        self.n = massEject.MassEjectDateTime()
        self.n.show()

    def extraD(self):
        self.m = extraDosage.ExtraDosage()
        self.m.show()

    def cTime(self):
        self.k = changeTime.ChangeTime(1)
        self.k.show()
#
if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = MyMedicines()

    window.show()

# start the app
    sys.exit(App.exec())



