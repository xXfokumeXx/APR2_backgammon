from game_parts.constants import *
from .herniPole import HerniPole

class Bar(HerniPole):

    def __init__(self, ID, x, y):
        super().__init__(ID, x, y)
    
    def pop(self):
        ...