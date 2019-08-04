"""
Bar Widget
"""

# python native modules

# third-party modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel

from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QPen

# sae project modules
try:
    from designer.widgets.base.algorithm import LinearAlgorithm
except:
    from base.algorithm import LinearAlgorithm


class BarWidget(QWidget):
    """ BarWidget """

    # BarWidget's Signals
    valueChanged = pyqtSignal(float)

    def __init__(self, parent=None):
        super(BarWidget, self).__init__(parent)

        # Standard parameter configuration
        self.setMinimumSize(QSize(30, 200))
        self.setWindowTitle("Bar Widget")

        # Resetting the properties
        self.resetValue()
        self.resetMinValue()
        self.resetMaxValue()
        self.resetIsHorizontal()
        self.resetIsInverted()
        self.resetTextMargin()
        self.resetMargin()
        self.resetRadius()
        self.resetColor()

        # Components
        self.label = QLabel(self)
        self.label.setNum(self.value)
        self.valueChanged.connect(self.label.setNum)

    def paintEvent(self, event):
        # Setting up instances
        painter = QPainter(self)
        brush = QBrush()
        pen = QPen()

        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(pen)
        painter.setBrush(brush)

        # Bar size computing...
        width = self.size().width() - self.margin * 2
        height = self.size().height() - self.margin * 2 - self.label.height() - self.textMargin

        # Text Printing...
        self.label.move(
            self.size().width() / 2 - self.label.width() / 2,
            self.size().height() - self.margin - self.label.height()
        )

        # Bar drawing...
        painter.drawRoundedRect(
            self.margin,
            self.margin,
            width,
            height,
            self.radius,
            self.radius
        )

        # Filling the bar...
        brush.setColor(self.color)
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.setPen(pen)

        yPositionAlgorithm = LinearAlgorithm(
            self.minValue,
            self.size().height() - self.margin - self.label.height() - self.textMargin if not self.isInverted else self.margin,
            self.maxValue,
            self.margin
        )

        xPositionAlgorithm = LinearAlgorithm(
            self.minValue,
            self.margin if not self.isInverted else self.size().width() - self.margin,
            self.maxValue,
            self.margin
        )

        heightAlgorithm = LinearAlgorithm(
            self.minValue,
            0,
            self.maxValue,
            height
        )

        widthAlgorithm = LinearAlgorithm(
            self.minValue,
            0,
            self.maxValue,
            width
        )

        painter.drawRoundedRect(
            xPositionAlgorithm(self.value) if self.isHorizontal else self.margin,
            yPositionAlgorithm(self.value) if not self.isHorizontal else self.margin,
            widthAlgorithm(self.value) if self.isHorizontal else width,
            heightAlgorithm(self.value) if not self.isHorizontal else height,
            self.radius,
            self.radius
        )

    # Getter, setter, resetter of value property
    def getValue(self):
        return self._value

    @pyqtSlot(float)
    def setValue(self, value: float):
        self._value = value
        self.update()
        self.valueChanged.emit(value)

    def resetValue(self):
        self._value = 68

    # Getter, setter, resetter of minValue property
    def getMinValue(self):
        return self._minValue

    def setMinValue(self, value: float):
        self._minValue = value
        self.update()

    def resetMinValue(self):
        self._minValue = 0

    # Getter, setter, resetter of maxValue property
    def getMaxValue(self):
        return self._maxValue

    def setMaxValue(self, value: float):
        self._maxValue = value
        self.update()

    def resetMaxValue(self):
        self._maxValue = 100

    # Getter, setter, resetter of isHorizontal property
    def getIsHorizontal(self):
        return self._isHorizontal

    def setIsHorizontal(self, value: bool):
        self._isHorizontal = value
        self.update()

    def resetIsHorizontal(self):
        self._isHorizontal = False

    # Getter, setter, resetter of isInverted property
    def getIsInverted(self):
        return self._isInverted

    def setIsInverted(self, value: bool):
        self._isInverted = value
        self.update()

    def resetIsInverted(self):
        self._isInverted = False

    # Getter, setter, resetter of margin property
    def getMargin(self):
        return self._margin

    def setMargin(self, value: float):
        self._margin = value
        self.update()

    def resetMargin(self):
        self._margin = 10

    # Getter, setter, resetter of radius property
    def getRadius(self):
        return self._radius

    def setRadius(self, value: float):
        self._radius = value
        self.update()

    def resetRadius(self):
        self._radius = 12

    # Getter, setter, resetter of color property
    def getColor(self):
        return self._color

    def setColor(self, value: QColor):
        self._color = value
        self.update()

    def resetColor(self):
        self._color = QColor(220, 0, 100)

    # Getter, setter, resetter of textMargin property
    def getTextMargin(self):
        return self._textMargin

    def setTextMargin(self, value: float):
        self._textMargin = value
        self.update()

    def resetTextMargin(self):
        self._textMargin = 10

    # BarWidget's Properties
    value = pyqtProperty(float, getValue, setValue, resetValue)
    minValue = pyqtProperty(float, getMinValue, setMinValue, resetMinValue)
    maxValue = pyqtProperty(float, getMaxValue, setMaxValue, resetMaxValue)

    isHorizontal = pyqtProperty(bool, getIsHorizontal, setIsHorizontal, resetIsHorizontal)
    isInverted = pyqtProperty(bool, getIsInverted, setIsInverted, resetIsInverted)
    textMargin = pyqtProperty(float, getTextMargin, setTextMargin, resetTextMargin)
    margin = pyqtProperty(float, getMargin, setMargin, resetMargin)
    radius = pyqtProperty(float, getRadius, setRadius, resetRadius)
    color = pyqtProperty(QColor, getColor, setColor, resetColor)


if __name__ == "__main__":
    app = QApplication([])
    widget = BarWidget()
    widget.show()
    app.exec()
