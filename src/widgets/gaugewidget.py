# PyQt5 modules
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPaintEvent, QPainter, QPainterPath, QFont, QBrush, QColor, QPen, QFontMetrics
from PyQt5.QtCore import QSize, QPoint, QPointF, QRectF, Qt
from PyQt5.QtCore import pyqtSlot, pyqtProperty

# Project modules
# noinspection PyBroadException
try:
    from src.widgets.bases.utils import draw_adjusted_text, draw_circular_bar, draw_labeled_value
except:
    # noinspection PyUnresolvedReferences
    from bases.utils import draw_adjusted_text, draw_circular_bar, draw_labeled_value


class CircularGauge(QWidget):
    """ Shows a circular bar graph according to the current value, it expects
        to be told the minimum and maximum value, which defines the relative bar position.
        It also shows the numeric value.
    """

    @pyqtProperty(QFont)
    def label_font(self):
        return self._label_font

    @pyqtProperty(QFont)
    def value_font(self):
        return self._value_font

    @pyqtProperty(str)
    def label(self):
        return self._label

    @pyqtProperty(int)
    def value(self):
        return self._value

    @pyqtProperty(int)
    def min_value(self):
        return self._min_value

    @pyqtProperty(int)
    def max_value(self):
        return self._max_value

    @pyqtProperty(QBrush)
    def fill_color(self):
        return self._fill_color

    @pyqtProperty(int)
    def line_width(self):
        return self._line_width

    @pyqtProperty(QBrush)
    def line_color(self):
        return self._line_color

    @pyqtProperty(QBrush)
    def bar_background(self):
        return self._bar_background

    @pyqtProperty(int)
    def bar_width(self):
        return self._bar_width

    @pyqtProperty(int)
    def angle(self):
        return self._angle

    @pyqtProperty(int)
    def span(self):
        return self._span

    @pyqtProperty(QPoint)
    def center(self):
        radius = min(self.width() // 2, self.height() // 2)
        return QPoint(radius, radius)

    @label_font.setter
    def label_font(self, value: QFont):
        self._label_font = value

    @value_font.setter
    def value_font(self, value: QFont):
        self._value_font = value

    @label.setter
    def label(self, value: str):
        self._label = value

    @fill_color.setter
    def fill_color(self, value: QBrush):
        self._fill_color = value

    @line_width.setter
    def line_width(self, value: int):
        self._line_width = value

    @line_color.setter
    def line_color(self, value: QBrush):
        self._line_color = value

    @bar_background.setter
    def bar_background(self, value: QBrush):
        self._bar_background = value

    @bar_width.setter
    def bar_width(self, value: int):
        self._bar_width = value

    @angle.setter
    def angle(self, value: int):
        self._angle = value

    @span.setter
    def span(self, value: int):
        self.span = value

    @min_value.setter
    def min_value(self, value: int):
        self._min_value = value

    @max_value.setter
    def max_value(self, value: int):
        self._max_value = value

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

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)

        draw_circular_bar(
            painter,
            min(self.width() // 2, self.height() // 2),
            self.angle,
            self.span,
            self.bar_width,
            self.bar_background,
            self.line_color,
            self.line_width
        )

        draw_circular_bar(
            painter,
            min(self.width() // 2, self.height() // 2),
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


if __name__ == "__main__":
    app = QApplication([])
    widget = CircularGauge()
    widget.show()
    app.exec()
