import random

class Dvojkostka:
    def __init__(self):
        ...

    def hod_kostkou():
        vrzene = []
        for x in range(2):
            vrzene.append(random.randint(1,6))
        if vrzene[0] == vrzene[1]:
            for x in range(2):
                i = 2
                vrzene.insert(i,vrzene[0])
                i += 1
        print(vrzene)
    
    hod_kostkou()
        