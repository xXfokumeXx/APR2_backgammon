import tkinter as tk

from Config import *


class Point:
    def __init__(self, x: int, y: int, color: str, canvas: tk.Canvas):
        self.color = color
        self.x = x
        self.y = y
        self.canvas = canvas

        borderOffset = (WINDOW_WIDTH / 2 + WINDOW_WIDTH / 30) - (WINDOW_WIDTH / 2 - WINDOW_WIDTH / 30) if self.x > 5 else 0
        self.triangle = self.canvas.create_polygon([self.x * POINT_WIDTH + borderOffset, self.y * WINDOW_HEIGHT,
                                                    self.x * POINT_WIDTH + POINT_WIDTH + borderOffset, self.y * WINDOW_HEIGHT,
                                                    self.x * POINT_WIDTH + POINT_WIDTH / 2 + borderOffset, (self.y + 1) * WINDOW_HEIGHT * .33],
                                                   fill=self.color, width=0)
