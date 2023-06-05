import pygame
import game_parts.herniDeska as hd
import game_parts.herniPole as hp
from game_parts.herniPole import HerniPole
from game_parts.constants import *
from game import Game

# 3 - Initializer okna
pygame.init()

game = Game()
game.run_game_loop()