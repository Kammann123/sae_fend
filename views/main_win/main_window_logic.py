"""
Main Window control methods and logic.
"""

# python native modules

# third-party modules
from PyQt5 import QtWidgets
from PyQt5 import QtCore

# sae project modules
from views.main_win.main_window_view import Ui_MainWindow

from fend.core.sae_fend import SAEFend


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """ MainWindow, main window class.
    """

    # Constant values
    PROCESS_TIMER = 25

    def __init__(self, fend_model: SAEFend, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # MainWindow members
        self.fend_model = fend_model

        # Subscribing to events
        self.fend_model.state_changed.subscribe(self, self.on_state_changed)

        # Background concurrent processing timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.fend_model.run)
        self.timer.start(self.PROCESS_TIMER)

    def on_state_changed(self, event_id, event_data):
        """ OnStateChanged event callback. """
        pass
