"""
Number Widget
"""

# python native modules

# third-party modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QBrush
from PyQt5.QtGui import QPen
from PyQt5.QtGui import QColor

# sae project modules


class NumberWidget(QWidget):
    """ NumberWidget class. """

    # NumberWidget's Signals
    valueChanged = pyqtSignal(float)

    def __init__(self, parent=None):
        super(NumberWidget, self).__init__(parent)

        # General settings
        self.setWindowTitle("Number Widget")

        self.resetValue()
        self.resetMinValue()
        self.resetMaxValue()

        self.resetArrowFactor()
        self.resetArrowMargin()
        self.resetMargin()

        self.resetBackgroundColor()
        self.resetUpColor()
        self.resetOkColor()
        self.resetDownColor()

        self.resetPrefix()
        self.resetSuffix()

    def paintEvent(self, event):
        # Drawing instances...
        painter = QPainter(self)
        brush = QBrush()
        pen = QPen()

        brush.setStyle(Qt.SolidPattern)
        brush.setColor(self.backgroundColor)
        painter.setBrush(brush)

        # Computing values...
        boxWidth = self.size().width() - self.margin * 2
        boxHeight = self.size().height() - self.margin * 2
        arrowWidth = boxWidth * self.arrowFactor

        # Rectangle drawing...
        painter.drawRect(
            self.margin,
            self.margin,
            boxWidth - arrowWidth - self.arrowMargin * 2,
            boxHeight
        )

        # Text drawing...
        if self.value < self.minValue + (self.maxValue - self.minValue) / 3:
            pen.setColor(self.downColor)
        elif self.value < self.minValue + (self.maxValue - self.minValue) * 2 / 3:
            pen.setColor(self.okColor)
        elif self.value < self.minValue + (self.maxValue - self.minValue):
            pen.setColor(self.upColor)

        painter.setPen(pen)

        painter.drawText(
            self.margin,
            self.margin,
            boxWidth - arrowWidth - self.arrowMargin * 2,
            boxHeight,
            Qt.AlignHCenter | Qt.AlignVCenter,
            "{} {} {}".format(
                self.prefix,
                self.value,
                self.suffix
            )
        )

        # Triangle arrow
        if self._hasValueChanged:
            pointOne = QPoint(
                self.margin + boxWidth - arrowWidth - self.arrowMargin,
                self.size().height() / 2
            )
            pointTwo = QPoint(
                self.margin + boxWidth - self.arrowMargin,
                self.size().height() / 2
            )
            pointThree = QPoint(
                self.margin + boxWidth - self.arrowMargin - arrowWidth / 2,
                self.size().height() / 2
            )
            if self._previousValue > self._value:
                pen.setColor(QColor(255, 0, 0))
                brush.setColor(QColor(255, 0, 0))
                pointThree = QPoint(
                    self.margin + boxWidth - self.arrowMargin - arrowWidth / 2,
                    self.size().height() - self.margin - self.arrowMargin
                )
            elif self._previousValue < self._value:
                pen.setColor(QColor(0, 255, 0))
                brush.setColor(QColor(0, 255, 0))
                pointThree = QPoint(
                    self.margin + boxWidth - self.arrowMargin - arrowWidth / 2,
                    self.margin + self.arrowMargin
                )

            painter.setBrush(brush)
            painter.setPen(pen)
            painter.drawPolygon(
                pointOne,
                pointTwo,
                pointThree
            )

            # Preventing random size
            self.setMinimumSize(QSize(self.size().width(), self.size().height()))

    # Getter, setter and resetter of value property
    def getValue(self):
        return self._value

    @pyqtSlot(float)
    def setValue(self, value: float):
        self._previousValue = self._value
        self._value = value
        self._hasValueChanged = self._previousValue != self._value
        self.update()
        self.valueChanged.emit(value)

    def resetValue(self):
        self._value = 0
        self._previousValue = 0
        self._hasValueChanged = False

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
        self._maxValue = 100

    # Getter, setter and resetter of margin property
    def getMargin(self):
        return self._margin

    def setMargin(self, value: float):
        self._margin = value
        self.update()

    def resetMargin(self):
        self._margin = 5

    # Getter, setter and resetter of backgroundColor property
    def getBackgroundColor(self):
        return self._backgroundColor

    def setBackgroundColor(self, value: QColor):
        self._backgroundColor = value
        self.update()

    def resetBackgroundColor(self):
        self._backgroundColor = QColor(0, 0, 0, 225)

    # Getter, setter and resetter of upColor property
    def getUpColor(self):
        return self._upColor

    def setUpColor(self, value: QColor):
        self._upColor = value
        self.update()

    def resetUpColor(self):
        self._upColor = QColor(255, 0, 0)

    # Getter, setter and resetter of okColor property
    def getOkColor(self):
        return self._okColor

    def setOkColor(self, value: QColor):
        self._okColor = value
        self.update()

    def resetOkColor(self):
        self._okColor = QColor(0, 255, 0)

    # Getter, setter and resetter of downColor property
    def getDownColor(self):
        return self._downColor

    def setDownColor(self, value: QColor):
        self._downColor = value
        self.update()

    def resetDownColor(self):
        self._downColor = QColor(0, 0, 255)

    # Getter, setter and resetter of prefix property
    def getPrefix(self):
        return self._prefix

    def setPrefix(self, value: str):
        self._prefix = value
        self.update()

    def resetPrefix(self):
        self._prefix = ""

    # Getter, setter and resetter of suffix property
    def getSuffix(self):
        return self._suffix

    def setSuffix(self, value: str):
        self._suffix = value
        self.update()

    def resetSuffix(self):
        self._suffix = ""

    # Getter, setter, resetter of arrowFactor property
    def getArrowFactor(self):
        return self._arrowFactor

    def setArrowFactor(self, value: float):
        self._arrowFactor = value
        self.update()

    def resetArrowFactor(self):
        self._arrowFactor = 0.1

    # Getter, setter, resetter of arrowMargin property
    def getArrowMargin(self):
        return self._arrowMargin

    def setArrowMargin(self, value: float):
        self._arrowMargin = value
        self.update()

    def resetArrowMargin(self):
        self._arrowMargin = 10

    # NumberWidget's Properties
    value = pyqtProperty(float, getValue, setValue, resetValue)
    minValue = pyqtProperty(float, getMinValue, setMinValue, resetMinValue)
    maxValue = pyqtProperty(float, getMaxValue, setMaxValue, resetMaxValue)

    arrowFactor = pyqtProperty(float, getArrowFactor, setArrowFactor, resetArrowFactor)
    arrowMargin = pyqtProperty(float, getArrowMargin, setArrowMargin, resetArrowMargin)
    margin = pyqtProperty(float, getMargin, setMargin, resetMargin)

    backgroundColor = pyqtProperty(QColor, getBackgroundColor, setBackgroundColor, resetBackgroundColor)
    upColor = pyqtProperty(QColor, getUpColor, setUpColor, resetUpColor)
    okColor = pyqtProperty(QColor, getOkColor, setOkColor, resetOkColor)
    downColor = pyqtProperty(QColor, getDownColor, setDownColor, resetDownColor)

    prefix = pyqtProperty(str, getPrefix, setPrefix, resetPrefix)
    suffix = pyqtProperty(str, getSuffix, setSuffix, resetSuffix)

if __name__ == "__main__":
    app = QApplication([])
    widget = NumberWidget()
    widget.show()
    app.exec()
