# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'init_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InitWindow(object):
    def setupUi(self, InitWindow):
        InitWindow.setObjectName("InitWindow")
        InitWindow.resize(485, 317)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        InitWindow.setFont(font)
        self.title = QtWidgets.QLabel(InitWindow)
        self.title.setGeometry(QtCore.QRect(0, 30, 481, 41))
        self.title.setStyleSheet("")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.itbaLogo = QtWidgets.QLabel(InitWindow)
        self.itbaLogo.setGeometry(QtCore.QRect(30, 80, 201, 111))
        self.itbaLogo.setText("")
        self.itbaLogo.setPixmap(QtGui.QPixmap("X:/Users/Emilia/Downloads/logo_itba.png"))
        self.itbaLogo.setScaledContents(True)
        self.itbaLogo.setObjectName("itbaLogo")
        self.saeLogo = QtWidgets.QLabel(InitWindow)
        self.saeLogo.setGeometry(QtCore.QRect(290, 100, 141, 71))
        self.saeLogo.setText("")
        self.saeLogo.setPixmap(QtGui.QPixmap("X:/Users/Emilia/Desktop/ITBA/SAE/sae_logo_sf.png"))
        self.saeLogo.setScaledContents(True)
        self.saeLogo.setObjectName("saeLogo")
        self.redCar = QtWidgets.QLabel(InitWindow)
        self.redCar.setGeometry(QtCore.QRect(0, 230, 71, 31))
        self.redCar.setText("")
        self.redCar.setPixmap(QtGui.QPixmap("X:/Users/Emilia/Desktop/ITBA/SAE/red_car.png"))
        self.redCar.setScaledContents(True)
        self.redCar.setObjectName("redCar")

        self.retranslateUi(InitWindow)
        QtCore.QMetaObject.connectSlotsByName(InitWindow)

    def retranslateUi(self, InitWindow):
        _translate = QtCore.QCoreApplication.translate
        InitWindow.setWindowTitle(_translate("InitWindow", "Form"))
        self.title.setText(_translate("InitWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#0000ff;\">WELCOME TO ITBA FORMULA SAE</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InitWindow = QtWidgets.QWidget()
    ui = Ui_InitWindow()
    ui.setupUi(InitWindow)
    InitWindow.show()
    sys.exit(app.exec_())

