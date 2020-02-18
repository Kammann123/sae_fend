# PyQt modules
from PyQt5.QtCore import pyqtSignal, pyqtSlot

# Project modules
from src.package.bases.baseservice import BaseService
from src.package.bases.basestream import Audio


class StreamService(BaseService):
    """ StreamService should be an interface or pipe to connect whatever you're using to send and receive
    the communication with the widget responsible of sending and receiving that same data from user's operating system.
    For general purpose, only slot and signal may be used now.
    """

    """ StreamService's signals """
    audio_received = pyqtSignal(Audio, name='audioReceived')
    frames_received = pyqtSignal(bytes, int, name='framesReceived')

    @pyqtSlot(bytes, int, name='sendFrames')
    def send_frames(self, frames: bytes, frames_count: int):
        """
        Sending frames with the StreamService to the other point of the communication.
        :param frames:
        :param frames_count:
        """
        raise NotImplementedError

    @pyqtSlot(Audio, name='sendAudio')
    def send_audio(self, audio: Audio):
        """
        Sending audio, container of frames, with the StreamService.
        :param audio:
        """
        raise NotImplementedError
