# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot, pyqtSignal

# Python modules
from enum import Enum

# Project modules
# noinspection PyBroadException
from src.widgets.bases.utils import quick_property


class ToggleButton(QPushButton):
    """ Binary states button, with signals or events being emitted whenever the status changes.
        States should be refer as PrimaryState and SecondaryState.
    """
    Primary = 'PrimaryState'
    Secondary = 'SecondaryState'

    # ToggleButton's signals
    state_changed = pyqtSignal(name='stateChanged')
    primary_active = pyqtSignal(name='primaryActive')
    secondary_active = pyqtSignal(name='secondaryActive')

    # ToggleButton's properties
    state = quick_property(str, 'state')
    primary_text = quick_property(str, 'primary_text')
    secondary_text = quick_property(str, 'secondary_text')

    @primary_text.setter
    def primary_text(self, value: str):
        self._primary_text = value
        if self.state == ToggleButton.Primary:
            self.setText(self._primary_text)

    @secondary_text.setter
    def secondary_text(self, value: str):
        self._secondary_text = value
        if self.state == ToggleButton.Secondary:
            self.setText(self._secondary_text)

    def __init__(self, parent=None):
        super(ToggleButton, self).__init__(parent)

        # Private members/attributes of the class
        self._state = ToggleButton.Primary
        self._primary_text = 'PrimaryText'
        self._secondary_text = 'SecondaryText'

        # Connecting the slots and signals
        self.clicked.connect(self.toggle)

        # Initialization of the current state of the ToggleButton
        self.set_primary()

    @pyqtSlot(name='setPrimary')
    def set_primary(self):
        """
        Sets the current state of the ToggleButton to the primary one.
        """
        self._state = ToggleButton.Primary
        self.setText(self._primary_text)
        self.state_changed.emit()
        self.primary_active.emit()

    @pyqtSlot(name='setSecondary')
    def set_secondary(self):
        """
        Sets the current state of the ToggleButton to the secondary one.
        """
        self._state = ToggleButton.Secondary
        self.setText(self._secondary_text)
        self.state_changed.emit()
        self.secondary_active.emit()

    @pyqtSlot(name='toggle')
    def toggle(self):
        """
        Toggles the current state of the ToggleButton.
        """
        if self._state == ToggleButton.Primary:
            self.set_secondary()
        else:
            self.set_primary()


if __name__ == "__main__":
    app = QApplication([])
    widget = ToggleButton()
    widget.show()
    app.exec()
