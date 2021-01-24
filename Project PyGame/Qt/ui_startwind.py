# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StartWind.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(221, 221, 221);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 150, 291, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.startButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(28)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("background-color: rgb(159, 101, 6);\n"
"border-radius: 10px;\n"
"text-shadow: 100px 500px 600px #66cc99;")
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.settingsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.settingsButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(28)
        self.settingsButton.setFont(font)
        self.settingsButton.setStyleSheet("background-color: rgb(159, 101, 6);\n"
"border-radius: 10px;\n"
"text-shadow: 100px 500px 600px #66cc99;")
        self.settingsButton.setObjectName("settingsButton")
        self.verticalLayout.addWidget(self.settingsButton)
        self.quitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.quitButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(28)
        self.quitButton.setFont(font)
        self.quitButton.setStyleSheet("background-color: rgb(159, 101, 6);\n"
"border-radius: 10px;\n"
"text-shadow: 100px 500px 600px #66cc99;")
        self.quitButton.setObjectName("quitButton")
        self.verticalLayout.addWidget(self.quitButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Super Kolobok Bros"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.settingsButton.setText(_translate("MainWindow", "Settings"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))
