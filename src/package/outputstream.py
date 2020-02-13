# PyQt5 modules
from PyQt5.QtCore import pyqtSignal, pyqtSlot

# PyAudio module
from pyaudio import *

# Project modules
from src.package.bases.basestream import BaseStream, Audio


class OutputStream(BaseStream):
    """ BaseStream's child class for an output stream to play realtime audio
    """

    """ OutputStream's events or signals """
    playing_finished = pyqtSignal(name='playingFinished')

    def __init__(self, rate=48000, channels=1, audio_format=paInt16, frames_per_buffer=1024):
        super(OutputStream, self).__init__(
            BaseStream.Output,
            rate,
            channels,
            audio_format,
            frames_per_buffer
        )

        # Private members/attributes of this class
        self._audios = []
        self._frames = []

        # Setting everything up
        self.loop.signals.frames_finished.connect(self.stop)
        self.disabled.connect(self.stop)

    @pyqtSlot(Audio, name='playAudio')
    def play_audio(self, audio: Audio):
        """
        Plays an audio in the Output stream device
        :param audio: Audio to be reproduced
        """
        if not self.state == BaseStream.Disabled:
            self._audios.append(audio)
            for frame in audio.frames:
                self.write_frames(frame, audio.frames_per_buffer)
            if self.state == BaseStream.Idle:
                self.start_stream()

    @pyqtSlot(bytes, int, name='playFrames')
    def play_frames(self, frames: bytes, frames_count: int):
        """
        Plays some frames in the Output stream device
        :param frames: Frames to be reproduced
        :param frames_count: Amount of frames
        """
        if not self.state == BaseStream.Disabled:
            self._frames.append(frames)
            self.write_frames(frames, frames_count)
            if self.state == BaseStream.Idle:
                self.start_stream()

    @pyqtSlot(name='stop')
    def stop(self):
        """
        Stops reproducing content, queue is flushed.
        """
        if self.state == BaseStream.Streaming or self.state == BaseStream.Disabled:
            self.stop_stream()
            self.flush()
            self.playing_finished.emit()
