import random


class Player:
    def __init__(self, color):
        self.color = color
        self.is_turn = False

    
    def randplayer(players):
        return random.choice(players)
