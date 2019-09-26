# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CinemaUI(object):
    def setupUi(self, CinemaUI):
        CinemaUI.setObjectName("CinemaUI")
        CinemaUI.resize(1011, 583)
        self.verticalLayoutWidget = QtWidgets.QWidget(CinemaUI)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(860, 20, 121, 120))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.showCameraButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.showCameraButton.setObjectName("showCameraButton")
        self.verticalLayout.addWidget(self.showCameraButton)
        self.faceReidButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.faceReidButton.setObjectName("faceReidButton")
        self.verticalLayout.addWidget(self.faceReidButton)
        self.inCinemaButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.inCinemaButton.setObjectName("inCinemaButton")
        self.verticalLayout.addWidget(self.inCinemaButton)
        self.exitButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        self.graphicsView = QtWidgets.QGraphicsView(CinemaUI)
        self.graphicsView.setGeometry(QtCore.QRect(30, 30, 811, 521))
        self.graphicsView.setMouseTracking(False)
        self.graphicsView.setAcceptDrops(True)
        self.graphicsView.setObjectName("graphicsView")

        self.retranslateUi(CinemaUI)
        QtCore.QMetaObject.connectSlotsByName(CinemaUI)

    def retranslateUi(self, CinemaUI):
        _translate = QtCore.QCoreApplication.translate
        CinemaUI.setWindowTitle(_translate("CinemaUI", "Dialog"))
        self.showCameraButton.setText(_translate("CinemaUI", "Show Camera"))
        self.faceReidButton.setText(_translate("CinemaUI", "Face Reid"))
        self.inCinemaButton.setText(_translate("CinemaUI", "In Cinema"))
        self.exitButton.setText(_translate("CinemaUI", "Exit"))

