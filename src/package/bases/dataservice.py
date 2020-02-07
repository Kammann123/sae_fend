# PyQt5 modules
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtProperty, pyqtSignal

# Project modules
from src.package.collection import DataCollection
from src.package.bases.baseservice import BaseService

# Python modules
from typing import List
from enum import Enum


class DataService(BaseService):
    """ DataService provides the interface used to create a service which will provide
        the DataCollection objects from any source or input of data.
    """

    # Signals
    data_changed = pyqtSignal(list, name='dataChanged')

    @pyqtProperty(bool)
    def has_data(self) -> bool:
        return len(self._data) > 0

    @pyqtProperty(list)
    def data(self) -> list:
        return self._data

    @pyqtProperty(list)
    def names(self) -> list:
        return [data.name for data in self._data]

    def __init__(self):
        super(DataService, self).__init__()

        # Private members/attributes of the class
        self._data: List[DataCollection] = []

    def set_data(self, data: List[DataCollection]):
        """
        Sets a new reference of DataCollection objects
        :param data: New list of data being fetched
        """
        self._data = data
        self.data_changed.emit(self._data)

    def get_data_by_names(self, names: List[str]) -> List[DataCollection]:
        """
        Returns a list of DataCollection, only containing those whose name
        is in the given list as parameter.
        :param names: Selected names
        :return: List of DataCollection corresponding to the given names
        """
        return [data for data in self._data if data.name in names]
