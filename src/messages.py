# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot, pyqtSignal

# Project modules
from src.ui.messages import Ui_Messages

# Python modules


class MessagesWidget(QWidget, Ui_Messages):
    """ Messages widget to handle the message sending ui function"""

    send_message = pyqtSignal(str, name='sendMessage')

    def __init__(self, parent=None):
        super(MessagesWidget, self).__init__(parent)
        self.setupUi(self)

        # Private members/attributes of this class
        self.old_text = []
        self.sample_size = self.sample.sizePolicy()
        self.sample_style = self.sample.styleSheet()

        # Signal and slot connections
        self.send_button.clicked.connect(self.on_send_clicked)

        # Other things to do
        self.sample.hide()

    @pyqtSlot(name='onSendClicked')
    def on_send_clicked(self):
        """
        When the send button is clicked, the message signal should be raised and the message will be saved for future
        selection
        """
        new_message = str(self.message.toPlainText())
        if new_message == '':  # Do nothing if it is empty
            return

        self.send_message.emit(new_message)
        self.message.clear()

        is_old = False
        for each in self.old_text:
            if new_message == str(each.text()):
                is_old = True

        if not is_old:
            new_button = QPushButton(new_message)
            new_button.setSizePolicy(self.sample_size)
            new_button.setStyleSheet(self.sample_style)
            self.messeges_layout.addWidget(new_button)
            self.old_text.append(new_button)
            new_button.clicked.connect(lambda: self.get_old_message(new_button))
            self.old_text[-1].show()

    def get_old_message(self, button):
        """
        Fill the Text box with the message selected
        """
        self.message.clear()
        self.message.setText(button.text())


if __name__ == "__main__":
    app = QApplication([])
    panel = MessagesWidget()
    panel.show()
    app.exec()
