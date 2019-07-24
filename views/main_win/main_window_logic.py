"""
Main Window control methods and logic.
"""

# python native modules

# third-party modules
from PyQt5 import QtWidgets

# sae project modules
from views.main_win.main_window_view import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """ MainWindow, main window class.
    """

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
