# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\navbar.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NavBar(object):
    def setupUi(self, NavBar):
        NavBar.setObjectName("NavBar")
        NavBar.resize(600, 36)
        NavBar.setStyleSheet("background-color: #6c7b95;\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(NavBar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(NavBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sound = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sound.sizePolicy().hasHeightForWidth())
        self.sound.setSizePolicy(sizePolicy)
        self.sound.setMaximumSize(QtCore.QSize(16777215, 25))
        self.sound.setStyleSheet("QPushButton {\n"
"    font: 8pt \"All the Way to the Sun\";\n"
"    color: white;\n"
"    padding: 8;\n"
"    border-style: solid;\n"
"    background-color: #6c7b95;\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    color: white;\n"
"    background-color: rgb(81, 76, 149);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    color: white;\n"
"    background-color: rgb(37, 33, 98);\n"
"}\n"
"")
        self.sound.setObjectName("sound")
        self.horizontalLayout_2.addWidget(self.sound)
        self.mic = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mic.sizePolicy().hasHeightForWidth())
        self.mic.setSizePolicy(sizePolicy)
        self.mic.setMaximumSize(QtCore.QSize(16777215, 25))
        self.mic.setStyleSheet("QPushButton {\n"
"    font: 8pt \"All the Way to the Sun\";\n"
"    color: white;\n"
"    padding: 8;\n"
"    border-style: solid;\n"
"    background-color: #6c7b95;\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    color: white;\n"
"    background-color: rgb(81, 76, 149);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    color: white;\n"
"    background-color: rgb(37, 33, 98);\n"
"}\n"
"")
        self.mic.setObjectName("mic")
        self.horizontalLayout_2.addWidget(self.mic)
        self.usb = QtWidgets.QPushButton(self.frame)
        self.usb.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.usb.sizePolicy().hasHeightForWidth())
        self.usb.setSizePolicy(sizePolicy)
        self.usb.setMaximumSize(QtCore.QSize(16777215, 25))
        self.usb.setStyleSheet("QPushButton {\n"
"    font: 8pt \"All the Way to the Sun\";\n"
"    color: white;\n"
"    padding: 8;\n"
"    border-style: solid;\n"
"    background-color: #6c7b95;\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    color: white;\n"
"    background-color: rgb(81, 76, 149);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    color: white;\n"
"    background-color: rgb(37, 33, 98);\n"
"}\n"
"")
        self.usb.setObjectName("usb")
        self.horizontalLayout_2.addWidget(self.usb)
        spacerItem = QtWidgets.QSpacerItem(368, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(20, 30))
        self.label.setMaximumSize(QtCore.QSize(30, 30))
        self.label.setBaseSize(QtCore.QSize(50, 50))
        self.label.setStyleSheet("border-width: 0;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/logo/assets/logo/logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(NavBar)
        QtCore.QMetaObject.connectSlotsByName(NavBar)

    def retranslateUi(self, NavBar):
        _translate = QtCore.QCoreApplication.translate
        NavBar.setWindowTitle(_translate("NavBar", "Form"))
        self.sound.setText(_translate("NavBar", "Sound"))
        self.mic.setText(_translate("NavBar", "Microphone"))
        self.usb.setText(_translate("NavBar", "Serial Port"))


from src.resources import index_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NavBar = QtWidgets.QWidget()
    ui = Ui_NavBar()
    ui.setupUi(NavBar)
    NavBar.show()
    sys.exit(app.exec_())
