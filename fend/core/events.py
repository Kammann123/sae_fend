"""
SAEFend Events
"""

# python native modules

# third-party modules

# sae project modules
from pystates.state_event import StateEvent


class GoBack(StateEvent):
    """ Go back to the previous state. """
    id = "GoBack"


class Finished(StateEvent):
    """ Current state finished doing its job, go to the
    next state. """
    id = "Finished"


class Close(StateEvent):
    """ Close the front-end. """
    id = "Close"
