# Python modules
import os
from datetime import datetime

# PyQt5 modules
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal, pyqtProperty, pyqtSlot

# Project modules
from src.package.bases.dataservice import DataService
from src.package.bases.streamservice import StreamService

# Third party modules
import pandas as pd


class UserSession(QObject):
    """ All the user's settings and session data is being saved in this singleton class
        which will be instanced only once per application running.
        UserSession is intended to own the services being used by the user, so every change on them
        should pass through this object.
    """

    # UserSession's Signals
    services_changed = pyqtSignal(name='servicesChanged')
    data_service_changed = pyqtSignal(name='dataServiceChanged')
    stream_service_changed = pyqtSignal(name='streamServiceChanged')
    sound_settings_changed = pyqtSignal(dict, name='soundSettingsChanged')
    mic_settings_changed = pyqtSignal(dict, name='micSettingsChanged')

    @pyqtProperty(DataService)
    def data_service(self) -> DataService:
        return self._data_service

    @pyqtProperty(StreamService)
    def stream_service(self) -> StreamService:
        return self._stream_service

    @pyqtProperty(bool)
    def has_stream_service(self) -> bool:
        return self._stream_service is not None

    @pyqtProperty(bool)
    def has_data_service(self) -> bool:
        return self._data_service is not None

    @pyqtProperty(list)
    def services(self) -> list:
        return [
            self._data_service,
            self._stream_service
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
        self._stream_service = None

        self._sound_settings = sound_settings
        self._mic_settings = mic_settings

        # Creating the session folder for future use
        self._dir = datetime.now().strftime('%d-%m-%Y__%H-%M')
        os.mkdir(self._dir)

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

    @pyqtSlot(StreamService, name='setStreamService')
    def set_stream_service(self, service: StreamService):
        """
        Sets the new StreamService.
        :param service: StreamService instance
        """
        self._stream_service = service
        self.stream_service_changed.emit()
        self.services_changed.emit()

    @pyqtSlot(name='saveData')
    def save_data(self):
        """
        Save DataCollections from DataServices
        """
        properties = self._data_service.names
        properties_data = self._data_service.get_data_by_names(properties)
        csv_file_names = []
        for data in properties_data:
            time = [datetime.fromtimestamp(moment/1000) for moment in data.timestamps]
            formatted_time = [instant.strftime('%H:%M:%S') for instant in time]
            values = data.values
            csv_file_names.append(self._dir+'/'+data.name+'.csv')
            file = open(csv_file_names[-1], 'w')
            file.write('Time,Value' + os.linesep)
            for index in range(len(time)):
                file.write(formatted_time[index] + ',' + str(values[index]) + os.linesep)
            file.close()
        excel_file = pd.ExcelWriter(self._dir+'/Data.xlsx')
        for csv_file in csv_file_names:
            to_attach = pd.read_csv(csv_file)
            to_attach.to_excel(excel_file, sheet_name=csv_file.split('/')[-1].split('.')[0])
        excel_file.save()
