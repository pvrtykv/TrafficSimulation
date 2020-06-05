class Cell:
    def __init__(self,):
        self.cond=0
        self.car=NULL
        self.vmax=0
        self.exists=1

class Car:
    def __init__(self,category):
        self.v=0
        self.category="car"
        self.lane=0

firstlane=[]
secondlane=[]
thirdlane=[]

def creation():
    for i in range (7587):
        firstlane.append(Cell())
        secondlane.append(Cell())
        thirdlane.append(Cell())
        if i>3266:
            thirdlane[i].exists=0