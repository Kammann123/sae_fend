"""
Front-End base class, data model and interface with the back end.
"""

# python native modules
from enum import Enum

# third-party modules

# sae project modules
from pytasks.concurrent_scheduler import ConcurrentScheduler

from pypublisher.publisher import Publisher

from pyevents.event import EventData
from pyevents.event import Event

from fend.interface.properties.number_property import NumberProperty


class PropertyNotFound(Exception):
    def __init__(self):
        Exception.__init__(self, "BaseFend property not found.")


class Events(Enum):
    """ Declaring Front-End events. """

    TextMessageSent = "TextMessageSent"


class Properties(Enum):
    """ Declaring Front-End properties. """

    RPMAngularSpeed = "RPMAngularSpeed"
    ThrottlePosition = "ThrottlePosition"
    AirTemperature = "AirTemperature"
    EngineTemperature = "EngineTemperature"
    LambdaOne = "LambdaOne"
    OilPressure = "OilPressure"
    BatteryVoltage = "BatteryVoltage"
    GroundSpeed = "GroundSpeed"
    IgnitionAdvance = "IgnitionAdvance"
    FuelUsed = "FuelUsed"


class FendInterface(Publisher, ConcurrentScheduler):
    """
    BaseFend interface class works as an event publisher, and the back-end instance subscribes to specific
    events and gets notified with a callback method.
    """

    def __init__(self, buffer_length: int):
        ConcurrentScheduler.__init__(self)
        Publisher.__init__(self)

        # Front-End action events
        self.register_event(Events.TextMessageSent)

        # Front-End properties
        self.angular_speed = NumberProperty(Properties.RPMAngularSpeed, 0.0, 16000.0, buffer_length)
        self.throttle_position = NumberProperty(Properties.ThrottlePosition, 0, 100, buffer_length)
        self.air_temperature = NumberProperty(Properties.AirTemperature, 0.0, 60.0, buffer_length)
        self.engine_temperature = NumberProperty(Properties.EngineTemperature, 0.0, 130.0, buffer_length)
        self.lambda_one = NumberProperty(Properties.LambdaOne, 0.7, 1.2, buffer_length)
        self.oil_pressure = NumberProperty(Properties.OilPressure, 0, 1000, buffer_length)
        self.battery_voltage = NumberProperty(Properties.BatteryVoltage, 10, 16, buffer_length)
        self.ground_speed = NumberProperty(Properties.GroundSpeed, 0, 200, buffer_length)
        self.ignition_advance = NumberProperty(Properties.IgnitionAdvance, 0, 90, buffer_length)
        self.fuel_used = NumberProperty(Properties.FuelUsed, 0, 10, buffer_length)

      # Object events
        self.changed = Event("InterfaceChanged")

    def update(self, magnitude: Properties, new_value):
        """ Updates a magnitude's value. """
        for attribute_name, attribute_value in self.__dict__.items():
            if isinstance(attribute_value, NumberProperty):
                if getattr(self, attribute_name).id == magnitude:
                    if getattr(self, attribute_name).set(new_value):
                        self.changed(EventData())
                    break
        else:
            raise PropertyNotFound
