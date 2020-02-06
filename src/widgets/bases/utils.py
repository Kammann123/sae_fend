# PyQt5 modules
from PyQt5.QtGui import QPaintEvent, QPainter, QPainterPath, QFont, QBrush, QColor, QPen, QFontMetrics
from PyQt5.QtCore import QSize, QPoint, QPointF, QRectF, Qt
from PyQt5.Qt import pyqtProperty

# Python modules
from math import sin, cos, radians, floor


def quick_property(property_type, property_name):

    def getter(self):
        return getattr(self, '_{}'.format(property_name))

    def setter(self, val):
        return setattr(self, '_{}'.format(property_name), val)

    return pyqtProperty(property_type, fget=getter, fset=setter)


def proxy_property(child_name, child_type, child_property):
    meta_object = child_type.staticMetaObject
    meta_property = meta_object.property(meta_object.indexOfProperty(child_property))

    def getter(self):
        return meta_property.read(getattr(self, child_name))

    def setter(self, val):
        return meta_property.write(getattr(self, child_name), val)

    return pyqtProperty(meta_property.typeName(), fget=getter, fset=setter)


def draw_head_arrow(
        painter: QPainter,
        up: bool,
        center_x: int,
        center_y: int,
        width: int,
        height: int,
        brush: QBrush
):
    painter.save()

    pen = QPen()
    pen.setBrush(brush)
    painter.setBrush(brush)
    painter.setPen(pen)

    path = QPainterPath()
    path.moveTo(center_x + width // 2, center_y)
    path.lineTo(center_x - width // 2, center_y)
    path.lineTo(center_x, center_y - height if up else center_y + height)
    path.lineTo(center_x + width // 2, center_y)

    painter.fillPath(path, brush)
    painter.drawPath(path)

    painter.restore()


def draw_arrow(
        painter: QPainter,
        up: bool,
        x: int,
        y: int,
        width: int,
        height: int,
        brush: QBrush
):
    width_factor = 0.2
    height_factor = 0.33
    height_line = height * height_factor * 2
    width_line = width * width_factor

    painter.save()

    if up:
        painter.translate(x, y + height)
        painter.scale(1.0, -1.0)

    pen = QPen()
    pen.setBrush(brush)
    painter.setBrush(brush)
    painter.setPen(pen)

    path = QPainterPath()
    path.moveTo(width // 2 - width_line // 2, 0)
    path.lineTo(width // 2 + width_line // 2, 0)
    path.lineTo(width // 2 + width_line // 2, height_line)
    path.lineTo(width, height_line)
    path.lineTo(width // 2, height)
    path.lineTo(0, height_line)
    path.lineTo(width // 2 - width_line // 2, height_line)
    path.lineTo(width // 2 - width_line // 2, 0)

    painter.fillPath(path, brush)
    painter.drawPath(path)

    painter.restore()


def draw_labeled_value(
        painter: QPainter,
        label: str,
        value: int,
        label_font: QFont,
        value_font: QFont,
        center_x: int,
        center_y: int,
        color: QBrush = QBrush(QColor(255, 255, 255, 255))
):
    value_str = "{}".format(value)
    label_str = "{}".format(label)
    value_metrics = QFontMetrics(value_font)
    label_metrics = QFontMetrics(label_font)

    painter.save()

    center_y += abs(value_metrics.height() - label_metrics.height()) // 2

    draw_adjusted_text(
        painter,
        value_str,
        value_font,
        center_x,
        center_y - value_metrics.height() // 2,
        color
    )

    draw_adjusted_text(
        painter,
        label_str,
        label_font,
        center_x,
        center_y + label_metrics.height() // 2,
        color
    )

    painter.restore()


def draw_adjusted_text(
        painter: QPainter,
        label: str,
        font: QFont,
        center_x: int,
        center_y: int,
        color: QBrush = QBrush(QColor(255, 255, 255, 255))
):
    """
    Draw a string text with a particular format in the screen
    :param painter:
    :param label:
    :param font:
    :param center_x:
    :param center_y:
    :param color:
    """
    painter.save()
    painter.setRenderHints(QPainter.TextAntialiasing)
    painter.setFont(font)
    pen = QPen()
    pen.setBrush(color)
    painter.setPen(pen)
    metrics = QFontMetrics(font)
    label_width = metrics.boundingRect(label).width()
    label_height = metrics.boundingRect(label).height()

    painter.drawText(
        QRectF(
            center_x - label_width / 2,
            center_y - label_height / 2,
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