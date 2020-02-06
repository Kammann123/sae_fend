# PyQt5 modules
from PyQt5.QtGui import QPaintEvent, QPainter, QIcon, QBrush, QPainterPath, QColor, QFont, QFontMetrics, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import QSize, QPoint, QRectF, Qt
from PyQt5.QtCore import pyqtProperty, pyqtSlot

# Python modules
from enum import Enum
from math import floor

# Project modules
try:
    from src.widgets.bases.utils import draw_labeled_value, draw_arrow, proxy_property, quick_property
except:
    from bases.utils import draw_labeled_value, draw_arrow, proxy_property, quick_property


class IconWidget(QWidget):
    """ Shows an icon
    """

    icon = quick_property(QIcon, 'icon')

    def __init__(self, parent=None):
        super(IconWidget, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self._icon = QIcon()

    @pyqtSlot(name='onUpdate')
    def on_update(self):
        """
        Updates the widget view.
        """
        self.update()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)
        self.icon.paint(
            painter,
            0, 0,
            self.size().width(),
            self.size().height(),
            Qt.AlignVCenter | Qt.AlignHCenter
        )

    def resizeEvent(self, event):
        self.update()

    def sizeHint(self):
        return QSize(50, 50)


class DataStatus(Enum):
    Increasing = "Increasing"
    Decreasing = "Decreasing"
    Steady = "Steady"


class ArrowWidget(QWidget):
    """ Shows an arrow up or down according to the current value status
    """

    scale = quick_property(float, 'scale')
    up_brush = quick_property(QBrush, 'up_brush')
    down_brush = quick_property(QBrush, 'down_brush')

    def __init__(self, parent=None):
        super(ArrowWidget, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self._down_brush = QBrush(QColor(255, 0, 0))
        self._up_brush = QBrush(QColor(0, 255, 0))
        self._scale = 0.5
        self._status = DataStatus.Steady

    @pyqtSlot(name='onUpdate')
    def on_update(self):
        """
        Updates the widget view.
        """
        self.update()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)

        real_width = self.size().width() * self.scale
        real_height = self.size().height() * self.scale

        if self._status != DataStatus.Steady:
            draw_arrow(
                painter,
                True if self._status == DataStatus.Increasing else False,
                (self.size().width() - real_width) // 2, (self.size().height() - real_height) // 2,
                real_width, real_height,
                self.up_brush if self._status == DataStatus.Increasing else self.down_brush
            )

    def resizeEvent(self, event):
        self.update()

    def sizeHint(self):
        return QSize(25, 80)

    @pyqtSlot(name='setIncreasing')
    def set_increasing(self):
        self._status = DataStatus.Increasing
        self.update()

    @pyqtSlot(name='setDecreasing')
    def set_decreasing(self):
        self._status = DataStatus.Decreasing
        self.update()

    @pyqtSlot(name='setSteady')
    def set_steady(self):
        self._status = DataStatus.Steady
        self.update()


class ValueWidget(QWidget):
    """ Show a value with a labeled hint
    """

    value_font = quick_property(QFont, 'value_font')
    label_font = quick_property(QFont, 'label_font')
    value = quick_property(int, 'value')
    label = quick_property(str, 'label')

    def __init__(self, parent=None):
        super(ValueWidget, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self._value = 0
        self._label = ''
        self._value_font = QFont()
        self._label_font = QFont()

    @pyqtSlot(int, name='setValue')
    @pyqtSlot(float, name='setValue')
    def set_value(self, value):
        """
        Sets a new value
        :param value: New value
        """
        self._value = value
        self.update()

    @pyqtSlot(name='onUpdate')
    def on_update(self):
        """
        Updates the widget view.
        """
        self.update()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)

        draw_labeled_value(
            painter,
            self.label,
            self.value,
            self.label_font,
            self.value_font,
            self.size().width() // 2,
            self.size().height() // 2
        )

    def resizeEvent(self, event):
        self.update()

    def sizeHint(self):
        return QSize(100, 100)


class IconData(QWidget):
    """ Visualizes a numeric value with an icon related to what
        the data's value mean, and it shows whether the value has been
        increasing or decreasing from previous samples.
    """

    value = proxy_property('value_widget', ValueWidget, 'value')
    label = proxy_property('value_widget', ValueWidget, 'label')
    value_font = proxy_property('value_widget', ValueWidget, 'value_font')
    label_font = proxy_property('value_widget', ValueWidget, 'label_font')

    scale = proxy_property('arrow_widget', ArrowWidget, 'scale')
    up_brush = proxy_property('arrow_widget', ArrowWidget, 'up_brush')
    down_brush = proxy_property('arrow_widget', ArrowWidget, 'down_brush')

    icon = proxy_property('icon_widget', IconWidget, 'icon')

    def __init__(self, parent=None):
        super(IconData, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.icon_widget = IconWidget()
        self.value_widget = ValueWidget()
        self.arrow_widget = ArrowWidget()

        self.horizontal_layout = QHBoxLayout(self)
        self.horizontal_layout.addWidget(self.icon_widget, alignment=Qt.AlignVCenter)
        self.horizontal_layout.addWidget(self.value_widget, alignment=Qt.AlignVCenter)
        self.horizontal_layout.addWidget(self.arrow_widget, alignment=Qt.AlignVCenter)

        self.setLayout(self.horizontal_layout)

    @pyqtSlot(name='onUpdate')
    def on_update(self):
        self.icon_widget.update()
        self.value_widget.update()
        self.arrow_widget.update()

    @pyqtSlot(int, name='setValue')
    @pyqtSlot(float, name='setValue')
    def set_value(self, value):
        self.value_widget.set_value(value)

    @pyqtSlot(name='setIncreasing')
    def set_increasing(self):
        self.arrow_widget.set_increasing()

    @pyqtSlot(name='setDecreasing')
    def set_decreasing(self):
        self.arrow_widget.set_decreasing()

    @pyqtSlot(name='setSteady')
    def set_steady(self):
        self.arrow_widget.set_steady()


if __name__ == "__main__":
    app = QApplication([])
    widget = IconData()
    widget.show()
    app.exec()
