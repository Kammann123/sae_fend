# PyQt5 modules
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot

# Widgets import
from src.ui.monitor import Ui_Monitor
from src.slider import ChartSlider
from src.panel import Panel


class Monitor(QWidget, Ui_Monitor):
    """ Monitor Widget is where all data and user configurations
        will be set, is the main screen, its name could be refactored in the future.
    """

    def __init__(self, router):
        super(Monitor, self).__init__(router)
        self.setupUi(self)

        # Setting the reference to the router parent
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

    @pyqtSlot(name='goPanel')
    def go_panel(self):
        self.data_widget.setCurrentWidget(self.panel)

    @pyqtSlot(name='goSlider')
    def go_slider(self):
        self.data_widget.setCurrentWidget(self.slider)
