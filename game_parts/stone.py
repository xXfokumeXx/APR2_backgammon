import pygame
import sys
from game_parts.constants import *
import game_parts.herniDeska as hd
import game_parts.herniPole as hp
from game_parts.herniPole import HerniPole

class Stone:

    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.kicked = False
        self.history = []
        self.position = None
    
    def move(self, pole):
        if isinstance(pole, HerniPole):
            # Mark the current pole as visited
            self.history.append(pole)
            self.position = (pole.x, pole.y)  # Update the stone's position
            print(f"presun na pole {pole.ID}")
        else:
            print("neplatne pole.")

    def draw(self, win):
        if self.position:
            pygame.draw.circle(win, self.color, self.position, STONE_RADIUS)