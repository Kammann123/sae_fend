"""
Sample 01. Test of publisher/subscriber system and property's history.
"""

# python native modules

# third-party modules

# sae project modules
from pypublisher.subscriber import Subscriber

from fend.interface.interface import FendInterface

from fend.interface.interface import Events

from fend.interface.events.text_message import TextMessageData
from fend.interface.properties.angular_speed import RPMAngularSpeed


class BackEnd(Subscriber):
    """ BackEnd Simulator.-
    """

    def __init__(self, fend: FendInterface):
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
    front_end = FendInterface(100)
    back_end = BackEnd(front_end)

    # Setting property values
    front_end.update(RPMAngularSpeed, 3150)

    # Show values
    print("Current RPM value: {}".format(front_end.angular_speed.value))

    # Event triggering
    front_end.raise_event(Events.TextMessageSent,
                          TextMessageData(False, "Hola Mundo!")
                          )
