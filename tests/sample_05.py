"""
Sample 05. Testing the monitor window
"""
# python native modules
import random
import threading
import time
import sys

# third-party modules

# sae project modules
from pypublisher.subscriber import Subscriber
from fend.core.sae_fend import SAEFend
from fend.interface.properties.angular_speed import RPMAngularSpeed
from views.monitor_win.monitor_window_logic import MonitorWindow, QtWidgets


class BackEnd(Subscriber):
    """ BackEnd Simulator.-
    """

    def __init__(self, fend: SAEFend):
        Subscriber.__init__(self)

        # Keep the front end reference
        self.front_end = fend

        # Start catching rpm values from car
        thread = threading.Thread(target=self.__catch_rmp_value, daemon=True)
        thread.start()

    def __catch_rmp_value(self):
        while True:
            time.sleep(0.1)
            rpm = random.randint(3000, 7000)
            self.front_end.update(RPMAngularSpeed, rpm)


if __name__ == "__main__":

    # Constant values
    BUFFER_LENGTH = 100

    # Instances
    app = QtWidgets.QApplication([])
    front_end = SAEFend(BUFFER_LENGTH)
    back_end = BackEnd(front_end)
    window = MonitorWindow(front_end)

    # start running
    window.show()
    sys.exit(app.exec_())

