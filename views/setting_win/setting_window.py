"""
Setting UART staff window (port, speed, parity)
"""

# python native modules

# third-party modules
import serial.tools.list_ports
from PyQt5 import uic, QtWidgets

# sae project modules


class SettingWindow(QtWidgets.QDialog):
    def __init__(self):
        super(SettingWindow, self).__init__()
        uic.loadUi('settingWindow.ui', self)

        self.finishButton.clicked.connect(self.finished_callback)

        """ getting available serial ports"""
        port = list(serial.tools.list_ports.comports())
        for puerto in port:
            self.portBox.addItem(puerto.device)

    def start_showing(self):
        self.show()

    def finished_callback(self):
        """ Callback to send information after selecting UART's options """
        print(self.portBox.currentText())
        print(self.speedBox.currentText())
        print(self.parityBox.currentText())
        self.hide()
