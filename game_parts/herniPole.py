

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
        # if not self.stones or item.color == self.stones[0].color:
        self.stones.append(item)
        # else:
            # ...
   
    def pop(self):
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
