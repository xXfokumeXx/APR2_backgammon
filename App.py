import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Backgammon")
        self.resizable(False, False)

        self.label = tk.Label(self, text="Hello world")
        self.label.pack()


