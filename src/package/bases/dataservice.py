# PyQt5 modules
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtProperty

# Project modules
from src.package.collection import DataCollection

# Python modules
from typing import List


class DataService(QObject):
    """ DataService provides the interface used to create a service which will provide
        the DataCollection objects from any source or input of data.
    """

    @pyqtProperty(list)
    def data(self) -> list:
        return self._data

    def __init__(self):
        super(DataService, self).__init__()
        self._data: List[DataCollection] = []
