import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QMovie
from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
import UI.myprofile as myProfile
import UI.homeScreen as homeScreen
import Controllers.login_controller as my_con
import MyDatabase.my_database as db

class MovieSplashScreen(QtWidgets.QSplashScreen):

    def __init__(self, pathToGIF):
        self.movie = QtGui.QMovie(pathToGIF)
        self.movie.jumpToFrame(0)
        pixmap = QtGui.QPixmap(self.movie.frameRect().size())
        QtWidgets.QSplashScreen.__init__(self, pixmap)
        self.movie.frameChanged.connect(self.repaint)

    def showEvent(self, event):
        self.movie.start()

    def hideEvent(self, event):
        self.movie.stop()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        pixmap = self.movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0, 0, pixmap)

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()

        if db.isLogggedIn():
            QtCore.QTimer.singleShot(3500, self.showHomeScreen)
        else:
            self.defineUI()

    def showHomeScreen(self):
        self.myprofileObj = homeScreen.HomeScreen(self)
        self.myprofileObj.show()
        self.close()

    def defineUI(self):
        self.label = QLabel(self)
        self.setWindowTitle('MAHI')
        self.resize(1220, 685)
        self.label.setPixmap(QPixmap('..\Resources\login.png'))

        # username entry
        self.username = QLineEdit(self)
        self.username.move(663, 222)
        self.username.resize(312, 52)
        self.username.setText("9131577259")

        self.username.setStyleSheet("border-radius : 10; padding: 15px; font: 24px")
        # self.username.setStyleSheet("")

        # password entrty
        self.password = QLineEdit(self)
        self.password.move(663, 311)
        self.password.resize(312, 52)
        self.password.setText("admin")
        self.password.setStyleSheet("border-radius : 10; padding: 15px; font: 24px")
        self.password.setEchoMode(QLineEdit.Password)

        btn_login = QPushButton("", self)
        btn_login.setGeometry(663, 402, 117, 55)
        btn_login.setStyleSheet("border-radius : 30; background-color : #7ACEDA")
        btn_login.setIcon(QtGui.QIcon('..\Resources\loginbutton.png'))
        btn_login.setIconSize(QtCore.QSize(117, 55))
        btn_login.clicked.connect(self.doLogin)

    # btn_pro.clicked.connect(self.)   click event goes here new function to be created
    # self.show()
    def doLogin(self):
        user = str(self.username.text().strip())
        passw = str(self.password.text().strip())

        messagebox = QMessageBox()
        if my_con.validateUserNumber(user) and len(passw) > 0:

            response = my_con.callLoginApi(user, passw)
            if response is not None:
                print("Login Successful")
                self.showHomeScreen()

            else:
                messagebox.setIcon(QMessageBox.Warning)
                messagebox.setText("Invalid username or password")  # add message box
                messagebox.exec()
        else:
            messagebox.setIcon(QMessageBox.Warning)
            messagebox.setText("Invalid username or password")  # add message box
            messagebox.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pathToGIF = "..\Resources\splash.gif"
    splash = MovieSplashScreen(pathToGIF)
    splash.show()


    def showWindow():
        splash.close()
        if db.isLogggedIn() != True:
            form.show()

    QtCore.QTimer.singleShot(3500, showWindow)
    # MainWindow.show()

    form = LoginForm()
    # form.show()

    sys.exit(app.exec_())
