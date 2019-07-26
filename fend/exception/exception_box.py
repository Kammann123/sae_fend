"""
ExceptionBox.
ExceptionHandler wrapper with a QtMessageBox notifying exception being catched.
"""

# python native modules

# third-party modules
from PyQt5.QtWidgets import QMessageBox

# sae project modules
from fend.exception.base.exception_handler import ExceptionHandler


class ExceptionBox(ExceptionHandler):
    """ ExceptionHandler wrapper.
    When ExceptionHandler is called at an exception being raised.
    """

    def __call__(self, *args, **kwargs):
        # Creating MessageBox and showing it to the user
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Warning)
        message_box.setWindowTitle("Application Error")
        message_box.setInformativeText("""An error has occurred while running the application. 
        More details in exception file.""")
        message_box.exec()

        # Super __call__
        ExceptionHandler.__call__(self, *args, **kwargs)
