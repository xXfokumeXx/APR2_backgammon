import pygame
import game_parts.herniDeska as hd
import game_parts.herniPole as hp
import game
import random
from player import Player
from game_parts.herniPole import HerniPole
from game_parts.constants import *
from game import Game
from game_parts.stone import *

# 3 - Inicializer okna

if __name__ == "__main__":
    pygame.init()

    # Load and place stones from the JSON file
    game = Game()
    game.run_game_loop()