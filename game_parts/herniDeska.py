from herniPole import HerniPole
from constants import ROWS, COLS

class HerniDeska:

    def __init__(self):
        self._hernideska = []
        self.create_herni_deska()
        

    def create_herni_deska(self):
        """ vytvori herni desku slozenou z hernich polí implementovaných jako zásobníky"""
        i = 0
        for row in range(ROWS):
            for col in range(COLS):
                pole=HerniPole(i)
                self._hernideska.append(pole)
                i += 1

    def __repr__(self):
        return f"{self._hernideska}"

# deska = HerniDeska()
# print(deska)

        