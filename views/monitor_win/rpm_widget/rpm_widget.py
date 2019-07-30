"""
RPM class to show evolution through time
"""
# python native modules

# third-party modules
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# sae project modules
from fend.core.sae_fend import SAEFend
from fend.interface.interface import Events
from fend.interface.properties.angular_speed import RPMAngularSpeed


class RPMGraphWidget(QWidget):

    def __init__(self, parent=None, fend: SAEFend = None):
        QWidget.__init__(self, parent)

        self.rpm_values = []
        self.rpm_time = []
        self._fend = fend
        self.canvas = FigureCanvasQTAgg(Figure())

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        # self.canvas.axes.hold(False)
        # self.canvas.axes.set_title("RPM")
        # self.canvas.axes.xaxis.set_ticklabels([])  # to hide x axis values

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.setLayout(vertical_layout)

        if fend is not None:
            self._fend.angular_speed.property_changed.subscribe(self, self.update_graph)

    def __del__(self):
        if self._fend is not None:
            self._fend.angular_speed.property_changed.unsubscribe(self)

    def update_graph(self, id, data):
        if self._fend is not None:
            self.rpm_values.append(self._fend.angular_speed.value)
            if len(self.rpm_time) is not 0:
                last = self.rpm_time[len(self.rpm_time)-1]
                self.rpm_time.append(last + 1)
            else:
                self.rpm_time.append(0)

            if len(self.rpm_time) > self._fend.angular_speed.max_length:
                del self.rpm_time[0]
                del self.rpm_values[0]
            self.canvas.axes.plot(self.rpm_time, self.rpm_values, color="k", linewidth=1)
            self.canvas.draw()

    def set_sae_fend(self, fend: SAEFend):
        if fend is not None:
            self._fend = fend
            self._fend.angular_speed.property_changed.subscribe(self, self.update_graph)
