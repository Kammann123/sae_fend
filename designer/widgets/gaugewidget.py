"""
Gauge Widget
"""

# python native modules
from math import radians
from math import sin
from math import cos

# third-party modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QPoint

from PyQt5.QtGui import QTransform
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QPen
from PyQt5.QtGui import QColor

from PyQt5.QtCore import Qt

# sae project modules


class IndexedValueAlgorithm:
    """ IndexedValueAlgorithm
    Class Methods containing different types of algorithms to
    distribute a range of values through an iterable collection of objects.
    """

    def __init__(
            self,
            from_x,
            from_y,
            to_x,
            to_y):
        self.from_x = from_x
        self.from_y = from_y
        self.to_x = to_x
        self.to_y = to_y

    def __call__(self, x):
        raise NotImplemented


class LinearAlgorithm(IndexedValueAlgorithm):
    """ LinearAlgorithm
    Linear distribution of the range of values.
    """

    def __init__(
            self,
            from_x,
            from_y,
            to_x,
            to_y):
        super(LinearAlgorithm, self).__init__(
            from_x,
            from_y,
            to_x,
            to_y)

        self.scope = (to_y - from_y) / (to_x - from_x)
        self.origin = from_y

    def __call__(self, x):
        return self.origin + self.scope * (x - self.from_x)


class AngularLine(object):
    """ AngularLine to be painted in a QPaintDevice """

    def __init__(self,
                 origin: QPoint,
                 angle: float,
                 radius_one: float,
                 radius_two: float,
                 width: float,
                 lineColor = QColor(0, 0, 0),
                 fillColor = QColor(255, 255, 255)):
        # Constructor values
        self.origin = origin
        self.angle = angle
        self.radius_one = radius_one
        self.radius_two = radius_two
        self.width = width

        # Default values
        self.lineColor = lineColor
        self.fillColor = fillColor

    def setFillColor(self, color: QColor):
        self.fillColor = color

    def setLineColor(self, color: QColor):
        self.lineColor = color

    def draw(self, painter: QPainter):
        painter.save()

        brush = QBrush()
        pen = QPen()
        brush.setColor(self.fillColor)
        brush.setStyle(Qt.SolidPattern)
        pen.setColor(self.lineColor)
        painter.setBrush(brush)
        painter.setPen(pen)

        # Delta values
        delta_x = (self.width / 2) * cos( radians(self.angle - 90) )
        delta_y = (self.width / 2) * sin( radians(self.angle - 90) )

        # Building up the polygon
        bottom_x = self.radius_one * cos( radians(self.angle) ) + self.origin.x()
        bottom_y = self.radius_one * sin( radians(self.angle) ) + self.origin.y()
        top_x = self.radius_two * cos( radians(self.angle) ) + self.origin.x()
        top_y = self.radius_two * sin( radians(self.angle) ) + self.origin.y()

        painter.drawPolygon(
            QPoint(bottom_x - delta_x, bottom_y - delta_y),
            QPoint(bottom_x + delta_x, bottom_y + delta_y),
            QPoint(top_x + delta_x, top_y + delta_y),
            QPoint(top_x - delta_x, top_y - delta_y)
        )

        painter.restore()


class RadialIndicator(AngularLine):
    """ Indicator component of the GaugeWidget. """

    def __init__(self,
                 trigger: float,
                 origin: QPoint,
                 angle: float,
                 radius_one: float,
                 radius_two: float,
                 width: float,
                 lineColor = QColor(0, 0, 0),
                 offFillColor = QColor(255, 255, 255, 100),
                 onFillColor = QColor(255, 255, 255)):
        super(RadialIndicator, self).__init__(origin,
                                              angle,
                                              radius_one,
                                              radius_two,
                                              width,
                                              lineColor,
                                              offFillColor)

        self.offFillColor = offFillColor
        self.onFillColor = onFillColor
        self.triggerValue = trigger

    def setOnFillColor(self, color: QColor):
        self.onFillColor = color

    def setOffFillColor(self, color: QColor):
        self.offFillColor = color

    def trigger(self, value: float):
        if value >= self.triggerValue:
            self.setFillColor(self.onFillColor)
        else:
            self.setFillColor(self.offFillColor)


class NeedleIndicator(object):
    """ NeedleIndicator component of the GaugeWidget. """

    def __init__(self,
                 origin: QPoint,
                 base_radius: float,
                 needle_length: float,
                 color: QColor,
                 default_angle = 0):
        self.origin = origin
        self.base_radius = base_radius
        self.needle_length = needle_length
        self.color = color
        self.angle = default_angle

    def setAngle(self, angle: float):
        self.angle = angle

    def draw(self, painter: QPainter):
        painter.save()

        brush = QBrush(Qt.SolidPattern)
        pen = QPen()
        brush.setColor(self.color)
        pen.setColor(self.color)
        painter.setBrush(brush)
        painter.setPen(pen)

        painter.drawEllipse(self.origin,
                            self.base_radius,
                            self.base_radius)

        painter.drawPolygon(
            QPoint(self.origin.x() + self.base_radius * cos(radians(self.angle - 90)),
                   self.origin.y() + self.base_radius * sin(radians(self.angle - 90))
                   ),
            QPoint(self.origin.x() + self.base_radius * cos(radians(self.angle + 90)),
                   self.origin.y() + self.base_radius * sin(radians(self.angle + 90))
                   ),
            QPoint(
                self.origin.x() + self.needle_length * cos(radians(self.angle)),
                self.origin.y() + self.needle_length * sin(radians(self.angle))
            )
        )

        painter.restore()


class GaugeWidget(QWidget):
    """ GaugeWidget """

    # GaugeWidget's signals
    valueChanged = pyqtSignal(float)

    def __init__(self, parent=None):
        super(GaugeWidget, self).__init__(parent)

        # Components
        self.indicators = []
        self.needle = None

        # Widget General Settings
        self.setWindowTitle("Gauge Widget")

        self.resetIndicatorsNumber()
        self.resetIndicatorLength()
        self.resetIndicatorWidth()
        self.resetDeltaLength()
        self.resetStartAngle()
        self.resetEndAngle()
        self.resetMargin()
        self.resetMirror()

        self.resetMaxValue()
        self.resetMinValue()
        self.resetValue()

        self.update()

    def updateComponents(self):
        """ Creates all the GaugeWidget's components by updating
        its properties or size values.
        """

        def generateIndicatorColor(index: int, indicatorsNumber: int, alpha: int):
            redComponent = 0
            greenComponent = 0
            blueComponent = 0

            begin_value = 255
            end_value = 25

            redAlgorithm = LinearAlgorithm(0, begin_value, indicatorsNumber / 3, end_value)
            greenAlgorithm = LinearAlgorithm(indicatorsNumber / 3, begin_value, indicatorsNumber * 2 / 3, end_value)
            blueAlgorithm = LinearAlgorithm(indicatorsNumber * 2 / 3, begin_value, indicatorsNumber, end_value)

            if index < indicatorsNumber / 3:
                greenComponent = redAlgorithm(index + 1)
            elif index < (indicatorsNumber * 2) / 3:
                redComponent = greenAlgorithm(index + 1)
            elif index < indicatorsNumber:
                blueComponent = blueAlgorithm(index + 1)

            return QColor(redComponent, greenComponent, blueComponent, alpha)

        radiusAlgorithm = LinearAlgorithm(
            0,
            self.size().width() / 2 - self.margin - self.deltaLength,
            self.indicatorsNumber,
            self.size().width() / 2 - self.margin)

        self.indicator = [
            RadialIndicator(
                self.minValue + (self.maxValue - self.minValue) * (index + 1) / self.indicatorsNumber,
                QPoint(self.size().width() / 2, self.size().height() - self.margin),
                self.startAngle - (self.endAngle - self.startAngle) * index / (self.indicatorsNumber - 1),
                self.size().width() / 2 - self.margin - self.indicatorLength - self.deltaLength,
                radiusAlgorithm(index),
                self.indicatorWidth,
                QColor(0, 0, 0),
                generateIndicatorColor(index, self.indicatorsNumber, 100),
                generateIndicatorColor(index, self.indicatorsNumber, 255)
            )
            for index in range(self.indicatorsNumber)
        ]

        self.needle = NeedleIndicator(
            QPoint(self.size().width() / 2, self.size().height() - self.margin),
            (self.size().width() / 2 - self.margin - self.indicatorLength) * 0.07,
            (self.size().width() / 2 - self.margin - self.indicatorLength - self.deltaLength) * 0.9,
            QColor(0, 0, 0)
        )

    def resizeEvent(self, event):
        self.update()

    def update(self):
        self.updateComponents()
        super(GaugeWidget, self).update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.mirror:
            painter.translate(self.size().width(), 0)
            painter.rotate(180)
            painter.scale(1, -1)

        for indicator in self.indicator:
            indicator.trigger(self.value)
            indicator.draw(painter)

        self.needle.setAngle(self.startAngle - (self.endAngle - self.startAngle) * (self.value - self.minValue) / (self.maxValue - self.minValue))
        self.needle.draw(painter)

        painter.end()

    # Getter, setter and resetter of indicatorsNumber
    def getIndicatorsNumber(self):
        return self._indicatorsNumber

    def setIndicatorsNumber(self, value: int):
        self._indicatorsNumber = value
        self.update()

    def resetIndicatorsNumber(self):
        self._indicatorsNumber = 100

    # Getter, setter and resetter of indicatorWidth
    def getIndicatorWidth(self):
        return self._indicatorWidth

    def setIndicatorWidth(self, value: int):
        self._indicatorWidth = value
        self.update()

    def resetIndicatorWidth(self):
        self._indicatorWidth = 4

    # Getter, setter and resetter of indicatorLength
    def getIndicatorLength(self):
        return self._indicatorLength

    def setIndicatorLength(self, value: int):
        self._indicatorLength = value
        self.update()

    def resetIndicatorLength(self):
        self._indicatorLength = 25

    # Getter, setter and resetter of startAngle
    def getStartAngle(self):
        return self._startAngle

    def setStartAngle(self, value: int):
        self._startAngle = value
        self.update()

    def resetStartAngle(self):
        self._startAngle = 180

    # Getter, setter and resetter of endAngle
    def getEndAngle(self):
        return self._endAngle

    def setEndAngle(self, value: int):
        self._endAngle = value
        self.update()

    def resetEndAngle(self):
        self._endAngle = 0

    # Getter, setter and resetter of margin
    def getMargin(self):
        return self._margin

    def setMargin(self, value: float):
        self._margin = value
        self.update()

    def resetMargin(self):
        self._margin = 30

    # Getter, setter and resetter of value property
    def getValue(self):
        return self._value

    @pyqtSlot(int)
    def setIntValue(self, value: int):
        self.setValue(float(value))

    @pyqtSlot(float)
    def setValue(self, value: float):
        self._value = value
        self.valueChanged.emit(value)
        self.update()

    def resetValue(self):
        self._value = 0

    # Getter, setter and resetter of minValue property
    def getMinValue(self):
        return self._minValue

    def setMinValue(self, value: float):
        self._minValue = value
        self.update()

    def resetMinValue(self):
        self._minValue = 0

    # Getter, setter and resetter of maxValue property
    def getMaxValue(self):
        return self._maxValue

    def setMaxValue(self, value: float):
        self._maxValue = value
        self.update()

    def resetMaxValue(self):
        self._maxValue = 10000

    # Getter, setter and resetter of the DeltaLength property
    def getDeltaLength(self):
        return self._deltaLength

    def setDeltaLength(self, value: float):
        self._deltaLength = value
        self.update()

    def resetDeltaLength(self):
        self._deltaLength = 0

    # Getter, setter and resetter of the mirror property
    def getMirror(self):
        return self._mirror

    def setMirror(self, value: bool):
        self._mirror = value
        self.update()

    def resetMirror(self):
        self._mirror = False

    # GaugeWidget's Properties
    indicatorsNumber = pyqtProperty(int, getIndicatorsNumber, setIndicatorsNumber, resetIndicatorsNumber)
    indicatorLength = pyqtProperty(int, getIndicatorLength, setIndicatorLength, resetIndicatorLength)
    indicatorWidth = pyqtProperty(int, getIndicatorWidth, setIndicatorWidth, resetIndicatorWidth)
    deltaLength = pyqtProperty(float, getDeltaLength, setDeltaLength, resetDeltaLength)
    startAngle = pyqtProperty(int, getStartAngle, setStartAngle, resetStartAngle)
    endAngle = pyqtProperty(int, getEndAngle, setEndAngle, resetEndAngle)
    margin = pyqtProperty(float, getMargin, setMargin, resetMargin)
    mirror = pyqtProperty(bool, getMirror, setMirror, resetMirror)

    value = pyqtProperty(float, getValue, setValue, resetValue)
    minValue = pyqtProperty(float, getMinValue, setMinValue, resetMinValue)
    maxValue = pyqtProperty(float, getMaxValue, setMaxValue, resetMaxValue)


if __name__ == "__main__":
    app = QApplication([])
    widget = GaugeWidget()
    widget.show()
    app.exec()
