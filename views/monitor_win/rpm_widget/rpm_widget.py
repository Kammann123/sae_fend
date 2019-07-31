"""
RPM class to show evolution through time
"""

# python native modules

# third-party modules
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# sae project modules
from views.monitor_win.graph_widget.base_widget import GraphWidget
from fend.core.sae_fend import SAEFend

from fend.interface.interface import Events
from fend.interface.properties.angular_speed import RPMAngularSpeed


class RPMGraphWidget(GraphWidget):

    def __init__(self, parent=None, fend: SAEFend = None):
        GraphWidget.__init__(self, "RPM", parent, fend)

        self.rpm_values = []
        self.rpm_time = []
        self.curr = 0

        self.canvas.axes.get_xaxis().set_visible(False)  # Hiding x axis numbers

        self.canvas.axes.set_xlabel("time")  # I don't know why is not working
        self.canvas.axes.set_ylabel("value")

        """ Subscribing to the rpm property """
        if fend is not None:
            for i in range(fend.angular_speed.max_length):
                self.rpm_values.append(0)
                self.rpm_time.append(i)

            self._fend.angular_speed.property_changed.subscribe(self, self.update_graph)

    def __del__(self):
        if self._fend is not None:
            self._fend.angular_speed.property_changed.unsubscribe(self)

    def update_graph(self, id, data):
        """ Callback to be run when the rmp's value changes"""
        if self._fend is not None:
            """ Checking if the graph is completed """
            if self.curr >= self._fend.angular_speed.max_length:
                del self.rpm_values[0]
                del self.rpm_time[0]
                self.rpm_time.append(self.rpm_time[self.curr-2]+1)
                self.rpm_values.append(0)
                self.curr -= 1

            """ Saving the current value """
            self.rpm_values[self.curr] = self._fend.angular_speed.value / 1000
            self.curr += 1
            self.canvas.axes.clear()
            self.canvas.axes.plot(self.rpm_time, self.rpm_values, color="k", linewidth=1)
            print(len(self.rpm_time))
            self.canvas.draw()

    def set_sae_fend(self, fend: SAEFend):
        if fend is not None:
            for i in range(fend.angular_speed.max_length):
                self.rpm_values.append(0)
                self.rpm_time.append(i)
            self._fend = fend
            self._fend.angular_speed.property_changed.subscribe(self, self.update_graph)
