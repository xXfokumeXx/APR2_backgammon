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
    
    def mozno_tahnout(self):
        # kontrola za je pole prazdne
        if self.is_empty():
            return True
        if not self.is_empty():
            return False
        """ 
            if len(other.stones) == 1 and self.selected_pole.stones[-1].color == self.players[self.aktualni_hrac_i].color:
                return True
            else:
                return False
        """

    def set_stone(self, stone):
        self.stone = stone  # polozim kámen
        stone.position = (self.x, self.y)  # update pozice kamene

    def draw(self, win):
        # vykresli kameny v poli
        for i,stone in enumerate(self.stones):
            # vypocet pozice v poli
            stone_x = self.x + RECT_WIDTH/2
            stone_y = self.y + STONE_RADIUS + i * STONE_RADIUS


            # nakresli kamen na sve pozici
            stone.draw(win, stone_x, stone_y)
