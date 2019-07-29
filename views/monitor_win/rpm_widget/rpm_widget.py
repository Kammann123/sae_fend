"""
RPM class to show evolution through time
"""
# python native modules

# third-party modules
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure

# sae project modules
from fend.core.sae_fend import SAEFend
from fend.interface.interface import Events
from fend.interface.properties.angular_speed import RPMAngularSpeed


class RPMGraphWidget(QWidget):

    def __init__(self, fend: SAEFend, parent=None):
        QWidget.__init__(self, parent)

        self.rpm_values = []
        self.rpm_time = []
        self._fend = fend
        self.canvas = FigureCanvas(Figure())
        self.canvas.axes.set_title("RPM")
        self.canvas.axes.xaxis.set_ticklabels([])  # to hide x axis values

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)

        self._fend.angular_speed.property_changed.subscribe(self, self.update_graph)

    def __del__(self):
        self._fend.angular_speed.property_changed.unsubscribe(self)

    def update_graph(self):
        self.rpm_values.append(self._fend.angular_speed.value)
        last = self.rpm_time[len(self.rpm_time)-1]
        self.rpm_time.append(last + 1)
        if len(self.rpm_time) > self._fend.angular_speed.max_length:
            del self.rpm_time[0]
            del self.rpm_values[0]
        self.canvas.axes.plot(self.rpm_time, self.rpm_time)
        self.canvas.draw()
