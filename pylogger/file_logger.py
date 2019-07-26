"""
FileLogger class.
"""

# python native modules

# third-party modules

# sae project modules
from pylogger.base.logger import Logger


class FileLogger(Logger):
    """ FileLogger, Logger's interface implementation to save data in files.
    """

    def __init__(self, username: str, filename: str):
        Logger.__init__(self, username)

        self._filename = filename
        self._formatted_filename = "{}_{}.txt".format(
            self._filename,
            self._session_date.strftime(
                "%d.%m.%y_%H.%M"
            )
        )

    def log(self, message: str):
        # Verify if file does not exist, creates it and adds header data
        try:
            file = open(self._formatted_filename, "r")
            file.close()
        except FileNotFoundError:
            file = open(self._formatted_filename, "w")
            file.write("[Application Session]\nUsername: {}\nDate: {}\n\n- Logged data -\n\n".format(
                self._session_user,
                self._session_date.strftime("%d/%m/%y %H:%M")
            ))
            file.close()

        # Open the file, save new data and close it
        file = open(self._formatted_filename, "a")
        file.write("{}\n".format(message))
        file.close()
