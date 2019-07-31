"""
Thermometer Widget
"""

# python native modules
from math import sqrt, atan, degrees

# third-party modules
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QSize

from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QPen

from PyQt5.QtCore import Qt

# sae project modules


class BaseThermometerWidget(QWidget):
    """ BaseThermometerWidget
    Defines a thermometer widget property, signals and slots.
    """

    # ThermometerWidget's signals
    temperatureChanged = pyqtSignal(float)

    def __init__(self, parent=None):
        super(BaseThermometerWidget, self).__init__(parent)

        self.resetMinTemperature()
        self.resetMaxTemperature()
        self.resetTemperature()

    # Getter, setter and resetter of the minimum temperature value
    def getMinTemperature(self):
        return self._min_temperature

    def setMinTemperature(self, min_temperature: float):
        self._min_temperature = min_temperature

    def resetMinTemperature(self):
        self._min_temperature = 0

    # Getter, setter and resetter of the maximum temperature value
    def getMaxTemperature(self):
        return self._max_temperature

    def setMaxTemperature(self, max_temperature: float):
        self._max_temperature = max_temperature

    def resetMaxTemperature(self):
        self._max_temperature = 100.0

    # Getter, setter and resetter of the temperature value
    def getTemperature(self):
        return self._temperature

    def setTemperature(self, temperature: float):
        self._temperature = temperature
        self.temperatureChanged.emit(temperature)

    def resetTemperature(self):
        self._temperature = 0.0

    temperature = pyqtProperty(float, getTemperature, setTemperature, resetTemperature)
    maxTemperature = pyqtProperty(float, getMaxTemperature, setMaxTemperature, resetMaxTemperature)
    minTemperature = pyqtProperty(float, getMinTemperature, setMinTemperature, resetMinTemperature)


class ThermometerWidget(BaseThermometerWidget):
    """ Thermometer Widget """

    PEN_WIDTH = 2
    MARGIN = 5

    def __init__(self, parent=None):
        super(ThermometerWidget, self).__init__(parent)

        self.setMinimumSize(QSize(90, 300))
        self.setWindowTitle("Thermometer Widget")

    def updateSize(self):
        if self.size().width() < self.size().height() / 3:
            self.bottom_diameter = self.size().width() - self.MARGIN * 2
            self.top_diameter = self.bottom_diameter * 0.5

    def paintEvent(self, event):
        # Updating and resizing
        self.updateSize()

        # Instances
        painter = QPainter(self)
        pen = QPen()
        pen.setJoinStyle(Qt.RoundJoin)
        pen.setCapStyle(Qt.RoundCap)
        pen.setWidth(self.PEN_WIDTH)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(pen)

        # Frame drawing
        painter.drawLine(self.size().width() / 2 - self.top_diameter / 2,
                        self.MARGIN,
                        self.size().width() / 2 + self.top_diameter / 2,
                        self.MARGIN)

        painter.drawLine(self.size().width() / 2 - self.top_diameter / 2,
                         self.MARGIN,
                         self.size().width() / 2 - self.top_diameter / 2,
                         self.size().height() - self.MARGIN - self.bottom_diameter / 2 - self.bottom_diameter * sqrt(3 / 4) / 2)

        painter.drawLine(self.size().width() / 2 + self.top_diameter / 2,
                         self.MARGIN,
                         self.size().width() / 2 + self.top_diameter / 2,
                         self.size().height() - self.MARGIN - self.bottom_diameter / 2 - self.bottom_diameter * sqrt(3 / 4) / 2)

        painter.drawArc(self.size().width() / 2 - self.bottom_diameter / 2,
                        self.size().height() - self.bottom_diameter - self.MARGIN,
                        self.bottom_diameter,
                        self.bottom_diameter,
                        120 * 16,
                        300 * 16)

        # Computing current values
        effective_height = (self.size().height() - self.MARGIN * 2) * ((self.getTemperature() - self.getMinTemperature()) / (self.getMaxTemperature() - self.getMinTemperature()))
        current_height = (self.size().height() - self.MARGIN * 2) - effective_height
        if effective_height < float(self.bottom_diameter):
            h = effective_height - self.bottom_diameter / 2
            x = sqrt((self.bottom_diameter / 2) ** 2 - h ** 2)
            if x == 0:
                phi = -90
            else:
                phi = degrees(atan(h / x))
            alpha = 180 - phi
            beta = 180 + 2 * phi
        else:
            alpha = 90
            beta = 360

        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor(255, 0, 0))
        pen.setColor(QColor(255, 0, 0))
        painter.setPen(pen)
        painter.setBrush(brush)

        if effective_height >= self.bottom_diameter:
            painter.fillRect(self.size().width() / 2  - self.top_diameter / 2,
                             current_height + self.MARGIN,
                             self.top_diameter,
                             self.size().height() - self.MARGIN * 2 - self.bottom_diameter * sqrt(3 / 4) / 2 - current_height,
                             pen.color())


        painter.drawChord(self.size().width() / 2 - self.bottom_diameter / 2 + 2,
                          self.size().height() - self.bottom_diameter + 2 - self.MARGIN,
                          self.bottom_diameter - 3,
                          self.bottom_diameter - 3,
                          alpha * 16,
                          beta * 16)

        painter.end()

    @pyqtSlot(float)
    def setValue(self, value: float):
        self.setTemperature(value)
        self.update()


if __name__ == "__main__":
    app = QApplication([])
    widget = ThermometerWidget()

    widget.setFixedSize(QSize(50, 200))
    widget.setValue(0)

    widget.show()
    app.exec()
