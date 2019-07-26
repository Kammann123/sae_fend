"""
Setting UART staff window (port, speed, parity)
"""

# python native modules

# third-party modules
import serial.tools.list_ports
from PyQt5 import QtWidgets

# sae project modules
from views.setting_win.setting_window_view import Ui_SettingWindow
from fend.user.serial_config import SerialConfig
from fend.core.sae_fend import SAEFend


class SettingWindow(QtWidgets.QDialog, Ui_SettingWindow):
    def __init__(self, sae_fend: SAEFend, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self._sae_fend = sae_fend
        self.finishButton.clicked.connect(self.finished_callback)

        """ getting available serial ports """
        port = list(serial.tools.list_ports.comports())
        for puerto in port:
            self.portBox.addItem(puerto.device)

    def start_showing(self):
        self.show()

    def finished_callback(self):
        """ Callback to send information after selecting UART's options """
        # print(self.portBox.currentText())
        # print(self.speedBox.currentText())
        # print(self.parityBox.currentText())
        """ Loading the current session's serial information """
        self._sae_fend.session.serial = SerialConfig(self.speedBox.currentText(), 0, self.parityBox.currentText(), 0)

        self.hide()
