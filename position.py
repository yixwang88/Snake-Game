"""
Provide an encapsulation of a position in two dimensions.
"""

class Position:
    """Every position holds two coordinates, an x and a y."""

    def __init__(self, x, y) -> None:
        self.xpos = x
        self.ypos = y

    def get_x(self):
        return self.xpos

    def get_y(self):
        return self.ypos

    def set_x(self, new_x):
        self.xpos = new_x

    def set_y(self, new_y):
        self.ypos = new_y
