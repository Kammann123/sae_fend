# PyQt5 modules
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

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
    increased = pyqtSignal(name='increased')
    decreased = pyqtSignal(name='decreased')
    remained = pyqtSignal(name='remained')
    collection_changed = pyqtSignal(name='collectionChanged')
    value_added = pyqtSignal(DataValue, name='valueAdded')
    value_removed = pyqtSignal(DataValue, name='valueRemoved')

    def __init__(self, name: str, values: List[DataValue] = None):
        super(DataCollection, self).__init__()

        # Default arguments control
        if values is None:
            values = []

        # Class private attributes
        self._name = name
        self._values = values
        self._last_value_added = None

    @property
    def name(self):
        return self._name

    @property
    def values(self):
        return self._values

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
            self.collection_changed.emit()
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
                self.collection_changed.emit()
                return True
        return False
