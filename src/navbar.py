# PyQt5 modules
from PyQt5.QtWidgets import QWidget, QApplication, QListWidgetItem
from PyQt5.QtCore import pyqtSlot, pyqtSignal, pyqtProperty

# Project modules
from src.ui.navbar import Ui_NavBar
from src.soundconfig import SoundConfig
from src.micconfig import MicConfig


class NavBarWidget(QWidget, Ui_NavBar):
    """ Nav Bar for configuration menues
    """

    """ Settings signals """
    mic_settings_changed = pyqtSignal(dict, name='micSettingsChanged')
    sound_settings_changed = pyqtSignal(dict, name='soundSettingsChanged')

    @pyqtProperty(dict)
    def mic_settings(self) -> dict:
        return self.mic_setter.settings

    @pyqtProperty(dict)
    def sound_settings(self) -> dict:
        return self.sound_setter.settings

    def __init__(self, parent=None):
        super(NavBarWidget, self).__init__(parent)
        self.setupUi(self)

        self.sound_setter = SoundConfig()
        self.mic_setter = MicConfig()

        self.sound_setter.settings_changed.connect(self.sound_config_change)
        self.mic_setter.settings_changed.connect(self.mic_config_change)

        self.mic.clicked.connect(self.on_mic)
        self.sound.clicked.connect(self.on_sound)

    @pyqtSlot(name="on_mic")
    def on_mic(self):
        self.sound_setter.show()

    @pyqtSlot(name="on_sound")
    def on_sound(self):
        self.mic_setter.show()

    @pyqtSlot(dict, name="sound_config_change")
    def sound_config_change(self, data: dict):
        self.sound_settings_changed.emit(data)
        self.sound_setter.hide()

    @pyqtSlot(dict, name="mic_config_change")
    def mic_config_change(self, data: dict):
        self.mic_settings_changed.emit(data)
        self.mic_setter.hide()


if __name__ == "__main__":
    app = QApplication([])
    widget = NavBarWidget()
    widget.show()
    app.exec()
