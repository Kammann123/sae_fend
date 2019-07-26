"""
ExceptionHandler base class
"""

# python native modules

# third-party modules

# sae project modules
from pylogger.base.logger import Logger


class ExceptionHandler(object):
    """ ExceptionHandler handles exceptions thrown at the
    highest level of the application, and logs its description
    into some output.
    """

    def __init__(self, logger: Logger):
        self.logger = logger

    def __call__(self, exception_type, value, traceback):
        message = """[EXCEPTION]
        Type: {}
        Value: {}
        Traceback: {}
        
        Good luck :D""".format(exception_type, value, traceback)

        self.logger.log(message)
