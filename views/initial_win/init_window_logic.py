"""
"""

# python native modules

# third-party modules

# sae project modules
from views.initial_win.init_window_view import *

from fend.core.sae_fend import SAEFend

from PyQt5 import QtWidgets


class InitWindow(QtWidgets.QWidget, Ui_InitWindow):
    """ InitialWindow class """

    LIFETIME = 3000

    def __init__(self, fend_model: SAEFend, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("ITBA SAE")

        # member
        self.fend_model = fend_model

        # animation configuration
        self.animation_time = 3000      # animation's duration in milliseconds
        self.carAnimation = QtCore.QPropertyAnimation(self.redCar, b"geometry")  # creating and configuring animation
        self.carAnimation.setDuration(self.animation_time)
        self.animationTimer = QtCore.QTimer()
        self.animationTimer.timeout.connect(self._repeat_animation)  # timer to repeat the animation when it's over
        x_car, y_car, w_car, h_car = self.redCar.geometry().getRect()
        x_win, y_win, w_win, h_win = self.geometry().getRect()
        self.carAnimation.setStartValue(QtCore.QRect(-w_car, y_car, w_car, h_car))
        self.carAnimation.setEndValue(QtCore.QRect(w_win, y_car, w_car, h_car))
        self.carAnimation.start()
        self.animationTimer.start(self.animation_time)
        self.show()

        # timer to end window's life
        self.lifeTimer = QtCore.QTimer()
        self.lifeTimer.timeout.connect(self._stop_showing)
        self.lifeTimer.start(self.LIFETIME)

    def _stop_showing(self):
        self.hide()
        self.animationTimer.stop()

    def _repeat_animation(self):
        self.carAnimation.start()
        self.animationTimer.start(self.animation_time)
