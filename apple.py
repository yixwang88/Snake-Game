"""
This module represents the apple that appears at random places on the screen.
"""
import random
from typing import List

from gui import Gui
from position import Position



def collides(p, positions):
    """Return true if p is any of the positions in the list."""
    for position in positions:
        if p.get_x() == position.get_x() and p.get_y() == position.get_y():
            return True
    return False


class Apple:
    """The apple's location is randomly generated."""

    def __init__(self, gui, snake_position):
        random_x, random_y = self.random_apple(gui, snake_position)
        self.position = Position(random_x, random_y)
#return true if apple hits snake, return false if apple not hits snake
    def hit_snake(self, gui, snake_position):
        result = collides(self.position,snake_position)
        return result

    def draw(self,gui):
        gui.draw_text("*", self.position.get_x(), self.position.get_y(), "RED", "GREEN")

    def random_apple(self, gui, snake_position):
        a = random.randint(2, int(gui.get_width())-2)
        b = random.randint(2, int(gui.get_height())-2)
        while True:
            for i in range(len(snake_position)):
                if a == int(snake_position[i].get_x()) and b == int(snake_position[i].get_y()):
                    a = random.randint(2, int(gui.get_width())-2)
                    b = random.randint(2, int(gui.get_height())-2)
                    continue
            break
        return a, b
