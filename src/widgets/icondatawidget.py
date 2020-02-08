# PyQt5 modules
from PyQt5.QtGui import QPaintEvent, QPainter, QIcon, QBrush, QPainterPath, QColor, QFont, QFontMetrics, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QVBoxLayout, QSizePolicy, QLayout
from PyQt5.QtCore import QSize, QPoint, QRectF, Qt
from PyQt5.QtCore import pyqtProperty, pyqtSlot

# Python modules
from enum import Enum
from math import floor
from os import getcwd, path

# Project modules
from src.widgets.bases.utils import draw_adjusted_text, draw_head_arrow, proxy_property, quick_property


class IconWidget(QWidget):
    """ Shows an icon
    """

    icon = quick_property(QIcon, 'icon')
    icon_size = quick_property(int, 'icon_size')

    def __init__(self, parent=None):
        super(IconWidget, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self._icon = QIcon()
        self._icon_size = 40

    @pyqtSlot(name='onUpdate')
    def update(self):
        """
        Updates the widget view.
        """
        super(IconWidget, self).update()
        self.updateGeometry()

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
        return QSize(self.icon_size, self.icon_size)

    def minimumSizeHint(self):
        return self.sizeHint()

    def minimumSize(self):
        return self.sizeHint()


class DataStatus(Enum):
    Increasing = "Increasing"
    Decreasing = "Decreasing"
    Steady = "Steady"


class ArrowWidget(QWidget):
    """ Shows an arrow up or down according to the current value status
    """

    arrow_width = quick_property(int, 'arrow_width')
    arrow_height = quick_property(int, 'arrow_height')
    up_brush = quick_property(QBrush, 'up_brush')
    down_brush = quick_property(QBrush, 'down_brush')

    def __init__(self, parent=None):
        super(ArrowWidget, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self._down_brush = QBrush(QColor(255, 0, 0))
        self._up_brush = QBrush(QColor(0, 255, 0))
        self._status = DataStatus.Steady
        self._arrow_width = 15
        self._arrow_height = 15

    @pyqtSlot(name='onUpdate')
    def update(self):
        """
        Updates the widget view.
        """
        super(ArrowWidget, self).update()
        self.updateGeometry()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)

        if self._status != DataStatus.Steady:
            draw_head_arrow(
                painter,
                True if self._status == DataStatus.Increasing else False,
                self.size().width() // 2, self.size().height() // 2,
                self.arrow_width, self.arrow_height,
                self.up_brush if self._status == DataStatus.Increasing else self.down_brush
            )

    def resizeEvent(self, event):
        self.update()

    def sizeHint(self):
        return QSize(self.arrow_width, self.arrow_height * 2)

    def minimumSizeHint(self):
        return self.sizeHint()

    def minimumSize(self):
        return self.sizeHint()

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

    text_font = quick_property(QFont, 'text_font')
    value = quick_property(int, 'value')
    label = quick_property(str, 'label')

    @pyqtProperty(str)
    def text(self) -> str:
        return "{} {}".format(self.value, self.label)

    def __init__(self, parent=None):
        super(ValueWidget, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self._value = 0
        self._label = ''
        self._text_font = QFont()

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
    def update(self):
        """
        Updates the widget view.
        """
        super(ValueWidget, self).update()
        self.updateGeometry()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        draw_adjusted_text(
            painter,
            self.text,
            self.text_font,
            self.size().width() // 2,
            self.size().height() // 2
        )

    def resizeEvent(self, event):
        self.update()

    def sizeHint(self):
        metrics = QFontMetrics(self.text_font)
        size = metrics.boundingRect(self.text)
        return QSize(size.width(), size.height())

    def minimumSizeHint(self):
        return self.sizeHint()

    def minimumSize(self):
        return self.sizeHint()


class IconData(QWidget):
    """ Visualizes a numeric value with an icon related to what
        the data's value mean, and it shows whether the value has been
        increasing or decreasing from previous samples.
    """

    value = proxy_property('value_widget', ValueWidget, 'value')
    label = proxy_property('value_widget', ValueWidget, 'label')
    text_font = proxy_property('value_widget', ValueWidget, 'text_font')

    up_brush = proxy_property('arrow_widget', ArrowWidget, 'up_brush')
    down_brush = proxy_property('arrow_widget', ArrowWidget, 'down_brush')

    icon = proxy_property('icon_widget', IconWidget, 'icon')

    def __init__(self, parent=None):
        super(IconData, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        # Setting up the widget
        self.icon_widget = IconWidget()
        self.value_widget = ValueWidget()
        self.arrow_widget = ArrowWidget()

        # Setting up the layouts
        self.data_layout = QVBoxLayout()
        self.data_layout.setSpacing(0)
        self.data_layout.addWidget(self.icon_widget, alignment=Qt.AlignHCenter)
        self.data_layout.addWidget(self.value_widget, alignment=Qt.AlignHCenter)

        self.arrow_layout = QVBoxLayout()
        self.arrow_layout.setSpacing(0)
        self.arrow_layout.addWidget(self.arrow_widget, alignment=Qt.AlignVCenter)

        self.main_layout = QHBoxLayout(self)
        self.main_layout.setSpacing(5)
        self.main_layout.addLayout(self.data_layout)
        self.main_layout.addLayout(self.arrow_layout)
        self.setLayout(self.main_layout)

        # Default settings
        self.value = 12.0
        self.label = 'V'
        self.text_font = QFont('Rockwell', 15)

        self.icon = QIcon(path.join(getcwd(), '..', '..', 'assets', 'battery', 'battery.png'))

    @pyqtSlot(name='onUpdate')
    def update(self):
        super(IconData, self).update()

        self.icon_widget.update()
        self.value_widget.update()
        self.arrow_widget.update()

        self.updateGeometry()

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
