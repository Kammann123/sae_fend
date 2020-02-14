# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/voicepanel.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VoicePanel(object):
    def setupUi(self, VoicePanel):
        VoicePanel.setObjectName("VoicePanel")
        VoicePanel.resize(560, 40)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VoicePanel.sizePolicy().hasHeightForWidth())
        VoicePanel.setSizePolicy(sizePolicy)
        VoicePanel.setMaximumSize(QtCore.QSize(600, 16777215))
        VoicePanel.setStyleSheet("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(VoicePanel)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mic_button = QtWidgets.QPushButton(VoicePanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.mic_button.sizePolicy().hasHeightForWidth())
        self.mic_button.setSizePolicy(sizePolicy)
        self.mic_button.setMinimumSize(QtCore.QSize(40, 40))
        self.mic_button.setMaximumSize(QtCore.QSize(40, 40))
        self.mic_button.setStyleSheet("QPushButton::active {\n"
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
        self.horizontalLayout.addWidget(self.mic_button)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.status_label = QtWidgets.QLabel(VoicePanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.status_label.sizePolicy().hasHeightForWidth())
        self.status_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("The Bold Font")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.status_label.setFont(font)
        self.status_label.setMouseTracking(True)
        self.status_label.setTabletTracking(True)
        self.status_label.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.status_label.setAcceptDrops(False)
        self.status_label.setWordWrap(False)
        self.status_label.setObjectName("status_label")
        self.verticalLayout.addWidget(self.status_label, 0, QtCore.Qt.AlignLeft)
        self.volume_bar = QtWidgets.QProgressBar(VoicePanel)
        self.volume_bar.setMaximumSize(QtCore.QSize(16777215, 15))
        self.volume_bar.setStyleSheet("QProgressBar::chunk {\n"
"    width: 5px;\n"
"    margin: 0.5px;\n"
"    background-color: rgb(255, 115, 117);\n"
"}\n"
"\n"
"QProgressBar {\n"
"    background-color: rgb(135, 135, 135, 100);\n"
"    border-color:  rgb(135, 135, 135, 100);\n"
"}")
        self.volume_bar.setProperty("value", 0)
        self.volume_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.volume_bar.setTextVisible(False)
        self.volume_bar.setOrientation(QtCore.Qt.Horizontal)
        self.volume_bar.setInvertedAppearance(False)
        self.volume_bar.setObjectName("volume_bar")
        self.verticalLayout.addWidget(self.volume_bar)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(VoicePanel)
        QtCore.QMetaObject.connectSlotsByName(VoicePanel)

    def retranslateUi(self, VoicePanel):
        _translate = QtCore.QCoreApplication.translate
        VoicePanel.setWindowTitle(_translate("VoicePanel", "Form"))
        self.status_label.setText(_translate("VoicePanel", "TRANSMITIENDO..."))
        self.volume_bar.setFormat(_translate("VoicePanel", "%p%"))
from src.resources import buttons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VoicePanel = QtWidgets.QWidget()
    ui = Ui_VoicePanel()
    ui.setupUi(VoicePanel)
    VoicePanel.show()
    sys.exit(app.exec_())
