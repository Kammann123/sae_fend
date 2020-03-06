# PyQt5 modules
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import pyqtSlot

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

        # Private members/attributes
        self.session = UserSession()

        # Setting the session services
        # self.session.set_data_service( ... )
        # self.session.set_message_service( ... )
        # self.session.set_stream_service( ...)

        # Connections between signals and slots
        self.routing.connect(self.on_routing)

        # Setting up the Router class with the StackedWidget to be used
        self.declare_router(
            'index', self.router_widget,
            {
                'index': Index(self.session, self),
                'monitor': Monitor(self.session, self)
            }
        )

    @pyqtSlot(str, QWidget, name='onRouting')
    def on_routing(self, path: str, widget: QWidget):
        """
        When some external actuator routes the screen of the MainWindow, some updates
        on its internal configuration must be done.
        :param widget:
        :param path:
        """
        pass
        # TODO! Should not resize sometimes, depends on the current widget being displayed
        # TODO! self.layout().setSizeConstraint(widget.layout().sizeConstraint())
