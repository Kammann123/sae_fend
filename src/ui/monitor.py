# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/monitor.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Monitor(object):
    def setupUi(self, Monitor):
        Monitor.setObjectName("Monitor")
        Monitor.resize(808, 508)
        self.verticalLayout = QtWidgets.QVBoxLayout(Monitor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.panel_button = QtWidgets.QPushButton(Monitor)
        self.panel_button.setObjectName("panel_button")
        self.horizontalLayout.addWidget(self.panel_button)
        self.graphic_button = QtWidgets.QPushButton(Monitor)
        self.graphic_button.setObjectName("graphic_button")
        self.horizontalLayout.addWidget(self.graphic_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.data_widget = QtWidgets.QStackedWidget(Monitor)
        self.data_widget.setObjectName("data_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.data_widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.data_widget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.data_widget)

        self.retranslateUi(Monitor)
        QtCore.QMetaObject.connectSlotsByName(Monitor)

    def retranslateUi(self, Monitor):
        _translate = QtCore.QCoreApplication.translate
        Monitor.setWindowTitle(_translate("Monitor", "Form"))
        self.panel_button.setText(_translate("Monitor", "Modo Panel"))
        self.graphic_button.setText(_translate("Monitor", "Modo Gráfico"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Monitor = QtWidgets.QWidget()
    ui = Ui_Monitor()
    ui.setupUi(Monitor)
    Monitor.show()
    sys.exit(app.exec_())
