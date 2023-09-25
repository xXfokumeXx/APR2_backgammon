import pygame
import sys
import random
from player import Player
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
        self.players = [Player("white", [12,11,10,9,8,7,6,5,4,3,2,1,0,12,13,14,15,16,17,18,19,20,21,22,23,24]),
                         Player("black", [24,23,22,21,20,19,18,17,16,15,14,13,12,0,1,2,3,4,5,6,7,8,9,10,11,12])] 
        self.aktualni_hrac_i = random.randint(0,1)
        self.vytvor_kostku()
        
 

    def vytvor_kostku(self):
        for player in self.players:
            player.create_kostka()

    def hod_kostkou(self):
        self.players[self.aktualni_hrac_i].hod_kostkou()

    def draw_objects(self):
        #vykresleni kamenu
        self.deska.draw(self.win)
        for pole in self.deska.hernideska:
            pole.draw(self.win)
        # vykreslení zmen na obrazovku
        for stone in self.stones:
            if stone.position:
                stone.draw(self.win, stone.position[0], stone.position[1])
        pygame.display.flip()

    def switch_player(self):
        self.aktualni_hrac_i = (self.aktualni_hrac_i + 1) % len(self.players)
        self.hod_kostkou()
        print(self.aktualni_hrac_i)
        return self.aktualni_hrac_i

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            curs_x, curs_y = pygame.mouse.get_pos()
            for pole in self.deska.hernideska:
                if pygame.Rect(pole.x, pole.y, RECT_WIDTH, RECT_HEIGHT).collidepoint(curs_x, curs_y):
                    if self.selecting:
                        if self.selected_pole is None:
                            if not pole.is_empty():
                                self.selected_pole = pole
                                self.selected_stone = pole.stones[-1]
                                
                                print(f"Selected stone: {self.selected_stone.number}, Color: {self.selected_stone.color}")
                            else:
                                print("prazdne pole, nelze vybrat herni kamen, vyber jine pole")

                        else:
                            if pole == self.selected_pole:
                                self.selected_stone = None
                                self.selected_pole = None
                                self.click(event)
                            elif self.selected_pole.stones[-1].color == self.players[self.aktualni_hrac_i].color:
                                if pole.ID != 6 and pole.ID != 19:
                                    if len(pole.stones) <= 1 or pole.stones[-1].color == self.selected_stone.color:
                                        self.selected_stone.move(pole)
                                        self.selected_pole.stones.pop()
                                    else:
                                        print("Nelze tahnout na pozici s kameny odlišné barvy nebo na pole s více než 1 kamenem stejné barvy.")
                                else:
                                    print("Nelze presunout hraci kameny na toto herni pole! \nZkus tahnout na jine povolene pole")
                                self.selected_pole = None
                                self.selected_stone = None
                                self.switch_player()
                            else:
                                print("Nelze presunout hraci kameny na toto herni pole! \nZkus tahnout na jine povolene pole")
                                self.selected_pole = None
                                self.selected_stone = None    
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
            self.draw_objects()


            # "zpomalení" behu programu na FPS definované v constants.py
            self.clock.tick(FRAMES_PER_SECOND)