"""
This module implements the four walls of the room within which Snake is played.
"""

from gui import Gui

class Room:
    """The room has a width and height, a character to draw, and color."""

    def __init__(self, width, height, c,
            fore_color, back_color):
        self.width = width
        self.height = height
        self.c = c
        self.fore_color = fore_color
        self.back_color = back_color

    def draw(self, gui, score):
        gui.draw_line(self.c, 0, 0, self.width - 1, 0,
             self.fore_color, self.back_color) #上
        gui.draw_line(self.c, 0, 0, 0, self.height - 1,
             self.fore_color, self.back_color) #左
        gui.draw_line(self.c, self.width - 1, 0, self.width - 1, self.height - 1,
             self.fore_color, self.back_color) #右
        gui.draw_line(self.c, 0, self.height - 1, self.width - 1, self.height - 1,
             self.fore_color, self.back_color) #下

        if score >= 50:
            gui.draw_line(self.c, (self.width) // 3,self.height // 3 , (self.width // 3) , (self.height // 3) + 8,
                 self.fore_color, self.back_color)
