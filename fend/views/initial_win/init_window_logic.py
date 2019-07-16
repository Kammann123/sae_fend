from fend.views.initial_win.init_window_view import *
import threading


class InitWindow(QtWidgets.QDialog, Ui_InitWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.timer = threading.Timer(5.0, self.stop_showing)
        self.movingTimer = threading.Timer(0.1, self.update_animation)

    def start_showing(self):
        self.show()
        self.timer.start()

    def stop_showing(self):
        self.hide()

    #Red car animation
    def update_animation(self):
        x1, y1, w, h = self.redCar.geometry().getRect()
        xf = self.geometry().getRect()
        if x1 < xf:
            self.redCar.setGeometry(x1 + 10, y1, w, h)
        else:
            self.redCar.setGeometry(-70, y1, w, h)

