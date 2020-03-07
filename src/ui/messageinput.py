# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\messageinput.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MessageInput(object):
    def setupUi(self, MessageInput):
        MessageInput.setObjectName("MessageInput")
        MessageInput.resize(587, 70)
        MessageInput.setFocusPolicy(QtCore.Qt.ClickFocus)
        MessageInput.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(MessageInput)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.message = QtWidgets.QTextEdit(MessageInput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setMinimumSize(QtCore.QSize(100, 0))
        self.message.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.message.setFont(font)
        self.message.setStyleSheet("QTextEdit {\n"
"    background: rgba(255, 255, 255, 255);\n"
"    border-radius: 12px;\n"
"    text-align: center;\n"
"    padding: 3px;\n"
"}")
        self.message.setTabChangesFocus(True)
        self.message.setObjectName("message")
        self.horizontalLayout.addWidget(self.message)
        self.send_button = QtWidgets.QPushButton(MessageInput)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_button.sizePolicy().hasHeightForWidth())
        self.send_button.setSizePolicy(sizePolicy)
        self.send_button.setMinimumSize(QtCore.QSize(35, 35))
        self.send_button.setStyleSheet(":active {\n"
"    border-image:url(:/message_v3/assets/buttons/messages/v3/mic_normal.png) 0 0 0 0;\n"
"}\n"
"\n"
":closed {\n"
"    border-image: url(:/message_v3/assets/buttons/messages/v3/mic_normal.png) 0 0 0 0;\n"
"}\n"
"        \n"
":hover {\n"
"    border-image: url(:/message_v3/assets/buttons/messages/v3/mic_hover.png) 0 0 0 0;\n"
"}\n"
"        \n"
":pressed {\n"
"    border-image: url(:/message_v3/assets/buttons/messages/v3/mic_pressed.png) 0 0 0 0;\n"
"}\n"
"")
        self.send_button.setText("")
        self.send_button.setCheckable(False)
        self.send_button.setFlat(True)
        self.send_button.setObjectName("send_button")
        self.horizontalLayout.addWidget(self.send_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MessageInput)
        QtCore.QMetaObject.connectSlotsByName(MessageInput)

    def retranslateUi(self, MessageInput):
        _translate = QtCore.QCoreApplication.translate
        MessageInput.setWindowTitle(_translate("MessageInput", "Form"))
        self.message.setHtml(_translate("MessageInput", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\';\"><br /></p></body></html>"))
        self.message.setPlaceholderText(_translate("MessageInput", "Escribe un mensaje..."))


from src.resources import buttons_rc
from src.resources import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MessageInput = QtWidgets.QWidget()
    ui = Ui_MessageInput()
    ui.setupUi(MessageInput)
    MessageInput.show()
    sys.exit(app.exec_())
