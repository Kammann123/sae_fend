# PyQt5 modules
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPaintEvent
from PyQt5.QtCore import QSize


class CircularGauge(QWidget):
    """ Shows a circular bar graph according to the current value, it expects
        to be told the minimum and maximum value, which defines the relative bar position.
        It also shows the numeric value.
    """

    def __init__(self, parent=None):
        super(CircularGauge, self).__init__(parent)

    def paintEvent(self, event: QPaintEvent):
        pass

    def sizeHint(self) -> QSize:
        pass


if __name__ == "__main__":
    app = QApplication([])
    widget = CircularGauge()
    widget.show()
    app.exec()
