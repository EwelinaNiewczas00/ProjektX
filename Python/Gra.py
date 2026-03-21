#Gra jest mojego pomysłu zastrzegam Sobie jej prawa autorskie

import time
import sys
import random
time.sleep(2)
print("Hej, zagrajmy w grę, twoja rola polega na wybraniu jednej z kilku opcji. \nObiecuję, ze będzie ciekawie! \nTa gra opiera się na paradoksie Newcomba, we własnej interpretacji wyników odpowiedzi")

time.sleep(3)
print("Wobraź sobie, ze jeste w teleturnieju gdzie mozesz wygrać duze pieniadze ")
time.sleep(2)
print("I to zalezy tylko od jednej twojej małej decyzji...")
time.sleep(2)
udział = input("Czy bierzecz udział w zabawie? (TAK/NIE) : ").upper()
while True:
    if udział == "TAK":
        print("Okeyy, let's goo")
        time.sleep(2)
        break
    elif udział == "NIE":
        wybor = input("Szkoda! Tracisz szansę na wielka wygrana. Jestes pewien? (TAK/NIE): ").upper()
        if wybor == " TAK":
            print("Gra skończona! YOU GIVE UP!")
            sys.exit()
        elif wybor == "NIE":
            print("Widze kto tu jest niezdecydowany.. Decyduje za Ciebie - grasz! \nNie stracisz przeciez takiej okazji")
            break
        else:
            print("CZEKAJ CZEKAJ wpisz TAK lub NIE (tylko to przyjmuje) NIE OSZUKUJ!")
        
    else:
        print("Wpisz TAK lub NIE. Nie komplikuj mi zycia :)")

print("\nFABUŁA")
time.sleep(2)
print("\nSuper, ze tu jestes i zagrasz w te grę!")
time.sleep(1)
print("A teraz wyobraz sobie, ze jestes w pokoju przygotowań")
time.sleep(1)
print("Dostajesz informację, ze bedziesz musiał wybrać jedna z dwoch skrzynek")
time.sleep(2)
print("\n--- ZASADY ---")
time.sleep(2)
print("Skrzynka A: Zawsze jest w niej 1000 zł")
time.sleep(2)
print("Skrzynka B: Moze byc w niej 1 000 000 zł (MILION) lub moze być pusta")
time.sleep(2)
print("Jest jeden mały chaczyk")
time.sleep(1)
print("Wszystko zalezy od tego, co ja obstawiłam i czy włozyłam milion do drugiej skrzynki")
time.sleep(2)
print("Jeśli przewidzialam, że wezmiesz OBIE skrzynki - zostawiłam B pusta")
time.sleep(2)
print("Jeśli przewidzialam, że wezmiesz TYLKO skrzynke B - włozylam tam milion")
time.sleep(2)
print("Decyzja nalezy do Ciebie")

print("Ja juz obstawiłam co wybierzesz, a ty jestes gotowy?")
print("Wiec wybierz, wpisz B lub OBIE")
time.sleep(1)
lista = ["B", "OBIE"]
moj_wybor = random.choice(lista).upper()
while True:
    twoj_wybor = input("\nJak decydujesz? Wpisz B lub OBIE: ").upper()

    if twoj_wybor == "B":
        print("Twój wybór padł na skrzynkę B. Jeste ciekawy poznać odpowiedź czy milion jest twój?")
        time.sleep(2)
        if moj_wybor == "B":
            print("Nagradzam Cię włanie milionem złotych! Gratuluję. \nPrzewidziałam, ze weźmiesz skrzynkę B")
            break
        elif moj_wybor =="OBIE":
            print("Skrzynka B jest pusta, mylalam, ze weźmiesz OBIE - \nten 1% procent moich błednych strzałów")
            time.sleep(2)
            break
        else:
            print("Musisz wpisać B lub OBIE, znów utrudniasz mi zycie!")
    
    elif twoj_wybor == "OBIE":
        print("Twój wybór padł na OBIE skrzynki, ale czy się zgadzamy?")
        time.sleep(2)
        if moj_wybor == "B":
            print("oo proszę, nie wiedziałam, ze jestes taki łasy na pieniadze! \nW skrzynce B jest milion. Oszukales mnie")
            time.sleep(2)
           
            break
        elif moj_wybor =="OBIE":
            print("wiedzialam, ze jestes łasy na pieniadze, \nB zostawiłam pusta, nie wygrywasz miliona")
            time.sleep(1)
            
            
        
            break

        else:
            print("Musisz wpisać B lub OBIE, znów utrudniasz mi zycie!")

print()
print("Jak się bawiłes? Było ciekawie, teraz zostawiam Cię, \nprzemyl swoje wybory i ten eksperyment!")
time.sleep(1)
print("KONIEC")