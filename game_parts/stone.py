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
        self.history = []
        self.kicked = False
        self.position = None
        self.destPole = None
    
    def move(self, pole):
        if isinstance(pole, HerniPole):
            if pole.ID != -1:
                # prida aktuální pole do historie navštivených polí
                self.history.append(pole.ID)
                pole.push(self)
                self.position = (pole.x, pole.y)
                #self.position = (pole.x, pole.y)  #Update pozice kamene
                print(f"presun kamene {self.number} na pole {pole.ID}")
        else:
            print("neplatne pole.")

    def draw(self, win, x, y):
        if self.position:
            stone_color = BLACK if self.color == 'white' else WHITE
            pygame.draw.circle(win, stone_color, (x, y), STONE_RADIUS)
            stone_color = WHITE if self.color == 'white' else BLACK
            pygame.draw.circle(win, stone_color, (x, y), STONE_RADIUS*0.8)

    def __repr__(self):
        return f"{self.number} {self.color}"
