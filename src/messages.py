# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot, pyqtProperty

# Project modules
from src.ui.messages import Ui_Messages

# Python modules


class Messages(QWidget, Ui_Messages):
    """ Messages widget to handle the message sending ui function"""
    @pyqtProperty()