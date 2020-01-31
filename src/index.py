# PyQt5 modules
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot

# Project modules
from src.ui.index import Ui_Index


class Index(QWidget, Ui_Index):
    """ Index widget, here goes the initial presentation screen when
        the application starts.
        The router received is the main window that handles switching the screen
        in each step of the application's flow.
    """

    def __init__(self, router):
        super(Index, self).__init__(router)
        self.setupUi(self)

        # Setting the reference of the router parent
        self.router = router

        # Connecting signals and slots in the widget
        self.continue_button.clicked.connect(self.on_continue)

    @pyqtSlot(name='onContinue')
    def on_continue(self):
        """
        When continue button is pressed, MainWindow is told to route
        the application to the monitor screen.
        """
        self.router.route('monitor')
