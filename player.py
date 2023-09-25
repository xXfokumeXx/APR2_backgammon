from game_parts.dvojkostka import *
from game_parts.stone import *
from game_parts.herniPole import *
from game import *
import random


class Player:
    def __init__(self, color, player_route):
        self.color = color
        self.player_route = None
        self.is_on_turn = False
        self.hozene = None
        self.kostka = None

    def create_kostka(self):
        self.kostka = Dvojkostka()
    
    def hod_kostkou(self):
        self.hozene = self.kostka.hod_kostkou()
        print(f"{self.color} hodil(a) {self.hozene}")
    
    def create_poss_moves(self,current_position, dice_values):
        possible_moves = []
        
        for dice_value in dice_values:
            new_position = current_position + dice_value
            if new_position <= len(self.player_route) - 1:
                # Check if the new position is within bounds of the player's route
                candidate_pole = self.player_route[new_position]
                if candidate_pole.is_empty() or (len(candidate_pole.stones) == 1 and candidate_pole.stones[0].color == self.color):
                    # Can move to an empty pole or a pole with own stone
                    possible_moves.append((current_position, new_position))
        
        return possible_moves

    def move_stone(self, stone, cilove_pole):
        if stone and cilove_pole is not None:
            stone.move(cilove_pole)