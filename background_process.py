# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time
import datetime


class Example(QWidget):

    def __init__(self):
        super().__init__()

        # calling initUI method
        self.initUI()

    # method for creating widgets
    def initUI(self):
        # creating progress bar
        self.pbar = QProgressBar(self)

        # setting its geometry
        self.pbar.setGeometry(30, 40, 200, 25)

        # creating push button
        self.btn = QPushButton('Start', self)

        # changing its position
        self.btn.move(40, 80)

        # adding action to push button
        self.btn.clicked.connect(self.doAction)

        # setting window geometry
        self.setGeometry(300, 300, 280, 170)

        # setting window action
        self.setWindowTitle("Python")

        self.StopBtn = QPushButton("Stop", self)
        self.StopBtn.move(40, 130)
        self.StopBtn.clicked.connect(self.StopAction)


        # showing all the widgets
        self.show()

    # when button is pressed this method is being called
    def doAction(self):
        # setting for loop to set value of progress bar
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.finished.connect(self.evt_worker_finished)
        self.worker.update_progress.connect(self.evt_update_progress)

    def StopAction(self):
        # setting for loop to set value of progress bar
        print("clicked")
        # self.worker = WorkerThread()
        self.worker.terminate()
        self.worker.finished.connect(self.evt_worker_finished)
        self.worker.update_progress.connect(self.evt_update_progress)



    def evt_worker_finished(self):
        QMessageBox.information(self, "Done!", "Thread is complete")

    def evt_update_progress(self, val):
        self.pbar.setValue(val)
        print("hellllo")


class WorkerThread(QThread):
    update_progress = pyqtSignal(int)
    def run(self):
        i = 0
        while True:
            # slowing down the loop
            print(datetime.datetime.now())
            time.sleep(0.05)
            self.update_progress.emit(i)

            # setting value to progress bar
            self.pbar.setValue(i)
            i = i+1




# main method
if __name__ == '__main__':
    # create pyqt5 app
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = Example()

    # start the app
    sys.exit(App.exec())
