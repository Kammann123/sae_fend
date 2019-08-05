"""
Thermometer Widget Plugin
"""

# python native modules

# third-party modules
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from PyQt5.QtGui import QIcon

# sae project modules
from designer.widgets.thermometer import ThermometerWidget


class ThermometerPlugin(QPyDesignerCustomWidgetPlugin):
    """ ThermometerPlugin Class. """

    def __init__(self, parent=None):
        super(ThermometerPlugin, self).__init__(parent)
        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return ThermometerWidget(parent)

    def name(self):
        return "ThermometerWidget"

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
        return '<widget class="ThermometerWidget" name="thermometerWidget">\n' \
               ' <property name="toolTip">\n' \
               '  <string>Click and drag here</string>\n' \
               ' </property>\n' \
               ' <property name="whatsThis">\n' \
               '  <string>Temperature visualizer. ' \
               ' </string>\n' \
               ' </property>\n' \
               '</widget>\n'

    def includeFile(self):
        return "thermometer"
