"""
Sample 04. MainWindow ViewController tests!
"""

# python native modules

# third-party modules
from PyQt5 import QtWidgets

# sae project modules
from fend.core.sae_fend import SAEFend

from views.main_win.main_window_logic import MainWindow


if __name__ == "__main__":
    # Constant values
    BUFFER_LENGTH = 100

    # Instances
    app = QtWidgets.QApplication([])
    fend_model = SAEFend(BUFFER_LENGTH)
    fend_view_controller = MainWindow(fend_model)

    # Setup and show methods
    fend_view_controller.show()

    # Running loop
    app.exec_()
