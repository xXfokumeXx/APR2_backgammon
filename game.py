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
        self.stone = Stone(1, "red")

    def draw_objects(self):
        #vykresleni kamenu
        self.deska.draw(self.win)
        self.stone.draw(self.win)
        # vykreslení zmen na obrazovku
        pygame.display.flip()
    
    #funkce na overeni na co klikam
    def click(self, event):
        #pokud vybírám
        if self.selecting:
            #kontrola zda je kámen, respektive pole s nějakým kamenem vybráno
            curs_x, curs_y = pygame.mouse.get_pos()
            for stone in self.stones:
                if stone.position and pygame.Rect(stone.position[0] - STONE_RADIUS, stone.position[1] - STONE_RADIUS, 2 * STONE_RADIUS, 2 * STONE_RADIUS).collidepoint(curs_x, curs_y):
                    self.selected_stone = stone
                    self.selecting_mode = False
                    break
        else:
            # Check if a valid pole is clicked and move the stone
            curs_x, curs_y = pygame.mouse.get_pos()
            for pole in self.deska.hernideska:
                if pygame.Rect(pole.x, pole.y, RECT_WIDTH, RECT_HEIGHT).collidepoint(curs_x, curs_y):
                    if pole.mozno_tahnout(self.selected_stone):
                        self.selected_stone.move(pole)
                        self.selected_stone = None
                        self.selecting_mode = True
                    break

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
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.click(event)
                """  curs_x, curs_y = pygame.mouse.get_pos()
                    print(curs_x, curs_y)
                    for pole in self.deska:
                        if pygame.Rect(pole.x, pole.y, RECT_WIDTH, RECT_HEIGHT).collidepoint(curs_x, curs_y):
                            print(f"pole.ID: {pole.ID}")
 """

            self.draw_objects()


            # "zpomalení" behu programu na FPS definované v constants.py
            self.clock.tick(FRAMES_PER_SECOND)
