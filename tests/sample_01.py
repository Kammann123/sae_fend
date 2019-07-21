"""
Sample 01. Test of publisher/subscriber system and property's history.
"""

# python native modules

# third-party modules

# sae project modules
from pypublisher.bases.subscriber import Subscriber

from fend.interface.base.base_fend import BaseFend

from fend.interface.base.base_fend import Events

from fend.interface.events.textmessage import TextMessageData


class BackEnd(Subscriber):
    """ BackEnd Simulator.-
    """

    def __init__(self, fend: BaseFend):
        Subscriber.__init__(self)

        # Keep the front end reference
        self.front_end = fend

        # Subscribe to front end events
        self.front_end.subscribe(Events.TextMessageSent,
                                 self,
                                 self.on_message_sent)

    @staticmethod
    def on_message_sent(event_id, event_data):
        """ TextMessageSent callback.
        """
        print("[{}] A Text Message has been sent: \"{}\"".format(
                event_id,
                event_data.content
            )
        )


if __name__ == "__main__":

    # Instances
    front_end = BaseFend(100)
    back_end = BackEnd(front_end)

    # Event triggering
    front_end.raise_event(Events.TextMessageSent,
                          TextMessageData(False, "Hola Mundo!")
                          )
