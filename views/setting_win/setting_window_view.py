# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingWindow(object):
    def setupUi(self, SettingWindow):
        SettingWindow.setObjectName("SettingWindow")
        SettingWindow.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingWindow.sizePolicy().hasHeightForWidth())
        SettingWindow.setSizePolicy(sizePolicy)
        SettingWindow.setWindowOpacity(1.0)
        self.finishButton = QtWidgets.QPushButton(SettingWindow)
        self.finishButton.setGeometry(QtCore.QRect(284, 242, 75, 23))
        self.finishButton.setObjectName("finishButton")
        self.layoutWidget = QtWidgets.QWidget(SettingWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 50, 211, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.portLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.portLayout.setContentsMargins(0, 0, 0, 0)
        self.portLayout.setObjectName("portLayout")
        self.port = QtWidgets.QLabel(self.layoutWidget)
        self.port.setObjectName("port")
        self.portLayout.addWidget(self.port)
        self.portBox = QtWidgets.QComboBox(self.layoutWidget)
        self.portBox.setObjectName("portBox")
        self.portBox.addItem("")
        self.portLayout.addWidget(self.portBox)
        self.layoutWidget1 = QtWidgets.QWidget(SettingWindow)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 100, 211, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.speedLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.speedLayout.setContentsMargins(0, 0, 0, 0)
        self.speedLayout.setObjectName("speedLayout")
        self.speed = QtWidgets.QLabel(self.layoutWidget1)
        self.speed.setObjectName("speed")
        self.speedLayout.addWidget(self.speed)
        self.speedBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.speedBox.setObjectName("speedBox")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedBox.addItem("")
        self.speedLayout.addWidget(self.speedBox)
        self.layoutWidget2 = QtWidgets.QWidget(SettingWindow)
        self.layoutWidget2.setGeometry(QtCore.QRect(80, 150, 211, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.parity = QtWidgets.QLabel(self.layoutWidget2)
        self.parity.setObjectName("parity")
        self.horizontalLayout_3.addWidget(self.parity)
        self.parityBox = QtWidgets.QComboBox(self.layoutWidget2)
        self.parityBox.setObjectName("parityBox")
        self.parityBox.addItem("")
        self.parityBox.addItem("")
        self.parityBox.addItem("")
        self.horizontalLayout_3.addWidget(self.parityBox)

        self.retranslateUi(SettingWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingWindow)

    def retranslateUi(self, SettingWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingWindow.setWindowTitle(_translate("SettingWindow", "Configuration"))
        self.finishButton.setText(_translate("SettingWindow", "Finish"))
        self.port.setText(_translate("SettingWindow", "Select port"))
        self.portBox.setItemText(0, _translate("SettingWindow", "Offline"))
        self.speed.setText(_translate("SettingWindow", "Bits/second"))
        self.speedBox.setItemText(0, _translate("SettingWindow", "9600"))
        self.speedBox.setItemText(1, _translate("SettingWindow", "75"))
        self.speedBox.setItemText(2, _translate("SettingWindow", "110"))
        self.speedBox.setItemText(3, _translate("SettingWindow", "134"))
        self.speedBox.setItemText(4, _translate("SettingWindow", "150"))
        self.speedBox.setItemText(5, _translate("SettingWindow", "300"))
        self.speedBox.setItemText(6, _translate("SettingWindow", "600"))
        self.speedBox.setItemText(7, _translate("SettingWindow", "1200"))
        self.speedBox.setItemText(8, _translate("SettingWindow", "1800"))
        self.speedBox.setItemText(9, _translate("SettingWindow", "2400"))
        self.speedBox.setItemText(10, _translate("SettingWindow", "4800"))
        self.speedBox.setItemText(11, _translate("SettingWindow", "7200"))
        self.speedBox.setItemText(12, _translate("SettingWindow", "14400"))
        self.speedBox.setItemText(13, _translate("SettingWindow", "19200"))
        self.speedBox.setItemText(14, _translate("SettingWindow", "38400"))
        self.speedBox.setItemText(15, _translate("SettingWindow", "57600"))
        self.speedBox.setItemText(16, _translate("SettingWindow", "115200"))
        self.speedBox.setItemText(17, _translate("SettingWindow", "128000"))
        self.parity.setText(_translate("SettingWindow", "Parity"))
        self.parityBox.setItemText(0, _translate("SettingWindow", "Even"))
        self.parityBox.setItemText(1, _translate("SettingWindow", "Odd"))
        self.parityBox.setItemText(2, _translate("SettingWindow", "Nothing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingWindow = QtWidgets.QDialog()
    ui = Ui_SettingWindow()
    ui.setupUi(SettingWindow)
    SettingWindow.show()
    sys.exit(app.exec_())
