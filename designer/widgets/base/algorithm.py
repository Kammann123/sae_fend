"""
IndexedValueAlgorithm
"""

# python native modules

# third-party modules

# sae project modules


class IndexedValueAlgorithm:
    """ IndexedValueAlgorithm
    Class Methods containing different types of algorithms to
    distribute a range of values through an iterable collection of objects.
    """

    def __init__(
            self,
            from_x,
            from_y,
            to_x,
            to_y):
        self.from_x = from_x
        self.from_y = from_y
        self.to_x = to_x
        self.to_y = to_y

    def __call__(self, x):
        raise NotImplemented


class LinearAlgorithm(IndexedValueAlgorithm):
    """ LinearAlgorithm
    Linear distribution of the range of values.
    """

    def __init__(
            self,
            from_x,
            from_y,
            to_x,
            to_y):
        super(LinearAlgorithm, self).__init__(
            from_x,
            from_y,
            to_x,
            to_y)

        self.scope = (to_y - from_y) / (to_x - from_x)
        self.origin = from_y

    def __call__(self, x):
        return self.origin + self.scope * (x - self.from_x)
