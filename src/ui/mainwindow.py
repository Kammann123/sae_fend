# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(477, 162)
        MainWindow.setStyleSheet("background-color: #6c7b95;")
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.router_widget = QtWidgets.QStackedWidget(self.central_widget)
        self.router_widget.setStyleSheet("QWidget {\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    contentMargins: 0px;\n"
"}")
        self.router_widget.setObjectName("router_widget")
        self.page = QtWidgets.QWidget()
        self.page.setStyleSheet("QWidget {\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}")
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.router_widget.addWidget(self.page)
        self.verticalLayout.addWidget(self.router_widget)
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ITBA SAE"))
from src.resources import index_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
