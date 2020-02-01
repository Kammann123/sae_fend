# PyQt5 modules
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPaintEvent, QPainter, QPainterPath, QFont, QBrush, QColor, QPen, QFontMetrics
from PyQt5.QtCore import QSize, QPoint, QPointF, QRectF, Qt
from PyQt5.QtCore import pyqtSlot, pyqtProperty

# Python modules
from math import sin, cos, radians, floor


def draw_adjusted_text(
        painter: QPainter,
        label: str,
        font: QFont,
        center_x: int,
        center_y: int
):
    """
    Draw a string text with a particular format in the screen
    :param painter:
    :param label:
    :param font:
    :param center_x:
    :param center_y:
    """
    painter.save()
    painter.setFont(font)
    metrics = QFontMetrics(font)
    label_width = metrics.boundingRect(label).width()
    label_height = metrics.boundingRect(label).height()

    painter.drawText(
        QRectF(
            center_x - floor(label_width / 2),
            center_y - floor(label_height / 2),
            label_width,
            label_height
        ),
        Qt.AlignHCenter,
        label
    )
    painter.restore()


def draw_circular_bar(
        painter: QPainter,
        radius: int,
        angle: int,
        span: int,
        width: int,
        fill_brush: QBrush,
        line_brush: QBrush,
        line_width: int
):
    """
    Draw a circular bar using the QPainter handler given by the outer caller.
    :param painter: Painter handler
    :param radius:  Circular radius
    :param angle:   Starting angle
    :param span:    Span angle
    :param width:   Width between circular
    :param fill_brush:  Color pattern used to fill the path
    :param line_brush:  Color pattern used to draw lines
    :param line_width:  Line width
    """
    painter.save()
    path = QPainterPath()
    path.moveTo(
        QPointF(
            (radius - width / 2) * cos(radians(angle)) + radius,
            -(radius - width / 2) * sin(radians(angle)) + radius
        )
    )
    path.lineTo(
        QPointF(
            radius * cos(radians(angle)) + radius,
            -radius * sin(radians(angle)) + radius
        )
    )
    path.arcTo(QRectF(0, 0, radius * 2, radius * 2), angle, span)
    path.lineTo(
        QPointF(
            (radius - width / 2) * cos(radians(angle + span)) + radius,
            -(radius - width / 2) * sin(radians(angle + span)) + radius
        )
    )
    path.arcTo(
        QRectF(
            width // 2, width // 2,
            radius * 2 - width, radius * 2 - width
        ),
        angle + span,
        -span
    )

    pen = QPen(line_brush, line_width)
    pen.setJoinStyle(Qt.RoundJoin)

    painter.setPen(pen)
    painter.fillPath(path, fill_brush)
    painter.drawPath(path)
    painter.restore()


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

    def __init__(self, parent=None):
        super(CircularGauge, self).__init__(parent)

        # Private class attributes definition
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

        self.resize(600, 600)

    @pyqtSlot(int, float, name='setValue')
    def set_value(self, value):
        self.value = int(value)

    def paintEvent(self, event: QPaintEvent):
        # QPainter instance to draw over this QWidget, and
        # settings to allow customizable details of the CircularGauge
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

        value_metrics = QFontMetrics(self.value_font)
        label_metrics = QFontMetrics(self.label_font)

        draw_adjusted_text(
            painter,
            "{}".format(self.value),
            self.value_font,
            self.center.x(),
            self.center.y()
        )

        draw_adjusted_text(
            painter,
            self.label,
            self.label_font,
            self.center.x(),
            self.center.y() + value_metrics.boundingRect("{}".format(self.value)).height() // 2
            + label_metrics.boundingRect(self.label).height() // 2
        )

    def sizeHint(self) -> QSize:
        return super(CircularGauge, self).sizeHint()


if __name__ == "__main__":
    app = QApplication([])
    widget = CircularGauge()
    widget.show()
    app.exec()
