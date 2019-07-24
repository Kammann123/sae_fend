"""
StateEvent base class
"""

# python native modules

# third-party modules

# sae project modules


class StateEvent(object):
    """ StateEvent base class.
    Every event used to change an object's state when using State Pattern in OOP.

    Here every event should has its own identifier, the source and the data
    describing the context where the event occurred
    """

    # Static members of the declared state event
    id = "EventId"

    def __init__(self, event_source: object, event_data: object):
        self.source = event_source
        self.data = event_data

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return self.id
