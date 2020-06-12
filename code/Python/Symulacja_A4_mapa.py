import time 
import turtle
import math

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
        for i in range (0,7586):
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
    mapa=turtle.Screen()
    mapa.setup(1116,756)
    mapa.title("Symulacja IV obwodnicy Krakowa")
    turtle.register_shape("map.gif")
    mapa.bgpic("map.gif")

    odc1=turtle.Turtle()
    odc2=turtle.Turtle()
    odc3=turtle.Turtle()
    odc4=turtle.Turtle()
    odc5=turtle.Turtle()
    odc6=turtle.Turtle()
    odc7=turtle.Turtle()
    odc7a=turtle.Turtle()
    odc7b=turtle.Turtle()
    odc8=turtle.Turtle()
    odc9=turtle.Turtle()
    odc10=turtle.Turtle()
    odc11=turtle.Turtle()
    odc12=turtle.Turtle()
    odc13=turtle.Turtle()
    odc14=turtle.Turtle()
    odc15=turtle.Turtle()
    odc16=turtle.Turtle()

    creation()
    random_auto(randomauto)
    tlo=turtle.Turtle()
    
    #tlo.shape("map.gif")

    while (1):
        for i in range(7586,0,-1):
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
            if i>7581:
                if firstlane[i].cond==1:
                    cars[firstlane[i].id].exists=0
                    firstlane[i].cond=0
                    firstlane[i].id=0
                if secondlane[i].cond==1:
                    cars[secondlane[i].id].exists=0
                    secondlane[i].cond=0
                if thirdlane[i].cond==1:               
                    secondlane[i].id=0
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
            if timer.get()%2==0 and timer.get()%10!=0:
                if firstlane[0].cond==0 and firstlane[1].cond==0 and firstlane[2].cond==0 and firstlane[3].cond==0:
                    firstlane[0].cond=1 #zajmowanie komórki
                    cars.append(Car())
                    cars[len(cars)-1].category="car"
                    cars[len(cars)-1].v=1 #1 k/s to ok 25 km/h
                    cars[len(cars)-1].id=carid.get()
                    carid.plus()
                    firstlane[i].id=cars[len(cars)-1].id
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
            if timer.get()%2==0 and timer.get()%10==0:
                if firstlane[0].cond==0 and firstlane[1].cond==0 and firstlane[2].cond==0 and firstlane[3].cond==0:
                    firstlane[0].cond=1 #zajmowanie komórki
                    cars.append(Car())
                    cars[len(cars)-1].category="truck"
                    cars[len(cars)-1].v=1 #1 k/s to ok 25 km/h
                    cars[len(cars)-1].id=carid.get()
                    carid.plus()
                    firstlane[i].id=cars[len(cars)-1].id
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

        carcounter1 = car_counter(0,7586)
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
          'Tyniec - Skawina', 'Skawina - Poludnie', 'Poludnie-Wieliczka', 'Wieliczka - Bieżanów',
                  'Bieżanów - Przewóz', 'Przewóz - Nowa Huta', 'Nowa Huta - Grębałów',
                  'Grębałów - Mistrzejowice', 'Mistrzejowice - Batowice', 'Batowice - Węgrzce',
                  'Węgrzce - Zielonki', 'Zielonki - Modlnica']
        sizes = [modlnica, modlniczka, balice1, balice2, bielany, tyniec,
         skawina, poludnie, wieliczka, biezanow, przewoz, nowahuta, grebalow, mistrzejowice, batowice,
                 wegrzce, zielonki]
        """
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes,  autopct='%1.1f%%')
        ax1.axis('equal')
        ax1.legend(labels, loc=3, fontsize="x-small")
        plt.show()
        """
        print("Ilość pojazdów na odcinkach obwodnicy:")
        print("Modlnica - Modlniczka:", modlnica, "\nModlniczka - Balice I:", modlniczka,
              "\nBalice I - Balice II :", balice1, "\nBalice II - Bielany:", balice2,
              "\nBielany - Tyniec:", bielany, "\nTyniec - Skawina:", tyniec,
         "\nSkawina - Południe:", skawina, "\nPołudnie-Łagiewniki:", poludnie, "\nŁagiewniki-Wieliczka:", lagiewniki,"\nWieliczka - Bieżanów:", wieliczka,
            "\nBieżanów - Przewóz:", biezanow, "\nPrzewóz - Nowa Huta:", przewoz,
            "\nNowa Huta - Grębałów:", nowahuta, "\nGrębałów - Mistrzejowice:", grebalow,
            "\nMistrzejowice - Batowice:", mistrzejowice, "\nBatowice - Węgrzce:", batowice,
             "\nWęgrzce - Zielonki:", wegrzce,  "\nZielonki - Modlnica:", zielonki,
              "\nSuma:", car_counter(0,7588))
        print("")

        odc1.speed(0)
        odc1.color("black")
        odc1.penup()
        odc1.setposition(-300,300)
        odc1.clear()
        odc1.write(modlnica, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc1.hideturtle()

        odc2.speed(0)
        odc2.color("black")
        odc2.penup()
        odc2.setposition(-390,220)
        odc2.clear()
        odc2.write(modlniczka, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc2.hideturtle()

        odc3.speed(0)
        odc3.color("black")
        odc3.penup()
        odc3.setposition(-450,130)
        odc3.clear()
        odc3.write(balice1, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc3.hideturtle()

        odc4.speed(0)
        odc4.color("black")
        odc4.penup()
        odc4.setposition(-450,0)
        odc4.clear()
        odc4.write(balice2, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc4.hideturtle()

        odc5.speed(0)
        odc5.color("black")
        odc5.penup()
        odc5.setposition(-400,-170)
        odc5.clear()
        odc5.write(bielany, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc5.hideturtle()

        odc6.speed(0)
        odc6.color("black")
        odc6.penup()
        odc6.setposition(-300,-270)
        odc6.clear()
        odc6.write(tyniec, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc6.hideturtle()

        odc7.speed(0)
        odc7.color("black")
        odc7.penup()
        odc7.setposition(-200,-350)
        odc7.clear()
        odc7.write(skawina, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc7.hideturtle()

        odc7a.speed(0)
        odc7a.color("black")
        odc7a.penup()
        odc7a.setposition(-30,-300)
        odc7a.clear()
        odc7a.write(poludnie, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc7a.hideturtle()

        odc7b.speed(0)
        odc7b.color("black")
        odc7b.penup()
        odc7b.setposition(120,-300)
        odc7b.clear()
        odc7b.write(lagiewniki, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc7b.hideturtle()

        odc8.speed(0)
        odc8.color("black")
        odc8.penup()
        odc8.setposition(370,-270)
        odc8.clear()
        odc8.write(wieliczka, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc8.hideturtle()

        odc9.speed(0)
        odc9.color("black")
        odc9.penup()
        odc9.setposition(420,-170)
        odc9.clear()
        odc9.write(biezanow, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc9.hideturtle()

        odc10.speed(0)
        odc10.color("black")
        odc10.penup()
        odc10.setposition(450,-50)
        odc10.clear()
        odc10.write(przewoz, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc10.hideturtle()

        odc11.speed(0)
        odc11.color("black")
        odc11.penup()
        odc11.setposition(420,100)
        odc11.clear()
        odc11.write(nowahuta, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc11.hideturtle()

        odc12.speed(0)
        odc12.color("black")
        odc12.penup()
        odc12.setposition(340,180)
        odc12.clear()
        odc12.write(grebalow, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc12.hideturtle()

        odc13.speed(0)
        odc13.color("black")
        odc13.penup()
        odc13.setposition(270,260)
        odc13.clear()
        odc13.write(mistrzejowice, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc13.hideturtle()

        odc14.speed(0)
        odc14.color("black")
        odc14.penup()
        odc14.setposition(150,270)
        odc14.clear()
        odc14.write(batowice, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc14.hideturtle()

        odc15.speed(0)
        odc15.color("black")
        odc15.penup()
        odc15.setposition(0,290)
        odc15.clear()
        odc15.write(wegrzce, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc15.hideturtle()

        odc16.speed(0)
        odc16.color("black")
        odc16.penup()
        odc16.setposition(-140,310)
        odc16.clear()
        odc16.write(zielonki, False, align="left", font=("Arial Black", 20, "normal", "bold"))
        odc16.hideturtle()


           # carcounter = car_counter(0, 2)
            #print(carcounter);


        #Tutaj po każdym kroku pętli ma być wykonywane rysowanie.
            #Należy przeiterować tablice firstlane, secondlane i thirdlane
            #Jeśli xxxxxlane[i].cond==1(znaczy to że komórka jest zapełniona), należy ją nanieść na wizualizację jako punkt.
            #Program nie znajduje błędów, ale jest możliwe, że nie działa poprawnie przez brak możliwości przetestowania.
            #Jaki węzeł ma jaki numer w tablicy można znaleźć w pliku Danev2.

        #print("Next step")
        timer.plus();
        time.sleep(refresh)
    turtle.mainloop()

