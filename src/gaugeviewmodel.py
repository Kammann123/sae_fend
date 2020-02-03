# Project modules
from src.package.bases.collectionviewmodel import BaseViewModel
from src.widgets.gaugewidget import CircularGauge


class CircularGaugeViewModel(BaseViewModel):
    """ This is the ViewModel for a CircularGauge widget to be used a View of any
        DataCollection model.
    """

    def __init__(self, widget: CircularGauge):
        super(CircularGaugeViewModel, self).__init__(widget)

    def __bind__(self):
        # Clean widget slot connections
        if self.previous_model is not None:
            self.previous_model.value_added.disconnect(self.set_value)

        # Create new connections to model's signals
        self.model.value_added.connect(self.set_value)
