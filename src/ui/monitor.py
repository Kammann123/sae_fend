# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/monitor.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Monitor(object):
    def setupUi(self, Monitor):
        Monitor.setObjectName("Monitor")
        Monitor.resize(1610, 561)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Monitor.sizePolicy().hasHeightForWidth())
        Monitor.setSizePolicy(sizePolicy)
        Monitor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Monitor.setStyleSheet("QWidget {\n"
"    background-color: #6c7b95;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    contentMargins: 0px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Monitor)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalFrame = QtWidgets.QFrame(Monitor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setStyleSheet("background-color: #464159;")
        self.verticalFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.verticalFrame.setObjectName("verticalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalFrame)
        self.horizontalLayout.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("The Bold Font")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #f5eaea;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.voice_panel = VoicePanel(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voice_panel.sizePolicy().hasHeightForWidth())
        self.voice_panel.setSizePolicy(sizePolicy)
        self.voice_panel.setMinimumSize(QtCore.QSize(500, 0))
        self.voice_panel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.voice_panel.setObjectName("voice_panel")
        self.horizontalLayout.addWidget(self.voice_panel, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.verticalFrame)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_5 = QtWidgets.QFrame(Monitor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("background-color: #8bbabb;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(1)
        self.frame_5.setMidLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.slider_0 = Slider(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_0.sizePolicy().hasHeightForWidth())
        self.slider_0.setSizePolicy(sizePolicy)
        self.slider_0.setObjectName("slider_0")
        self.verticalLayout_7.addWidget(self.slider_0)
        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(Monitor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet("background-color: #8bbabb;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setLineWidth(1)
        self.frame_6.setMidLineWidth(0)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.slider_2 = Slider(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_2.sizePolicy().hasHeightForWidth())
        self.slider_2.setSizePolicy(sizePolicy)
        self.slider_2.setObjectName("slider_2")
        self.verticalLayout_8.addWidget(self.slider_2)
        self.gridLayout.addWidget(self.frame_6, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(Monitor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: #8bbabb;")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.panel = Panel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panel.sizePolicy().hasHeightForWidth())
        self.panel.setSizePolicy(sizePolicy)
        self.panel.setMaximumSize(QtCore.QSize(1000, 354))
        self.panel.setStyleSheet("")
        self.panel.setObjectName("panel")
        self.verticalLayout_2.addWidget(self.panel, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frame, 1, 1, 2, 2)
        self.frame_4 = QtWidgets.QFrame(Monitor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet("background-color: #8bbabb;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(1)
        self.frame_4.setMidLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.slider_3 = Slider(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_3.sizePolicy().hasHeightForWidth())
        self.slider_3.setSizePolicy(sizePolicy)
        self.slider_3.setObjectName("slider_3")
        self.verticalLayout_5.addWidget(self.slider_3)
        self.gridLayout.addWidget(self.frame_4, 0, 2, 1, 1)
        self.frame_3 = QtWidgets.QFrame(Monitor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("background-color: #8bbabb;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.slider_1 = Slider(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_1.sizePolicy().hasHeightForWidth())
        self.slider_1.setSizePolicy(sizePolicy)
        self.slider_1.setObjectName("slider_1")
        self.verticalLayout_4.addWidget(self.slider_1)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Monitor)
        QtCore.QMetaObject.connectSlotsByName(Monitor)

    def retranslateUi(self, Monitor):
        _translate = QtCore.QCoreApplication.translate
        Monitor.setWindowTitle(_translate("Monitor", "Form"))
        self.label.setText(_translate("Monitor", "SAE Monitor"))
        self.voice_panel.setToolTip(_translate("Monitor", "Click and drag here"))
        self.voice_panel.setWhatsThis(_translate("Monitor", "Voice Panel Widget.  "))
        self.slider_0.setToolTip(_translate("Monitor", "Click and drag here"))
        self.slider_0.setWhatsThis(_translate("Monitor", "Slider Widget.  "))
        self.slider_2.setToolTip(_translate("Monitor", "Click and drag here"))
        self.slider_2.setWhatsThis(_translate("Monitor", "Slider Widget.  "))
        self.panel.setToolTip(_translate("Monitor", "Click and drag here"))
        self.panel.setWhatsThis(_translate("Monitor", "Panel Widget.  "))
        self.slider_3.setToolTip(_translate("Monitor", "Click and drag here"))
        self.slider_3.setWhatsThis(_translate("Monitor", "Slider Widget.  "))
        self.slider_1.setToolTip(_translate("Monitor", "Click and drag here"))
        self.slider_1.setWhatsThis(_translate("Monitor", "Slider Widget.  "))
from src.panel import Panel
from src.slider import Slider
from src.voicepanel import VoicePanel


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Monitor = QtWidgets.QWidget()
    ui = Ui_Monitor()
    ui.setupUi(Monitor)
    Monitor.show()
    sys.exit(app.exec_())
