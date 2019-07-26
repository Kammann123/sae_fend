"""
Main Window control methods and logic.
"""

# python native modules

# third-party modules
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets
from PyQt5 import QtCore

# sae project modules
from views.main_win.main_window_view import Ui_MainWindow

from views.initial_win.init_window_logic import InitWindow

from fend.core.sae_fend import SAEFend

from fend.core.states import InitialWindowState
from fend.core.states import SetupWindowState
from fend.core.states import MonitorWindowState
from fend.core.states import CloseState

from fend.core.events import Close


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """ MainWindow, main window class.
    """

    # Constant values
    PROCESS_TIMER = 25

    def __init__(self, fend_model: SAEFend, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # MainWindow members
        self.fend_model = fend_model

        # Subscribing to events
        self.fend_model.state_changed.subscribe(self, self.on_state_changed)

        # Background concurrent processing timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.fend_model.run)
        self.timer.start(self.PROCESS_TIMER)

        # Signals of MainWindow
        self.closeEvent = self.on_close

        # Initial view startup
        self.update_view()

    def on_state_changed(self, event_id, event_data):
        """ OnStateChanged event callback. """
        self.update_view()

    def on_close(self, event):
        """ OnClose event callback. """
        # Creating the question message box
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Question)
        message_box.setWindowTitle("Close the application")
        message_box.setInformativeText("Are you sure you want to exit the application?")
        message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Waiting for an answer
        answer = message_box.exec()

        # Closing decision...
        if answer == QMessageBox.Yes:
            self.fend_model.send_event(Close(self, None))
            event.accept()
        elif answer == QMessageBox.No:
            event.ignore()

    def update_view(self):
        """ Updates the widget's view according to the model's state. """
        state = self.fend_model.current_state()

        if state.name == InitialWindowState.name:
            self.swap_widget(InitWindow)
        elif state.name == SetupWindowState.name:
            pass
        elif state.name == MonitorWindowState.name:
            pass
        elif state.name == CloseState.name:
            self.close()

    def swap_widget(self, widget_class):
        """ Swaps the current widget for a new instance of the given class. """

        # Creating instance of the new widget
        widget_instance = widget_class(self.fend_model, self)

        # Removing the current widget
        current_widget = self.stacked_widget.currentWidget()
        self.stacked_widget.removeWidget(current_widget)

        # Resizing the widget's size

        # Replacing the new widget
        self.stacked_widget.addWidget(widget_instance)
        self.stacked_widget.setCurrentWidget(widget_instance)
