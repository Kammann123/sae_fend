"""
Time through graphic widget's base class
"""
# python native modules

# third-party modules
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# sae project modules
from fend.core.sae_fend import SAEFend


class GraphWidget(QWidget):

    def __init__(self, name: str, parent=None, fend: SAEFend = None):
        QWidget.__init__(self, parent)

        self.curr = 0
        self.name = name
        self._fend = fend  # Keeping the reference of the front-end

        """ Creating and adjusting the canvas to show the graph"""
        self.canvas = FigureCanvasQTAgg(Figure())

        self.canvas.axes = self.canvas.figure.add_subplot(111)

        self.canvas.figure.suptitle(self.name)

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.setLayout(vertical_layout)

    def set_sae_fend(self, fend: SAEFend):
        if fend is not None:
            self._fend = fend

