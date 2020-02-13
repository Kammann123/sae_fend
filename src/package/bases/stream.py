# PyQt5 modules
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal, pyqtSlot, pyqtProperty

# PyAudio modules
from pyaudio import PyAudio, Stream


class BaseStream(QObject):
    """ Base class for streaming sub-classes """

    """ Stream devices states """
    Disabled = 'Disabled'
    Idle = 'Idle'
    Streaming = ' Streaming'
    Blocked = ' Blocked'

    """ Stream devices types """
    Input = 'Input'
    Output = 'Output'

    """ Stream devices signals or events """
    state_changed = pyqtSignal(str, name='stateChanged')

    @pyqtProperty(str)
    def state(self) -> str:
        return self._state

    @pyqtProperty(Stream)
    def stream(self) -> Stream:
        return self._stream

    def __init__(self, stream_type: str = Stream.Input):
        super(BaseStream, self).__init__()

        # Description of the Stream type and state
        self._state = Stream.Disabled
        self._type = stream_type

        # Default setting of any streaming device opened through the PyAudio bindings
        self._rate = None
        self._channels = None
        self._format = None
        self._frames_per_buffer = None

        # Handlers or helpers
        self._py_audio = PyAudio()
        self._stream = None

    def __del__(self):
        super(BaseStream, self).__del__()
        if self._stream is not None:
            self._stream.close()
        self._py_audio.terminate()

    def open_stream(self, **kwargs):
        """
        Open a stream instance and saves the reference in the internal class.
        :param kwargs: Parameters needed for the Stream __init__() constructor
        """
        if self._stream is not None:
            self._stream.close()
        self._stream = self._py_audio.open(**kwargs)

    @pyqtSlot(str, name='setState')
    def set_state(self, value: str):
        """
        Changes the current state of the Stream object and updates or notifies.
        :param value: Current new value for the State
        """
        self._state = value
        self.state_changed.emit(self._state)
