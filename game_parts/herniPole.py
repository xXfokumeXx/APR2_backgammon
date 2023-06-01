

class HerniPole:
    def __init__(self, ID, stones):
        self.ID = ID
        if not self.stones:
            self.stones = []
    
    def is_empty(self):
        if len(self.stones) == 0:
            return True
    