# PyQt5 modules
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

# Python modules
from time import time
from typing import List


class DataValue(QObject):
    """ DataValue contains an individual value with any metadata we
        would like it to contain.
    """

    @property
    def value(self):
        return self._value

    @property
    def timestamp(self):
        return self._timestamp

    def __init__(self, value):
        super(DataValue, self).__init__()

        # Class private attributes
        self._timestamp = time() * 1000
        self._value = float(value)

    def __eq__(self, other) -> bool:
        return self._timestamp == other.timestamp


class DataCollection(QObject):
    """ DataCollection instances hold a collection of data values related to any
        type of magnitude, and allow their manipulation through several events,
        and other features.
    """

    increased = pyqtSignal(name='increased')
    decreased = pyqtSignal(name='decreased')
    remained = pyqtSignal(name='remained')
    changed = pyqtSignal(name='changed')
    value_added = pyqtSignal(DataValue, name='valueAdded')
    value_removed = pyqtSignal(DataValue, name='valueRemoved')

    @property
    def max_value(self):
        return max([value.value for value in self.values])

    @property
    def min_value(self):
        return min([value.value for value in self.values])

    @property
    def min_timestamp(self):
        return min([value.timestamp for value in self.values])

    @property
    def max_timestamp(self):
        return max([value.timestamp for value in self.values])

    @property
    def first_value(self):
        if self.has_values:
            return self._values[0]
        else:
            return None

    @property
    def last_value(self):
        if self.has_values:
            return self.values[-1]
        else:
            return None

    @property
    def has_values(self) -> bool:
        return len(self._values) > 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def units(self) -> str:
        return self._units

    @property
    def timestamps(self) -> List[float]:
        return [value.timestamp for value in self._values]

    @property
    def values(self) -> List[float]:
        return [value.value for value in self._values]

    @property
    def data_values(self) -> List[DataValue]:
        return self._values

    @property
    def magnitude(self):
        return self._magnitude

    def __init__(self, name: str, magnitude: str, units: str, values: List[DataValue] = None):
        super(DataCollection, self).__init__()

        # Default arguments control
        if values is None:
            values = []

        # Class private attributes
        self._name = name
        self._units = units
        self._values = values
        self._magnitude = magnitude
        self._last_value_added = None

    @pyqtSlot(DataValue, name='add', result=bool)
    def add(self, value: DataValue):
        """
        Adds a new value to the DataCollection.
        :param value: New DataValue to be added
        """
        if isinstance(value, DataValue):
            # Add new value
            self._values.append(value)

            # Emitting corresponding signals
            self.value_added.emit(value)
            self.changed.emit()
            if self._last_value_added is not None:
                if self._last_value_added.value > value.value:
                    self.decreased.emit()
                elif self._last_value_added.value < value.value:
                    self.increased.emit()
                else:
                    self.remained.emit()
            self._last_value_added = value
        else:
            raise ValueError('Type error when adding a new value to DataCollection. DataValue expected!')

    @pyqtSlot(DataValue, name='remove', result=bool)
    def remove(self, value: DataValue) -> bool:
        """
        Removes a specific DataValue from the collection.
        :param value: The DataValue to be removed
        :return: Boolean value on success
        """
        if isinstance(value, DataValue):
            if value in self._values:
                # Deleting the DataValue element
                del self._values[self._values.index(value)]

                # Emitting the corresponding signals
                self.value_removed.emit(value)
                self.changed.emit()
                return True
        return False
