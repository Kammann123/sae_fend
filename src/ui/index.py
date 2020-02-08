# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/index.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Index(object):
    def setupUi(self, Index):
        Index.setObjectName("Index")
        Index.resize(668, 576)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Index.sizePolicy().hasHeightForWidth())
        Index.setSizePolicy(sizePolicy)
        Index.setAutoFillBackground(False)
        Index.setStyleSheet("background-color: rgb(123, 46, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Index)
        self.verticalLayout.setObjectName("verticalLayout")
        self.welcome_message = QtWidgets.QLabel(Index)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome_message.sizePolicy().hasHeightForWidth())
        self.welcome_message.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(28)
        self.welcome_message.setFont(font)
        self.welcome_message.setAutoFillBackground(False)
        self.welcome_message.setText("")
        self.welcome_message.setPixmap(QtGui.QPixmap(":/logo/assets/logo/logo.png"))
        self.welcome_message.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_message.setWordWrap(True)
        self.welcome_message.setObjectName("welcome_message")
        self.verticalLayout.addWidget(self.welcome_message)
        self.continue_button = QtWidgets.QPushButton(Index)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.continue_button.sizePolicy().hasHeightForWidth())
        self.continue_button.setSizePolicy(sizePolicy)
        self.continue_button.setAutoFillBackground(False)
        self.continue_button.setStyleSheet("QPushButton {\n"
"    font: 18pt \"All the Way to the Sun\";\n"
"    padding: 8;\n"
"    border-style: solid;\n"
"    border-width: 1;\n"
"    border-color: black;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.250552 rgba(67, 0, 125, 255), stop:1 rgba(68, 0, 158, 255));\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color:qlineargradient(spread:repeat, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(39, 0, 97, 255));\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgba(67, 0, 125, 255);\n"
"}")
        self.continue_button.setObjectName("continue_button")
        self.verticalLayout.addWidget(self.continue_button, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Index)
        QtCore.QMetaObject.connectSlotsByName(Index)

    def retranslateUi(self, Index):
        _translate = QtCore.QCoreApplication.translate
        Index.setWindowTitle(_translate("Index", "Form"))
        self.continue_button.setText(_translate("Index", "CONTINUAR"))
from src.resources import index


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Index = QtWidgets.QWidget()
    ui = Ui_Index()
    ui.setupUi(Index)
    Index.show()
    sys.exit(app.exec_())
