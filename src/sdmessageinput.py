# PyQt5 modules
from PyQt5.QtWidgets import QWidget, QApplication, QMenu, QAction, QToolButton
from PyQt5.QtCore import pyqtSlot, pyqtSignal

# Project modules
from src.ui.sdmessageinput import Ui_SdMessage


class SdMessageInput(QWidget, Ui_SdMessage):
    """ Creates a ToolButton with a drop-down list to select a saved message.
    """

    send_index_message = pyqtSignal(int, name='sendIndexMessage')
    send_string_message = pyqtSignal(str, name='sendStringMessage')

    def __init__(self, parent=None):
        super(SdMessageInput, self).__init__(parent)
        self.setupUi(self)
        self.setStyleSheet("QToolButton::menu-indicator { image: none; }");

        # Private members/attributes of the class
        self.messages = [f'Mensaje en memoria {i}' for i in range(10)]

        # Connecting menu with tool button
        self.actions = [QAction(message, self) for index, message in enumerate(self.messages)]
        self.menu = QMenu()
        self.menu.addActions(self.actions)
        self.sd_button.setMenu(self.menu)
        self.sd_button.setPopupMode(QToolButton.InstantPopup)

        # Connecting slots and signals
        self.menu.triggered.connect(self.on_message_selected)

    @pyqtSlot(QAction, name='onMessageSelected')
    def on_message_selected(self, action: QAction):
        """
        When the message is selected in the drop-down list.
        """
        self.send_index_message.emit(self.actions.index(action))
        self.send_string_message.emit(action.text())


if __name__ == "__main__":
    app = QApplication([])
    widget = SdMessageInput()
    widget.show()
    app.exec()
