import pygame


# konstant, ktere jsou neměnné a budeme je pouzivat v dalsich castech programu
RICH_BROWN = (222, 184, 135)
LIGHT_BROWN = (139, 69, 19)
DARK_BROWN = (92,59,18)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480
BOARD_WIDTH = SCREEN_WIDTH - 200
BOARD_HEIGHT = SCREEN_HEIGHT - 100
FRAMES_PER_SECOND = 60
PADDING = 50


ROWS, COLS = 2, 14
RECT_WIDTH = BOARD_WIDTH//COLS  # Šířka jednoho pole pro hrací kámen
RECT_HEIGHT = BOARD_HEIGHT//ROWS  # Výška jednoho pole pro hrací kámen
STONE_RADIUS = RECT_WIDTH//2 * 0.7

#FONT = pygame.font.Font(None,  30)