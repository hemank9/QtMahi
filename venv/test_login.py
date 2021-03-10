import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QMovie
from PyQt5 import QtGui, QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QSize

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

		# defining the window and a background image
		self.label = QLabel(self)
		self.setWindowTitle('MAHI')
		self.resize(1220, 685)
		self.label.setPixmap(QPixmap('Resources\login.png'))
		self.label1= QLabel("testtt", self)
		self.label1.setGeometry(200,200,100,100)
		self.label1.setStyleSheet("QLabel{background-color : red;}")
		self.label1.setAlignment(QtCore.Qt.AlignRight)

		#username entry
		self.username  = QLineEdit(self)
		self.username.move(663, 222)
		self.username.resize(312, 52)
		self.username.setStyleSheet("border-radius : 20; padding: 15px; font: 24px")
		# self.username.setStyleSheet("")

		# password entrty
		self.password = QLineEdit(self)
		self.password.move(663, 311)
		self.password.resize(312, 52)
		self.password.setStyleSheet("border-radius : 20; padding: 15px; font: 24px")
		self.password.setEchoMode(QLineEdit.Password)

		btn_login = QPushButton("", self)
		btn_login.setGeometry(663, 402, 117, 55)
		btn_login.setStyleSheet("border-radius : 30; background-color : #7ACEDA")
		btn_login.setIcon(QtGui.QIcon('Resources\loginbutton.png'))
		btn_login.setIconSize(QtCore.QSize(117, 55))
		# btn_pro.clicked.connect(self.)   click event goes here new function to be created
		# self.show()
'''		
		label_name = QLabel('<font size="4"> Username </font>')
		self.lineEdit_username = QLineEdit()
		self.lineEdit_username.setPlaceholderText('Please enter your username')
		# layout.addWidget(label_name, 0, 0)
		self.lineEdit_username.setGeometry(663,222,312,52)

		label_password = QLabel('<font size="4"> Password </font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setPlaceholderText('Please enter your password')
		# layout.addWidget(label_password, 1, 0)
		self.lineEdit_username.setGeometry(63,322,312,52)

		button_login = QPushButton('Login')
		button_login.clicked.connect(self.check_password)
		layout.addWidget(button_login, 2, 0, 1, 2)
		layout.setRowMinimumHeight(2, 75)

		self.setLayout(layout)

	def check_password(self):
		msg = QMessageBox()

		if self.lineEdit_username.text() == 'Usernmae' and self.lineEdit_password.text() == '000':
			msg.setText('Success')
			msg.exec_()
			app.quit()
		else:
			msg.setText('Incorrect Password')
			msg.exec_()
'''
if __name__ == '__main__':
	app = QApplication(sys.argv)
	pathToGIF = "Resources\splash.gif"
	splash = MovieSplashScreen(pathToGIF)
	splash.show()


	def showWindow():
		splash.close()
		form.show()


	QtCore.QTimer.singleShot(3500, showWindow)
	# MainWindow.show()
	form = LoginForm()
	# form.show()

	sys.exit(app.exec_())