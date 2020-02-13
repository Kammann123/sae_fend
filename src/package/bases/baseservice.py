# PyQt5 modules
from PyQt5.QtCore import pyqtSignal, pyqtProperty

# Project modules

# Python modules
from enum import Enum


class ServiceStatus(Enum):
    """ Status of connection
    """
    Disconnected = 'Disconnected'
    Waiting = 'Waiting'
    Connected = 'Connected'


class BaseService:
    """ Every service has a status and is capable of posting a status message
        to notify some details about what is happening.
    """

    # Signals
    status_changed = pyqtSignal(ServiceStatus, name='statusChanged')
    message_posted = pyqtSignal(str, name='messagePosted')
    disconnected = pyqtSignal(name='disconnected')
    connected = pyqtSignal(name='connected')
    waiting = pyqtSignal(name='waiting')

    @pyqtProperty(ServiceStatus)
    def status(self) -> ServiceStatus:
        return self._status

    def __init__(self):
        super(BaseService, self).__init__()

        # Private members/attributes of the class
        self._status: ServiceStatus = ServiceStatus.Disconnected

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

