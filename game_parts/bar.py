from game_parts.constants import *
from .herniPole import HerniPole

class Bar(HerniPole):

    def __init__(self, ID, x, y):
        super().__init__(ID, x, y)

    def push(self, item):
        print("Na toto pole nelze vstoupit")
   
    def pop(self):
        ...