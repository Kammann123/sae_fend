"""
ExceptionHandler base class
"""

# python native modules
from traceback import extract_tb

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
        # Retrieves the traceback path
        traceback_message = ""
        for traceback_path in extract_tb(traceback):
            traceback_message += "{}\n".format(traceback_path)

        # Creates the formatted message to be logged
        message = """[EXCEPTION]
        Type: {}
        Value: {}
        Traceback: {}
        
        Good luck :D""".format(exception_type,
                               value,
                               traceback_message)

        self.logger.log(message)
