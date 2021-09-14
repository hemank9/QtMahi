from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import Custom.FileListItem as myFile
import Utility.MahiUtility as Util
import UI.fileView as fileView
import API.api_calls as myApis
import UI.WebPage as webPage

class FileList(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Files")
        self.setGeometry(0, 0, 1220, 685)
        self.setStyleSheet("background-color: #F5F5F5")
        # self.label = QLabel(self)
        # self.label.setStyleSheet("background-color:#FEC32E")
        # self.label.setGeometry(0, 0, 1220, 39)

        if Util.isInternetOn():
            temp = myApis.fetchMedicalFileTypes()
            if(temp!=None):
                self.fileTypes = list(temp["response"])
            else:
                print("File types not available")
        else:
            print("Internet not available")

        self.UiComponents()
        #
        #     # showing all the widgets
        # self.show()
    #
    def UiComponents(self):

        self.SortAscending = True
        self.btnStyle = "border-radius : 10; background-color : #FAFAFA; color:#006CB5; font:bold; font-size:22px; text-align: center;"
        self.btnStyleselected = "border-radius : 10; background-color : #C4DBF0; color:#006CB5; font:bold; font-size:22px; text-align: center;"



        filterBtn = QComboBox(self)
        filterBtn.setStyleSheet("QComboBox {border-radius: 10; color: #00A0B5 }"
                                "QComboBox::drop-down { background:rgb(255,255,255,0);padding-right:20px}")
        filterBtn.setGeometry(600, 57, 300, 50)
        filterBtn.setGraphicsEffect(Util.getNeuShadow(0))
        self.comboBoxfileType = QComboBox(self)
        self.comboBoxfileType.setGeometry(600, 57, 300, 50)
        self.comboBoxfileType.setGraphicsEffect(Util.getNeuShadow(1))
        self.comboBoxfileType.setStyleSheet("QComboBox {border-radius: 10; color: #006CB5;padding-left:15px;font-size:22px; font:bold;  }"
                                      "QComboBox::drop-down { background:rgb(255,255,255,0);padding-right:20px}"
                                      "QComboBox::down-arrow{image: url(../Resources/downArrowDarkBlue.png)}")




        self.btnAscending= QPushButton("Ascending", self)
        self.btnAscending.setGeometry(925, 58, 250, 50)
        self.btnAscending.setStyleSheet(self.btnStyleselected)
        self.btnAscending.setGraphicsEffect(Util.getNeuShadow(0))
        self.btnAscending.clicked.connect(self.SortClicked)
        btn_back = QPushButton("", self)
        btn_back.setGeometry(41, 55, 135, 50)
        btn_back.setStyleSheet("border-radius : 10; background-color: #F5F5F5")
        btn_back.setIcon(QtGui.QIcon('..\Resources\\backButton.png'))
        btn_back.setIconSize(QtCore.QSize(155, 71))
        btn_back.clicked.connect(self.close)

        self.myQListWidget = QListWidget(self)
        self.myQListWidget.setStyleSheet("border:None;")
        self.myQListWidget.setGeometry(41, 140, 1138, 520)

        if len(self.fileTypes)>0:

            self.currentFileType = -1
            for fileType in self.fileTypes:
                if self.currentFileType == -1:
                    self.currentFileType = fileType["file_id"]
                self.comboBoxfileType.addItem(fileType["file_type"])

            self.comboBoxfileType.currentIndexChanged.connect(self.fileTypeChanged)

            self.fetchMedicalFilesAPI()

    def fileClicked(self,item):
        self.x = webPage.WebPage(self.fileList[item.row()]["file_url"])
        # self.x = webPage.WebPage("https://www.google.com/maps/search/?api=1&query=23.0384%2C72.5288")
        self.x.show()

    def fetchMedicalFilesAPI(self):
        if Util.isInternetOn():
            sort = "asc"
            if not self.SortAscending:
                sort = "desc"
            temp = myApis.fetchMedicalFiles(sort,self.currentFileType)

            if (temp != None):
                self.fileList= list(temp["response"])
                self.myQListWidget.clear()
                for file in self.fileList:
                    myQCustomQWidget = myFile.FileListItem()
                    myQCustomQWidget.setTextFileName(file["fileNote"])
                    myQCustomQWidget.setTextDateDoctor(file["medicalObservation"])
                    myQCustomQWidget.setExtension(file["file_extention"])
                    myQListWidgetItem = QListWidgetItem(self.myQListWidget)
                    myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())

                    self.myQListWidget.addItem(myQListWidgetItem)
                    self.myQListWidget.setItemWidget(myQListWidgetItem, myQCustomQWidget)

                # self.myQListWidget.set
                self.myQListWidget.clicked.connect(self.fileClicked)
            else:
                print("File types not available")
        else:
            print("Internet not available")


    def SortClicked(self):
        if self.SortAscending:
            self.SortAscending = False
            self.btnAscending.setText("Descending")
        else:
            self.SortAscending = True
            self.btnAscending.setText("Ascending")

        self.fetchMedicalFilesAPI()

    def fileTypeChanged(self,index):

        self.currentFileType = self.fileTypes[index]["file_id"]
        self.fetchMedicalFilesAPI()


if __name__ == '__main__':
    App = QApplication(sys.argv)

    # create the instance of our Window
    window = FileList()

    window.show()

    # start the app
    sys.exit(App.exec_())