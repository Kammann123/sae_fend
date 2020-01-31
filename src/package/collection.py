# PyQt5 modules
from PyQt5.QtCore import QObject, pyqtSignal

# Python modules
from time import time
from typing import List


class DataValue(QObject):
    """ DataValue contains an individual value with any metadata we
        would like it to contain.
    """

    def __init__(self, value):
        super(DataValue, self).__init__()

        # Class private attributes
        self._timestamp = time()
        self._value = float(value)

    def __eq__(self, other) -> bool:
        return self._timestamp == other.timestamp

    @property
    def value(self):
        return self._value

    @property
    def timestamp(self):
        return self._timestamp


class DataCollection(QObject):
    """ DataCollection instances hold a collection of data values related to any
        type of magnitude, and allow their manipulation through several events,
        and other features.
    """

    # Class signals definition
    increased = pyqtSignal()
    decreased = pyqtSignal()
    remained = pyqtSignal()
    collectionChanged = pyqtSignal()
    valueAdded = pyqtSignal(DataValue)
    valueRemoved = pyqtSignal(DataValue)

    def __init__(self, values: List[DataValue] = None):
        super(DataCollection, self).__init__()

        # Default arguments control
        if values is None:
            values = []

        # Class private attributes
        self._values = values
        self._last_value_added = None

    @property
    def values(self):
        return self._values

    def add(self, value: DataValue):
        """
        Adds a new value to the DataCollection.
        :param value: New DataValue to be added
        """
        if isinstance(value, DataValue):
            # Add new value
            self._values.append(value)

            # Emitting corresponding signals
            self.valueAdded.emit(value)
            self.collectionChanged.emit()
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

    def remove_by_timestamp(self, timestamp: float) -> bool:
        """
        Removes a DataValue from the collection, it identifies
        the element by its timestamp.
        :param timestamp: The DataValue's timestamp
        :return Boolean value on success
        """
        for value in self._values:
            if value.timestamp == timestamp:
                self.remove(value)
                return True
        else:
            return False

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
                self.valueRemoved.emit(value)
                self.collectionChanged.emit()
                return True
        return False
