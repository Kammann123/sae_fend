# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer\voicepanel.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VoicePanel(object):
    def setupUi(self, VoicePanel):
        VoicePanel.setObjectName("VoicePanel")
        VoicePanel.resize(94, 58)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VoicePanel.sizePolicy().hasHeightForWidth())
        VoicePanel.setSizePolicy(sizePolicy)
        VoicePanel.setMaximumSize(QtCore.QSize(600, 16777215))
        VoicePanel.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(VoicePanel)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon_widget = QtWidgets.QStackedWidget(VoicePanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_widget.sizePolicy().hasHeightForWidth())
        self.icon_widget.setSizePolicy(sizePolicy)
        self.icon_widget.setObjectName("icon_widget")
        self.record_page = QtWidgets.QWidget()
        self.record_page.setObjectName("record_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.record_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mic_button = QtWidgets.QPushButton(self.record_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.mic_button.sizePolicy().hasHeightForWidth())
        self.mic_button.setSizePolicy(sizePolicy)
        self.mic_button.setMinimumSize(QtCore.QSize(40, 40))
        self.mic_button.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.mic_button.setFont(font)
        self.mic_button.setStyleSheet("QPushButton::active {\n"
"    border-image: url(:/mic/assets/buttons/mic/photoshop/mic_normal.png) 0 0 0 0;\n"
"}\n"
"\n"
"QPushButton::closed {\n"
"    border-image: url(:/mic/assets/buttons/mic/photoshop/mic_normal.png) 0 0 0 0;\n"
"}\n"
"        \n"
"QPushButton::hover {\n"
"    border-image: url(:/mic/assets/buttons/mic/photoshop/mic_hover.png) 0 0 0 0;\n"
"}\n"
"        \n"
"QPushButton::checked {\n"
"    border-image: url(:/mic/assets/buttons/mic/photoshop/mic_pressed.png) 0 0 0 0;\n"
"}\n"
"        \n"
"QPushButton::disabled {\n"
"     border-image: url(:/mic/assets/buttons/mic/photoshop/mic_disabled.png) 0 0 0 0;\n"
"}")
        self.mic_button.setText("")
        self.mic_button.setCheckable(True)
        self.mic_button.setObjectName("mic_button")
        self.verticalLayout_2.addWidget(self.mic_button)
        self.icon_widget.addWidget(self.record_page)
        self.listen_page = QtWidgets.QWidget()
        self.listen_page.setObjectName("listen_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.listen_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.listen_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(40, 40))
        self.label.setMaximumSize(QtCore.QSize(40, 40))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/listening/assets/listening/photoshop/listening.png"))
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.icon_widget.addWidget(self.listen_page)
        self.horizontalLayout.addWidget(self.icon_widget)

        self.retranslateUi(VoicePanel)
        self.icon_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VoicePanel)

    def retranslateUi(self, VoicePanel):
        _translate = QtCore.QCoreApplication.translate
        VoicePanel.setWindowTitle(_translate("VoicePanel", "Form"))
from src.resources import buttons_rc
from src.resources import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VoicePanel = QtWidgets.QWidget()
    ui = Ui_VoicePanel()
    ui.setupUi(VoicePanel)
    VoicePanel.show()
    sys.exit(app.exec_())
