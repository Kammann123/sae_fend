"""
SAEFend States
"""

# python native modules

# third-party modules

# sae project modules
from pystates.state import State


class InitialWindowState(State):
    """ The initial window state. """
    name = "InitialWindow"


class SetupWindowState(State):
    """ The setup window state. """
    name = "SetupWindowState"


class MonitorWindowState(State):
    """ The monitor window state. """
    name = "MonitorWindowState"


class ErrorState(State):
    """ The error state. """
    name = "ErrorState"


class CloseState(State):
    """ The closing state. """
    name = "CloseState"
