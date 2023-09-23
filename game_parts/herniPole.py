

class HerniPole:

    def __init__(self, ID, x, y, stones = None):
        self.ID = ID
        self.x = x
        self.y = y
        self.stone = None
        self.stones = stones
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
    
    def mozno_tahnout(self, stone):
        # kontrola za je pole prazdne
        if self.stone is not None:
            return False        
        return True

    def set_stone(self, stone):
        self.stone = stone  # polozim kámen
        stone.position = (self.x, self.y)  # update pozice kamene