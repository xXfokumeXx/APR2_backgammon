import pygame


# konstant, ktere jsou neměnné a budeme je pouzivat v dalsich castech programu
RICH_BROWN = (222, 184, 135)
LIGHT_BROWN = (139, 69, 19)
DARK_BROWN = (92,59,18)
BLACK = (0,0,0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
BOARD_WIDTH = SCREEN_WIDTH - 200
BOARD_HEIGHT = SCREEN_HEIGHT - 100
FRAMES_PER_SECOND = 60
PADDING = 50


ROWS, COLS = 2, 14  # standartní
RECT_WIDTH = BOARD_WIDTH//COLS  # Výška jednoho pole pro hrací kámen
RECT_HEIGHT = BOARD_HEIGHT//ROWS  # Šířka jednoho pole pro hrací kámen
STONE_RADIUS = 10

#FONT = pygame.font.Font(None,  30)