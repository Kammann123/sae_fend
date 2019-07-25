"""
Task base class. Callable object used to run several tasks.
"""

# python native modules

# third-party modules

# sae project modules


class Task(object):
    """ Task base class of a callable object. """

    def __call__(self, *args, **kwargs):
        raise NotImplemented
