"""
Serial Port configuration data class
"""

# python native modules
from enum import Enum

# third-party modules

# sae project modules


class BaudRates(Enum):
    """ Standard Serial Port Baud Rates. """
    _110 = "110"
    _300 = "300"
    _600 = "600"
    _1200 = "1200"
    _2400 = "2400"
    _4800 = "4800"
    _9600 = "9600"
    _14400 = "14400"
    _19200 = "19200"
    _38400 = "38400"
    _57600 = "57600"
    _115200 = "115200"
    _128000 = "128000"
    _256000 = "256000"


class Parity(Enum):
    """ Standard Serial Port Parities. """
    ODD = "Odd"
    EVEN = "Even"
    NONE = "None"


class SerialConfig(object):
    """ Serial Port configuration data. """

    def __init__(self,
                 baud_rate: BaudRates,
                 data_bits: int,
                 parity: Parity,
                 stop_bits: int,
                 port: str
                 ):
        self.baud_rate = baud_rate
        self.data_bits = data_bits
        self.parity = parity
        self.stop_bits = stop_bits
        self.port = port
