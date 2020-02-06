# PyQt5 modules
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtProperty, pyqtSignal

# Project modules
from src.package.collection import DataCollection

# Python modules
from typing import List
from enum import Enum


class ServiceStatus(Enum):
    """ Status of connection
    """
    Disconnected = 'Disconnected'
    Waiting = 'Waiting'
    Connected = 'Connected'


class DataService(QObject):
    """ DataService provides the interface used to create a service which will provide
        the DataCollection objects from any source or input of data.
    """

    # Signals
    status_changed = pyqtSignal(ServiceStatus, name='statusChanged')
    data_changed = pyqtSignal(List[DataCollection], name='dataChanged')
    disconnected = pyqtSignal(name='disconnected')
    connected = pyqtSignal(name='connected')
    waiting = pyqtSignal(name='waiting')
    message_posted = pyqtSignal(str, name='messagePosted')

    @pyqtProperty(list)
    def data(self) -> list:
        return self._data

    @pyqtProperty(ServiceStatus)
    def status(self) -> ServiceStatus:
        return self._status

    @pyqtProperty(list)
    def names(self) -> list:
        return [data.name for data in self._data]

    def __init__(self):
        super(DataService, self).__init__()

        # Public members/attributes of the class
        self._status: ServiceStatus = ServiceStatus.Disconnected
        self._data: List[DataCollection] = []

    def post(self, message: str):
        """
        Posts a new status message or info.
        :param message: New message
        """
        self.message_posted.emit(message)

    def set_status(self, status: ServiceStatus):
        """
        Sets the current status of the DataService instance
        :param status: Current connection status
        """
        self._status = status
        self.status_changed.emit(self._status)

        if self._status == ServiceStatus.Disconnected:
            self.disconnected.emit()
        elif self._status == ServiceStatus.Connected:
            self.connected.emit()
        elif self._status == ServiceStatus.Waiting:
            self.waiting.emit()

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
