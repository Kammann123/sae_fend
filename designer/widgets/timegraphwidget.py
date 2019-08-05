"""
Time through graphic widget's base class
"""
# python native modules

# third-party modules
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# sae project modules

class TimeGraphWidget(QWidget):

    # TimeGraphWidget's signals
    valueChanged = pyqtSignal(float)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # Components
        self.curr = 0
        self._value = []
        self.canvas = FigureCanvasQTAgg(Figure())

        # Canvas' setting
        self.canvas.axes = self.canvas.figure.add_subplot(111)

        # Layout setting
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.setLayout(vertical_layout)

        # Widget General Setting
        self.resetName()
        self.resetXLabel()
        self.resetYLabel()
        self.resetXVisibility()
        self.resetYVisibility()
        self.resetYLowLim()
        self.resetYTopLim()
        self.resetBufferLen()

    def paintEvent(self, event):
        self.canvas.axes.clear()

        self.canvas.axes.plot(0, self._low_lim, marker="o", color="k", markersize=0.1)
        self.canvas.axes.plot(0, self._top_lim, marker="o", color="k", markersize=0.1)

        self.canvas.axes.plot(self._value, color="k", linewidth=1)
        self.canvas.draw()

    def resizeEvent(self, event):
        self.update()

    # Getter, setter and resetter of value property
    def getValue(self):
        return self._value[self.curr]

    @pyqtSlot(float)
    def setValue(self, value: float):
        if self.curr >= len(self._value):
            del self._value[0]
            self._value.append(0)
            self.curr += 1

        self._value[self.curr] = value
        self.valueChanged.emit(value)

    def resetValue(self):
        for i in range(len(self._value)):
            self._value[i] = 0

    # Getter, setter and resetter of the graph name
    def setName(self, name: str):
        self.canvas.figure.suptitle(name)
        self._name = name

    def resetName(self):
        self.canvas.figure.suptitle("")
        self._name = ""

    def getName(self):
        return self._name

    # Getter, setter and resetter of the buffer length
    def setBufferLen(self, length: int):
        if length > len(self._value):
            for i in range(length - len(self._value)):
                self._value.append(0)
        else:
            for i in range(len(self._value)-length):
                del self._value[0]

    def resetBufferLen(self):
        self._value = [0]

    def getBufferLen(self):
        return len(self._value)

    # Getter, setter and resetter of y axe lower limit
    def setYLowLim(self, lim: float):
        self._low_lim = lim

    def resetYLowLim(self):
        self._low_lim = 0

    def getYLowLim(self):
        return self._low_lim

    # Getter, setter and resetter of y axe top limit
    def setYTopLim(self, lim: float):
        self._top_lim = lim

    def resetYTopLim(self):
        self._top_lim = 10

    def getYTopLim(self):
        return self._top_lim

    # Getter, setter and resetter of x axe visibility
    def setXVisibility(self, visibility: bool):
        self.canvas.axes.get_xaxis().set_visible(visibility)

    def resetXVisibility(self):
        self.canvas.axes.get_xaxis().set_visible(True)

    def getXVisibility(self):
        return self.canvas.axes.get_xaxis().get_visible()

    # Getter, setter and resetter of y axe visibility
    def setYVisibility(self, visibility: bool):
        self.canvas.axes.get_yaxis().set_visible(visibility)

    def resetYVisibility(self):
        self.canvas.axes.get_yaxis().set_visible(True)

    def getYVisibility(self):
        return self.canvas.axes.get_yaxis().get_visible()

    # Getter, setter and resetter x label
    def setXLabel(self, label: str):
        self.canvas.axes.set_xlabel(label)

    def resetXLabel(self):
        self.canvas.axes.set_xlabel("X")

    def getXLabel(self):
        self.canvas.axes.get_xlabel()

    # Getter, setter and resetter y label
    def setYLabel(self, label: str):
        self.canvas.axes.set_xlabel(label)

    def resetYLabel(self):
        self.canvas.axes.set_xlabel("Y")

    def getYLabel(self):
        self.canvas.axes.get_xlabel()

    # TimeGraphWidget's Properties
    yLabel = pyqtProperty(float, getYLabel, setYLabel, resetYLabel)
    xLabel = pyqtProperty(float, getXLabel, setXLabel, resetXLabel)
    yVisibility = pyqtProperty(bool, getYVisibility, setYVisibility, resetYVisibility)
    xVisibility = pyqtProperty(bool, getXVisibility, setXVisibility, resetXVisibility)
    name = pyqtProperty(str, getName, setName, resetName)
    yAxeLowLim = pyqtProperty(float, getYLowLim, setYLowLim, resetYLowLim)
    yAxeTopLim = pyqtProperty(float, getYTopLim, setYTopLim, resetYTopLim)
    bufferLength = pyqtProperty(int, getBufferLen, setBufferLen, resetBufferLen)

if __name__ == "__main__":
    app = QApplication([])
    widget = TimeGraphWidget()
    widget.show()
    app.exec()