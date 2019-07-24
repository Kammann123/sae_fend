"""
Sample 02. Testing and running Qt Application with the main window.
"""

# python native modules

# third-party modules
from PyQt5 import QtWidgets

# sae project modules


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.exec_()
