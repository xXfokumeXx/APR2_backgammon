import pygame
from game_parts.herniPole import HerniPole
from game_parts.constants import *
import game_parts.herniPole as hp
from game_parts.stone import *

class HerniDeska:

    def __init__(self, win, hernideska = None):
        self.hernideska = hernideska
        if not self.hernideska:
            self.hernideska = []
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
                self.hernideska.append(pole)
                i += 1
        
            
            """ for col in range(COLS-8,COLS-7):
                x = PADDING + col * RECT_WIDTH
                y = PADDING + row * RECT_HEIGHT
                ID = i
                pole = HerniPole(ID, x, y)
                print(pole.ID, pole.x, pole.y)
                self.hernideska.append(pole)
                if row % 2 == 0:
                    color = LIGHT_BROWN if col % 2 == 0 else BLACK
                else:
                    color = DARK_BROWN if col % 2 == 0 else BLACK
                i += 1
                pygame.Surface.fill(win, DARK_BROWN,pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT))
                pygame.draw.rect(win, BLACK, pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT),width=5)
 """
            for col in range(COLS-7,COLS-1):
                x = PADDING + col * RECT_WIDTH
                y = PADDING + row * RECT_HEIGHT
                ID = i
                pole = HerniPole(ID, x, y)
                self.hernideska.append(pole)
                i += 1

        for pole in self.hernideska:
            print(f"Pole ID: {pole.ID}, x: {pole.x}, y: {pole.y}")    
            
        """  for col in range(COLS-1,COLS):
                x = PADDING + col * RECT_WIDTH
                y = PADDING + row * RECT_HEIGHT
                ID = i
                pole = HerniPole(ID, x, y)
                print(pole.ID, pole.x, pole.y)
                self.hernideska.append(pole)
                if row % 2 == 0:
                    color = LIGHT_BROWN if col % 2 == 0 else BLACK
                else:
                    color = DARK_BROWN if col % 2 == 0 else BLACK
                i += 1
                pygame.Surface.fill(win, DARK_BROWN,pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT))
                pygame.draw.rect(win, color, pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT),width=5) """
                
    def draw(self, win):
        for pole in self.hernideska:
            if pole.ID % 2 == 0:
                color = LIGHT_BROWN
            else:
                color = DARK_BROWN
            pygame.Surface.fill(win, color,pygame.Rect(pole.x, pole.y, RECT_WIDTH, RECT_HEIGHT))
            pygame.draw.rect(win, BLACK, pygame.Rect(pole.x, pole.y, RECT_WIDTH, RECT_HEIGHT),width=2)

    #najdu pole podle pole.ID
    def umisti_kamen(self, stone, pole_id:int):
        for pole in self.hernideska:
            if pole.ID == pole_id:
                pole.push(stone)
                stone.position = (pole.ID, pole.x, pole.y)
                break

    def __repr__(self):
        return f"{self.hernideska}"
    
    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self.hernideska):
            result = self.hernideska[self.current_index]
            self.current_index += 1
            return result
        else:
            raise StopIteration

        