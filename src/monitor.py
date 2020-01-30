# PyQt5 modules
from PyQt5.QtWidgets import QWidget

# Widgets import
from src.ui.monitor import Ui_Monitor


class Monitor(QWidget, Ui_Monitor):
    """ Monitor Widget is where all data and user configurations
        will be set, is the main screen, its name could be refactored in the future.
    """

    def __init__(self, router):
        super(Monitor, self).__init__(router)
        self.setupUi(self)

        # Setting the reference to the router parent
        self.router = router
