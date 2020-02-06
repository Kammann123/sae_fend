# PyQt5 modules
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPaintEvent, QPainter, QPainterPath, QResizeEvent, QFont, QBrush, QColor, QPen, QFontMetrics
from PyQt5.QtCore import QSize, QPoint, QPointF, QRectF, Qt
from PyQt5.QtCore import pyqtSlot, pyqtProperty

# Project modules
# noinspection PyBroadException
try:
    from src.widgets.bases.utils import draw_adjusted_text, draw_circular_bar, draw_labeled_value, quick_property
except:
    # noinspection PyUnresolvedReferences
    from bases.utils import draw_adjusted_text, draw_circular_bar, draw_labeled_value, quick_property


class CircularGauge(QWidget):
    """ Shows a circular bar graph according to the current value, it expects
        to be told the minimum and maximum value, which defines the relative bar position.
        It also shows the numeric value.
    """

    label_font = quick_property(QFont, 'label_font')
    value_font = quick_property(QFont, 'value_font')
    label = quick_property(str, 'label')
    min_value = quick_property(int, 'min_value')
    max_value = quick_property(int, 'max_value')
    fill_color = quick_property(QBrush, 'fill_color')
    line_width = quick_property(int, 'line_width')
    line_color = quick_property(QBrush, 'line_color')
    bar_background = quick_property(QBrush, 'bar_background')
    bar_width = quick_property(int, 'bar_width')
    angle = quick_property(int, 'angle')
    span = quick_property(int, 'span')
    gauge_size = quick_property(int, 'gauge_size')

    @pyqtProperty(QPoint)
    def center(self):
        radius = min(self.width() // 2, self.height() // 2)
        return QPoint(radius, radius)

    @pyqtProperty(int)
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int):
        self._value = value
        self.update()

    def __init__(self, parent=None):
        super(CircularGauge, self).__init__(parent)

        self._fill_color = QBrush(QColor(255, 255, 255))
        self._bar_background = QBrush(QColor(0, 0, 0, 30))
        self._line_color = QBrush(QColor(0, 0, 0, 100))
        self._line_width = 1
        self._bar_width = 20
        self._angle = -120
        self._span = -300

        self._gauge_size = 200

        self._label = 'RPM'
        self._value = 25
        self._min_value = 0
        self._max_value = 100

        self._value_font = QFont()
        self._value_font.setPixelSize(100)
        self._label_font = QFont()
        self._label_font.setPixelSize(25)

    @pyqtSlot(float, name='setValue')
    @pyqtSlot(int, name='setValue')
    def set_value(self, value):
        """
        Sets a new value
        :param value: New value
        """
        self.value = int(value)

    @pyqtSlot(name='onUpdate')
    def update(self):
        """
        Updates the widget view.
        """
        super(CircularGauge, self).update()
        self.updateGeometry()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)

        draw_circular_bar(
            painter,
            self.gauge_size // 2,
            self.angle,
            self.span,
            self.bar_width,
            self.bar_background,
            self.line_color,
            self.line_width
        )

        draw_circular_bar(
            painter,
            self.gauge_size // 2,
            self.angle,
            self.span * ((self.value - self.min_value) / (self.max_value - self.min_value)),
            self.bar_width,
            self.fill_color,
            self.line_color,
            self.line_width
        )

        draw_labeled_value(
            painter,
            self.label,
            self.value,
            self.label_font,
            self.value_font,
            self.center.x(),
            self.center.y()
        )

    def resizeEvent(self, event: QResizeEvent):
        self.gauge_size = min(event.size().width(), event.size().height())
        self.resize(self.sizeHint())
        self.updateGeometry()

    def sizeHint(self):
        return QSize(self.gauge_size, self.gauge_size)

    def minimumSizeHint(self):
        return self.sizeHint()

    def minimumSize(self):
        return self.sizeHint()


if __name__ == "__main__":
    app = QApplication([])
    widget = CircularGauge()
    widget.show()
    app.exec()
