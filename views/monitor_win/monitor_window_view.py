# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from views.monitor_win.rpm_widget.rpm_widget import RPMGraphWidget


class Ui_MonitorWindow(object):
    def setupUi(self, MonitorWindow):
        MonitorWindow.setObjectName("MonitorWindow")
        MonitorWindow.resize(700, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MonitorWindow.sizePolicy().hasHeightForWidth())
        MonitorWindow.setSizePolicy(sizePolicy)
        self.rpmGraph = RPMGraphWidget(MonitorWindow)
        self.rpmGraph.setGeometry(QtCore.QRect(400, 20, 300, 200))
        self.rpmGraph.setObjectName("rpmGraph")

        self.retranslateUi(MonitorWindow)
        QtCore.QMetaObject.connectSlotsByName(MonitorWindow)

    def retranslateUi(self, MonitorWindow):
        _translate = QtCore.QCoreApplication.translate
        MonitorWindow.setWindowTitle(_translate("MonitorWindow", "Monitor"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MonitorWindow = QtWidgets.QDialog()
    ui = Ui_MonitorWindow()
    ui.setupUi(MonitorWindow)
    MonitorWindow.show()
    sys.exit(app.exec_())
