# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\sdmessageinput.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SdMessage(object):
    def setupUi(self, SdMessage):
        SdMessage.setObjectName("SdMessage")
        SdMessage.resize(94, 35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SdMessage.sizePolicy().hasHeightForWidth())
        SdMessage.setSizePolicy(sizePolicy)
        SdMessage.setMinimumSize(QtCore.QSize(35, 35))
        SdMessage.setMaximumSize(QtCore.QSize(94, 35))
        self.verticalLayout = QtWidgets.QVBoxLayout(SdMessage)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sd_button = QtWidgets.QToolButton(SdMessage)
        self.sd_button.setMinimumSize(QtCore.QSize(35, 35))
        self.sd_button.setStyleSheet(":active {\n"
"    border-image: url(:/sd/assets/buttons/sd/photoshop/sd_normal.png);\n"
"}\n"
"\n"
":closed {\n"
"    border-image: url(:/sd/assets/buttons/sd/photoshop/sd_normal.png);\n"
"}\n"
"\n"
":hover {\n"
"    border-image: url(:/sd/assets/buttons/sd/photoshop/sd_hover.png);\n"
"}\n"
"\n"
":pressed {\n"
"    border-image: url(:/sd/assets/buttons/sd/photoshop/sd_pressed.png);\n"
"}")
        self.sd_button.setText("")
        self.sd_button.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.sd_button.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.sd_button.setAutoRaise(False)
        self.sd_button.setArrowType(QtCore.Qt.NoArrow)
        self.sd_button.setObjectName("sd_button")
        self.verticalLayout.addWidget(self.sd_button, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.retranslateUi(SdMessage)
        QtCore.QMetaObject.connectSlotsByName(SdMessage)

    def retranslateUi(self, SdMessage):
        _translate = QtCore.QCoreApplication.translate
        SdMessage.setWindowTitle(_translate("SdMessage", "Form"))
from src.resources import buttons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SdMessage = QtWidgets.QWidget()
    ui = Ui_SdMessage()
    ui.setupUi(SdMessage)
    SdMessage.show()
    sys.exit(app.exec_())
