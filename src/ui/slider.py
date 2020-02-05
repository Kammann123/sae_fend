# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/slider.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChartSlider(object):
    def setupUi(self, ChartSlider):
        ChartSlider.setObjectName("ChartSlider")
        ChartSlider.resize(622, 456)
        self.verticalLayout = QtWidgets.QVBoxLayout(ChartSlider)
        self.verticalLayout.setObjectName("verticalLayout")
        self.slider_widget = QtWidgets.QStackedWidget(ChartSlider)
        self.slider_widget.setObjectName("slider_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.slider_widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.slider_widget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.slider_widget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previous_button = QtWidgets.QPushButton(ChartSlider)
        self.previous_button.setObjectName("previous_button")
        self.horizontalLayout.addWidget(self.previous_button)
        self.options_box = QtWidgets.QComboBox(ChartSlider)
        self.options_box.setObjectName("options_box")
        self.horizontalLayout.addWidget(self.options_box)
        self.next_button = QtWidgets.QPushButton(ChartSlider)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout.addWidget(self.next_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ChartSlider)
        QtCore.QMetaObject.connectSlotsByName(ChartSlider)

    def retranslateUi(self, ChartSlider):
        _translate = QtCore.QCoreApplication.translate
        ChartSlider.setWindowTitle(_translate("ChartSlider", "Form"))
        self.previous_button.setText(_translate("ChartSlider", "Anterior"))
        self.next_button.setText(_translate("ChartSlider", "Siguiente"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChartSlider = QtWidgets.QWidget()
    ui = Ui_ChartSlider()
    ui.setupUi(ChartSlider)
    ChartSlider.show()
    sys.exit(app.exec_())
