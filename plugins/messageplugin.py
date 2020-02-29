""" All python scripts and modules in the project may be imported with an absolute import using as root
    the root directory of the project. Only for plugins the relative import will be used because they
    are loaded by the QtDesigner tool, thus, no root directory can be used. Remember that an environment
    path has been added with the PYTHONPATH location of the widget.
"""

# PyQt5 modules
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from PyQt5.QtGui import QIcon

# Project modules
from messages import Messages


class MessagesPlugin(QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super(MessagesPlugin, self).__init__(parent)
        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return Messages(parent)

    def name(self):
        return "Messages"

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
        return '<widget class="Messages" name="message_box">\n' \
               ' <property name="toolTip">\n' \
               '  <string>Click and drag here</string>\n' \
               ' </property>\n' \
               ' <property name="whatsThis">\n' \
               '  <string>Messages Widget. ' \
               ' </string>\n' \
               ' </property>\n' \
               '</widget>\n'

    def includeFile(self):
        return "src/messages"
