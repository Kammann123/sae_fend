"""
State base class
"""

# python native modules

# third-party modules

# sae project modules


class State(object):
    """ State base class.
    Declares an object's state and defines its general information,
    when it's required so.

    Here every state should know its own name and the reference
    to the object with this state.
    """

    # Static members of the declared State
    name = "State"

    def __init__(self, state_object: object):
        self.object = state_object

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.name
