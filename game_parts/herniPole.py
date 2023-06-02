

class HerniPole:

    def __init__(self, ID, stones = None):
        self.ID = ID
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