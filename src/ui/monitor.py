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
        Monitor.resize(803, 134)
        Monitor.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Monitor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget = QtWidgets.QWidget(Monitor)
        self.horizontalWidget.setStyleSheet("")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.data_widget = QtWidgets.QStackedWidget(self.horizontalWidget)
        self.data_widget.setStyleSheet("")
        self.data_widget.setObjectName("data_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.data_widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.data_widget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.data_widget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toggle_button = ToggleButton(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggle_button.sizePolicy().hasHeightForWidth())
        self.toggle_button.setSizePolicy(sizePolicy)
        self.toggle_button.setObjectName("toggle_button")
        self.verticalLayout_2.addWidget(self.toggle_button)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.horizontalWidget)

        self.retranslateUi(Monitor)
        QtCore.QMetaObject.connectSlotsByName(Monitor)

    def retranslateUi(self, Monitor):
        _translate = QtCore.QCoreApplication.translate
        Monitor.setWindowTitle(_translate("Monitor", "Form"))
        self.toggle_button.setToolTip(_translate("Monitor", "Click and drag here"))
        self.toggle_button.setWhatsThis(_translate("Monitor", "Toggle Button Widget.  "))
        self.toggle_button.setProperty("primary_text", _translate("Monitor", "Modo Panel"))
        self.toggle_button.setProperty("secondary_text", _translate("Monitor", "Modo Gráfico"))
from src.widgets.togglebutton import ToggleButton


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Monitor = QtWidgets.QWidget()
    ui = Ui_Monitor()
    ui.setupUi(Monitor)
    Monitor.show()
    sys.exit(app.exec_())
