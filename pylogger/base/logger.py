"""
Base Logger class. Declares the general interface of a Logger object to save error data
in multiple platforms, systems, etc...
"""

# python native modules
from datetime import datetime

# third-party modules

# sae project modules


class Logger(object):
    """ Logger class.
    Base interface of Logger object. Used to log error data on files, server, database,
    etc by implementing it.
    """

    def __init__(self, username: str):
        self._session_user = username
        self._session_date = datetime.now()

    def log(self, message: str):
        """ Logs a message """
        raise NotImplemented
