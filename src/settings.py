# PyQt5 modules
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import pyqtSignal, pyqtProperty

# Project modules
from src.ui.settings import Ui_Settings


class Settings(QDialog, Ui_Settings):
    """ Custom QDialog containing current session's settings for the application
    """

    """ Settings signals """
    mic_settings_changed = pyqtSignal(dict, name='micSettingsChanged')
    sound_settings_changed = pyqtSignal(dict, name='soundSettingsChanged')

    @pyqtProperty(dict)
    def mic_settings(self) -> dict:
        return self.mic_config.settings

    @pyqtProperty(dict)
    def sound_settings(self) -> dict:
        return self.sound_config.settings

    def __init__(self):
        super(Settings, self).__init__()
        self.setupUi(self)

        # Inner signals forward emitting
        self.sound_config.settings_changed.connect(lambda data: self.sound_settings_changed.emit(data))
        self.mic_config.settings_changed.connect(lambda data: self.mic_settings_changed.emit(data))


if __name__ == "__main__":
    app = QApplication([])
    settings = Settings()
    settings.show()
    app.exec()
