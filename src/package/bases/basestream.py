# PyQt5 modules
from PyQt5.QtCore import *

# PyAudio modules
from pyaudio import PyAudio, Stream
from pyaudio import paInt16

# Python modules
from queue import Queue


class Audio:
    """ Class to hold information of a sound/audio recording """

    def __init__(self, rate=44100, channels=1, audio_format=paInt16, frames_per_buffer=1024):
        self.rate = rate
        self.channels = channels
        self.format = audio_format
        self.frames_per_buffer = frames_per_buffer
        self.frames = []

    def add_frames(self, frames):
        """
        Adds new frames to the Audio recording
        :param frames: New frames being added
        """
        self.frames.append(frames)


class BaseStreamLoopSignals(QObject):
    """
    BaseStreamLoop signals used in the QRunnable thread
    """
    frames_received = pyqtSignal(bytes, name='framesReceived')


class BaseStreamLoop(QRunnable):
    """
    Non-Blocking handler to run the loop for reading/writing over a Stream
    using concurrent architecture of Qt framework.
    """

    def __init__(self, stream):
        super(BaseStreamLoop, self).__init__()
        self.setAutoDelete(False)

        # Members/Attributes of this class
        self.stream = stream
        self.queue = Queue()
        self.alive = True
        self.signals = BaseStreamLoopSignals()

    def set_alive(self, value: bool):
        """
        Closes the Stream loop on this thread.
        """
        self.alive = value

    def send_frames(self, frames: bytes, frame_count: int):
        """
        Saves in the internal queue a new item to be sent to the Stream device.
        :param frames:         Frames
        :param frame_count:    Count of frames
        """
        self.queue.put([frames, frame_count])

    def run(self):
        while self.alive:
            if self.stream.type == BaseStream.Input:
                data = self.stream.stream.read(self.stream.frames_per_buffer)
                self.signals.frames_received.emit(data)
            elif self.stream.type == BaseStream.Output:
                if not self.queue.empty():
                    self.stream.stream.write(*self.queue.get())


class BaseStream(QObject):
    """ Base class for streaming sub-classes """

    """ Stream devices states """
    Disabled = 'Disabled'
    Idle = 'Idle'
    Streaming = ' Streaming'

    """ Stream devices types """
    Input = 'Input'
    Output = 'Output'

    """ Stream devices signals or events """
    state_changed = pyqtSignal(str, name='stateChanged')
    stream_stopped = pyqtSignal(name='streamStopped')
    frames_received = pyqtSignal(bytes, name='framesReceived')

    @pyqtProperty(str)
    def type(self) -> str:
        return self._type

    @pyqtProperty(str)
    def state(self) -> str:
        return self._state

    @pyqtProperty(Stream)
    def stream(self) -> Stream:
        return self._stream

    def __init__(self, stream_type: str, rate=44100, channels=1, audio_format=paInt16, frames_per_buffer=1024):
        super(BaseStream, self).__init__()

        # Private members/attributes of this class
        self._state = BaseStream.Idle
        self._type = stream_type

        # Public members/attributes of this class
        self.rate = rate
        self.channels = channels
        self.format = audio_format
        self.frames_per_buffer = frames_per_buffer

        # Handlers or helpers
        self._py_audio = PyAudio()
        self._stream = self._py_audio.open(
            rate=rate,
            channels=channels,
            format=audio_format,
            frames_per_buffer=frames_per_buffer,
            input=True if self._type == BaseStream.Input else False,
            output=True if self._type == BaseStream.Output else False
        )

        # Configuring the internal loop handler with private slot
        self._pool = QThreadPool()
        self._loop = BaseStreamLoop(self)
        self._loop.signals.frames_received.connect(self.frames_received.emit)

    def __del__(self):
        super(BaseStream, self).__del__()
        self._stream.stop_stream()
        self._stream.close()
        self._py_audio.terminate()

    @pyqtSlot(bytes, int, name='writeFrames')
    def write_frames(self, frames: bytes, frames_count: int):
        if self.state == BaseStream.Streaming:
            self._loop.send_frames(frames, frames_count)

    @pyqtSlot(name='startStream')
    def start_stream(self):
        """
        Starts recording or playing in the Stream device configured.
        """
        if self.state == BaseStream.Idle:
            # Turning on the loop enable
            self._loop.set_alive(True)

            # Changing Stream class state
            self.set_state(BaseStream.Streaming)

            # Running the ThreadPool
            self._pool.start(self._loop)

    @pyqtSlot(name='stopStream')
    def stop_stream(self):
        """
        Stops the streaming device.
        """
        if self.state == BaseStream.Streaming:
            # Turning on the loop enable
            self._loop.set_alive(False)

            # Changing Stream class state
            self.set_state(BaseStream.Idle)
            self.stream_stopped.emit()

    @pyqtSlot(str, name='setState')
    def set_state(self, value: str):
        """
        Changes the current state of the Stream object and updates or notifies.
        :param value: Current new value for the State
        """
        self._state = value
        self.state_changed.emit(self._state)
