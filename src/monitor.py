# PyQt5 modules
from PyQt5.QtWidgets import QWidget, QApplication, QGraphicsDropShadowEffect
from PyQt5.QtCore import pyqtSlot

# Python modules
from typing import List

# Project modules
from src.package.collection import DataCollection
from src.package.usersession import UserSession
from src.package.bases.router import Router

from src.ui.monitor import Ui_Monitor


class Monitor(QWidget, Ui_Monitor):
    """ Monitor Widget is where all data and user configurations
        will be set, is the main screen, its name could be refactored in the future.
    """

    def __init__(self, session: UserSession = None, router: Router = None):
        super(Monitor, self).__init__(router)
        self.setupUi(self)

        # Setting the reference to the router parent
        self.data_service = None
        self.router = router
        self.session = session

        # Connecting the UserSession's services
        if self.session is not None:

            # Handling the connections to the DataService if there is one available
            # also, if events where triggered before here, first loading of service and data
            # will be forced
            self.session.data_service_changed.connect(self.load_data_service)
            self.load_data_service()
            if self.session.has_data_service:
                if self.session.data_service.has_data:
                    self.load_data(self.session.data_service.data)

    @pyqtSlot(name='loadDataService')
    def load_data_service(self):
        """ DataService has been changed and binding must be done. """
        if self.session is not None:
            if self.session.has_data_service:
                self.session.data_service.data_changed.connect(self.load_data)
                self.session.data_service.disconnected.connect(self.unload_data_service)

    @pyqtSlot(name='unloadDataService')
    def unload_data_service(self):
        """ DataService has been disconnected, so the binding should be removed. """
        if self.session is not None:
            if self.session.has_data_service:
                self.session.data_service.data_changed.disconnect(self.load_data)
                self.session.data_service.disconnected.disconnect(self.unload_data_service)

    @pyqtSlot(list, name='loadData')
    def load_data(self, data: List[DataCollection]):
        """
        Data source from the DataService has changed and binding must be done.
        :param data:    New list of DataCollections
        """
        self.panel.set_data(data)
        self.slider_left.set_data(data)
        self.slider_middle.set_data(data)
        self.slider_right.set_data(data)


if __name__ == '__main__':
    app = QApplication([])
    widget = Monitor()
    widget.show()
    app.exec()
