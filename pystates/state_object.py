"""
StateObject base class
"""

# python native modules
from queue import Queue

# third-party modules

# sae project modules
from pyevents.event import Event

from pystates.state import State
from pystates.state_event import StateEvent


class StateObject(object):
    """ StateObject base class.

    A derived class of StateObject must first declare the flow using set_flow and
    set_default, then, before finishing the object's setup must execute restart.
    """

    def __init__(self):
        # State and flow members
        self._flow = {}
        self._previous = None
        self._current = None
        self._default = None

        # StateEvents members
        self._queue = Queue()

        # Object's events
        self.state_changed = Event("StateChanged")

    # Declaration/Definition methods of the
    # StateObject's state flow.

    def set_flow(self, from_state: State, event: StateEvent, to_state: State):
        """ Sets up a transition in the state flow of the object. """
        pass

    def set_default(self, default_state: State):
        """ Sets up the default state of the object. """
        pass

    def restart(self):
        """ Restarts the state of the object. """
        pass

    # Object-interaction methods with the
    # external actors.

    def send_event(self, event: StateEvent):
        """ An external actor or controller may send an event
        to the StateObject. """
        pass

    def run_event(self):
        """ Executes an event from the internal queue. """
        pass

    # Object's data access

    def previous_state(self) -> State:
        """ Returns the previous state of the object. """
        pass

    def current_state(self) -> State:
        """ Returns the current state of the object. """
        pass
