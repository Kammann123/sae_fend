# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLayout
from PyQt5.QtCore import pyqtSlot, QSize, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtChart import *

# Project modules
from src.widgets.bases.utils import quick_property

# Python modules
from typing import Union, List


""" Defining the constant values and handlers to map the SeriesType into
    an instance, using the indexed position or its name
"""
SeriesTypes = [
    'Line',
    'Area',
    'Bar',
    'StackedBar',
    'PercentBar',
    'Pie',
    'Scatter',
    'Spline',
    'HorizontalBar',
    'HorizontalStackedBar',
    'HorizontalPercentBar',
    'BoxPlot',
    'Candlestick',
]


def series_type(value: Union[int, str]) -> Union[int, str]:
    """
    Returns the series type, basically it translate from the int index,
    to its string name or from the string name to the int index.
    :param value: The current form of the series type
    """
    if type(value) is int:
        return SeriesTypes[value]
    elif type(value) is str:
        return SeriesTypes.index(value)
    else:
        try:
            return series_type(int(value))
        except:
            raise ValueError('Invalid type of argument.')


def create_series(value: Union[int, str]):
    """
    Creates an instance of the series, according to the given type of series
    in the value parameter.
    :param value: The type of series that you want
    """
    try:
        index = int(value)
    except:
        index = value if type(value) is int else series_type(value)

    handlers = [
        QLineSeries,
        QAreaSeries,
        QBarSeries,
        QStackedBarSeries,
        QPercentBarSeries,
        QPieSeries,
        QScatterSeries,
        QSplineSeries,
        QHorizontalBarSeries,
        QHorizontalStackedBarSeries,
        QHorizontalPercentBarSeries,
        QBoxPlotSeries,
        QCandlestickSeries
    ]

    return handlers[index]()


class DataChart(QWidget):
    """ DataChart Widget acts as a View of a DataCollection model, so it displays
        its values as a function of time, using a QtChart. This component is meant
        to be capable of reloading its model every time is needed.
    """

    values_label = quick_property(str, 'values_label')
    title = quick_property(str, 'title')

    def __init__(
            self,
            title: str = '',
            label: str = '',
            values: List[float] = None,
            timestamps: List[float] = None,
            chart_type: Union[int, str] = QAbstractSeries.SeriesTypeLine,
            parent=None):
        super(DataChart, self).__init__(parent)
        self.setMinimumSize(QSize(640, 480))

        # Private class members or attributes
        self._series_type = chart_type
        self._values_label = label
        self._timestamps = timestamps if timestamps is not None else []
        self._values = values if values is not None else []
        self._title = title

        # Building the DataChart, set as private members of this class
        self._chart = QChart()
        self._series = None
        self._y_axis = None
        self._x_axis = None
        self._chart_view = QChartView(self._chart, self)

        # Displaying the layout in the QWidget
        self._layout = QVBoxLayout(self)
        self._layout.addWidget(self._chart_view)
        self._layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.setLayout(self._layout)

        # Updating the chart's content
        self.update_chart()

    @pyqtSlot(name='onUpdate')
    def update(self):
        """
        Updates the widget view.
        """
        super(DataChart, self).update()
        self.update_chart()

    @pyqtSlot(list, list, name='setData')
    def set_data(self, timestamps: List[float], values: List[float]):
        """
        Sets new data in the chart view and updates the widget.
        """
        self._timestamps = timestamps
        self._values = values
        self.update_chart()

    def update_chart(self):
        """
        Updates the QChart and QChartView of this Widget, setting up all of its properties,
        and adding the needed series of data.
        Here is where everything about the view is handled.
        """
        # Should clean the previous series, axes, etc that were added
        if self._series is not None:
            self._chart.removeSeries(self._series)
        if self._y_axis is not None:
            self._chart.removeAxis(self._y_axis)
        if self._x_axis is not None:
            self._chart.removeAxis(self._x_axis)

        # Creating the data series, appending every value, adding the series to the chart
        self._series = create_series(self._series_type)
        for timestamp, value in zip(self._timestamps, self._values):
            self._series.append(timestamp, value)
        self._chart.addSeries(self._series)

        # Adding new axes to the chart
        self._y_axis = QValueAxis()
        self._y_axis.setTitleText(self._values_label)

        self._x_axis = QDateTimeAxis()
        self._x_axis.setFormat("hh:mm:ss")
        self._x_axis.setTitleText("Dates")

        self._chart.addAxis(self._x_axis, Qt.AlignBottom)
        self._chart.addAxis(self._y_axis, Qt.AlignLeft)
        self._series.attachAxis(self._y_axis)
        self._series.attachAxis(self._x_axis)

        # Adding style to the chart
        self._chart.setTitle(self._title)
        self._chart.setTheme(QChart.ChartThemeQt)
        self._chart_view.setRenderHints(QPainter.HighQualityAntialiasing)

        for marker in self._chart.legend().markers(self._series):
            marker.setVisible(False)


if __name__ == "__main__":
    app = QApplication([])
    widget = DataChart(chart_type=QAbstractSeries.SeriesTypeScatter)
    widget.show()
    app.exec()
