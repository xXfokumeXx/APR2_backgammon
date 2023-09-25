import pygame
import json
from game_parts.herniPole import HerniPole
from game_parts.constants import *
import game_parts.herniPole as hp
from game_parts.stone import *
from .bar import Bar

class HerniDeska:

    def __init__(self, win, hernideska = None):
        self.hernideska = hernideska
        if not self.hernideska:
            self.hernideska = []
        self.win = win
        self.create_herni_deska(win)
        self.load_board_from_json("game_parts/newgame.json")

    def load_board_from_json(self, json_file_path):
        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)
                board_data = data.get('board')

                for i, point_data in enumerate(board_data):
                    id = point_data.get("ID")
                    player = point_data.get('color', 'none')
                    count = point_data.get('count', 0)
                    print(id,player,count)

                    if player != 'none':
                        stone_color = 'white' if player == 'white' else 'black'
                        
                        for _ in range(count):
                            stone = Stone(i, stone_color)  # vytvori kamen
                            self.umisti_kamen(stone, i)  # polozi kamen na herniDesku
                            

        except FileNotFoundError:
            print("Error: JSON file not found.")
        except Exception as e:
            print(f"Error loading JSON data: {str(e)}")
        


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
        
            # vykresleni Baru
            for col in range(COLS-8,COLS-7):
                x = PADDING + col * RECT_WIDTH
                y = PADDING + row * RECT_HEIGHT
                ID = i
                bar = Bar(ID, x, y)
                print(bar.ID, bar.x, bar.y)
                self.hernideska.append(bar)
                i += 1


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
                pygame.draw.rect(win, color, pygame.Rect(x, y, RECT_WIDTH, RECT_HEIGHT),width=5)
                #"domecky" do kterých musí ideálně každý z hráču vyvést co nejvíce kamenů
    """
                
    def draw(self, win):
        for pole in self.hernideska:
            if pole.ID % 2 == 0:
                color = LIGHT_BROWN
            else:
                color = DARK_BROWN
            pygame.Surface.fill(win, color,pygame.Rect(pole.x, pole.y, RECT_WIDTH, RECT_HEIGHT))
            pygame.draw.rect(win, BLACK, pygame.Rect(pole.x, pole.y, RECT_WIDTH, RECT_HEIGHT),width=2)
            if pole.ID == 6 or pole.ID == 19:
                pygame.Surface.fill(win, RICH_BROWN,pygame.Rect(pole.x, pole.y, RECT_WIDTH, RECT_HEIGHT))
                pygame.draw.rect(win, BLACK, pygame.Rect(pole.x, pole.y, RECT_WIDTH, RECT_HEIGHT),width=5)


    #najdu pole podle pole.ID
    def umisti_kamen(self, stone, pole_id:int):
        for pole in self.hernideska:
            if pole.ID == pole_id:
                pole.push(stone)
                stone.position = (pole.x, pole.y)


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