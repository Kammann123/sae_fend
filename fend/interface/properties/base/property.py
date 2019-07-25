"""
"""

# python native modules
from datetime import datetime

# third-party modules

# sae project modules
from pyevents.event import Event
from pyevents.event import EventData


class InvalidPropertyValue(Exception):
    def __init__(self):
        Exception.__init__(self, "The given value did not satisfy the property rules. Invalid value.")


class Property(object):
    """ Any state variable of an object may be modeled as a Property, containing the current
    value or status with its validation rules.
    Property state history will be saved.
    """

    # value's history is saved as a list of two element tuple
    # history = [ (datetime, value), ... , (datetime, value) ]

    def __init__(self, buffer_length: int):
        # Property's members
        self.max_length = buffer_length
        self.history = []
        self.value = None

        # Property's events
        self.property_changed = Event("PropertyChanged")

    def clear(self):
        """ Clear property state's history. """
        self.history = []
        self.value = None

    def set(self, new_value):
        """ Sets a new value for the property.
        If the given one is not valid, then an
        exception will be raised.
        """
        if self.verify(new_value):
            if self.value != new_value:
                self.value = new_value
                if len(self.history) >= self.max_length:
                    del self.history[0]
                self.history.append((datetime.now(), new_value))

                self.property_changed(EventData())
        else:
            raise InvalidPropertyValue

    def verify(self, new_value) -> bool:
        """ Verifies if the given value is a valid property state
        and returns a boolean result.
        """
        raise NotImplemented
