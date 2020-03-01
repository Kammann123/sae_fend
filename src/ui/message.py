# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\message.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Message(object):
    def setupUi(self, Message):
        Message.setObjectName("Message")
        Message.resize(530, 52)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Message.sizePolicy().hasHeightForWidth())
        Message.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setStrikeOut(False)
        Message.setFont(font)
        Message.setMouseTracking(True)
        Message.setStyleSheet(":hover{\n"
"    \n"
"    background-color: rgb(218, 218, 218);\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Message)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.time_label = QtWidgets.QLabel(Message)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_label.sizePolicy().hasHeightForWidth())
        self.time_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("")
        self.time_label.setObjectName("time_label")
        self.horizontalLayout.addWidget(self.time_label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.message_label = QtWidgets.QLabel(Message)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_label.sizePolicy().hasHeightForWidth())
        self.message_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.message_label.setFont(font)
        self.message_label.setStyleSheet("QLabel {\n"
"    border: 2pxn;\n"
"    background: rgb(96, 115, 202);\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"}")
        self.message_label.setWordWrap(True)
        self.message_label.setObjectName("message_label")
        self.horizontalLayout.addWidget(self.message_label, 0, QtCore.Qt.AlignRight)

        self.retranslateUi(Message)
        QtCore.QMetaObject.connectSlotsByName(Message)

    def retranslateUi(self, Message):
        _translate = QtCore.QCoreApplication.translate
        Message.setWindowTitle(_translate("Message", "Form"))
        self.time_label.setText(_translate("Message", "11:00"))
        self.message_label.setText(_translate("Message", "Este es un mensaje predeterminado para probar el componente de mensaje."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Message = QtWidgets.QWidget()
    ui = Ui_Message()
    ui.setupUi(Message)
    Message.show()
    sys.exit(app.exec_())
