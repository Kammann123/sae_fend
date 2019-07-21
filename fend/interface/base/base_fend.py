"""
This is the Front-End interface class which defines the interface for
the Back-End interaction with the user interface.
"""

# python native modules
from enum import Enum

# third-party modules

# sae project modules
from pypublisher.bases.publisher import Publisher


class Events(Enum):
    """ Declaring Front-End events. """

    TextMessageSent = "TextMessageSent"


class BaseFend(Publisher):
    """
    BaseFend interface class works as an event publisher, and the back-end instance subscribes to specific
    events and gets notified with a callback method.
    """

    def __init__(self):
        super(BaseFend, self).__init__()

        # Declaring front end events
        self.register_event(Events.TextMessageSent)
