# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot, pyqtProperty

# Project modules
from src.ui.voicepanel import Ui_VoicePanel

from src.package.inputstream import InputStream
from src.package.outputstream import OutputStream
from src.package.bases.basestream import BaseStream

# Python modules
import struct
import math


class VoicePanel(QWidget, Ui_VoicePanel):
    """ VoicePanel for input, output stream ui controls
    """
    LOOP_BUFFERING = False

    @pyqtProperty(InputStream)
    def input_stream(self) -> InputStream:
        return self._input

    @pyqtProperty(OutputStream)
    def output_stream(self) -> OutputStream:
        return self._output

    def __init__(self, parent=None):
        super(VoicePanel, self).__init__(parent)
        self.setupUi(self)

        # Private members/attributes of this class
        self._output = OutputStream()
        self._input = InputStream()

        # Signal and slot connections
        self.mic_button.clicked.connect(self.on_mic_clicked)
        self._input.state_changed.connect(self.on_input_state_changed)
        self._input.frames_recorded.connect(self.update_bar)
        self._input.stream_stopped.connect(self.clear_bar)
        self._output.state_changed.connect(self.on_output_state_changed)
        self._output.frames_played.connect(self.update_bar)
        self._output.stream_stopped.connect(self.clear_bar)

        if VoicePanel.LOOP_BUFFERING:
            self._input.frames_recorded.connect(self._output.play_frames)

        # Initial internal update
        self.on_general_update()

    @pyqtSlot(name='clearBar')
    def clear_bar(self):
        """
        Clears the volume bar's value when stopping the streaming device
        """
        self.volume_bar.setValue(0)

    @pyqtSlot(bytes, int, name='updateBar')
    def update_bar(self, frames: bytes, frames_count: int):
        """
        Updates the VU meter bar with the current measure of the frames
        :param frames:          Frames being processed
        :param frames_count:    Amount of frames processed
        """
        normalize_factor = 100.0 / 128.0
        shorts = struct.unpack("%dh" % (len(frames)/2), frames)
        sum_squares = 0.0
        for sample in shorts:
            n = sample * normalize_factor
            sum_squares += n * n
        self.volume_bar.setValue(int(math.sqrt(sum_squares) // len(frames)))

    @pyqtSlot(name='onGeneralUpdate')
    def on_general_update(self):
        """
        Every time something has changed, some general things should be
        modified or updated.
        """
        if self._input.state == BaseStream.Streaming:
            self.status_label.setText("Transmitiendo comunicación")
        elif self._output.state == BaseStream.Streaming:
            self.status_label.setText("Recibiendo transmisión")
        elif self._input.state == BaseStream.Idle and self._output.state == BaseStream.Idle:
            self.status_label.setText("En espera...")
        else:
            self.status_label.setText("Comunicación por voz deshabilitada")

    @pyqtSlot(name='onMicClicked')
    def on_mic_clicked(self):
        """
        When the mic button is clicked, the input stream should change its state.
        """
        if self.mic_button.isChecked():
            self._input.start()
        else:
            self._input.stop()

    @pyqtSlot(str, name='onInputStateChanged')
    def on_input_state_changed(self, state: str):
        """
        When the InputStream has changed its state.
        :param state: New state
        """
        if not VoicePanel.LOOP_BUFFERING:
            if state == BaseStream.Streaming:
                self._output.set_state(BaseStream.Disabled)
            elif state == BaseStream.Idle:
                self._output.set_state(BaseStream.Idle)
        self.on_general_update()

    @pyqtSlot(str, name='onOutputStateChanged')
    def on_output_state_changed(self, state: str):
        """
        When the OutputStream has changed its state.
        :param state: New state
        """
        if not VoicePanel.LOOP_BUFFERING:
            if state == BaseStream.Streaming:
                self._input.set_state(BaseStream.Disabled)
                self.mic_button.setEnabled(False)
            elif state == BaseStream.Idle:
                self._input.set_state(BaseStream.Idle)
                self.mic_button.setEnabled(True)
        self.on_general_update()


if __name__ == "__main__":
    app = QApplication([])
    panel = VoicePanel()
    panel.show()
    app.exec()
