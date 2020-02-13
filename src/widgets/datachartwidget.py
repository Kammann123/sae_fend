# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLayout
from PyQt5.QtCore import pyqtSlot, pyqtProperty, Qt
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont

from pyqtgraph import PlotWidget, PlotDataItem, mkPen

# Project modules
from src.widgets.bases.utils import quick_property

# Python modules
from typing import Union, List
from numpy import array
from random import random
from time import time, sleep


class DataChart(PlotWidget):
    """ DataChart Widget acts as a View of a DataCollection model, so it displays
        its values as a function of time, using a QtChart. This component is meant
        to be capable of reloading its model every time is needed.
    """

    def __init__(self, parent=None):
        super(DataChart, self).__init__(parent, background=QColor(0, 0, 0, 0))

        # Private members/attributes
        self._timestamps: List[float] = []
        self._values: List[float] = []
        self._title = ''
        self._x_label = ''
        self._y_label = ''

        # Initial configuration of the PlotWidget
        self.update()

    @pyqtSlot(name='update')
    def update(self):
        """
        Updates the current state of the PlotWidget with the internal values of the DataChart
        instance created.
        """

        # Setting the axis labels and the plot title
        self.getPlotItem().setLabels(
            left=self._y_label
        )

        # Setting the grid, menu, etc
        self.getPlotItem().setMenuEnabled(False)
        self.getPlotItem().showGrid(x=True, y=True, alpha=0.3)

        # Setting the axis configurations
        self.getPlotItem().getAxis('left').setPen(QPen(QColor(0, 0, 0), 2))
        self.getPlotItem().getAxis('bottom').setPen(QPen(QColor(0, 0, 0), 2))

        # Plot current values of the data
        self.getPlotItem().clear()
        self.getPlotItem().plot(
            x=array([index for index in range(len(self._timestamps))]),
            y=array(self._values),
            antialias=True,
            legend=self._title,
            pen=mkPen(color=(255, 200, 0), width=2),
            shadowPen=mkPen(color=(255, 200, 0, 100))
        )

    @pyqtSlot(str, name='setTitle')
    def set_title(self, value: str):
        """
        Sets the current title.
        :param value: String value
        """
        self._title = value
        self.update()

    @pyqtSlot(str, name='setLabels')
    def set_labels(self, x_label: str, y_label: str):
        """
        Sets the current axis.
        :param x_label: String value
        :param y_label: String value
        """
        self._x_label = x_label
        self._y_label = y_label
        self.update()

    @pyqtSlot(list, list, name='setData')
    def set_data(self, timestamps: List[float], values: List[float]):
        """
        Sets the current timestamps
        :param timestamps: List of timestamps
        :param values: List of values
        """
        self._timestamps = timestamps
        self._values = values
        self.update()


if __name__ == "__main__":
    app = QApplication([])
    widget = DataChart()

    widget.set_title('Engine Temperature')
    widget.set_labels('Sample', 'Temperature [°C]')

    x = []
    y = []
    for i in range(50):
        x.append(time())
        y.append(random() * 20)

    widget.set_data(x, y)

    widget.show()
    app.exec()
