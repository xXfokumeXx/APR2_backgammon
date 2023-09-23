

class Stone:

    def __init__(self, number, color, kicked = False, history=None):
        self.number = number
        self.color = color
        self.kicked = kicked
        if history is None:
            history = []