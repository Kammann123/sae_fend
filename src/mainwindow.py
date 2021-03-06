# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import pyqtSlot

# Python modules
from typing import Dict, List
from os import path, getcwd

# Project modules
from src.package.bases.router import Router
from src.package.usersession import UserSession
from src.ui.mainwindow import Ui_MainWindow
from src.index import Index
from src.monitor import Monitor


class MainWindow(QMainWindow, Ui_MainWindow, Router):
    """ Application's main window, here is where an internal router path
        will be used to control what to show in the screen. It manages the
        application flow.
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle('[ITBA] Formula SAE')
        self.setStyleSheet("background-color: rgb(153, 153, 153);")

        # Private members/attributes
        self.session = UserSession()

        # TODO! Here we are setting a manual service for testing purpose, please remember to REMOVE THIS LINE!
        from src.manualservice import ManualService
        self.manual_service = ManualService()
        self.session.set_data_service(self.manual_service)
        self.manual_service.show()

        # Setting up the Router class with the StackedWidget to be used
        self.declare_router(
            'index', self.router_widget,
            {
                'index': Index(self.session, self),
                'monitor': Monitor(self.session, self)
            }
        )

    def get_paths(self) -> List[str]:
        """
        Returns a list of valid string paths to be used in the main window's router
        :return: List of string paths
        """
        return list(self._widget_paths.keys())
