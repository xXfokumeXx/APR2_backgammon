import random

class Dvojkostka:
    def __init__(self):
        ...

    def hod_kostkou():
        vrzene = []
        for x in range(2):
            vrzene.append(random.randint(1,6))
        if vrzene[0] == vrzene[1]:
            vrzene = vrzene.append(vrzene)
  
        print(vrzene)
    
    hod_kostkou()
        