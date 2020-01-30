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
        Index.resize(393, 143)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Index.sizePolicy().hasHeightForWidth())
        Index.setSizePolicy(sizePolicy)
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
        self.continue_button.setObjectName("continue_button")
        self.verticalLayout.addWidget(self.continue_button, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Index)
        QtCore.QMetaObject.connectSlotsByName(Index)

    def retranslateUi(self, Index):
        _translate = QtCore.QCoreApplication.translate
        Index.setWindowTitle(_translate("Index", "Form"))
        self.welcome_message.setText(_translate("Index", "¡Welcome to SAEFend!"))
        self.continue_button.setText(_translate("Index", "Continuar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Index = QtWidgets.QWidget()
    ui = Ui_Index()
    ui.setupUi(Index)
    Index.show()
    sys.exit(app.exec_())
