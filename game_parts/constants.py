import pygame


# konstant, ktere jsou neměnné a budeme je pouzivat v dalsich castech programu
RICH_BROWN = (222, 184, 135)
LIGHT_BROWN = (139, 69, 19)
DARK_BROWN = (92,59,18)
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 60

ROWS, COLS = 2, 12  # standartní
RECT_WIDTH = SCREEN_WIDTH//COLS  # Výška jednoho pole pro hrací kámen
RECT_HEIGHT = SCREEN_HEIGHT//ROWS  # Šířka jednoho pole pro hrací kámen