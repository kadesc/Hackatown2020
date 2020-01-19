# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deTRItus.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from image_recognition_api import makeImageRecognitionAPI, findInDatabase 
from PyQt5 import QtCore, QtGui, QtWidgets 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitreApp = QtWidgets.QLabel(self.centralwidget)
        self.lblTitreApp.setGeometry(QtCore.QRect(50, -10, 151, 91))
        
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(28)
        
        self.lblTitreApp.setFont(font)
        self.lblTitreApp.setObjectName("lblTitreApp")
        
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(130, 340, 56, 17))
        self.btnSearch.setObjectName("btnSearch")
        
        self.txtSearch = QtWidgets.QTextEdit(self.centralwidget)
        self.txtSearch.setGeometry(QtCore.QRect(20, 310, 291, 20))
        self.txtSearch.setObjectName("txtSearch")
        
        self.lblImg = QtWidgets.QLabel(self.centralwidget)
        self.lblImg.setGeometry(QtCore.QRect(30, 70, 291, 231))
        self.lblImg.setAutoFillBackground(True)
        self.lblImg.setText("")
        self.lblImg.setObjectName("lblImg")
       
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(360, 100, 211, 101))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.rd3 = QtWidgets.QRadioButton(self.frame)
        self.rd3.setGeometry(QtCore.QRect(60, 60, 62, 14))
        self.rd3.setText("")
        self.rd3.setObjectName("rd3")
        
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.rd3)
       
        self.rd2 = QtWidgets.QRadioButton(self.frame)
        self.rd2.setGeometry(QtCore.QRect(60, 40, 62, 14))
        self.rd2.setText("")
        self.rd2.setObjectName("rd2")
        
        self.buttonGroup.addButton(self.rd2)
       
        self.rd1 = QtWidgets.QRadioButton(self.frame)
        self.rd1.setGeometry(QtCore.QRect(60, 20, 62, 14))
        self.rd1.setText("")
        self.rd1.setObjectName("rd1")
       
        self.buttonGroup.addButton(self.rd1)
       
        self.lblNomItem = QtWidgets.QLabel(self.frame)
        self.lblNomItem.setGeometry(QtCore.QRect(10, 10, 35, 10))
        self.lblNomItem.setObjectName("lblNomItem")
       
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(360, 210, 211, 61))
        self.frame_2.setAutoFillBackground(True)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
       
        self.lblNomSac = QtWidgets.QLabel(self.frame_2)
        self.lblNomSac.setGeometry(QtCore.QRect(10, 0, 81, 16))
        self.lblNomSac.setObjectName("lblNomSac")
        
        self.lblTypeBac = QtWidgets.QLabel(self.frame_2)
        self.lblTypeBac.setGeometry(QtCore.QRect(70, 20, 51, 16))
        self.lblTypeBac.setObjectName("lblTypeBac")
       
        MainWindow.setCentralWidget(self.centralwidget)
       
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 18))
        self.menubar.setObjectName("menubar")
       
        MainWindow.setMenuBar(self.menubar)
       
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
       
        MainWindow.setStatusBar(self.statusbar)
       
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setText("")
        self.action.setObjectName("action")

        self.btnFileSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnFileSearch.setGeometry(QtCore.QRect(180, 340, 56, 17))
        self.btnFileSearch.setObjectName("btnFileSearch")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnSearch.clicked.connect(self.clickedBtnSearch)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTitreApp.setText(_translate("MainWindow", "deTRItus"))
        self.btnSearch.setText(_translate("MainWindow", "Search"))
        self.lblNomItem.setText(_translate("MainWindow", "Items: "))
        self.lblNomSac.setText(_translate("MainWindow", "Bac correspondant:"))
        self.lblTypeBac.setText(_translate("MainWindow", "Type de bac"))

    def clickedBtnSearch(self):
        txt = self.txtSearch.toPlainText()
        if txt [4:] == "http":
            tags = makeImageRecognitionAPI("remote", txt)
        else:
            tags = [txt]

        search_results = [["fruit","compost"],["bottle","recyclable"],["fruit","compost"]]
        #search_results = findInDatabase(['trash.txt','recyclable.txt','compost.txt','other.txt'], tags)
        
            self.rd1.setText(search_results[0][0])
            


    def clickedRdButton(self, radioButton, search_results):
        if (radioButton == self.rd1):
            self.lblTypeBac.setText(search_results[0][1])
        elif (radioButton == self.rd2):
            self.lblTypeBac.setText(search_results[1][1])
        elif (radioButton == self.rd3):
            self.lblTypeBac.setText(search_results[2][1])


    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
