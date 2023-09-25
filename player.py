from game_parts.dvojkostka import *
from game_parts.stone import *
from game import *
import random


class Player:
    def __init__(self, color):
        self.color = color
        self.is_on_turn = False
        self.player_white_route = [-1,11,10,9,8,7,6,5,4,3,2,1,0,12,13,14,15,16,17,18,19,20,21,22,23]
        self.player_black_route = [-1,23,22,21,20,19,18,17,16,15,14,13,12,0,1,2,3,4,5,6,7,8,9,10,11]
        self.hozene = None
        self.kostka = None

    def create_kostka(self):
        self.kostka = Dvojkostka()
    
    def hod_kostkou(self):
        self.hozene = self.kostka.hod_kostkou()
        print(f"{self.color} hodil(a) {self.hozene}")