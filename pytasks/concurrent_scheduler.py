"""
ConcurrentScheduler base class.
"""

# python native modules

# third-party modules

# sae project modules
from pytasks.scheduler import Scheduler


class ConcurrentScheduler(Scheduler):
    """ Schedules and runs every task concurrently. """

    def run_task(self):
        """ Runs the next task registered by the scheduler. """
        task = self.fetch_task()
        task()
