# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messages.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Messages(object):
    def setupUi(self, Messages):
        Messages.setObjectName("Messages")
        Messages.resize(309, 195)
        Messages.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Messages)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(Messages)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.oldMessages = QtWidgets.QWidget()
        self.oldMessages.setGeometry(QtCore.QRect(0, 0, 289, 117))
        self.oldMessages.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.oldMessages.setObjectName("oldMessages")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.oldMessages)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea_2.setWidget(self.oldMessages)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Message = QtWidgets.QTextEdit(Messages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Message.sizePolicy().hasHeightForWidth())
        self.Message.setSizePolicy(sizePolicy)
        self.Message.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Message.setStyleSheet("border-width: 2px;\n"
"background-color: rgba(255, 255, 255, 200);\n"
"border-color: darkkhaki;\n"
"border-style: solid;\n"
"border-radius: 5;\n"
"padding: 3px;\n"
"")
        self.Message.setObjectName("Message")
        self.horizontalLayout.addWidget(self.Message)
        self.sendButton = QtWidgets.QPushButton(Messages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendButton.sizePolicy().hasHeightForWidth())
        self.sendButton.setSizePolicy(sizePolicy)
        self.sendButton.setMinimumSize(QtCore.QSize(25, 25))
        self.sendButton.setStyleSheet("QPushButton::active {\n"
"    border-image: url(:message/assets/buttons/messages/send_normal.png) 0 0 0 0;\n"
"}\n"
"        \n"
"QPushButton::hover {\n"
"    border-image: url(:message/assets/buttons/messages/send_hover.png) 0 0 0 0;\n"
"}\n"
"        \n"
"QPushButton::checked {\n"
"    border-image: url(::message/assets/buttons/messages/send_press.png) 0 0 0 0;\n"
"}\n"
"")
        self.sendButton.setText("")
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Messages)
        QtCore.QMetaObject.connectSlotsByName(Messages)

    def retranslateUi(self, Messages):
        _translate = QtCore.QCoreApplication.translate
        Messages.setWindowTitle(_translate("Messages", "Form"))


import buttons_rc
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Messages = QtWidgets.QWidget()
    ui = Ui_Messages()
    ui.setupUi(Messages)
    Messages.show()
    sys.exit(app.exec_())
