import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import UI.prescriptionTable as preTable

# class Window3(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Medical Files")
#         self.setGeometry(0, 0, 1220, 685)
#         self.setStyleSheet("background-color: #F0F0F3")
#         self.label = QLabel(self)
#         self.label.setPixmap(QPixmap('../Resources/Group 47.png'))
#         self.label.setGeometry(0, -10, 1220, 685)
#
#         self.UiComponents()
#     #
#     #     # showing all the widgets
#         self.show()
#     #
#     def UiComponents(self):
#
#         btn_back = QPushButton("", self)
#         btn_back.setGeometry(40, 53, 173, 41)
#         btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
#         btn_back.setIcon(QtGui.QIcon('../Resources/Group 49.png'))
#         btn_back.setIconSize(QtCore.QSize(155, 71))
#         btn_back.clicked.connect(self.close)
#
#         tlbl = QLabel(self)
#         tlbl.setPixmap(QPixmap('../Resources/mtable.png'))
#         tlbl.setGeometry(25, 146, 1169, 863)
#
#         ilbl = QLabel("2", self)
#         ilbl.setGeometry(459, 249, 90, 30)
#         ilbl.setAlignment(QtCore.Qt.AlignCenter)

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../Resources/Group 47.png'))
        self.label.setGeometry(0, 0, 1220, 685)

        self.UiComponents()
    #
    #     # showing all the widgets
        self.show()
    #
    def UiComponents(self):

        btn_back = QPushButton("", self)
        btn_back.setGeometry(40, 53, 173, 41)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('../Resources/backButton.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)


class Refill(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F0F0F3")
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('../Resources/Group 48.png'))
        self.label.setGeometry(0, -10, 1220, 685)
        self.UiComponents()
        self.show()

    def UiComponents(self):

        # self.vLayout = QHBoxLayout()

        checkbox_A = QCheckBox('A', self)
        checkbox_A.setGeometry(493, 368, 80, 80)
        checkbox_A.setStyleSheet("QCheckBox::indicator"
                               "{"
                               "width :80px;"
                               "height : 80px;"
                               "}")



        checkbox_B = QCheckBox('B', self)
        checkbox_B.setGeometry(813, 368, 80, 80)
        checkbox_B.setStyleSheet("QCheckBox::indicator"
                                 "{"
                                 "width :80px;"
                                 "height : 80px;"
                                 "}")


        checkbox_A.stateChanged.connect(self.selectChkboxA)
        checkbox_B.stateChanged.connect(self.selectChkboxB)

        btn_back = QPushButton("", self)
        btn_back.setGeometry(40, 53, 173, 41)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F0F0F3")
        btn_back.setIcon(QtGui.QIcon('../Resources/Group 49.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)



    def selectChkboxA(self, checked):
        if Qt.Checked == checked:
            self.l = Window2()
        else:
            print('Checkbox A is unchecked')

    def selectChkboxB(self, checked):
        if Qt.Checked == checked:
            self.t = preTable.PrescriptionTable()
            self.t.show()
        else:
            print('Checkbox B is unchecked')

    # def medfiles(self):
    #     self.l = Window2()
    #     self.l.show()
    #     # self.hide()




#
# if __name__ == '__main__':
#     #     app = QApplication(sys.argv)
#     #
#     #     demo = AppDemo()
#     #     demo.show()
#     #
#     #     app.exit(app.exec_())
#     App = QApplication(sys.argv)
#
#     # create the instance of our Window
#     window = Refill()
#
#     window.show()
#
#     # start the app
#     sys.exit(App.exec())