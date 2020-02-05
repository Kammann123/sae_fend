# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal, pyqtProperty

# Python modules
from typing import List

# Project modules
from src.package.collection import DataCollection
from src.ui.slider import Ui_ChartSlider
from src.widgets.datachartwidget import DataChart
from src.datachartviewmodel import DataChartViewModel


class ChartSlider(QWidget, Ui_ChartSlider):
    """ Chart slider widget to display as a carousel several DataChart widgets
    """

    chart_changed = pyqtSignal(str, name='chartChanged')

    @pyqtProperty(bool)
    def has_charts(self) -> bool:
        return len(self._views) > 0

    def __init__(self, parent=None):
        super(ChartSlider, self).__init__(parent)
        self.setupUi(self)

        # Private class members/attributes
        self._views: List[DataChartViewModel] = []
        self._current_view = None

        # Signal and slot connections
        self.options_box.currentTextChanged.connect(self.set_current_chart)
        self.previous_button.clicked.connect(self.previous_chart)
        self.next_button.clicked.connect(self.next_chart)
        self.chart_changed.connect(self.options_box.setCurrentText)

    @pyqtSlot(name='previousChart')
    def previous_chart(self):
        """
        Goes to the previous chart, if there's one.
        """
        if self.has_charts:
            self.set_current_chart(self._views.index(self._current_view) - 1)

    @pyqtSlot(name='nextChart')
    def next_chart(self):
        """
        Goes to the next chart, if there's one.
        """
        if self.has_charts:
            self.set_current_chart(self._views.index(self._current_view) + 1)

    @pyqtSlot(int, name='setCurrentChart')
    @pyqtSlot(str, name='setCurrentChart')
    def set_current_chart(self, index):
        """
        Sets the current chart in the slider by its index.
        :param index:  Chart index in the list
        """
        if self.has_charts:
            if type(index) is int:
                if 0 <= index < len(self._views):
                    self._current_view = self._views[index]
                    self.slider_widget.setCurrentWidget(self._current_view.widget)
                    self.chart_changed.emit(self._current_view.model.name)
            elif type(index) is str:
                for view in self._views:
                    if view.model.name == index:
                        self.set_current_chart(self._views.index(view))
                        break

    @pyqtSlot(name='removeData')
    def remove_data(self):
        """
        Removes the current data being used as models of the ViewModels instances.
        """
        # Removing all widgets from the current stacked widget and
        # going back to the default setup of the ChartSlide
        for view in self._views:
            self.slider_widget.removeWidget(view.widget())
        self.options_box.clear()
        self._current_view = None
        self._views = []

    @pyqtSlot(list, name='setData')
    def set_data(self, data: List[DataCollection]):
        """
        Sets the current data used for each of the ViewModels.
        :param data: List of new DataCollection's provided by some service
        """
        # First of all, data must be removed before setting new data
        self.remove_data()

        # Then, setting the new data requires creating instances and linking models and views
        for collection in data:
            # Creating the Widget and adding it to the current layout
            widget = DataChart()
            self.slider_widget.addWidget(widget)

            # Linking the model to the view, and registering it in private list
            view = DataChartViewModel(widget)
            view.set_model(collection)
            self._views.append(view)

            # Setting up initial configuration
            if self._current_view is None:
                self._current_view = view
                self.slider_widget.setCurrentWidget(self._current_view.widget)

        # Loading ComboBox string options
        self.options_box.addItems([view.model.name for view in self._views])


if __name__ == "__main__":
    app = QApplication([])
    slider_widget = ChartSlider()
    slider_widget.show()
    app.exec()
