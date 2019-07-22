"""
"""

# python native modules

# third-party modules

# pypublisher modules


class AlreadySubscribed(Exception):
    def __init__(self):
        Exception.__init__(self, "The callback's owner has already subscribed to the event.")


class NotSubscribed(Exception):
    def __init__(self):
        Exception.__init__(self, "The given object has not subscribed to the event.")


class EventData(object):
    """ Data passed to subscribers when raising an event. """
    def __init__(self):
        pass


class Event(object):
    """ Base class of an event.
    An internal dictionary saves the callback and its owner instance to identify who
    is subscribing each callback. """

    def __init__(self, identifier):
        self.id = identifier
        self.subscribers = {}

    def subscribe(self, owner: object, callback: callable):
        """ Subscribes to the event the class instance and its callback. """
        owner_key = str(id(owner))

        # verify double subscribing
        if owner_key in self.subscribers.keys():
            raise AlreadySubscribed

        # dictionary key reference with the unique id of python's object
        self.subscribers[owner_key] = callback

    def unsubscribe(self, owner: object):
        """ Unsubscribe to the event. """
        owner_key = str(id(owner))

        # verify subscribed
        if owner_key in self.subscribers.keys():
            del self.subscribers[owner_key]
        else:
            raise NotSubscribed

    def __call__(self, data: EventData):
        """ Raises the event and call the subscribers callbacks.
        Every callback will be called and receive the event and its data. """
        for callback in self.subscribers.values():
            callback(self.id, data)
