# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\messages.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Messages(object):
    def setupUi(self, Messages):
        Messages.setObjectName("Messages")
        Messages.resize(400, 383)
        self.verticalLayout = QtWidgets.QVBoxLayout(Messages)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(Messages)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 400, 383))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.message_box = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.message_box.setAutoFillBackground(True)
        self.message_box.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);\n"
"border: 0px;")
        self.message_box.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.message_box.setDragEnabled(False)
        self.message_box.setAlternatingRowColors(False)
        self.message_box.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.message_box.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.message_box.setObjectName("message_box")
        self.verticalLayout_3.addWidget(self.message_box)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Messages)
        self.message_box.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Messages)

    def retranslateUi(self, Messages):
        _translate = QtCore.QCoreApplication.translate
        Messages.setWindowTitle(_translate("Messages", "Form"))
        self.message_box.setSortingEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Messages = QtWidgets.QWidget()
    ui = Ui_Messages()
    ui.setupUi(Messages)
    Messages.show()
    sys.exit(app.exec_())
