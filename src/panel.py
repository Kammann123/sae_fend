# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot

# Python modules
from typing import List

# Project modules
from src.package.collection import DataCollection

from src.gaugeviewmodel import CircularGaugeViewModel
from src.icondataviewmodel import IconDataViewModel

from src.ui.panel import Ui_Panel


class Panel(QWidget, Ui_Panel):
    """ This Panel Widget is used to display and visualize all the car's parameters
        and values in a friendly way.
    """

    def __init__(self, parent=None):
        super(Panel, self).__init__(parent)
        self.setupUi(self)

        # Private member/attributes of this class
        self._data = None

        # Wrapping each widget with its ViewModel definition to connect model's data to the view
        self.oil_pressure_view = IconDataViewModel(self.oil_pressure_display)
        self.lambda_view = IconDataViewModel(self.lambda_display)
        self.air_temperature_view = IconDataViewModel(self.air_temperature_display)
        self.battery_view = IconDataViewModel(self.battery_display)
        self.engine_temperature_view = IconDataViewModel(self.engine_temperature_display)
        self.throttle_view = IconDataViewModel(self.throttle_display)
        self.fuel_used_view = IconDataViewModel(self.fuel_used_display)
        self.ignition_advance_view = IconDataViewModel(self.ignition_advance_display)
        self.rpm_view = CircularGaugeViewModel(self.rpm_display)
        self.ground_speed_view = CircularGaugeViewModel(self.ground_speed_display)

        # Creating the map to dynamically connect data models to each view
        self._map = {
            'Oil Pressure': self.oil_pressure_view,
            'Lambda': self.lambda_view,
            'Air Temperature': self.air_temperature_view,
            'Battery': self.battery_view,
            'Engine Temperature': self.engine_temperature_view,
            'Throttle': self.throttle_view,
            'Fuel Used': self.fuel_used_view,
            'Ignition Advance': self.ignition_advance_view,
            'RPM': self.rpm_view,
            'Ground Speed': self.ground_speed_view
        }

    @pyqtSlot(list, name='setData')
    def set_data(self, data: List[DataCollection]):
        """
        Sets the current data used for each of the ViewModels.
        :param data: List of new DataCollection's provided by some service
        """
        # Saving an internal reference to data collections
        self._data = data

        # Binding each model with its view, if exists
        for data_collection in data:
            if data_collection.name in self._map.keys():
                self._map[data_collection.name].set_model(data_collection)

    @pyqtSlot(name='removeData')
    def remove_data(self):
        """
        Removes the current data being used as models of the ViewModels instances.
        """
        # Clearing references
        self._data = None

        # Unbinding views
        for view in self._map.values():
            view.remove_model()


if __name__ == "__main__":
    app = QApplication([])
    widget = Panel()

    from src.package.collection import DataCollection, DataValue
    data = DataCollection(
        'Ground Speed',
        'Speed',
        'km/h'
    )
    widget.set_data(
        [
            data
        ]
    )
    data.add(DataValue(243))

    widget.show()
    app.exec()
