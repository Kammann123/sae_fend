# PyQt5 modules
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPaintEvent, QResizeEvent, QPainter, QBrush, QColor, QPen
from PyQt5.QtCore import QSize, pyqtSlot

# Python modules
import struct

# Project modules
from src.widgets.bases.utils import quick_property


class VoiceSignalWidget(QWidget):
    """ Displays the signal form of an array of bytes or frames
        got of a recording...
    """

    bar_color = quick_property(QBrush, 'bar_color')
    bar_margin = quick_property(int, 'bar_margin')

    def __init__(self, parent=None):
        super(VoiceSignalWidget, self).__init__(parent)

        # Private members/attributes of the VoiceSignal class
        self.frames = None
        self.frames_count = None

        self._bar_color = QBrush(QColor(255, 0, 0, 150))
        self._bar_margin = 0

    @pyqtSlot(name='clear')
    def clear(self):
        """
        Clears the current values of frames
        """
        self.frames = [0 for i in range(self.frames_count)]
        self.update()

    @pyqtSlot(bytes, int, name='setSamples')
    def set_samples(self, frames: bytes, frame_count: int):
        """
        Sets the current samples being played or recorded.
        :param frames:
        :param frame_count:
        """
        self.frames = [abs(short) for short in struct.unpack("%dh" % (len(frames)/2), frames)]
        self.frames_count = len(self.frames)
        self.update()

    def paintEvent(self, event: QPaintEvent):
        if self.frames is not None:
            painter = QPainter(self)
            painter.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)
            painter.setBrush(self.bar_color)

            pen = QPen(self.bar_color, 0)
            painter.setPen(pen)

            bar_width = (self.size().width() - self.bar_margin) / self.frames_count - self.bar_margin
            bar_factor = self.size().height() / max(self.frames) if max(self.frames) != 0 else 1

            for index, frame in enumerate(self.frames):
                painter.drawRect(
                    index * (bar_width + self.bar_margin),
                    self.size().height() // 2 - frame * bar_factor // 2,
                    int(bar_width),
                    frame * bar_factor
                )

    def resizeEvent(self, event: QResizeEvent):
        self.update()

    def sizeHint(self):
        return QSize()

    def minimumSizeHint(self):
        return self.sizeHint()

    def minimumSize(self):
        return self.sizeHint()


if __name__ == "__main__":
    app = QApplication([])
    widget = VoiceSignalWidget()
    widget.show()
    app.exec()
