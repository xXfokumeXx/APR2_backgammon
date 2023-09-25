from game_parts.dvojkostka import *
from game_parts.stone import *
from game_parts.herniPole import *
from game import *
import random


class Player:
    def __init__(self, color, player_route):
        self.color = color
        self.player_route = player_route
        self.is_on_turn = False
        self.hozene = None
        self.kostka = None
        self.selected_stone = None
        """ self.player_routes = [[12,11,10,9,8,7,5,4,3,2,1,0,14,15,16,17,18,19,21,22,23,24,25,26],
                              [26,25,24,23,22,21,19,18,17,16,15,14,0,1,2,3,4,5,7,8,9,10,11,12]] 
         """


    def create_kostka(self):
        self.kostka = Dvojkostka()

    def convert_pos(self):
        for x in self.player_route:
            self.player_route.append(self.deska.hernideska[x])
            print(self.player_routes)
        return
    
    def hod_kostkou(self):
        self.hozene = self.kostka.hod_kostkou()
        print(f"{self.color} hodil(a) {self.hozene}")
    
    def create_poss_moves(self, aktualni_pozice, hozena_cisla):
        possible_moves = []

        for cislo in hozena_cisla:
            nova_pozice = aktualni_pozice + cislo
            if nova_pozice <= len(self.player_route) - 1:
                mozna_pozice = self.player_route[nova_pozice]
                # Check if the pole is empty or has at most 1 stone of the player's color
                if mozna_pozice.is_empty() or (len(mozna_pozice.stones) == 1 and mozna_pozice.stones[0].color == self.color):
                    possible_moves.append((aktualni_pozice, nova_pozice))
        return possible_moves
        

    def move_stone(self, stone, cilove_pole):
        if stone and cilove_pole is not None:
            stone.move(cilove_pole)
    
    def get_current_position(self):
        if self.selected_stone is not None and self.selected_stone.position is not None:
            return self.player_route.index(self.selected_stone.ID)
        return -1