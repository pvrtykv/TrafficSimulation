import time 

refresh=1 #czas odświeżania w sekundach
randomauto=1 #rozrzuca samochody po mapie w momencie rozpoczęcia symulacji

class Cell:
    def __init__(self):
        self.cond=0
        self.exists=0
        self.id=0
class Car:
    def __init__(self):
        self.v=0
        self.category="car"
        self.id=0
        self.exists=1

class Counter:
    def __init__(self):
        self.value=0
    def plus(self):
        self.value+=1
    def get(self):
        return self.value

carid=Counter()
timer=Counter()
firstlane=[]
secondlane=[]
thirdlane=[]
cars=[]
def creation():
    for i in range (7587):
        firstlane.append(Cell())
        secondlane.append(Cell())
        thirdlane.append(Cell())
        if i>3266:
            thirdlane[i].exists=1
        else:
            thirdlane[i].exists=0

def random_auto(randomauto):
    if randomauto==1:
        for i in range (7587):
            if i%7==0 and i%35!=0:
                #firstlane.append(Cell())
                firstlane[i].cond=1 #zajmowanie komórki
                cars.append(Car())
                cars[len(cars)-1].category="car"
                cars[len(cars)-1].v=4 #4 k/s to ok 100 km/h
                cars[len(cars)-1].id=carid.get()
                carid.plus()
                firstlane[i].id=cars[len(cars)-1].id
            if i%7==0 and i%35==0:
                #firstlane.append(Cell())
                firstlane[i].cond=1 #zajmowanie komórki
                cars.append(Car())
                cars[len(cars)-1].category="truck"
                cars[len(cars)-1].v=3 #4 k/s to ok 80 km/h
                cars[len(cars)-1].id=carid.get()
                carid.plus()
                firstlane[i].id=cars[len(cars)-1].id

creation()
random_auto(randomauto)
while (1):
    for i in range(7587):
        #kontrola zmiany pasa
        if i>3 and i<3267: #odcinek bez trzeciego pasa
            if firstlane[i].cond==1:
                if firstlane[i+1].cond==1 or firstlane[i+2].cond==1 or firstlane[i+3].cond==1 or firstlane[i+4].cond==1:
                    if secondlane[i].cond==0 and secondlane[i+1].cond==0 and secondlane[i+2].cond==0 and secondlane[i+3].cond==0 and secondlane[i+4].cond==0:
                        if secondlane[i-3].cond==0 and secondlane[i-2].cond==0 and secondlane[i-1].cond==0: #sprawdzanie warunków zmiany pasa
                            secondlane[i+1].id=firstlane[i].id
                            secondlane[i+1].cond=1
                            firstlane[i].cond=0
                            firstlane[i].id=0 #przenoszenie obiektu na drugi pas i opróżnianie zajmowanej dotychczas komórki
                            if cars[secondlane[i+1].id].v>0:
                                cars[secondlane[i+1].id].v-=1
            if secondlane[i].cond==1: #chce wrócić na prawy pas
                if firstlane[i+1].cond==0 or firstlane[i+2].cond==0 or firstlane[i+3].cond==0 or firstlane[i+4].cond==0:
                    if  firstlane[i-3].cond==0 and firstlane[i-2].cond==0 and firstlane[i-1].cond==0:
                        firstlane[i+1].id=secondlane[i+1].id
                        firstlane[i+1].cond=1
                        secondlane[i].cond=0
                        secondlane[i].id=0
                        if cars[firstlane[i+1].id].v>0:
                            cars[firstlane[i+1].id].v-=1
        if i>3266 and i<7583: #przy komórkach na skraju listy nie zmieniamy pasa; wariant dla części drogi z trzema pasami
            if firstlane[i].cond==1:
                if firstlane[i+1].cond==1 or firstlane[i+2].cond==1 or firstlane[i+3].cond==1 or firstlane[i+4].cond==1:
                    if secondlane[i].cond==0 and secondlane[i+1].cond==0 and secondlane[i+2].cond==0 and secondlane[i+3].cond==0 and secondlane[i+4].cond==0:
                        if secondlane[i-3].cond==0 and secondlane[i-2].cond==0 and secondlane[i-1].cond==0: #sprawdzanie warunków zmiany pasa
                            secondlane[i+1].id=firstlane[i].id
                            secondlane[i+1].cond=1
                            firstlane[i].cond=0
                            firstlane[i].id=0 #przenoszenie obiektu na drugi pas i opróżnianie zajmowanej dotychczas komórki
                            if cars[secondlane[i+1].id].v>0:
                                cars[secondlane[i+1].id].v-=1
            if secondlane[i].cond==1: #zmiana położenia z drugiego pasa
                if secondlane[i+1].cond==1 or secondlane[i+2].cond==1 or secondlane[i+3].cond==1 or secondlane[i+4].cond==1:
                    if firstlane[i+1].cond==0 or firstlane[i+2].cond==0 or firstlane[i+3].cond==0 or firstlane[i+4].cond==0: #zmiana pasa ze środkowego na prawy
                        if  firstlane[i-3].cond==0 and firstlane[i-2].cond==0 and firstlane[i-1].cond==0:
                            firstlane[i+1].id=secondlane[i+1].id
                            firstlane[i+1].cond=1
                            secondlane[i].cond=0
                            secondlane[i].id=0
                            if cars[firstlane[i+1].id].v>0:
                                cars[firstlane[i+1].id].v-=1
                    elif thirdlane[i+1].cond==0 or thirdlane[i+2].cond==0 or thirdlane[i+3].cond==0 or thirdlane[i+4].cond==0: #zmiana pasa ze środkowego na lewy
                        if  thirdlane[i-3].cond==0 and thirdlane[i-2].cond==0 and thirdlane[i-1].cond==0:
                            thirdlane[i+1].id=thirdlane[i+1].id
                            thirdlane[i+1].cond=1
                            secondlane[i].cond=0
                            secondlane[i].id=0
                            if cars[firstlane[i+1].id].v>0:
                                cars[firstlane[i+1].id].v-=1
            if thirdlane[i].cond==1: #zjazd z trzeciego pasa na środkowy
                if thirdlane[i+1].cond==1 or thirdlane[i+2].cond==1 or thirdlane[i+3].cond==1 or thirdlane[i+4].cond==1:
                    if secondlane[i].cond==0 and secondlane[i+1].cond==0 and secondlane[i+2].cond==0 and secondlane[i+3].cond==0 and secondlane[i+4].cond==0:
                        if secondlane[i-3].cond==0 and secondlane[i-2].cond==0 and secondlane[i-1].cond==0: #sprawdzanie warunków zmiany pasa
                            secondlane[i+1].id=thirdlane[i].id
                            secondlane[i+1].cond=1
                            thirdlane[i].cond=0
                            thirdlane[i].id=0 #przenoszenie obiektu na drugi pas i opróżnianie zajmowanej dotychczas komórki
                            if cars[secondlane[i+1].id].v>0:
                                cars[secondlane[i+1].id].v-=1

        #kontrola drogi przed pojazdem i dostosowanie prędkości
        if firstlane[i].cond==1 and i<7583: #sprawdzanie czy konieczne jest hamowanie lub można przyspieszyć
            if firstlane[i+1].cond==1 or firstlane[i+2].cond==1 or firstlane[i+3].cond==1 or firstlane[i+4].cond==1:
                if cars[firstlane[i].id].v>0:
                    cars[firstlane[i].id].v-=1
            else:
                if cars[firstlane[i].id].category=="car" and cars[firstlane[i].id].v<5:
                    cars[firstlane[i].id].v+=1
                if cars[firstlane[i].id].category=="truck" and cars[firstlane[i].id].v<4:
                    cars[firstlane[i].id].v+=1
        if secondlane[i].cond==1 and i<7583:
            if secondlane[i+1].cond==1 or secondlane[i+2].cond==1 or secondlane[i+3].cond==1 or secondlane[i+4].cond==1:
                if cars[secondlane[i].id].v>0:
                    cars[secondlane[i].id].v-=1
            else:
                if cars[secondlane[i].id].category=="car" and cars[secondlane[i].id].v<5:
                    cars[secondlane[i].id].v+=1
                if cars[secondlane[i].id].category=="truck" and cars[secondlane[i].id].v<4:
                    cars[secondlane[i].id].v+=1
        if thirdlane[i].cond==1 and i<7583:
            if thirdlane[i+1].cond==1 or thirdlane[i+2].cond==1 or thirdlane[i+3].cond==1 or thirdlane[i+4].cond==1:
                if cars[thirdlane[i].id].v>0:
                    cars[thirdlane[i].id].v-=1
            else:
                if cars[thirdlane[i].id].category=="car" and cars[thirdlane[i].id].v<5:
                    cars[thirdlane[i].id].v+=1
                if cars[thirdlane[i].id].category=="truck" and cars[thirdlane[i].id].v<4:
                    cars[thirdlane[i].id].v+=1

        #usuwanie samochodów znajdujących się poza drogą
        if i>7582:
            if firstlane[i].cond==1:
                cars[firstlane[i].id].exists=0
                firstlane[i].cond=0
                firstlane[i].id=0
            if secondlane[i].cond==1:
                cars[secondlane[i].id].exists=0
                secondlane[i].cond=0
                secondlane[i].id=0
            if thirdlane[i].cond==1:
                cars[thirdlane[i].id].exists=0
                thirdlane[i].cond=0
                thirdlane[i].id=0

        #przemieszczenie pojazdu w oparciu o obliczoną wcześniej prędkość
        if firstlane[i].cond==1:
            firstlane[i+cars[firstlane[i].id].v].cond=1
            firstlane[i].cond=0
            firstlane[i+cars[firstlane[i].id].v].id=firstlane[i].id
            firstlane[i].id=0
        if secondlane[i].cond==1:
            secondlane[i+cars[secondlane[i].id].v].cond=1
            secondlane[i].cond=0
            secondlane[i+cars[secondlane[i].id].v].id=secondlane[i].id
            secondlane[i].id=0
        if thirdlane[i].cond==1:
            thirdlane[i+cars[thirdlane[i].id].v].cond=1
            thirdlane[i].cond=0
            thirdlane[i+cars[thirdlane[i].id].v].id=thirdlane[i].id
            thirdlane[i].id=0

        #wjazd pojazdów na węzłach
        #na budowanych odcinkach nie ma tej funkcjonalności ze względu na brak wiedzy co do natężenia ruchu jakie tam ma być
        if timer.get()%3==0 and timer.get()%15!=0:
            if firstlane[333].cond==0 and firstlane[332].cond==0 and firstlane[331].cond==0 and firstlane[330].cond==0:
                firstlane[333].cond=1 #zajmowanie komórki
                cars.append(Car())
                cars[len(cars)-1].category="car"
                cars[len(cars)-1].v=1 #1 k/s to ok 25 km/h
                cars[len(cars)-1].id=carid.get()
                carid.plus()
                firstlane[i].id=cars[len(cars)-1].id
            if firstlane[880].cond==0 and firstlane[879].cond==0 and firstlane[878].cond==0 and firstlane[877].cond==0:
                firstlane[880].cond=1 #zajmowanie komórki
                cars.append(Car())
                cars[len(cars)-1].category="car"
                cars[len(cars)-1].v=1 #1 k/s to ok 25 km/h
                cars[len(cars)-1].id=carid.get()
                carid.plus()
                firstlane[i].id=cars[len(cars)-1].id
            if firstlane[1067].cond==0 and firstlane[1066].cond==0 and firstlane[1065].cond==0 and firstlane[1064].cond==0:
                firstlane[1067].cond=1 #zajmowanie komórki
                cars.append(Car())
                cars[len(cars)-1].category="car"
                cars[len(cars)-1].v=1 #1 k/s to ok 25 km/h
                cars[len(cars)-1].id=carid.get()
                carid.plus()
                firstlane[i].id=cars[len(cars)-1].id
            if firstlane[1667].cond==0 and firstlane[1666].cond==0 and firstlane[1665].cond==0 and firstlane[1664].cond==0:
                firstlane[1667].cond=1 #zajmowanie komórki
                cars.append(Car())
                cars[len(cars)-1].category="car"
                cars[len(cars)-1].v=1 #1 k/s to ok 25 km/h
                cars[len(cars)-1].id=carid.get()
                carid.plus()
                firstlane[i].id=cars[len(cars)-1].id
            if firstlane[1934].cond==0 and firstlane[1933].cond==0 and firstlane[1932].cond==0 and firstlane[1931].cond==0:
                firstlane[1934].cond=1 #zajmowanie komórki
                cars.append(Car())
                cars[len(cars)-1].category="car"
                cars[len(cars)-1].v=1 #1 k/s to ok 25 km/h
                cars[len(cars)-1].id=carid.get()
                carid.plus()
                firstlane[i].id=cars[len(cars)-1].id
            if firstlane[2387].cond==0 and firstlane[2386].cond==0 and firstlane[2385].cond==0 and firstlane[2384].cond==0:
                firstlane[2387].cond=1 #zajmowanie komórki
                cars.append(Car())
                cars[len(cars)-1].category="car"
                cars[len(cars)-1].v=1 #1 k/s to ok 25 km/h
                cars[len(cars)-1].id=carid.get()
                carid.plus()
                firstlane[i].id=cars[len(cars)-1].id
        if timer.get()%3==0 and timer.get()%15==0:
            if firstlane[333].cond==0 and firstlane[332].cond==0 and firstlane[331].cond==0 and firstlane[330].cond==0:
                firstlane[333].cond=1 #zajmowanie komórki
                cars.append(Car())
                cars[len(cars)-1].category="truck"
                cars[len(cars)-1].v=1 #1 k/s to ok 25 km/h
                cars[len(cars)-1].id=carid.get()
                carid.plus()
                firstlane[i].id=cars[len(cars)-1].id
            if firstlane[880].cond==0 and firstlane[879].cond==0 and firstlane[878].cond==0 and firstlane[877].cond==0:
                firstlane[880].cond=1 #zajmowanie komórki
                cars.append(Car())
                cars[len(cars)-1].category="truck"
                cars[len(cars)-1].v=1 #1 k/s to ok 25 km/h
                cars[len(cars)-1].id=carid.get()
                carid.plus()
                firstlane[i].id=cars[len(cars)-1].id
            if firstlane[1067].cond==0 and firstlane[1066].cond==0 and firstlane[1065].cond==0 and firstlane[1064].cond==0:
                firstlane[1067].cond=1 #zajmowanie komórki
                cars.append(Car())
                cars[len(cars)-1].category="truck"
                cars[len(cars)-1].v=1 #1 k/s to ok 25 km/h
                cars[len(cars)-1].id=carid.get()
                carid.plus()
                firstlane[i].id=cars[len(cars)-1].id
            if firstlane[1667].cond==0 and firstlane[1666].cond==0 and firstlane[1665].cond==0 and firstlane[1664].cond==0:
                firstlane[1667].cond=1 #zajmowanie komórki
                cars.append(Car())
                cars[len(cars)-1].category="truck"
                cars[len(cars)-1].v=1 #1 k/s to ok 25 km/h
                cars[len(cars)-1].id=carid.get()
                carid.plus()
                firstlane[i].id=cars[len(cars)-1].id
            if firstlane[1934].cond==0 and firstlane[1933].cond==0 and firstlane[1932].cond==0 and firstlane[1931].cond==0:
                firstlane[1934].cond=1 #zajmowanie komórki
                cars.append(Car())
                cars[len(cars)-1].category="truck"
                cars[len(cars)-1].v=1 #1 k/s to ok 25 km/h
                cars[len(cars)-1].id=carid.get()
                carid.plus()
                firstlane[i].id=cars[len(cars)-1].id
            if firstlane[2387].cond==0 and firstlane[2386].cond==0 and firstlane[2385].cond==0 and firstlane[2384].cond==0:
                firstlane[2387].cond=1 #zajmowanie komórki
                cars.append(Car())
                cars[len(cars)-1].category="truck"
                cars[len(cars)-1].v=1 #1 k/s to ok 25 km/h
                cars[len(cars)-1].id=carid.get()
                carid.plus()
                firstlane[i].id=cars[len(cars)-1].id

        #wyjazd pojazdów na węzłach od Skawiny
        if timer.get()%5==0:
            if firstlane[2974].cond==1:
                cars[firstlane[2974].id].exists=0
                firstlane[2974].id=0
            if firstlane[3267].cond==1:
                cars[firstlane[3267].id].exists=0
                firstlane[3267].id=0
            if firstlane[4040].cond==1:
                cars[firstlane[4040].id].exists=0
                firstlane[4040].id=0
            if firstlane[4533].cond==1:
                cars[firstlane[4533].id].exists=0
                firstlane[4533].id=0
            if firstlane[4880].cond==1:
                cars[firstlane[4880].id].exists=0
                firstlane[4880].id=0

        #Tutaj po każdym kroku pętli ma być wykonywane rysowanie.
        #Należy przeiterować tablice firstlane, secondlane i thirdlane
        #Jeśli xxxxxlane[i].cond==1(znaczy to że komórka jest zapełniona), należy ją nanieść na wizualizację jako punkt.
        #Program nie znajduje błędów, ale jest możliwe, że nie działa poprawnie przez brak możliwości przetestowania.
        #Jaki węzeł ma jaki numer w tablicy można znaleźć w pliku Danev2.

    print("Next step")
    timer.plus();
    time.sleep(refresh)
