"""
"""

# python native modules

# third-party modules

# sae project modules
from fend.interface.properties.base.property import Property


class RPMAngularSpeed(Property):
    """ Angular Speed Property measured in RPM. """

    def __init__(self, buffer_length: int):
        super(RPMAngularSpeed, self).__init__(buffer_length)

    def verify(self, new_value) -> bool:
        """ Verifies if the given value is a valid property state
        and returns a boolean result.
        """
        if type(new_value) is float or type(new_value) is int:
            if 0 <= new_value <= 16000.0:
                return True
        return False
