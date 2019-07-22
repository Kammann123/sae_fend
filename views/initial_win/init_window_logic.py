from views.initial_win.init_window_view import *
import threading


class InitWindow(QtWidgets.QDialog, Ui_InitWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.timer = threading.Timer(30.0, self._stop_showing)
        self.movingTimer = threading.Timer(0.025, self.update_animation)
        self.start_showing()

    def start_showing(self):
        self.show()
        self.timer.start()
        self.movingTimer.start()

    def _stop_showing(self):
        self.hide()

    # Red car animation
    def update_animation(self):
        x_car, y_car, w_car, h_car = self.redCar.geometry().getRect()
        x_win, y_win, w_win, h_win = self.geometry().getRect()
        if x_car < w_win:
            self.redCar.setGeometry(x_car + 5, y_car, w_car, h_car)
        else:
            self.redCar.setGeometry(-70, y_car, w_car, h_car)
        self.redCar.show()
        self.movingTimer.run()
