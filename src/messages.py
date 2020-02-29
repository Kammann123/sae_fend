# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot, pyqtProperty

# Project modules
from src.ui.messages import Ui_Messages

# Python modules


class Messages(QWidget, Ui_Messages):
    """ Messages widget to handle the message sending ui function"""

    def __init__(self, parent=None):
        super(Messages, self).__init__(parent)
        self.setupUi(self)
