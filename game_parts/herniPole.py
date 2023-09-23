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
        # Draw the stones within this pole
        for i,stone in enumerate(self.stones):
            # Calculate the position of each stone within the pole
            stone_x = self.x + RECT_WIDTH/2  # Adjust this as needed
            stone_y = self.y + STONE_RADIUS + i * STONE_RADIUS # Adjust this as needed


            # Draw the stone at its position
            stone.draw(win, stone_x, stone_y)
