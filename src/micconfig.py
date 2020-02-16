# PyQt5 modules
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSlot, pyqtSignal

# Python modules
from pyaudio import PyAudio, paDirectSound

# Project modules
from src.ui.micconfig import Ui_MicConfig
from src.package.bases.basestream import StreamDevice


# noinspection PyTypeChecker
class MicConfig(QWidget, Ui_MicConfig):
    """ Custom QWidget to configure and test the new settings for an input streaming device
    """

    """ MicConfig's signals """
    settings_changed = pyqtSignal(dict, name='settingsChanged')

    def __init__(self, parent=None):
        super(MicConfig, self).__init__(parent)
        self.setupUi(self)

        # Loading streaming devices into the configuration
        self.stream_devices = StreamDevice.get_devices()
        self.devices.addItems(
            [
                stream.name
                for stream in self.stream_devices
                if stream.is_input and stream.host_api == paDirectSound
            ]
        )

        # Settings configurations
        p = PyAudio()
        self.settings = {
            "rate": int(self.sample_rate.text()),
            "channels": int(self.channels.text()),
            "format": p.get_format_from_width(self.format.currentIndex() + 1),
            "frames_per_buffer": int(self.frames_per_buffer.text()),
            "device_index": None
        }
        p.terminate()

        self.apply.clicked.connect(self.apply_changes)

    @pyqtSlot(name='applyChanges')
    def apply_changes(self):
        """
        Saves current changes made on the settings.
        """
        p = PyAudio()

        try:
            self.settings['rate'] = int(self.sample_rate.text())
            self.settings['channels'] = int(self.channels.text())
            self.settings['format'] = p.get_format_from_width(self.format.currentIndex() + 1)
            self.settings['frames_per_buffer'] = int(self.frames_per_buffer.text())

            for stream_device in self.stream_devices:
                if stream_device.name == self.devices.currentText():
                    self.settings['device_index'] = stream_device.index
                    break

            self.settings_changed.emit(self.settings)
        finally:
            p.terminate()


if __name__ == "__main__":
    app = QApplication([])
    mic = MicConfig()
    mic.show()
    app.exec()
