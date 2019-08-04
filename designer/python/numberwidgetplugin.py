"""
Number Widget Plugin
"""

# python native modules

# third-party modules
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from PyQt5.QtGui import QIcon

# sae project modules
from numberwidget import NumberWidget


class NumberWidgetPlugin(QPyDesignerCustomWidgetPlugin):
    """ NumberWidget Plugin Class. """

    def __init__(self, parent=None):
        super(NumberWidgetPlugin, self).__init__(parent)
        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return NumberWidget(parent)

    def name(self):
        return "NumberWidget"

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
        return '<widget class="NumberWidget" name="numberWidget">\n' \
               ' <property name="toolTip">\n' \
               '  <string>Click and drag here</string>\n' \
               ' </property>\n' \
               ' <property name="whatsThis">\n' \
               '  <string>Number Widget. ' \
               ' </string>\n' \
               ' </property>\n' \
               '</widget>\n'

    def includeFile(self):
        return "numberwidget"