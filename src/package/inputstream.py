# PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot, pyqtSignal, pyqtProperty

# PyAudio modules
from pyaudio import *

# Python modules
from typing import List

# Project modules
from src.package.bases.basestream import BaseStream, Audio


class InputStream(BaseStream):
    """ BaseStream's child class for an input stream to get or record
        realtime audio and sound from any audio input as a microphone can be
    """

    """ InputStream's events or signals """
    frames_recorded = pyqtSignal(bytes, int, name='framesRecorded')
    audio_recorded = pyqtSignal(Audio, name='audioRecorded')

    @pyqtProperty(list)
    def audios(self) -> List[Audio]:
        return self._audios

    def __init__(self, rate=48000, channels=1, audio_format=paInt16, frames_per_buffer=1024):
        super(InputStream, self).__init__(
            BaseStream.Input,
            rate,
            channels,
            audio_format,
            frames_per_buffer
        )

        # Audio recording, saving log of recorded sounds and audios
        self._current_audio = None
        self._audios: List[Audio] = []

        # Connections to the BaseStream
        self.frames_received.connect(self.process_frames)
        self.disabled.connect(self.stop)

    @pyqtSlot(name='start')
    def start(self):
        """
        Starts recording and streaming the input audio received from the configured device.
        """
        if self.state == BaseStream.Idle:
            self._current_audio = Audio(self.rate, self.channels, self.format, self.frames_per_buffer)
            self.start_stream()

    @pyqtSlot(name='stop')
    def stop(self):
        """
        Stops recording and streaming, it will save a copy of the audio recorded while it was streaming.
        """
        if self.state == BaseStream.Streaming or self.state == BaseStream.Disabled:
            self.stop_stream()
            self._audios.append(self._current_audio)
            self.audio_recorded.emit(self._current_audio)
            self._current_audio = None

    @pyqtSlot(bytes, name='processFrames')
    def process_frames(self, data: bytes):
        """
        Callback used to process frames being recorded by the realtime stream used through the PyAudio binding library.
        :param data: Frames received
        """
        if self._current_audio is not None:
            self._current_audio.add_frames(data)
        self.frames_recorded.emit(data, self.frames_per_buffer)


if __name__ == "__main__":
    app = QApplication([])
    stream = InputStream()
    app.exec()
