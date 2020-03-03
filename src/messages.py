# PyQt5 modules
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem
from PyQt5.QtCore import pyqtSlot, pyqtSignal

# Project modules
from src.ui.messages import Ui_Messages
from src.message import MessageWidget


class MessagesWidget(QWidget, Ui_Messages):
    """ Displays a list of messages in a box.
    """

    message_selected = pyqtSignal(str, name='messageSelected')

    def __init__(self, parent=None):
        super(MessagesWidget, self).__init__(parent)
        self.setupUi(self)

        # Private members/attributes of the class
        self.messages = []
        self.item_messages = []

        self.message_box.itemSelectionChanged.connect(
            lambda: self.message_selected.emit(self.messages[self.message_box.currentRow()].message)
        )

    @pyqtSlot(str, name='addMessage')
    def add_message(self, text: str):
        """
        Adds a new message to the Messages
        :param text:
        """
        if text != '':
            new_message = MessageWidget(text)
            new_item = QListWidgetItem(self.message_box)
            new_item.setSizeHint(new_message.sizeHint())
            self.messages.append(new_message)
            self.item_messages.append(new_item)
            self.message_box.insertItem(0, new_item)
            self.message_box.setItemWidget(new_item, new_message)


if __name__ == "__main__":
    app = QApplication([])
    widget = MessagesWidget()
    widget.add_message("Mensaje en memoria 1")
    widget.add_message("Mensaje en memoria 2")
    widget.add_message("Mensaje en memoria 3")
    widget.add_message("Mensaje en memoria 4")
    widget.show()
    app.exec()
