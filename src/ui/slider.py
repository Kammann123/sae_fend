# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/slider.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Slider(object):
    def setupUi(self, Slider):
        Slider.setObjectName("Slider")
        Slider.resize(510, 391)
        self.verticalLayout = QtWidgets.QVBoxLayout(Slider)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.title = QtWidgets.QLabel(Slider)
        font = QtGui.QFont()
        font.setFamily("The Bold Font")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.horizontalLayout_2.addWidget(self.title, 0, QtCore.Qt.AlignBottom)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.previous_button = QtWidgets.QPushButton(Slider)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.previous_button.sizePolicy().hasHeightForWidth())
        self.previous_button.setSizePolicy(sizePolicy)
        self.previous_button.setMaximumSize(QtCore.QSize(30, 30))
        self.previous_button.setStyleSheet("QPushButton {\n"
"    border-image: url(:/arrow_left/assets/buttons/arrow_left/left.png);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border-image: url(:/arrow_left/assets/buttons/arrow_left/left_hover.png)\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-image: url(:/arrow_left/assets/buttons/arrow_left/left_pressed.png)\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"    border-image: url(:/arrow_left/assets/buttons/arrow_left/left_disabled.png);\n"
"}")
        self.previous_button.setText("")
        self.previous_button.setIconSize(QtCore.QSize(40, 40))
        self.previous_button.setAutoDefault(False)
        self.previous_button.setDefault(False)
        self.previous_button.setFlat(True)
        self.previous_button.setObjectName("previous_button")
        self.horizontalLayout_2.addWidget(self.previous_button)
        self.next_button = QtWidgets.QPushButton(Slider)
        self.next_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)
        self.next_button.setMaximumSize(QtCore.QSize(30, 30))
        self.next_button.setStyleSheet("QPushButton {\n"
"    border-image: url(:/arrow_right/assets/buttons/arrow_right/right.png);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    border-image: url(:/arrow_right/assets/buttons/arrow_right/right_hover.png);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    border-image: url(:/arrow_right/assets/buttons/arrow_right/right_pressed.png);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"    border-image: url(:/arrow_right/assets/buttons/arrow_right/right_disabled.png);\n"
"}")
        self.next_button.setText("")
        self.next_button.setIconSize(QtCore.QSize(40, 40))
        self.next_button.setAutoDefault(False)
        self.next_button.setDefault(False)
        self.next_button.setFlat(True)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout_2.addWidget(self.next_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(Slider)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.data_chart = DataChart(Slider)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.data_chart.sizePolicy().hasHeightForWidth())
        self.data_chart.setSizePolicy(sizePolicy)
        self.data_chart.setObjectName("data_chart")
        self.verticalLayout.addWidget(self.data_chart)

        self.retranslateUi(Slider)
        QtCore.QMetaObject.connectSlotsByName(Slider)

    def retranslateUi(self, Slider):
        _translate = QtCore.QCoreApplication.translate
        Slider.setWindowTitle(_translate("Slider", "Form"))
        self.title.setText(_translate("Slider", "Engine Temperature"))
        self.data_chart.setToolTip(_translate("Slider", "Click and drag here"))
        self.data_chart.setWhatsThis(_translate("Slider", "Data Chart Widget.  "))
from src.widgets.datachartwidget import DataChart
import buttons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Slider = QtWidgets.QWidget()
    ui = Ui_Slider()
    ui.setupUi(Slider)
    Slider.show()
    sys.exit(app.exec_())
