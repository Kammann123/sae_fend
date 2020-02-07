# PyQt5 modules
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal, pyqtProperty

# Project modules
from src.package.bases.dataservice import DataService


class UserSession(QObject):
    """ All the user's settings and session data is being saved in this singleton class
        which will be instanced only once per application running.
        UserSession is intended to own the services being used by the user, so every change on them
        should pass through this object.
    """

    # UserSession's Signals
    services_changed = pyqtSignal(name='servicesChanged')
    data_service_changed = pyqtSignal(name='dataServiceChanged')

    @pyqtProperty(DataService)
    def data_service(self) -> DataService:
        return self._data_service

    @pyqtProperty(list)
    def services(self) -> list:
        return [
            self._data_service
        ]

    def __init__(self):
        super(UserSession, self).__init__()

        # Private members/attributes of the class
        self._data_service = None

    def set_data_service(self, service: DataService):
        """
        Sets the new DataService.
        :param service: DataService instance
        """
        self._data_service = service
        self.data_service_changed.emit()
        self.services_changed.emit()
