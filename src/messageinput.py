# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit
from PyQt5.QtCore import pyqtSlot, pyqtSignal, Qt
from PyQt5.QtGui import QKeyEvent

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
        self.message.keyPressEvent = self.keyPressEvent

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

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Return:
            self.on_send_clicked()
        else:
            QTextEdit.keyPressEvent(self.message, event)


if __name__ == "__main__":
    app = QApplication([])
    panel = MessageInputWidget()
    panel.show()
    app.exec()
