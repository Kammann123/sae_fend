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
        Messages.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Messages)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Messages)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.messages_box = QtWidgets.QVBoxLayout()
        self.messages_box.setContentsMargins(-1, -1, -1, 0)
        self.messages_box.setSpacing(0)
        self.messages_box.setObjectName("messages_box")
        self.verticalLayout_3.addLayout(self.messages_box)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Messages)
        QtCore.QMetaObject.connectSlotsByName(Messages)

    def retranslateUi(self, Messages):
        _translate = QtCore.QCoreApplication.translate
        Messages.setWindowTitle(_translate("Messages", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Messages = QtWidgets.QWidget()
    ui = Ui_Messages()
    ui.setupUi(Messages)
    Messages.show()
    sys.exit(app.exec_())
