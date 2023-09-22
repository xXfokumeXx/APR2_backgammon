import pygame
from game_parts.herniPole import HerniPole
from game_parts.constants import ROWS, COLS, RECT_HEIGHT, RECT_WIDTH, LIGHT_BROWN, DARK_BROWN, RICH_BROWN

class HerniDeska:

    def __init__(self, win, hernideska = None):
        self.hernideska = hernideska
        if not self.hernideska:
            self._hernideska = []
        self.win = win
        self.create_herni_deska(win)
        

    def create_herni_deska(self, win):
        """ vytvori herni desku slozenou z hernich polí implementovaných jako zásobníky"""
        i = 0
        for row in range(ROWS):
            for col in range(COLS):
                x = 50 + col * RECT_WIDTH
                y = 50 + row * RECT_HEIGHT
                ID = i
                pole = HerniPole(ID, x, y)
                print(pole.ID, pole.x, pole.y)
                self._hernideska.append(pole)
                if row % 2 == 0:
                    color = LIGHT_BROWN if col % 2 == 0 else DARK_BROWN
                else:
                    color = DARK_BROWN if col % 2 == 0 else LIGHT_BROWN
                i += 1
                pygame.draw.rect(win, color, pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT))

    def __repr__(self):
        return f"{self._hernideska}"

# deska = HerniDeska()
# print(deska)

        