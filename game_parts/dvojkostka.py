import random

class Dvojkostka:
    def __init__(self):
        ...

    def hod_kostkou():
        vrzene = []
        for x in range(2):
            vrzene.append(random.randint(1,6))
        if vrzene[0] == vrzene[1]:
            vrzene = [vrzene[0]] * 4
        print(vrzene)
        return (vrzene)
  
    
    hod_kostkou()
        