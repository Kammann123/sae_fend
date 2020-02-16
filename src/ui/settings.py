# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(342, 245)
        self.verticalLayout = QtWidgets.QVBoxLayout(Settings)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Settings)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mic_config = MicConfig(self.tab)
        self.mic_config.setObjectName("mic_config")
        self.verticalLayout_2.addWidget(self.mic_config)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sound_config = SoundConfig(self.tab_2)
        self.sound_config.setObjectName("sound_config")
        self.verticalLayout_3.addWidget(self.sound_config)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Dialog"))
        self.mic_config.setToolTip(_translate("Settings", "Click and drag here"))
        self.mic_config.setWhatsThis(_translate("Settings", "Mic Config Widget.  "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Settings", "Micrófono"))
        self.sound_config.setToolTip(_translate("Settings", "Click and drag here"))
        self.sound_config.setWhatsThis(_translate("Settings", "Sound Config Widget.  "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Settings", "Sonido"))
from src.micconfig import MicConfig
from src.soundconfig import SoundConfig


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Settings = QtWidgets.QDialog()
    ui = Ui_Settings()
    ui.setupUi(Settings)
    Settings.show()
    sys.exit(app.exec_())
