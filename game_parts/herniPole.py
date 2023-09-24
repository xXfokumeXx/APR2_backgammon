from game_parts.constants import *

class HerniPole:

    def __init__(self, ID, x, y, stones = None):
        self.ID = ID
        self.x = x
        self.y = y
        self.stones = None
        if not self.stones:
            self.stones = []
    
    def is_empty(self):
        if len(self.stones) == 0:
            return True
    
    def push(self, item):
        self.stones.append(item)
   
    def pop(self):
        if not self.is_empty():
            self.stones.pop()

    def __repr__(self):
        return f"{self.ID} {self.stones}"
    
    def mozno_tahnout(self, stones):
        # kontrola za je pole prazdne
        if self.is_empty():
            return True

    def set_stone(self, stone):
        self.stone = stone  # polozim kámen
        stone.position = (self.x, self.y)  # update pozice kamene

    def draw(self, win):

        bottom_row_y = self.y - RECT_HEIGHT - STONE_RADIUS
        # vykresli kameny v poli
        for i,stone in enumerate(self.stones):
            # vypocet pozice v poli
            stone_x = self.x + RECT_WIDTH/2
            stone_y = self.y + STONE_RADIUS + i * STONE_RADIUS


            # nakresli kamen na sve pozici
            stone.draw(win, stone_x, stone_y)
