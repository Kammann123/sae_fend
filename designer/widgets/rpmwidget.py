"""
RPMWidget

Custom QTDesigner widget to visualize RPM values of a car's engine.
"""

# python native modules

# third-party modules
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot, pyqtSignal, pyqtProperty

# sae project modules


class BaseRPMWidget(QWidget):
    """ BaseRPMWidget
    Defines the property interface for the widget.
    """

    def __init__(self, parent=None):
        super(BaseRPMWidget, self).__init__(parent)

    # Base signals
    valueChanged = pyqtSignal(float)

    # Getter, Setter and Resetter of the value property
    def getValue(self):
        return self._value

    @pyqtSlot(float)
    def setValue(self, value: float):
        self._value = value
        self.valueChanged.emit(self._value)

    def resetValue(self):
        self._value = 0

    value = pyqtProperty(float, getValue, setValue, resetValue)


class RPMWidget(BaseRPMWidget):
    """ RPMWidget custom widget """

    def __init__(self, parent=None):
        super(RPMWidget, self).__init__(parent)

        self.setWindowTitle("RPMWidget")

    def paintEvent(self, event):

        painter = QPainter()


if __name__ == "__main__":
    app = QApplication([])
    widget = RPMWidget()
    widget.show()
    app.exec()
