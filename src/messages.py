# PyQt5 modules
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt

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

    @pyqtSlot(str, name='addMessage')
    def add_message(self, text: str):
        """
        Adds a new message to the Messages
        :param text:
        """
        if text != '':
            new_message = MessageWidget(text)
            new_message.clicked.connect(lambda message: self.message_selected.emit(message))
            self.messages.append(new_message)
            self.messages_box.addWidget(new_message)


if __name__ == "__main__":
    app = QApplication([])
    widget = MessagesWidget()
    widget.add_message("Mensaje en memoria")
    widget.show()
    app.exec()
