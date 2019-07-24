"""
StateObject base class
"""

# python native modules
from queue import Queue

# third-party modules

# sae project modules
from pyevents.event import Event
from pyevents.event import EventData

from pystates.state import State
from pystates.state_event import StateEvent


class StateEventNotExpected(Exception):
    def __init__(self):
        Exception.__init__(self, "The StateEvent was not expected during current state of the object.")


class NotAValidEvent(Exception):
    def __init__(self):
        Exception.__init__(self, "A valid event must be used.")


class EventTransitionAlreadyRegistered(Exception):
    def __init__(self):
        Exception.__init__(self, "Transition event has already been used with this states")


class DefaultStateNotRegistered(Exception):
    def __init__(self):
        Exception.__init__(self, "Default state must be defined before setting up the StateObject")


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

    def set_flow(self, from_state, event, to_state):
        """ Sets up a transition in the state flow of the object.
                from_state: State class
                event: StateEvent class
                to_state: State class
        """
        # Creates an instance of each class
        from_state_instance = from_state(self)
        event_instance = event(None, None)
        to_state_instance = to_state(self)

        # First time either of the states are set or declared
        if from_state_instance not in self._flow.keys():
            self._flow[from_state_instance] = {}
        if to_state_instance not in self._flow.keys():
            self._flow[to_state_instance] = {}

        # Verify double event setup
        if event_instance in self._flow[from_state_instance].keys():
            raise EventTransitionAlreadyRegistered
        else:
            self._flow[from_state_instance][event_instance] = to_state_instance

    def set_default(self, default_state: State):
        """ Sets up the default state of the object. """
        self._default = default_state

    def restart(self):
        """ Restarts the state of the object. """

        # Verify existing default state
        if self._default is None:
            raise DefaultStateNotRegistered

        # Restart states
        self._previous = self._default
        self._current = self._default

    # Object-interaction methods with the
    # external actors.

    def send_event(self, event: StateEvent):
        """ An external actor or controller may send an event
        to the StateObject. """
        # Verify valid event
        if event is not None:
            if isinstance(event, StateEvent):
                self._queue.put(event)

        # Was not a valid event...
        raise NotAValidEvent

    def run_event(self):
        """ Executes an event from the internal queue. """
        if not self._queue.empty():
            event = self._queue.get()
            if event in self._flow[self._current].keys():
                self._previous = self._current
                self._current = self._flow[self._current][event]
                self.state_changed(EventData())
            else:
                raise StateEventNotExpected

    # Object's data access

    def previous_state(self) -> State:
        """ Returns the previous state of the object. """
        return self._previous

    def current_state(self) -> State:
        """ Returns the current state of the object. """
        return self._current
