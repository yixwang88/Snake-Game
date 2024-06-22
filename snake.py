"""
This module implements the snake class.
"""
from gui import Gui
from position import Position
from typing import List

class Snake:
    """This is the Snake.
    It has a list of positions. The head is at index 0.
    The tail occupies the rest of the list.
    """
    def __init__(self, x, y):
        self.position = []
        self.position.append(Position(x, y))
        self.position.append(Position(x-1, y))
        self.position.append(Position(x-2, y))
        self.direction = "RIGHT"

    def draw(self, gui):
        for i, c in enumerate(self.position):
            print(c)
            if i == 0:
                if self.direction == "RIGHT":
                    gui.draw_text(">", c.get_x(), c.get_y(), "WHITE", "RED")
                elif self.direction == "LEFT":
                    gui.draw_text("<", c.get_x(), c.get_y(), "WHITE", "RED")
                elif self.direction == "UP":
                    gui.draw_text("^", c.get_x(), c.get_y(), "WHITE", "RED")
                elif self.direction == "DOWN":
                    gui.draw_text("V", c.get_x(), c.get_y(), "WHITE", "RED")
            else:
                gui.draw_text("+", c.get_x(), c.get_y(), "WHITE", "RED")



    def move(self):
        for i in range(len(self.position)-1,0,-1):
            pre = self.position[i-1]
            prex = pre.get_x()
            prey = pre.get_y()
            self.position[i].set_x(prex)
            self.position[i].set_y(prey)
        if self.direction == "RIGHT":
            preh = self.position[0]
            prehx = preh.get_x()
            self.position[0].set_x(prehx+1)
        elif self.direction == "LEFT":
            preh = self.position[0]
            prehx = preh.get_x()
            self.position[0].set_x(prehx-1)
        elif self.direction == "UP":
            preh = self.position[0]
            prehx = preh.get_x()
            prey = preh.get_y()
            self.position[0].set_y(prey-1)
        elif self.direction == "DOWN":
            preh = self.position[0]
            prehx = preh.get_x()
            prey = preh.get_y()
            self.position[0].set_y(prey+1)


    def change_direction(self, c):
        if c == "KEY_LEFT":
            if self.direction == "UP" or self.direction == "DOWN":
                self.direction = "LEFT"
        elif c == "KEY_RIGHT":
            if self.direction == "UP" or self.direction == "DOWN":
                self.direction = "RIGHT"
        elif c == "KEY_UP":
            if self.direction == "RIGHT" or self.direction == "LEFT":
                self.direction = "UP"
        elif c == "KEY_DOWN":
            if self.direction == "LEFT" or self.direction == "RIGHT":
                self.direction = "DOWN"

    def grow(self):
        last = self.position[len(self.position)-1]
        self.position.append(Position(last.get_x() - 1, last.get_y()))
