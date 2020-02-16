# PyQt5 modules
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal, pyqtProperty, pyqtSlot

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
    sound_settings_changed = pyqtSignal(dict, name='soundSettingsChanged')
    mic_settings_changed = pyqtSignal(dict, name='micSettingsChanged')

    @pyqtProperty(DataService)
    def data_service(self) -> DataService:
        return self._data_service

    @pyqtProperty(bool)
    def has_data_service(self) -> bool:
        return self._data_service is not None

    @pyqtProperty(list)
    def services(self) -> list:
        return [
            self._data_service
        ]

    @pyqtProperty(dict)
    def sound_settings(self) -> dict:
        return self._sound_settings

    @pyqtProperty(dict)
    def mic_settings(self) -> dict:
        return self._mic_settings

    def __init__(self, mic_settings: dict = {}, sound_settings: dict = {}):
        super(UserSession, self).__init__()

        # Private members/attributes of the class
        self._data_service = None
        self._sound_settings = sound_settings
        self._mic_settings = mic_settings

    @pyqtSlot(dict, name='setSoundSettings')
    def set_sound_settings(self, settings: dict):
        """
        Sets the current settings for the sound streaming device
        :param settings: Current settings
        """
        self._sound_settings = settings
        self.sound_settings_changed.emit(settings)

    @pyqtSlot(dict, name='setMicSettings')
    def set_mic_settings(self, settings: dict):
        """
        Sets the current settings for the mic streaming device
        :param settings:  Current settings
        """
        self._mic_settings = settings
        self.mic_settings_changed.emit(settings)

    @pyqtSlot(DataService, name='setDataService')
    def set_data_service(self, service: DataService):
        """
        Sets the new DataService.
        :param service: DataService instance
        """
        self._data_service = service
        self.data_service_changed.emit()
        self.services_changed.emit()
