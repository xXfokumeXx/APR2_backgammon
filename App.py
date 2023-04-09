import tkinter as tk
from Config import *


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Backgammon")
        self.resizable(False, False)

        self.canvas = tk.Canvas(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.pack()

