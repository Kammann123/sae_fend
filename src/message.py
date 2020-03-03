# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSignal

# Project modules
from src.ui.message import Ui_Message

# Python modules
from datetime import datetime


class MessageWidget(Ui_Message, QWidget):
    """ Displays a message with a timestamp
    """

    clicked = pyqtSignal(str, name='clicked')

    def __init__(self, message: str, parent=None):
        super(MessageWidget, self).__init__(parent)
        self.setupUi(self)

        # Private members/attributes of the class
        self.message = message
        self.timestamp = datetime.now()

        self.message_label.setText(self.message)
        self.time_label.setText(self.timestamp.strftime("%H:%M"))

    def mouseReleaseEvent(self, event):
        self.clicked.emit(self.message)


if __name__ == "__main__":
    app = QApplication([])
    widget = MessageWidget(
        "Mensaje en memoria"
    )
    widget.show()
    app.exec()
