# Project modules
from src.package.bases.collectionviewmodel import BaseViewModel
from src.widgets.icondatawidget import IconData


class IconDataViewModel(BaseViewModel):
    """ This is the ViewModel for a IconData widget to be used a View of any
        DataCollection model.
    """

    def __init__(self, widget: IconData):
        super(IconDataViewModel, self).__init__(widget)

    def __unbind__(self):
        # Clean widget slot connections
        if self.model is not None:
            self.model.increased.disconnect(self.widget.set_increasing)
            self.model.decreased.disconnect(self.widget.set_decreasing)
            self.model.remained.disconnect(self.widget.set_steady)
            self.model.value_added.disconnect(self.set_value)

    def __bind__(self):
        # Create new connections to model's signals
        self.model.increased.connect(self.widget.set_increasing)
        self.model.decreased.connect(self.widget.set_decreasing)
        self.model.remained.connect(self.widget.set_steady)
        self.model.value_added.connect(self.set_value)
