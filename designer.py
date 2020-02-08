""" This Designer script is an utility that can be used to run the Qt Designer tool interface
    adding automatically the environment variables needed to detect the new widget plugins from the project.
"""

# PyQt5 modules
from PyQt5.QtCore import QProcess, QProcessEnvironment

# Python modules
import os

if __name__ == "__main__":
    designer_bin = 'designer'

    plugin_path = os.path.join(os.path.dirname(__file__), 'plugins')
    widget_path = os.path.join(os.path.dirname(__file__), 'src', 'widgets')
    custom_path = os.path.join(os.path.dirname(__file__), 'src')
    project_path = os.path.join(os.path.dirname(__file__))

    env = QProcessEnvironment.systemEnvironment()
    env.insert('PYQTDESIGNERPATH', plugin_path)
    env.insert('PYTHONPATH', f"{widget_path};{custom_path};{project_path}")

    designer = QProcess()
    designer.setProcessEnvironment(env)
    designer.start(designer_bin)
    designer.waitForFinished(-1)
    designer.exitCode()
