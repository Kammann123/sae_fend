# PyQt5 modules
from PyQt5.QtCore import QObject, pyqtSlot, pyqtProperty
from PyQt5.QtWidgets import QWidget

# Project modules
from src.package.collection import DataCollection, DataValue


class BaseViewModel(QObject):
    """ Defines a general o base interface for any ViewModel used to link a DataCollection
        as model with a widget as a view
    """

    @pyqtProperty(DataCollection)
    def previous_model(self) -> DataCollection:
        return self._previous_model

    @pyqtProperty(DataCollection)
    def model(self) -> DataCollection:
        return self._model

    @pyqtProperty(QWidget)
    def widget(self) -> QWidget:
        return self._widget

    def __init__(self, widget: QWidget):
        super(BaseViewModel, self).__init__()
        self._widget = widget
        self._previous_model = None
        self._model = None

    def __bind__(self):
        """
        Handler to be overwritten by any child class, to define
        how the widget and the model should be connecting one to each other
        """
        raise NotImplementedError

    @pyqtSlot(DataValue, name='setValue')
    def set_value(self, value: DataValue):
        """
        Handler to set the widget's value using a DataValue input,
        could be said to be a pipe.
        :param value: DataValue to be translated
        """
        self._widget.set_value(value.value)

    @pyqtSlot(DataCollection, name='setModel')
    def set_model(self, value: DataCollection):
        """
        Sets the new model of the ViewModel
        :param value:  New model
        """
        self._previous_model = self._model
        self._model = value
        self.__bind__()
