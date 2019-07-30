"""
Window with cars properties views
"""
# python native modules

# third-party modules
from PyQt5 import QtWidgets

# sae project modules
from views.monitor_win.monitor_window_view import Ui_MonitorWindow
from fend.core.sae_fend import SAEFend


class MonitorWindow(QtWidgets.QWidget, Ui_MonitorWindow):
    def __init__(self, fend: SAEFend, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self._sae_fend = fend
        self.rpmGraph.set_sae_fend(self._sae_fend)
