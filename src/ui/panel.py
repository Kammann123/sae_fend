# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/panel.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Panel(object):
    def setupUi(self, Panel):
        Panel.setObjectName("Panel")
        Panel.resize(984, 354)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Panel.sizePolicy().hasHeightForWidth())
        Panel.setSizePolicy(sizePolicy)
        Panel.setMaximumSize(QtCore.QSize(16777215, 354))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Panel)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.ground_speed_display = CircularGauge(Panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ground_speed_display.sizePolicy().hasHeightForWidth())
        self.ground_speed_display.setSizePolicy(sizePolicy)
        self.ground_speed_display.setMinimumSize(QtCore.QSize(250, 250))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(15)
        self.ground_speed_display.setProperty("label_font", font)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(50)
        self.ground_speed_display.setProperty("value_font", font)
        self.ground_speed_display.setProperty("max_value", 250)
        self.ground_speed_display.setProperty("value", 125)
        brush = QtGui.QBrush(QtGui.QColor(77, 104, 112, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.ground_speed_display.setProperty("bar_background", brush)
        self.ground_speed_display.setObjectName("ground_speed_display")
        self.verticalLayout.addWidget(self.ground_speed_display, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fuel_used_display = IconData(Panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fuel_used_display.sizePolicy().hasHeightForWidth())
        self.fuel_used_display.setSizePolicy(sizePolicy)
        self.fuel_used_display.setProperty("value", 9)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/fuel/assets/fuel/fuel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fuel_used_display.setProperty("icon", icon)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.fuel_used_display.setProperty("value_font", font)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        self.fuel_used_display.setProperty("label_font", font)
        self.fuel_used_display.setProperty("scale", 0.8)
        self.fuel_used_display.setObjectName("fuel_used_display")
        self.verticalLayout_3.addWidget(self.fuel_used_display)
        self.battery_display = IconData(Panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.battery_display.sizePolicy().hasHeightForWidth())
        self.battery_display.setSizePolicy(sizePolicy)
        self.battery_display.setProperty("value", 12)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/battery/assets/battery/car+battery+icon-1320184285905906096.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.battery_display.setProperty("icon", icon1)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.battery_display.setProperty("value_font", font)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        self.battery_display.setProperty("label_font", font)
        self.battery_display.setProperty("scale", 0.8)
        self.battery_display.setObjectName("battery_display")
        self.verticalLayout_3.addWidget(self.battery_display)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.throttle_display = CircularGauge(Panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.throttle_display.sizePolicy().hasHeightForWidth())
        self.throttle_display.setSizePolicy(sizePolicy)
        self.throttle_display.setMinimumSize(QtCore.QSize(200, 200))
        self.throttle_display.setMaximumSize(QtCore.QSize(200, 200))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(15)
        self.throttle_display.setProperty("label_font", font)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(50)
        self.throttle_display.setProperty("value_font", font)
        self.throttle_display.setProperty("min_value", 0)
        self.throttle_display.setProperty("max_value", 100)
        self.throttle_display.setProperty("span", -300)
        self.throttle_display.setProperty("gauge_size", 200)
        brush = QtGui.QBrush(QtGui.QColor(90, 79, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.throttle_display.setProperty("normal_fill", brush)
        self.throttle_display.setProperty("value", 35)
        brush = QtGui.QBrush(QtGui.QColor(77, 104, 112, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.throttle_display.setProperty("bar_background", brush)
        self.throttle_display.setObjectName("throttle_display")
        self.verticalLayout_5.addWidget(self.throttle_display, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ignition_advance_display = IconData(Panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ignition_advance_display.sizePolicy().hasHeightForWidth())
        self.ignition_advance_display.setSizePolicy(sizePolicy)
        self.ignition_advance_display.setProperty("value", 9)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ignition/assets/ignition/50425-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ignition_advance_display.setProperty("icon", icon2)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.ignition_advance_display.setProperty("value_font", font)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        self.ignition_advance_display.setProperty("label_font", font)
        self.ignition_advance_display.setProperty("scale", 0.8)
        self.ignition_advance_display.setObjectName("ignition_advance_display")
        self.horizontalLayout_2.addWidget(self.ignition_advance_display)
        self.lambda_display = IconData(Panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lambda_display.sizePolicy().hasHeightForWidth())
        self.lambda_display.setSizePolicy(sizePolicy)
        self.lambda_display.setProperty("value", 12)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/lambda/assets/lambda/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lambda_display.setProperty("icon", icon3)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.lambda_display.setProperty("value_font", font)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        self.lambda_display.setProperty("label_font", font)
        self.lambda_display.setProperty("scale", 0.8)
        self.lambda_display.setObjectName("lambda_display")
        self.horizontalLayout_2.addWidget(self.lambda_display)
        self.oil_pressure_display = IconData(Panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.oil_pressure_display.sizePolicy().hasHeightForWidth())
        self.oil_pressure_display.setSizePolicy(sizePolicy)
        self.oil_pressure_display.setProperty("value", 2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/oil/assets/oil/17696-200.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.oil_pressure_display.setProperty("icon", icon4)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.oil_pressure_display.setProperty("value_font", font)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        self.oil_pressure_display.setProperty("label_font", font)
        self.oil_pressure_display.setProperty("scale", 0.8)
        self.oil_pressure_display.setObjectName("oil_pressure_display")
        self.horizontalLayout_2.addWidget(self.oil_pressure_display)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.engine_temperature_display = IconData(Panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.engine_temperature_display.sizePolicy().hasHeightForWidth())
        self.engine_temperature_display.setSizePolicy(sizePolicy)
        self.engine_temperature_display.setProperty("value", 198)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/thermometer/assets/thermometer/Car_Engine_-_Dashboard_Lights_110-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.engine_temperature_display.setProperty("icon", icon5)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.engine_temperature_display.setProperty("value_font", font)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        self.engine_temperature_display.setProperty("label_font", font)
        self.engine_temperature_display.setProperty("scale", 0.8)
        self.engine_temperature_display.setObjectName("engine_temperature_display")
        self.verticalLayout_4.addWidget(self.engine_temperature_display)
        self.air_temperature_display = IconData(Panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.air_temperature_display.sizePolicy().hasHeightForWidth())
        self.air_temperature_display.setSizePolicy(sizePolicy)
        self.air_temperature_display.setProperty("value", 35)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/thermometer/assets/thermometer/120779.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.air_temperature_display.setProperty("icon", icon6)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        self.air_temperature_display.setProperty("value_font", font)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        self.air_temperature_display.setProperty("label_font", font)
        self.air_temperature_display.setProperty("scale", 0.8)
        self.air_temperature_display.setObjectName("air_temperature_display")
        self.verticalLayout_4.addWidget(self.air_temperature_display)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.rpm_display = CircularGauge(Panel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rpm_display.sizePolicy().hasHeightForWidth())
        self.rpm_display.setSizePolicy(sizePolicy)
        self.rpm_display.setMinimumSize(QtCore.QSize(250, 250))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(15)
        self.rpm_display.setProperty("label_font", font)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(50)
        self.rpm_display.setProperty("value_font", font)
        self.rpm_display.setProperty("min_value", 0)
        self.rpm_display.setProperty("max_value", 20000)
        self.rpm_display.setProperty("value", 10000)
        brush = QtGui.QBrush(QtGui.QColor(77, 104, 112, 30))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.rpm_display.setProperty("bar_background", brush)
        self.rpm_display.setObjectName("rpm_display")
        self.verticalLayout_2.addWidget(self.rpm_display, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Panel)
        QtCore.QMetaObject.connectSlotsByName(Panel)

    def retranslateUi(self, Panel):
        _translate = QtCore.QCoreApplication.translate
        Panel.setWindowTitle(_translate("Panel", "Form"))
        self.ground_speed_display.setToolTip(_translate("Panel", "Click and drag here"))
        self.ground_speed_display.setWhatsThis(_translate("Panel", "Circular Gauge Widget.  "))
        self.ground_speed_display.setProperty("label", _translate("Panel", "KM/H"))
        self.fuel_used_display.setToolTip(_translate("Panel", "Click and drag here"))
        self.fuel_used_display.setWhatsThis(_translate("Panel", "Icon Data Widget.  "))
        self.fuel_used_display.setProperty("label", _translate("Panel", "L"))
        self.battery_display.setToolTip(_translate("Panel", "Click and drag here"))
        self.battery_display.setWhatsThis(_translate("Panel", "Icon Data Widget.  "))
        self.battery_display.setProperty("label", _translate("Panel", "V"))
        self.throttle_display.setToolTip(_translate("Panel", "Click and drag here"))
        self.throttle_display.setWhatsThis(_translate("Panel", "Circular Gauge Widget.  "))
        self.throttle_display.setProperty("label", _translate("Panel", "%"))
        self.ignition_advance_display.setToolTip(_translate("Panel", "Click and drag here"))
        self.ignition_advance_display.setWhatsThis(_translate("Panel", "Icon Data Widget.  "))
        self.ignition_advance_display.setProperty("label", _translate("Panel", "°"))
        self.lambda_display.setToolTip(_translate("Panel", "Click and drag here"))
        self.lambda_display.setWhatsThis(_translate("Panel", "Icon Data Widget.  "))
        self.lambda_display.setProperty("label", _translate("Panel", "°"))
        self.oil_pressure_display.setToolTip(_translate("Panel", "Click and drag here"))
        self.oil_pressure_display.setWhatsThis(_translate("Panel", "Icon Data Widget.  "))
        self.oil_pressure_display.setProperty("label", _translate("Panel", "kPa"))
        self.engine_temperature_display.setToolTip(_translate("Panel", "Click and drag here"))
        self.engine_temperature_display.setWhatsThis(_translate("Panel", "Icon Data Widget.  "))
        self.engine_temperature_display.setProperty("label", _translate("Panel", "°C"))
        self.air_temperature_display.setToolTip(_translate("Panel", "Click and drag here"))
        self.air_temperature_display.setWhatsThis(_translate("Panel", "Icon Data Widget.  "))
        self.air_temperature_display.setProperty("label", _translate("Panel", "°C"))
        self.rpm_display.setToolTip(_translate("Panel", "Click and drag here"))
        self.rpm_display.setWhatsThis(_translate("Panel", "Circular Gauge Widget.  "))
from src.widgets.gaugewidget import CircularGauge
from src.widgets.icondatawidget import IconData
from src.resources import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Panel = QtWidgets.QWidget()
    ui = Ui_Panel()
    ui.setupUi(Panel)
    Panel.show()
    sys.exit(app.exec_())
