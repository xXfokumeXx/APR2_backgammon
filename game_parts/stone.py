

class Stone:

    def __init__(self, number, color, kicked = False, history = None):
        self.number = number
        self.color = color
        self.kicked = kicked
        if not history:
            self.history = []