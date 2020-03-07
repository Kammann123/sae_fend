# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\index.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Index(object):
    def setupUi(self, Index):
        Index.setObjectName("Index")
        Index.resize(500, 581)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Index.sizePolicy().hasHeightForWidth())
        Index.setSizePolicy(sizePolicy)
        Index.setMaximumSize(QtCore.QSize(500, 581))
        Index.setAutoFillBackground(False)
        Index.setStyleSheet("background-color: #6c7b95;\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Index)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(20)
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
        font = QtGui.QFont()
        font.setFamily("All the Way to the Sun")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.continue_button.setFont(font)
        self.continue_button.setAutoFillBackground(False)
        self.continue_button.setStyleSheet("QPushButton {\n"
"    font: 18pt \"All the Way to the Sun\";\n"
"    color: black;\n"
"    padding: 8;\n"
"    border-style: solid;\n"
"    border-width: 0;\n"
"    border-color: black;\n"
"    background-color: #142850;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    color: black;\n"
"    background-color: #27496d;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    color: black;\n"
"    background-color: #0c7b93;\n"
"}")
        self.continue_button.setFlat(True)
        self.continue_button.setObjectName("continue_button")
        self.verticalLayout.addWidget(self.continue_button, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Index)
        QtCore.QMetaObject.connectSlotsByName(Index)

    def retranslateUi(self, Index):
        _translate = QtCore.QCoreApplication.translate
        Index.setWindowTitle(_translate("Index", "Form"))
        self.continue_button.setText(_translate("Index", "CONTINUAR"))


from src.resources import index_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Index = QtWidgets.QWidget()
    ui = Ui_Index()
    ui.setupUi(Index)
    Index.show()
    sys.exit(app.exec_())
