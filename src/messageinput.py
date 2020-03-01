# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal

# Project modules
from src.ui.messageinput import Ui_MessageInput


class MessageInputWidget(QWidget, Ui_MessageInput):
    """ Messages widget to handle the message sending ui function"""

    send_message = pyqtSignal(str, name='sendMessage')

    def __init__(self, parent=None):
        super(MessageInputWidget, self).__init__(parent)
        self.setupUi(self)

        # Private members/attributes
        self.messages = []

        # Signal and slot connections
        self.send_button.clicked.connect(self.on_send_clicked)

    @pyqtSlot(str, name='setMessage')
    def set_message(self, text: str):
        """
        Sets a new message in the box.
        :param text:
        """
        self.message.setText(text)

    @pyqtSlot(name='onSendClicked')
    def on_send_clicked(self):
        """
        When the send button is clicked, the message signal should be raised and the message will be saved for future
        selection.
        """
        new_message = str(self.message.toPlainText())
        if new_message == '':  # Do nothing if it is empty
            return
        else:
            self.send_message.emit(new_message)
            self.messages.append(new_message)
            self.message.clear()


if __name__ == "__main__":
    app = QApplication([])
    panel = MessageInputWidget()
    panel.show()
    app.exec()
