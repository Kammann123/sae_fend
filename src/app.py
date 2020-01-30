# PyQt5 modules
from PyQt5 import QtWidgets

# Python modules
import sys

# Main window ui import
from src.mainwindow import MainWindow


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
