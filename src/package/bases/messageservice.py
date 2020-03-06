# PyQt modules
from PyQt5.QtCore import pyqtSlot

# Project modules
from src.package.bases.baseservice import BaseService


class MessageService(BaseService):
    """ MessageService is an interface that declares the way GUI controls connect
    to the underground service that sends the messages to the other point of the
    communication """

    @pyqtSlot(str, name='sendMessage')
    def send_message(self, message: str):
        """
        Sends a new string/text message.
        :param message: New message to be sent
        """
        raise NotImplementedError

    @pyqtSlot(int, name='sendMemoryMessage')
    def send_memory_message(self, index: int):
        """
        Sends an indexed in memory message
        :param index: Message's index
        """
        raise NotImplementedError
