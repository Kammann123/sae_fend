# PyQt5 modules
from PyQt5.QtCore import *

# PyAudio modules
from pyaudio import PyAudio, Stream
from pyaudio import paInt16

# Python modules
from queue import Queue
from time import time


class StreamDevice:
    """ Class to hold information of any streaming device detected by the operating system """

    """ Static variables of StreamDevice to handle devices through my own helper
        using static members and function of StreamDevice class
    """
    @staticmethod
    def get_devices() -> list:
        """
        Returns a list of detected and parsed StreamDevices.
        :return: List of StreamDevices
        """
        p = PyAudio()
        devices = []
        for i in range(p.get_device_count()):
            raw_device = p.get_device_info_by_index(i)
            device = StreamDevice(raw_device)
            devices.append(device)
        return devices

    @pyqtProperty(bool)
    def is_input(self) -> bool:
        return self.max_input_channels > 0

    @pyqtProperty(bool)
    def is_output(self) -> bool:
        return self.max_output_channels > 0

    def __init__(self, raw_settings: dict):
        self.index = raw_settings['index']
        self.name = raw_settings['name']
        self.host_api = raw_settings['hostApi']
        self.max_input_channels = raw_settings['maxInputChannels']
        self.max_output_channels = raw_settings['maxOutputChannels']
        self.default_sample_rate = raw_settings['defaultSampleRate']
        self.default_low_input_latency = raw_settings['defaultLowInputLatency']
        self.default_high_input_latency = raw_settings['defaultHighInputLatency']
        self.default_low_output_latency = raw_settings['defaultLowOutputLatency']
        self.default_high_output_latency = raw_settings['defaultHighOutputLatency']


class Audio:
    """ Class to hold information of a sound/audio recording """

    @pyqtProperty(float)
    def duration(self) -> float:
        if self.finishing_time is not None:
            return self.finishing_time - self.starting_time
        else:
            return 0.0

    def __init__(self, rate=44100, channels=1, audio_format=paInt16, frames_per_buffer=1024):
        self.rate = rate
        self.channels = channels
        self.format = audio_format
        self.frames_per_buffer = frames_per_buffer
        self.frames = []

        self.starting_time = time()
        self.finishing_time = None

    def add_frames(self, frames):
        """
        Adds new frames to the Audio recording
        :param frames: New frames being added
        """
        self.frames.append(frames)
        self.finishing_time = time()


class BaseStreamLoopSignals(QObject):
    """
    BaseStreamLoop signals used in the QRunnable thread
    """
    frames_played = pyqtSignal(bytes, int, name='framesPlayed')
    frames_received = pyqtSignal(bytes, name='framesReceived')
    frames_finished = pyqtSignal(name='framesFinished')
    stream_stopped = pyqtSignal(name='streamStopped')


class BaseStreamLoop(QRunnable):
    """
    Non-Blocking handler to run the loop for reading/writing over a Stream
    using concurrent architecture of Qt framework.
    """
    MINIMUM_QUEUE_SIZE = 5

    def __init__(self, stream):
        super(BaseStreamLoop, self).__init__()
        self.setAutoDelete(False)

        # Members/Attributes of this class
        self.signals = BaseStreamLoopSignals()
        self.stream = stream
        self.queue = Queue()
        self.alive = True

        # Internal flags
        self.minimum_queue_fulfilled = False
        self.finished_notified = False

    @pyqtSlot(name='flush')
    def flush(self):
        """
        Cleans the frames queue
        """
        self.queue = Queue()

    @pyqtSlot(bool, name='setAlive')
    def set_alive(self, value: bool):
        """
        Closes the Stream loop on this thread.
        """
        self.alive = value

    @pyqtSlot(bytes, int, name='sendFrames')
    def send_frames(self, frames: bytes, frame_count: int):
        """
        Saves in the internal queue a new item to be sent to the Stream device.
        :param frames:         Frames
        :param frame_count:    Count of frames
        """
        self.queue.put([frames, frame_count])

    @pyqtSlot(name='run')
    def run(self):
        while self.alive:
            if self.stream.type == BaseStream.Input:
                data = self.stream.stream.read(self.stream.frames_per_buffer)
                self.signals.frames_received.emit(data)
            elif self.stream.type == BaseStream.Output:
                if self.minimum_queue_fulfilled:
                    if not self.queue.empty():
                        frames, frames_count = self.queue.get()
                        self.stream.stream.write(frames, frames_count)
                        self.signals.frames_played.emit(frames, frames_count)
                        self.finished_notified = False
                    elif not self.finished_notified:
                        self.signals.frames_finished.emit()
                        self.finished_notified = True
                        self.minimum_queue_fulfilled = False
                else:
                    if self.queue.qsize() > BaseStreamLoop.MINIMUM_QUEUE_SIZE:
                        self.minimum_queue_fulfilled = True
        self.signals.stream_stopped.emit()


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
    frames_received = pyqtSignal(bytes, name='framesReceived')
    state_changed = pyqtSignal(str, name='stateChanged')
    stream_stopped = pyqtSignal(name='streamStopped')
    disabled = pyqtSignal(name='disabled')

    @pyqtProperty(int)
    def device_index(self) -> int:
        return self._settings['device_index']

    @pyqtProperty(int)
    def rate(self) -> int:
        return self._settings['rate']

    @pyqtProperty(int)
    def frames_per_buffer(self) -> int:
        return self._settings['frames_per_buffer']

    @pyqtProperty(int)
    def format(self) -> int:
        return self._settings['format']

    @pyqtProperty(int)
    def channels(self) -> int:
        return self._settings['channels']

    @pyqtProperty(str)
    def type(self) -> str:
        return self._type

    @pyqtProperty(str)
    def state(self) -> str:
        return self._state

    @pyqtProperty(Stream)
    def stream(self) -> Stream:
        return self._stream

    @pyqtProperty(dict)
    def settings(self) -> dict:
        return self._settings

    @pyqtProperty(BaseStreamLoop)
    def loop(self) -> BaseStreamLoop:
        return self._loop

    def __init__(self, stream_type: str, rate=44100, channels=1, audio_format=paInt16, frames_per_buffer=1024):
        super(BaseStream, self).__init__()

        # Private members/attributes of this class
        self._state = BaseStream.Idle
        self._type = stream_type
        self._settings = {
            "rate": rate,
            "channels": channels,
            "format": audio_format,
            "frames_per_buffer": frames_per_buffer,
            "device_index": None
        }

        # Handlers or helpers
        self._py_audio = PyAudio()
        self._stream = None

        # Configuring the internal loop handler with private slot
        self._pool = QThreadPool()
        self._loop = BaseStreamLoop(self)
        self._loop.signals.frames_received.connect(self.frames_received.emit)
        self._loop.signals.stream_stopped.connect(self.stream_stopped.emit)
        self._loop.signals.stream_stopped.connect(self.close_stream)

    def __del__(self):
        self.close_stream()
        self._py_audio.terminate()

    def set_settings(self, settings: dict):
        """
        Overwrites the internal settings used to open a new stream device.
        :param settings: New settings
        """
        self._settings = settings

    def set_settings_by_fields(self, **kwargs):
        """
        Changes the current value of individual fields in the current settings
        :param kwargs: Current values
        """
        for key, value in kwargs.items():
            self._settings[key] = value

    def close_stream(self):
        """
        Closes the current Stream device.
        """
        if self._stream is not None:
            self._stream.stop_stream()
            self._stream.close()
            self._stream = None

    def open_stream(self):
        """
        Opens a new Stream device, updating its settings
        """
        if self._stream is None:
            self._stream = self._py_audio.open(
                rate=self.settings['rate'],
                channels=self.settings['channels'],
                format=self.settings['format'],
                frames_per_buffer=self.settings['frames_per_buffer'],
                input=True if self._type == BaseStream.Input else False,
                output=True if self._type == BaseStream.Output else False,
                input_device_index=self.device_index if self._type == BaseStream.Input else None,
                output_device_index=self.device_index if self._type == BaseStream.Output else None
            )

    @pyqtSlot(name='flush')
    def flush(self):
        """
        Cleans the internal state of the class
        """
        self._loop.flush()

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
            # Opening the stream
            self.open_stream()

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

            # Note, close_stream() should be expected to be called here, but we cannot be sure
            # that the BaseStreamLoop thread has been closed to this point... so close_stream is closed
            # when it has been effectively closed!

    @pyqtSlot(str, name='setState')
    def set_state(self, value: str):
        """
        Changes the current state of the Stream object and updates or notifies.
        :param value: Current new value for the State
        """
        if value != self.state:
            self._state = value
            self.state_changed.emit(self._state)
            if value == BaseStream.Disabled:
                self.disabled.emit()
