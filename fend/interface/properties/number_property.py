"""
Number Property class to simple declaration in the class
"""

# python native modules

# third-party modules

# sae project modules
from fend.interface.properties.base.property import Property


class NumberProperty(Property):
    """ NumberProperty class. """

    def __init__(self,
                 identifier,
                 min_value,
                 max_value,
                 buffer_length = 100):
        super(NumberProperty, self).__init__(identifier, buffer_length)

        self.min_value = min_value
        self.max_value = max_value

    def verify(self, new_value) -> bool:
        """ Verifies if the given value is a valid property state
        and returns a boolean result.
        """
        if type(new_value) is float or type(new_value) is int:
            if self.min_value <= new_value <= self.max_value:
                return True
        return False
