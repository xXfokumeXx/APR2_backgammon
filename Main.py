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

    def drawGrid():
        for x in range(0, SCREEN_WIDTH, RECT_WIDTH):
            for y in range(0, SCREEN_HEIGHT, RECT_HEIGHT):
                rect = pygame.Rect(x, y, RECT_WIDTH , RECT_HEIGHT)
                pygame.draw.rect(window, LIGHT_BROWN, rect, 1)
    drawGrid()
    # vypsani fps na listu okna
    pygame.display.set_caption("FPS: " + str(clock.get_fps()))
    # vykreslení zmen na obrazovku
    pygame.display.flip()

    # "zpomalení" behu programu na FPS definované v constants.py
    clock.tick(FRAMES_PER_SECOND)
