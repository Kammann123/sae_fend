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
        Monitor.resize(986, 682)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Monitor.sizePolicy().hasHeightForWidth())
        Monitor.setSizePolicy(sizePolicy)
        Monitor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Monitor.setStyleSheet("background-color: rgb(153, 153, 153);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Monitor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(Monitor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(1)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.slider_left = Slider(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_left.sizePolicy().hasHeightForWidth())
        self.slider_left.setSizePolicy(sizePolicy)
        self.slider_left.setObjectName("slider_left")
        self.verticalLayout_4.addWidget(self.slider_left)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(Monitor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(1)
        self.frame_4.setMidLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.slider_middle = Slider(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_middle.sizePolicy().hasHeightForWidth())
        self.slider_middle.setSizePolicy(sizePolicy)
        self.slider_middle.setObjectName("slider_middle")
        self.verticalLayout_5.addWidget(self.slider_middle)
        self.horizontalLayout_2.addWidget(self.frame_4)
        self.frame_2 = QtWidgets.QFrame(Monitor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.slider_right = Slider(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_right.sizePolicy().hasHeightForWidth())
        self.slider_right.setSizePolicy(sizePolicy)
        self.slider_right.setObjectName("slider_right")
        self.verticalLayout_3.addWidget(self.slider_right)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.frame = QtWidgets.QFrame(Monitor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
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
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Monitor)
        QtCore.QMetaObject.connectSlotsByName(Monitor)

    def retranslateUi(self, Monitor):
        _translate = QtCore.QCoreApplication.translate
        Monitor.setWindowTitle(_translate("Monitor", "Form"))
        self.slider_left.setToolTip(_translate("Monitor", "Click and drag here"))
        self.slider_left.setWhatsThis(_translate("Monitor", "Slider Widget.  "))
        self.slider_middle.setToolTip(_translate("Monitor", "Click and drag here"))
        self.slider_middle.setWhatsThis(_translate("Monitor", "Slider Widget.  "))
        self.slider_right.setToolTip(_translate("Monitor", "Click and drag here"))
        self.slider_right.setWhatsThis(_translate("Monitor", "Slider Widget.  "))
        self.panel.setToolTip(_translate("Monitor", "Click and drag here"))
        self.panel.setWhatsThis(_translate("Monitor", "Panel Widget.  "))
from src.panel import Panel
from src.slider import Slider


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Monitor = QtWidgets.QWidget()
    ui = Ui_Monitor()
    ui.setupUi(Monitor)
    Monitor.show()
    sys.exit(app.exec_())
