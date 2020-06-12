import time 
import matplotlib.pyplot as plt

refresh=1 #czas odświeżania w sekundach
randomauto=1 #rozrzuca samochody po mapie w momencie rozpoczęcia symulacji

class Cell:
    def __init__(self):
        self.cond=0
        self.exists=0
        self.v=0
        self.category="car"

class Counter:
    def __init__(self):
        self.value=0
    def plus(self):
        self.value+=1
    def get(self):
        return self.value

timer=Counter()
firstlane=[]
secondlane=[]
thirdlane=[]
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
        for i in range (0,7586):
            if i%7==0 and i%35!=0:
                #firstlane.append(Cell())
                firstlane[i].cond=1 #zajmowanie komórki
                firstlane[i].category="car"
                firstlane[i].v=4 #4 k/s to ok 100 km/h
            if i%7==0 and i%35==0:
                #firstlane.append(Cell())
                firstlane[i].cond=1 #zajmowanie komórki
                firstlane[i].category="truck"
                firstlane[i].v=3 #4 k/s to ok 100 km/h

def car_counter(start, end):
    counter = 0
    for i in range (start, end-1):
        if firstlane[i].cond == 1:
            counter = counter + 1
        if secondlane[i].cond == 1:
            counter = counter + 1
        if thirdlane[i].cond == 1:
            counter = counter + 1
    return counter;



if __name__ == '__main__':
    creation()
    random_auto(randomauto)

    while (1):
        for i in range(7586,0,-1):
            """
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
            """   
            #kontrola drogi przed pojazdem i dostosowanie prędkości
            if firstlane[i].cond==1 and i<7583: #sprawdzanie czy konieczne jest hamowanie lub można przyspieszyć
                if firstlane[i+1].cond==1 or firstlane[i+2].cond==1 or firstlane[i+3].cond==1 or firstlane[i+4].cond==1:
                    if firstlane[i].v>0:
                        firstlane[i].v-=1
                else:
                    if firstlane[i].category=="car" and firstlane[i].v<5:
                        firstlane[i].v+=1
                    if firstlane[i].category=="truck" and firstlane[i].v<4:
                        firstlane[i].v+=1
            if secondlane[i].cond==1 and i<7583: #sprawdzanie czy konieczne jest hamowanie lub można przyspieszyć
                if secondlane[i+1].cond==1 or secondlane[i+2].cond==1 or secondlane[i+3].cond==1 or secondlane[i+4].cond==1:
                    if secondlane[i].v>0:
                        secondlane[i].v-=1
                else:
                    if secondlane[i].category=="car" and secondlane[i].v<5:
                        secondlane[i].v+=1
                    if secondlane[i].category=="truck" and secondlane[i].v<4:
                        secondlane[i].v+=1
            if thirdlane[i].cond==1 and i<7583: #sprawdzanie czy konieczne jest hamowanie lub można przyspieszyć
                if thirdlane[i+1].cond==1 or thirdlane[i+2].cond==1 or thirdlane[i+3].cond==1 or thirdlane[i+4].cond==1:
                    if thirdlane[i].v>0:
                        thirdlane[i].v-=1
                else:
                    if thirdlane[i].category=="car" and thirdlane[i].v<5:
                        thirdlane[i].v+=1
                    if thirdlane[i].category=="truck" and thirdlane[i].v<4:
                        thirdlane[i].v+=1
            
            
            #usuwanie samochodów znajdujących się poza drogą
            if i>7581:
                if firstlane[i].cond==1:
                    firstlane[i].cond=0
                if secondlane[i].cond==1:
                    secondlane[i].cond=0
                if thirdlane[i].cond==1:       
                    thirdlane[i].cond=0

            #przemieszczenie pojazdu w oparciu o obliczoną wcześniej prędkość
            if firstlane[i].cond==1:
                tmp=firstlane[i].v
                print("ABC")
                firstlane[i+tmp].cond=1
                firstlane[i+tmp].category=firstlane[i].category
                firstlane[i+tmp].v=firstlane[i].v
                firstlane[i].cond=0
            if secondlane[i].cond==1:
                secondlane[i+secondlane[i].v].cond=1
                secondlane[i+secondlane[i].v].category=secondlane[i].category
                secondlane[i+secondlane[i].v].v=secondlane[i].v
                scondlane[i].cond=0
            if thirdlane[i].cond==1:
                thirdlane[i+thirdlane[i].v].cond=1
                thirdlane[i+thirdlane[i].v].category=thirdlane[i].category
                thirdlane[i+thirdlane[i].v].v=thirdlane[i].v
                thirdlane[i].cond=0
            """
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
            """

        ####################################################################################################
        ####################################################################################################  
        ####################################################################################################
        ####################################################################################################
        ####################################################################################################
        ####################################################################################################
                  
        carcounter1 = car_counter(0,7586)
        print(carcounter1)
        """
        modlnica = car_counter(0,334)
        modlniczka = car_counter(334, 548)
        balice1 = car_counter(548, 881)
        balice2 = car_counter(881, 1068)
        bielany = car_counter(1068, 1935)
        tyniec = car_counter(1935, 2388)
        skawina = car_counter(2388, 2975)
        poludnie = car_counter(2975, 3268)
        lagiewniki = car_counter(3268, 4041)
        wieliczka = car_counter(4041, 4534)
        biezanow = car_counter(4534, 4881)
        przewoz = car_counter(4881, 5294)
        nowahuta = car_counter(5294, 5601)
        grebalow = car_counter(5601, 6001)
        mistrzejowice = car_counter(6001, 6241)
        batowice = car_counter(6241, 6641)
        wegrzce = car_counter(6641, 7188)
        zielonki = car_counter(7188,7588)


        labels = ['Modlnica - Modlniczka', 'Modlniczka - Balice I', 'Balice I - Balice II',
                  'Balice II - Bielany', 'Bielany - Tyniec',
          'Tyniec - Skawina', 'Skawina - Wieliczka', 'Wieliczka - Bieżanów',
                  'Bieżanów - Przewóz', 'Przewóz - Nowa Huta', 'Nowa Huta - Grębałów',
                  'Grębałów - Mistrzejowice', 'Mistrzejowice - Batowice', 'Batowice - Węgrzce',
                  'Węgrzce - Zielonki', 'Zielonki - Modlnica']
        sizes = [modlnica, modlniczka, balice1, balice2, bielany, tyniec,
         skawina, wieliczka, biezanow, przewoz, nowahuta, grebalow, mistrzejowice, batowice,
                 wegrzce, zielonki]
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes,  autopct='%1.1f%%')
        ax1.axis('equal')
        ax1.legend(labels, loc=3, fontsize="x-small")
        plt.show()

        print("Ilość pojazdów na odcinkach obwodnicy:\n")
        print("Modlnica - Modlniczka:", modlnica, "\nModlniczka - Balice I:", modlniczka,
              "\nBalice I - Balice II :", balice1, "\nBalice II - Bielany:", balice2,
              "\nBielany - Tyniec:", bielany, "\nTyniec - Skawina:", tyniec,
         "\nSkawina - Wieliczka:", skawina, "\nWieliczka - Bieżanów:", wieliczka,
            "\nBieżanów - Przewóz:", biezanow, "\nPrzewóz - Nowa Huta:", przewoz,
            "\nNowa Huta - Grębałów:", nowahuta, "\nGrębałów - Mistrzejowice:", grebalow,
            "\nMistrzejowice - Batowice:", mistrzejowice, "\nBatowice - Węgrzce:", batowice,
             "\nWęgrzce - Zielonki:", wegrzce,  "\nZielonki - Modlnica:", zielonki,
              "\nSuma:", car_counter(0,7588))
        """



           # carcounter = car_counter(0, 2)
            #print(carcounter);


        #Tutaj po każdym kroku pętli ma być wykonywane rysowanie.
            #Należy przeiterować tablice firstlane, secondlane i thirdlane
            #Jeśli xxxxxlane[i].cond==1(znaczy to że komórka jest zapełniona), należy ją nanieść na wizualizację jako punkt.
            #Program nie znajduje błędów, ale jest możliwe, że nie działa poprawnie przez brak możliwości przetestowania.
            #Jaki węzeł ma jaki numer w tablicy można znaleźć w pliku Danev2.

        print("Next step")
        timer.plus();
        time.sleep(refresh)
