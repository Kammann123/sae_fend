# PyQt5 modules
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from PyQt5.QtGui import QIcon

# Project modules
from src.widgets.gaugewidget import CircularGauge


class CircularGaugePlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(CircularGaugePlugin, self).__init__(parent)
        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return CircularGauge(parent)

    def name(self):
        return "CircularGauge"

    def group(self):
        return "SAE Widgets"

    def icon(self):
        return QIcon()

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def domXml(self):
        return '<widget class="CircularGauge" name="circular_gauge">\n' \
               ' <property name="toolTip">\n' \
               '  <string>Click and drag here</string>\n' \
               ' </property>\n' \
               ' <property name="whatsThis">\n' \
               '  <string>Circular Gauge Widget. ' \
               ' </string>\n' \
               ' </property>\n' \
               '</widget>\n'

    def includeFile(self):
        return "gaugewidget"
