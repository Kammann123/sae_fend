# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import pyqtSlot, QObject

# Project modules
from src.package.bases.dataservice import DataService, ServiceStatus
from src.package.collection import DataCollection
from src.ui.manualservice import Ui_ManualService


class ManualService(DataService, QDialog, Ui_ManualService):
    """ QDialog to allow the user to manually enter the data
        and be logged as a DataService.
    """

    def __init__(self):
        super(ManualService, self).__init__()
        self.setupUi(self)

        # Signal and slot connections
        self.connect_button.clicked.connect(self.on_connect)
        self.disconnect_button.clicked.connect(self.on_disconnected)
        self.waiting_button.clicked.connect(self.on_waiting)
        self.message_button.clicked.connect(self.on_post)
        self.load_button.clicked.connect(self.on_load)

        # Creating the data
        self._manual_data = [
            DataCollection('Air Temperature', 'Temperature', '°C'),
            DataCollection('Engine Temperature', 'Temperature', '°C'),
            DataCollection('Oil Pressure', 'Pressure', 'kPa'),
            DataCollection('Battery', 'Voltage', 'V'),
            DataCollection('Fuel Used', 'Volume', 'L'),
            DataCollection('Throttle', 'Relative', '%'),
            DataCollection('Ignition Advance', 'Relative', '%'),
            DataCollection('Lambda', 'Relative Degrees', '°'),
            DataCollection('Ground Speed', 'Speed', 'km/h'),
            DataCollection('RPM', 'RPM', 'RPM')
        ]
        self.set_data(self._manual_data)

    def _fetch_data(self, name: str) -> DataCollection:
        """
        Returns the DataCollection fetching through the internal list.
        :param name: DataCollection's name
        """
        for data in self._manual_data:
            if data.name == name:
                return data

    @pyqtSlot(name='onLoad')
    def on_load(self):
        self._fetch_data('Air Temperature').add(self.air_temperature.value())
        self._fetch_data('Engine Temperature').add(self.engine_temperature.value())
        self._fetch_data('Battery').add(self.battery.value())
        self._fetch_data('Oil Pressure').add(self.oil_pressure.value())
        self._fetch_data('Throttle').add(self.throttle.value())
        self._fetch_data('Lambda').add(self.lambda_1.value())
        self._fetch_data('Fuel Used').add(self.fuel_used.value())
        self._fetch_data('Ground Speed').add(self.ground_speed.value())
        self._fetch_data('RPM').add(self.rpm.value())
        self._fetch_data('Ignition Advance').add(self.ignition_advance.value())

    @pyqtSlot(name='onPost')
    def on_post(self):
        message = self.message_box.toPlainText()
        self.message_box.clear()
        self.post(message)

    @pyqtSlot(name='onConnect')
    def on_connect(self):
        self.set_status(ServiceStatus.Connected)

    @pyqtSlot(name='onWaiting')
    def on_waiting(self):
        self.set_status(ServiceStatus.Waiting)

    @pyqtSlot(name='onDisconnected')
    def on_disconnected(self):
        self.set_status(ServiceStatus.Disconnected)


if __name__ == "__main__":
    app = QApplication([])
    dialog = ManualService()
    dialog.show()
    app.exec()
