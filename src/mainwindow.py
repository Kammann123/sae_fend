# PyQt5 modules
from PyQt5 import QtWidgets
from PyQt5 import QtCore

# Python modules
from typing import Dict, List

# MainWindow import
from src.ui.mainwindow import Ui_MainWindow

# Widgets import
from src.index import Index


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
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
        self._widget_paths: Dict[str, QtWidgets.QWidget] = {}
        self._default_path: str = 'index'

        self.declare_router(
            {
                'index': Index(self)
            }
        )
        self.route(self._default_path)

    def get_paths(self) -> List[str]:
        """
        Returns a list of valid string paths to be used in the main window's router
        :return: List of string paths
        """
        return list(self._widget_paths.keys())

    def declare_router(self, paths: Dict[str, QtWidgets.QWidget]):
        """
        Declares the router paths of the main window, basically it creates a dictionary
        so we can dynamically declare and switch the current widget on screen, by
        using only its internal name.
        :param paths: Dictionary with string's indexed widgets
        """
        if type(paths) is dict:
            for target in paths.values():
                if not isinstance(target, QtWidgets.QWidget):
                    raise ValueError('Invalid type of path targets in dictionary received at declare_router() method')
            else:
                self._widget_paths = paths
                for key, value in paths.items():
                    self.router_widget.addWidget(value)
        else:
            raise ValueError('Invalid type of paths parameter in declare_router() method')

    @QtCore.pyqtSlot(str)
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
