"""
SAEFend class
"""

# python native modules

# third-party modules

# sae project modules
from fend.interface.interface import FendInterface

from pystates.state_object import StateObject

from fend.core.states import InitialWindowState
from fend.core.states import SetupWindowState
from fend.core.states import MonitorWindowState
from fend.core.states import ErrorState
from fend.core.states import CloseState

from fend.core.events import GoBack
from fend.core.events import Finished
from fend.core.events import Close
from fend.core.events import ErrorOccurred


class SAEFend(FendInterface, StateObject):
    """ SAEFend core class """

    def __init__(self, buffer_length: int):
        FendInterface.__init__(self, buffer_length)
        StateObject.__init__(self)

        # Setting up the state flow of the SAEFend Object
        self.set_flow(InitialWindowState, Finished, SetupWindowState)
        self.set_flow(InitialWindowState, ErrorOccurred, ErrorState)
        self.set_flow(InitialWindowState, Close, CloseState)

        self.set_flow(SetupWindowState, Finished, MonitorWindowState)
        self.set_flow(SetupWindowState, ErrorOccurred, ErrorState)
        self.set_flow(SetupWindowState, Close, CloseState)

        self.set_flow(MonitorWindowState, GoBack, SetupWindowState)
        self.set_flow(MonitorWindowState, ErrorOccurred, ErrorState)
        self.set_flow(MonitorWindowState, Close, CloseState)

        self.set_default(InitialWindowState)
        self.restart()

