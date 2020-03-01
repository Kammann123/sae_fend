# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\messages.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Messages(object):
    def setupUi(self, Messages):
        Messages.setObjectName("Messages")
        Messages.resize(307, 145)
        Messages.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Messages)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(Messages)
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.old_messages = QtWidgets.QWidget()
        self.old_messages.setGeometry(QtCore.QRect(0, 0, 289, 69))
        self.old_messages.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.old_messages.setObjectName("old_messages")
        self.messeges_layout = QtWidgets.QVBoxLayout(self.old_messages)
        self.messeges_layout.setObjectName("messeges_layout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.messeges_layout.addItem(spacerItem)
        self.sample = QtWidgets.QPushButton(self.old_messages)
        self.sample.setStyleSheet("")
        self.sample.setObjectName("sample")
        self.messeges_layout.addWidget(self.sample)
        self.scrollArea_2.setWidget(self.old_messages)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.message = QtWidgets.QTextEdit(Messages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setMaximumSize(QtCore.QSize(16777215, 50))
        self.message.setStyleSheet("")
        self.message.setObjectName("message")
        self.horizontalLayout.addWidget(self.message)
        self.send_button = QtWidgets.QPushButton(Messages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_button.sizePolicy().hasHeightForWidth())
        self.send_button.setSizePolicy(sizePolicy)
        self.send_button.setMinimumSize(QtCore.QSize(25, 25))
        self.send_button.setStyleSheet("QPushButton::active {\n"
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
        self.send_button.setText("")
        self.send_button.setObjectName("send_button")
        self.horizontalLayout.addWidget(self.send_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Messages)
        QtCore.QMetaObject.connectSlotsByName(Messages)

    def retranslateUi(self, Messages):
        _translate = QtCore.QCoreApplication.translate
        Messages.setWindowTitle(_translate("Messages", "Form"))
        self.sample.setText(_translate("Messages", "PushButton"))
from src.resources import buttons_rc
from src.resources import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Messages = QtWidgets.QWidget()
    ui = Ui_Messages()
    ui.setupUi(Messages)
    Messages.show()
    sys.exit(app.exec_())
