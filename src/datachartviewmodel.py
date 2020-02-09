# PyQt5 modules
from PyQt5.QtCore import pyqtSlot

# Project modules
from src.package.bases.collectionviewmodel import BaseViewModel
from src.widgets.datachartwidget import DataChart


class DataChartViewModel(BaseViewModel):
    """ This is the ViewModel for a DataChart widget to be used a View of any
        DataCollection model.
    """

    def __init__(self, widget: DataChart):
        super(DataChartViewModel, self).__init__(widget)

    def __unbind__(self):
        # Clean widget slot connections
        if self.model is not None:
            self.model.value_added.disconnect(self.set_values)

    def __bind__(self):
        # Create new connections to model's signals
        self.model.value_added.connect(self.set_values)
        self.set_values()

        # Updating the DataChart metadata
        self.widget.set_title(self.model.name)
        self.widget.set_labels("", f"{self.model.magnitude} [{self.model.units}]")

    @pyqtSlot(name='setValues')
    def set_values(self):
        """
        Whenever there is a change in the current state of DataCollection,
        this slot parses data and calls the widget's slot.
        """
        self.widget.set_data(self.model.timestamps, self.model.values)
