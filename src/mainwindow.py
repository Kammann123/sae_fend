# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import pyqtSlot

# Python modules
from typing import Dict, List

# Widgets import
from src.ui.mainwindow import Ui_MainWindow
from src.index import Index
from src.monitor import Monitor


class MainWindow(QMainWindow, Ui_MainWindow):
    """ Application's main window, here is where an internal router path
        will be used to control what to show in the screen. It manages the
        application flow.
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Declaring the router paths, and type checking to prevent
        # mistakes of the programmer, it also creates the widgets
        # as part of the stacked widget layout
        self._widget_paths: Dict[str, QWidget] = {}
        self._default_path: str = 'index'

        self.declare_router(
            {
                'index': Index(self),
                'monitor': Monitor(self)
            }
        )
        self.route(self._default_path)

    def get_paths(self) -> List[str]:
        """
        Returns a list of valid string paths to be used in the main window's router
        :return: List of string paths
        """
        return list(self._widget_paths.keys())

    def declare_router(self, paths: Dict[str, QWidget]):
        """
        Declares the router paths of the main window, basically it creates a dictionary
        so we can dynamically declare and switch the current widget on screen, by
        using only its internal name.
        :param paths: Dictionary with string's indexed widgets
        """
        if type(paths) is dict:
            for target in paths.values():
                if not isinstance(target, QWidget):
                    raise ValueError('Invalid type of path targets in dictionary received at declare_router() method')
            else:
                self._widget_paths = paths
                for key, value in paths.items():
                    self.router_widget.addWidget(value)
        else:
            raise ValueError('Invalid type of paths parameter in declare_router() method')

    @pyqtSlot(str, name='route')
    def route(self, path: str):
        """
        Switches the current displayed widget in the main window's screen,
        by using its path assigned in the router path declaration, which
        is set in the MainWindow's constructor.
        :param path: String name of the widget's path in the router
        """
        if path not in self.get_paths():
            raise ValueError('Unknown router path used in the route() method')
        else:
            self.router_widget.setCurrentWidget(self._widget_paths[path])
