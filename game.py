import pygame
import sys
from game_parts.constants import *
import game_parts.herniDeska as hd
import game_parts.herniPole as hp


class Game:


    def __init__(self):
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.window.fill(RICH_BROWN)
        self.deska = hd.HerniDeska(self.window)

    def draw_objects(self):
        # vykreslení zmen na obrazovku
        pygame.display.flip()

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
                    curs_x, curs_y = pygame.mouse.get_pos()
                    print(curs_x, curs_y)
                    for pole in self.deska:
                        if pygame.Rect(pole.x, pole.y, RECT_WIDTH, RECT_HEIGHT).collidepoint(curs_x, curs_y):
                            print(f"pole.ID: {pole.ID}")


            self.draw_objects()


            # "zpomalení" behu programu na FPS definované v constants.py
            self.clock.tick(FRAMES_PER_SECOND)
