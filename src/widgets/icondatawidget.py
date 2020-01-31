# PyQt5 modules
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPaintEvent
from PyQt5.QtCore import QSize


class IconData(QWidget):
    """ Visualizes a numeric value with an icon related to what
        the data's value mean, and it shows whether the value has been
        increasing or decreasing from previous samples.
    """

    def __init__(self, parent=None):
        super(IconData, self).__init__(parent)

    def paintEvent(self, event: QPaintEvent):
        pass

    def sizeHint(self) -> QSize:
        pass


if __name__ == "__main__":
    app = QApplication([])
    widget = IconData()
    widget.shoW()
    app.exec()
