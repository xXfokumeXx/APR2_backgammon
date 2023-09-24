import pygame
import sys
from game_parts.constants import *
from game_parts.stone import *
import game_parts.herniDeska as hd
import game_parts.herniPole as hp


class Game:

    def __init__(self):
        self.win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.win.fill(RICH_BROWN)
        self.deska = hd.HerniDeska(self.win)
        self.stones = []
        self.selecting = True
        self.selected_stone = None
        self.selected_pole = None

    def draw_objects(self):
        #vykresleni kamenu
        self.deska.draw(self.win)
        for pole in self.deska.hernideska:
            pole.draw(self.win)
        # vykreslení zmen na obrazovku
        pygame.display.flip()

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            curs_x, curs_y = pygame.mouse.get_pos()
            for pole in self.deska.hernideska:
                if pygame.Rect(pole.x, pole.y, RECT_WIDTH, RECT_HEIGHT).collidepoint(curs_x, curs_y):
                    """                     
                    if self.selecting:
                    """
                    if self.selected_pole is None:
                        if not pole.is_empty(): 
                            self.selected_pole = pole
                            self.selected_stone = pole.stones[-1]
                            print(f"Selected stone: {self.selected_stone.number}, Color: {self.selected_stone.color}")
                            self.selecting = True
                        elif pole.is_empty():
                            print("prazdne pole, nelze vybrat herni kamen, vyber v jine pole")

                    else:
                        if pole != self.selected_pole:
                            self.selected_stone.move(pole)
                            self.selected_pole.stones.pop()  # popnu kamen z puvodni pozice   
                        self.selected_pole = None
                        self.selected_stone = None

                    """  
                        else:
                        if pole.is_empty():
                            print("prazdne pole, nelze vybrat herni kamen, vyber v jine pole")
                            self.selected_stone = None
                            self.selecting = True 
                        """
                        

    # gameloop
    def run_game_loop(self):
        while True:
            # vypsani fps na listu okna
            pygame.display.set_caption("FPS: " + str(self.clock.get_fps()))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                    sys.exit()
                self.click(event)
            """   elif event.type == pygame.MOUSEBUTTONDOWN:
                    # self.click(event)
                     curs_x, curs_y = pygame.mouse.get_pos()
                    print(curs_x, curs_y)
                    for pole in self.deska:
                        if pygame.Rect(pole.x, pole.y, RECT_WIDTH, RECT_HEIGHT).collidepoint(curs_x, curs_y):
                            print(f"pole.ID: {pole.ID} stones {len(pole.stones)}") """


            self.draw_objects()


            # "zpomalení" behu programu na FPS definované v constants.py
            self.clock.tick(FRAMES_PER_SECOND)