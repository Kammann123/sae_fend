# PyQt5 modules
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSlot

# Python modules
from typing import List

# Project modules
from src.package.collection import DataCollection
from src.package.usersession import UserSession
from src.package.bases.router import Router
from src.ui.monitor import Ui_Monitor
from src.slider import ChartSlider
from src.panel import Panel


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

        # Adding widgets to the data stacked widget
        self.panel = Panel()
        self.slider = ChartSlider()
        self.data_widget.addWidget(self.panel)
        self.data_widget.addWidget(self.slider)
        self.data_widget.setCurrentWidget(self.panel)

        # Connecting signals and slots
        self.panel_button.clicked.connect(self.go_panel)
        self.graphic_button.clicked.connect(self.go_slider)

        # Connecting the UserSession's services
        if self.session is not None:
            self.session.data_service_changed.connect(self.load_data_service)
            self.load_data_service()

    @pyqtSlot(name='loadDataService')
    def load_data_service(self):
        """ DataService has been changed and binding must be done. """
        if self.session is not None:
            data_service = self.session.data_service
            data_service.data_changed.connect(self.load_data)
            data_service.disconnected.connect(self.unload_data_service)

    @pyqtSlot(name='unloadDataService')
    def unload_data_service(self):
        """ DataService has been disconnected, so the binding should be removed. """
        if self.session is not None:
            data_service = self.session.data_service
            data_service.data_changed.disconnect(self.load_data)
            data_service.disconnected.disconnect(self.unload_data_service)

    @pyqtSlot(list, name='loadData')
    def load_data(self, data: List[DataCollection]):
        """
        Data source from the DataService has changed and binding must be done.
        :param data:    New list of DataCollections
        """
        self.slider.set_data(data)
        self.panel.set_data(data)

    @pyqtSlot(name='goPanel')
    def go_panel(self):
        """ Changes the screen to show the Panel Widget """
        self.data_widget.setCurrentWidget(self.panel)

    @pyqtSlot(name='goSlider')
    def go_slider(self):
        """ Changed the screen to show the Slider Widget """
        self.data_widget.setCurrentWidget(self.slider)


if __name__ == '__main__':
    app = QApplication([])
    widget = Monitor()
    widget.show()
    app.exec()
