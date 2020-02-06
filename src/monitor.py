# PyQt5 modules
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot

# Python modules
from typing import List

# Project modules
from src.package.collection import DataCollection
from src.ui.monitor import Ui_Monitor
from src.slider import ChartSlider
from src.panel import Panel
from src.manualservice import ManualService


class Monitor(QWidget, Ui_Monitor):
    """ Monitor Widget is where all data and user configurations
        will be set, is the main screen, its name could be refactored in the future.
    """

    def __init__(self, router):
        super(Monitor, self).__init__(router)
        self.setupUi(self)

        # Setting the reference to the router parent
        self.data_service = None
        self.router = router

        # Adding widgets to the data stacked widget
        self.panel = Panel()
        self.slider = ChartSlider()
        self.data_widget.addWidget(self.panel)
        self.data_widget.addWidget(self.slider)
        self.data_widget.setCurrentWidget(self.panel)

        # Connecting signals and slots
        self.panel_button.clicked.connect(self.go_panel)
        self.graphic_button.clicked.connect(self.go_slider)
        self.open_service_button.clicked.connect(self.open_service)

    @pyqtSlot(name='openService')
    def open_service(self):
        self.data_service = ManualService()
        self.on_data_changed(self.data_service.data)
        self.data_service.show()

    @pyqtSlot(name='onDataChanged')
    def on_data_changed(self, data: List[DataCollection]):
        self.panel.set_data(data)
        self.slider.set_data(data)

    @pyqtSlot(name='goPanel')
    def go_panel(self):
        self.data_widget.setCurrentWidget(self.panel)

    @pyqtSlot(name='goSlider')
    def go_slider(self):
        self.data_widget.setCurrentWidget(self.slider)
