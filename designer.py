""" This Designer script is an utility that can be used to run the Qt Designer tool interface
    adding automatically the environment variables needed to detect the new widget plugins from the project.
"""

# PyQt5 modules
from PyQt5.QtCore import QProcess, QProcessEnvironment

# Python modules
import os

if __name__ == "__main__":
    designer_bin = 'designer'

    base = os.path.dirname(__file__)
    plugin_path = os.path.join(base, 'plugins')
    widget_path = os.path.join(base, 'src', 'widgets')

    env = QProcessEnvironment.systemEnvironment()
    env.insert('PYQTDESIGNERPATH', plugin_path)
    env.insert('PYTHONPATH', widget_path)

    designer = QProcess()
    designer.setProcessEnvironment(env)
    designer.start(designer_bin)
    designer.waitForFinished(-1)
    designer.exitCode()
