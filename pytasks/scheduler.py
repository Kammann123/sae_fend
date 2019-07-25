"""
Scheduler base class.
"""

# python native modules

# third-party modules

# sae project modules
from pytasks.task import Task


class UnregisteredTask(Exception):
    def __init__(self):
        Exception.__init__(self, "The task has not been registered.")


class Scheduler(object):
    """ Scheduler base class.
    Registers several tasks to be ran one after each other.
    """

    def __init__(self):
        self._tasks = []
        self._current = None

    def register_task(self, task: Task):
        """ Registers a new task to be executed. """
        self._tasks.append(task)

    def unregister_task(self, task: Task):
        """ Unregister a task. """
        if task in self._tasks:
            del self._tasks[self._tasks.index(task)]
        else:
            raise UnregisteredTask

    def fetch_task(self) -> Task:
        """ Returns the next task to be executed. """
        if self._current is None or self._current == len(self._tasks):
            self.restart()
        self._current += 1
        return self._tasks[self._current - 1]

    def restart(self):
        """ Restarts the order of the executed tasks. """
        self._current = 0
