""" This Designer script is an utility that can be used to run the Qt Designer tool interface
    adding automatically the environment variables needed to detect the new widget plugins.
"""

# PyQt5 modules
from PyQt5.QtCore import QProcess, QProcessEnvironment
from PyQt5.QtWidgets import QApplication, QMessageBox

# Python modules
import os
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    QMessageBox.information(None, "PyQt Designer Plugins",
                            "<p>This example will start Qt Designer when you click the <b>OK</b> "
                            "button.</p>"
                            "<p>Before doing so it sets the <tt>PYQTDESIGNERPATH</tt> environment "
                            "variable to the <tt>python</tt> directory that is part of this "
                            "example.  This directory contains all the example Python plugin "
                            "modules.</p>"
                            "<p>It also sets the <tt>PYTHONPATH</tt> environment variable to the "
                            "<tt>widgets</tt> directory that is also part of this example.  This "
                            "directory contains the Python modules that implement the example "
                            "custom widgets.</p>"
                            "<p>All of the example custom widgets should then appear in "
                            "Designer's widget box in the <b>PyQt Examples</b> group.</p>")

    designer_bin = 'designer'

    base = os.path.dirname(__file__)
    plugin_path = os.path.join(base, '..', 'src/widgets/plugins')
    widget_path = os.path.join(base, '..', 'src/widgets')

    env = QProcessEnvironment.systemEnvironment()
    env.insert('PYQTDESIGNERPATH', plugin_path)
    env.insert('PYTHONPATH', widget_path)

    designer = QProcess()
    designer.setProcessEnvironment(env)
    designer.start(designer_bin)
    designer.waitForFinished(-1)
    sys.exit(designer.exitCode())
