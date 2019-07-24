"""
Publisher
Design Pattern mix, using events and the observer pattern, allowing multiple event handling through identifiers.
"""

# python native modules

# third-party modules

# pypublisher modules
from pyevents.event import Event
from pyevents.event import EventData


class EventAlreadyRegistered(Exception):
    def __init__(self):
        Exception.__init__(self, "There's already an event with that identifier.")


class EventNotFound(Exception):
    def __init__(self):
        Exception.__init__(self, "There are no events under that identifier.")


class Publisher(object):
    """ Base class of a publisher. """

    def __init__(self):
        self.events = {}

    def register_event(self, identifier):
        """ Registers an event. """

        # Verify already used identifier or double registering
        if identifier in self.events.keys():
            raise EventAlreadyRegistered
        else:
            self.events[identifier] = Event(identifier)

    def subscribe(self, event_identifier, owner: object, callback: callable):
        """ Subscribes to an event. """

        # Verify existing event
        if event_identifier in self.events.keys():
            self.events[event_identifier].subscribe(owner, callback)
        else:
            raise EventNotFound

    def unsubscribe(self, event_identifier, owner: object):
        """ Unsubscribe to an event. """

        # Verify existing event
        if event_identifier in self.events.keys():
            self.events[event_identifier].unsubscribe(owner)
        else:
            raise EventNotFound

    def raise_event(self, event_identifier, event_data: EventData):
        """ Raises an event. """

        # Verify existing event
        if event_identifier in self.events.keys():
            self.events[event_identifier](event_data)
        else:
            raise EventNotFound
