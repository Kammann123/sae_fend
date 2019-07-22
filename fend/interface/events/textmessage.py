"""
"""

# python native modules

# third-party modules

# sae project modules
from pypublisher.bases.event import EventData


class TextMessageData(EventData):
    """ TextMessage Event Data """

    def __init__(self, is_default: bool, message):
        EventData.__init__(self)

        self.is_default = is_default
        self.content = message
