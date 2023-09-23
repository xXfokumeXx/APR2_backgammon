import pygame
import game_parts.herniDeska as hd
import game_parts.herniPole as hp
from game_parts.herniPole import HerniPole
from game_parts.constants import *
from game import Game
from game_parts.stone import *

# 3 - Inicializer okna
pygame.init()


game = Game()
stone1 = Stone(1, BLACK)
stone2 = Stone(2, BLACK)
game.stones.append(stone1)
game.stones.append(stone2)
game.run_game_loop()