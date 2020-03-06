# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot, pyqtProperty, pyqtSignal

# Project modules
from src.ui.voicepanel import Ui_VoicePanel

from src.package.inputstream import InputStream
from src.package.outputstream import OutputStream
from src.package.bases.basestream import BaseStream, Audio


class VoicePanel(QWidget, Ui_VoicePanel):
    """ VoicePanel for input, output stream ui controls
    """
    LISTEN_RECORDING = True
    LOOP_BUFFERING = False
    ICON_STATUS = {
        'Recording': 0,
        'Listening': 1
    }

    """ Stream signals forwarding """
    frames_recorded = pyqtSignal(bytes, int, name='framesRecorded')
    audio_recorded = pyqtSignal(Audio, name='audioRecorded')
    playing_finished = pyqtSignal(name='playingFinished')
    frames_played = pyqtSignal(bytes, int, name='framesPlayed')
    stream_stopped = pyqtSignal(name='streamStopped')

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
        self._output.state_changed.connect(self.on_output_state_changed)

        # VoicePanel shows the same signals as its inner streams
        self.output_stream.playing_finished.connect(self.playing_finished.emit)
        self.output_stream.frames_played.connect(self.frames_played.emit)
        self.output_stream.stream_stopped.connect(self.stream_stopped.emit)
        self.input_stream.frames_recorded.connect(self.frames_recorded.emit)
        self.input_stream.audio_recorded.connect(self.audio_recorded.emit)
        self.input_stream.stream_stopped.connect(self.stream_stopped.emit)

        if VoicePanel.LOOP_BUFFERING:
            self._input.frames_recorded.connect(self._output.play_frames)
        elif VoicePanel.LISTEN_RECORDING:
            self._input.audio_recorded.connect(lambda audio: self._output.play_audio(audio))

        # Initial internal update
        self.on_general_update()

    @pyqtSlot(name='onGeneralUpdate')
    def on_general_update(self):
        """
        Every time something has changed, some general things should be
        modified or updated.
        """
        if self._output.state == BaseStream.Streaming:
            self.icon_widget.setCurrentIndex(VoicePanel.ICON_STATUS['Listening'])
        else:
            self.icon_widget.setCurrentIndex(VoicePanel.ICON_STATUS['Recording'])

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
