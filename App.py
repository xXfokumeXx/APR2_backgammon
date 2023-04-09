import tkinter as tk
import math

from Config import *
from Point import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Backgammon")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)

        self.canvas = tk.Canvas(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.pack()

        self.background = self.canvas.create_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, fill="#807880", width=0)
        self.centerBorder = self.canvas.create_rectangle(WINDOW_WIDTH / 2 - WINDOW_WIDTH / 30, 0,
                                                         WINDOW_WIDTH / 2 + WINDOW_WIDTH / 30,
                                                         WINDOW_HEIGHT, fill="#302b30")

        self.points = []

        isBlack = True
        for row in range(2):
            for column in range(12):
                self.points.append(Point(column, row, "#211a21" if isBlack else "#695669", self.canvas))
                isBlack = not isBlack
            isBlack = not isBlack

