import pygame
from game_parts.constants import *

def drawGrid():
    for x in range(0, SCREEN_WIDTH, RECT_WIDTH):
        for y in range(0, SCREEN_HEIGHT, RECT_HEIGHT):
            rect = pygame.Rect(x, y, RECT_WIDTH , RECT_HEIGHT)
            pygame.draw.rect(window, LIGHT_BROWN, rect, 1)