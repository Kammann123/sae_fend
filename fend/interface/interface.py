"""
Front-End base class, data model and interface with the back end.
"""

# python native modules
from enum import Enum

# third-party modules

# sae project modules
from pypublisher.publisher import Publisher

from fend.interface.properties.angular_speed import RPMAngularSpeed


class PropertyNotFound(Exception):
    def __init__(self):
        Exception.__init__(self, "BaseFend property not found.")


class Events(Enum):
    """ Declaring Front-End events. """

    TextMessageSent = "TextMessageSent"


class FendInterface(Publisher):
    """
    BaseFend interface class works as an event publisher, and the back-end instance subscribes to specific
    events and gets notified with a callback method.
    """

    def __init__(self, buffer_length: int):
        Publisher.__init__(self)

        # Declaring front end events
        self.register_event(Events.TextMessageSent)

        # Defining properties
        self.angular_speed = RPMAngularSpeed(buffer_length)

    def update(self, magnitude, new_value):
        """ Updates a magnitude's value. """
        for attribute_name, attribute_value in self.__dict__.items():
            if isinstance(attribute_value, magnitude):
                getattr(self, attribute_name).set(new_value)
                break
        else:
            raise PropertyNotFound