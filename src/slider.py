# PyQt5 modules
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSlot

# Python modules
from typing import List

# Project modules
from src.ui.slider import Ui_Slider
from src.package.collection import DataCollection
from src.datachartviewmodel import DataChartViewModel


class Slider(QWidget, Ui_Slider):
    """ Slider to present several data charts
    """

    def __init__(self, parent=None):
        super(Slider, self).__init__(parent)
        self.setupUi(self)

        # Private members/attributes
        self._view = DataChartViewModel(self.data_chart)
        self._data: List[DataCollection] = []
        self._current: int = 0

        # Slot connections
        self.next_button.clicked.connect(self.next)
        self.previous_button.clicked.connect(self.previous)

        # Updating before constructing...
        self.update()

    @pyqtSlot(name='next')
    def next(self):
        """
        Goes to the next slide
        """
        if self._current < len(self._data) - 1:
            self._current += 1
        self.update()

    @pyqtSlot(name='previous')
    def previous(self):
        """
        Goes to the previous slide
        """
        if self._current > 0:
            self._current -= 1
        self.update()

    @pyqtSlot(name='update')
    def update(self):
        """
        Every change is updated through this method.
        """
        if self._data:
            current_data = self._data[self._current]
            self._view.set_model(current_data)
            self.title.setText(current_data.name)

    @pyqtSlot(list, name='setData')
    def set_data(self, data: List[DataCollection]):
        """
        Sets the current data used for each of the ViewModels.
        :param data: List of new DataCollection's provided by some service
        """
        self.remove_data()
        self._data = data
        self._current = 0
        self.update()

    @pyqtSlot(name='removeData')
    def remove_data(self):
        """
        Removes the current data being used as models of the ViewModels instances.
        """
        self._view.remove_model()
        self._data = []
        self.update()


if __name__ == "__main__":
    app = QApplication([])
    slider = Slider()
    slider.show()
    app.exec()
