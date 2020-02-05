# PyQt5 modules
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, pyqtProperty

# Python modules
from typing import Dict


class Router:
    """ Router class provides an interface to be used in a Window or Widget
        as to route between several pages registered as other custom Widgets.
    """

    @pyqtProperty(str)
    def default_path(self) -> str:
        return self._default_path

    def __init__(self):
        self._widget_paths: Dict[str, QWidget] = {}
        self._default_path: str = ''
        self._router_widget = None

    def declare_router(self, default_path: str, router_widget: QWidget, paths: Dict[str, QWidget]):
        """
        Declares the router paths of the main window, basically it creates a dictionary
        so we can dynamically declare and switch the current widget on screen, by
        using only its internal name.
        :param default_path:    Default path to routed
        :param router_widget:   QStackedWidget
        :param paths:           Dictionary with string indexed widgets
        """
        self._default_path = default_path
        self._router_widget = router_widget

        if type(paths) is dict:
            for target in paths.values():
                if not isinstance(target, QWidget):
                    raise ValueError('Invalid type of path targets in dictionary received at declare_router() method')
            else:
                self._widget_paths = paths
                for key, value in paths.items():
                    self._router_widget.addWidget(value)
        else:
            raise ValueError('Invalid type of paths parameter in declare_router() method')

        self.route(self.default_path)

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
            self._router_widget.setCurrentWidget(self._widget_paths[path])
