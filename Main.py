import pygame
import sys
from game_parts.constants import *

# 3 - Initializer okna
pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# podminky, kdy se ma okno zavrit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit() 
            sys.exit()

    window.fill(RICH_BROWN)

    # vypsani fps na listu okna
    pygame.display.set_caption("FPS: " + str(clock.get_fps()))
    # vykreslení zmen na obrazovku
    pygame.display.flip()

    # "zpomalení" behu programu na FPS definované v constants.py
    clock.tick(FRAMES_PER_SECOND)
