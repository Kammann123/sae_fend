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
    def model(self) -> DataCollection:
        return self._model

    @pyqtProperty(QWidget)
    def widget(self) -> QWidget:
        return self._widget

    def __init__(self, widget: QWidget):
        super(BaseViewModel, self).__init__()
        self._widget = widget
        self._model = None

    def __unbind__(self):
        """
        Unbinds the current model and view.
        Should be overwritten by child classes.
        """
        raise NotImplementedError

    def __bind__(self):
        """
        Binds the current model and view.
        Should be overwritten by child classes.
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
        if self.model is not None:
            self.__unbind__()
        self._model = value
        self.__bind__()

        self.widget.update()

    @pyqtSlot(name='removeModel')
    def remove_model(self):
        """
        Removes the current model.
        """
        if self.model is not None:
            self.__unbind__()
        self._model = None

        self.widget.update()
