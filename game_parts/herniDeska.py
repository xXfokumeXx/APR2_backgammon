import pygame
from game_parts.herniPole import HerniPole
from game_parts.constants import ROWS, COLS, RECT_HEIGHT, RECT_WIDTH, LIGHT_BROWN, DARK_BROWN,BLACK, RICH_BROWN, PADDING

class HerniDeska:

    def __init__(self, win, hernideska = None):
        self.hernideska = hernideska
        if not self.hernideska:
            self._hernideska = []
        self.win = win
        self.create_herni_deska(win)
        

    def create_herni_deska(self, win):
        """pripravi na vykresleni herni desku slozenou z hernich polí implementovaných jako zásobníky"""
        i = 0
        for row in range(ROWS):
            for col in range(0,COLS-8):
                x = PADDING + col * RECT_WIDTH
                y = PADDING + row * RECT_HEIGHT
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
        
            
            for col in range(COLS-8,COLS-7):
                x = PADDING + col * RECT_WIDTH
                y = PADDING + row * RECT_HEIGHT
                ID = i
                pole = HerniPole(ID, x, y)
                print(pole.ID, pole.x, pole.y)
                self._hernideska.append(pole)
                if row % 2 == 0:
                    color = LIGHT_BROWN if col % 2 == 0 else BLACK
                else:
                    color = DARK_BROWN if col % 2 == 0 else BLACK
                i += 1
                pygame.Surface.fill(win, DARK_BROWN,pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT))
                pygame.draw.rect(win, BLACK, pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT),width=5)

            for col in range(COLS-7,COLS-1):
                x = PADDING + col * RECT_WIDTH
                y = PADDING + row * RECT_HEIGHT
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
            
            for col in range(COLS-1,COLS):
                x = PADDING + col * RECT_WIDTH
                y = PADDING + row * RECT_HEIGHT
                ID = i
                pole = HerniPole(ID, x, y)
                print(pole.ID, pole.x, pole.y)
                self._hernideska.append(pole)
                if row % 2 == 0:
                    color = LIGHT_BROWN if col % 2 == 0 else BLACK
                else:
                    color = DARK_BROWN if col % 2 == 0 else BLACK
                i += 1
                pygame.Surface.fill(win, DARK_BROWN,pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT))
                pygame.draw.rect(win, color, pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT),width=5)
                

    def __repr__(self):
        return f"{self._hernideska}"

# deska = HerniDeska()
# print(deska)

        