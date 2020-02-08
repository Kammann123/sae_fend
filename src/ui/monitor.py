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
        Monitor.resize(1255, 308)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Monitor.sizePolicy().hasHeightForWidth())
        Monitor.setSizePolicy(sizePolicy)
        Monitor.setStyleSheet("background-color: rgb(123, 46, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Monitor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Monitor)
        self.frame.setStyleSheet("background-color: rgba(73, 69, 129, 150);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.panel = Panel(self.frame)
        self.panel.setStyleSheet("")
        self.panel.setObjectName("panel")
        self.verticalLayout_2.addWidget(self.panel)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Monitor)
        QtCore.QMetaObject.connectSlotsByName(Monitor)

    def retranslateUi(self, Monitor):
        _translate = QtCore.QCoreApplication.translate
        Monitor.setWindowTitle(_translate("Monitor", "Form"))
        self.panel.setToolTip(_translate("Monitor", "Click and drag here"))
        self.panel.setWhatsThis(_translate("Monitor", "Panel Widget.  "))
from src.panel import Panel


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Monitor = QtWidgets.QWidget()
    ui = Ui_Monitor()
    ui.setupUi(Monitor)
    Monitor.show()
    sys.exit(app.exec_())
