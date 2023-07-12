#!/usr/bin/env python
# az the game by nichtdevid

#die Klassen und Attribute der Klassen aus Unterordner "mapareale" als Python-Dateien laden und importieren. ("draußen.py", "drinnen.py", "ordern.py", "runter.py" & "Klo.py")

# Wenn das Spiel vom Hauptmenu aus gestartet wird, mit [Start], dann soll ein großes Ascii-Intro ablaufen und danach ist der Spieler im Draußen-Areal. Es werden Attribute der Klasse "draußen" ausgeprintet, wie: Ascii und Text. Draußen stehend soll man [rein] oder [raus] eingeben können. Tippt der Spieler "raus", so soll der Attribut Ascii der Klasse "draußen" geprintet werden und man steht wieder vor der Eingabeauswahl [rein] od#er [raus]. Tippt der Spieler [rein], so sollen die Ascii-Attribute und Text-Atributte der Klassene "drinnen" gerpintet werden, mit der Wahl [ordern] oder [runter] oder [Klo]. Tippt man "ordern" ein, werden die Ascii-Attribute und Text-Attribute von "runter" als Klasse geprintet. Tippt man "runter" ein, werden die Ascii-Attribute und Text-Attribute von "Klo" als Klasse geprintet. Tippt man "Klo" ein, werden die Ascii-Attribute und Text-Attribute von "ordern" als Klasse geprintet. 

#!/usr/bin/env python
# az the game by nichtdevid

import time
import pygame
import colorama
from colorama import init, Back, Fore

pygame.init()
pygame.mixer.music.load("./sounds/3.0_3-black0ut.dmf_ftt-filtered.mp3")
pygame.mixer.music.play(-1)  # -1 sorgt dafür, dass die Musik in einer Schleife abgespielt wird
door_sound = pygame.mixer.Sound("./sounds/tuer.mp3")

from mapareale.class_draußen import classdraußen
from mapareale.class_drinnen import classdrinnen
from mapareale.class_ordern import classordern
from mapareale.class_klo import classklo
from mapareale.class_unten import classunten
from mapareale.class_buehne import classbuehne
from mapareale.class_ummeladen import classummeladen

from zusaetze.intro import intro


# from mapareale.Klo import Klo

def animate_intro():
    for line in intro:
        for char in line:
            print(char, end="", flush=True)
            time.sleep(0.001)  # Anpassen der Animationsgeschwindigkeit
        print()
        time.sleep(0.001)  # Verzögerung zwischen den Zeilen
#Intro-Start
animate_intro() # animiert was
time.sleep(1) # wartet etwas
print("\n" * 100) # Konso leeren

def main_menu():

    start = input("Drücke [Start], um das Spiel zu beginnen: ")
    if start == "Start":
        print("Großes Ascii-Intro")
        draußen = classdraußen()  # Instanz der Klasse erstellen
        print(draußen.ascii)
        print(draußen.text)
        while True:
            choice = input("Du bist draußen. Möchtest du [rein] oder [raus]? ")
            if choice == "raus":
                print(draußen.ascii)
            elif choice == "rein":
                # drinnen = class_drinnen()
                drinnen = classdrinnen()  # Instanz der Klasse erstellen
                print(drinnen.ascii)
                print(drinnen.text)
                door_sound.play()
                while True:
                    inner_choice = input("Du bist drinnen. Möchtest du [ordern], [runter] oder [Klo]? Wieder [raus]?")
                    if inner_choice == "ordern":
                        ordern = classordern()
                        print(ordern.ascii)
                        print(ordern.text)
                        while True:
                            choice = input("[zurück] ? ?]")
                            ordezurü = classdrinnen()
                            print(drinnen.ascii)
                            print(drinnen.text)
                    elif inner_choice == "runter":
                        unten = classunten()
                        print(unten.ascii)
                        print(unten.text)
                        while True:
                            choice = input("Du bist unten. Möchtest du in den [Ummeladen] oder zur [Bühne]? Wieder [hoch]?")
                            if choice == "Ummeladen":
                                umme = classummeladen()  # Instanz der Klasse erstellen
                                print(umme.ascii)
                                door_sound.play()
                                while True:
                                    choice = input("zurück")
                                    ummezurü = classunten()
                                    print(unten.ascii)
                                    print(unten.text)
                                    door_sound.play()
                                    while True:
                                        choice = input("Du bist unten. Möchtest du in den [Ummeladen] oder zur [Bühne]? Wieder [hoch]?")
                                        if choice == "Ummeladen":
                                            umme = classummeladen()  # Instanz der Klasse erstellen
                                            print(umme.ascii)
                                            door_sound.play()
                                            while True:
                                                choice = input("zurück")
                                                ummezurü = classunten()
                                                print(unten.ascii)
                                                print(unten.text)
                                                door_sound.play()
                                                if choice == "Bühne":
                                                    # drinnen = class_drinnen()
                                                    buehne = classbuehne()  # Instanz der Klasse erstellen
                                                    print(buehne.ascii)
                                                    print(buehne.text)
                                                    while True:
                                                        choice = input("[zurück] ? ?]")
                                                        buehzurü = classdrinnen()
                                                        print(unten.ascii)
                                                        print(unten.text)
                                                elif choice == "Ummeladen":
                                                    umme = classummeladen()  # Instanz der Klasse erstellen
                                                    print(umme.ascii)
                                                    while True:
                                                        choice = input("[zurück] ? ?]")
                                                        buehzurü = classdrinnen()
                                                        print(unten.ascii)
                                                        print(unten.text)
                                                        door_sound.play()
                            elif choice == "Bühne":
                                # drinnen = class_drinnen()
                                buehne = classbuehne()  # Instanz der Klasse erstellen
                                print(buehne.ascii)
                                print(buehne.text)
                                while True:
                                    choice = input("[zurück] ? ?]")
                                    buehzurü = classdrinnen()
                                    print(unten.ascii)
                                    print(unten.text)
                            elif choice == "hoch":
                                # drinnen = class_drinnen()
                                kellzurü = classdrinnen()  # Instanz der Klasse erstellen
                                print(kellzurü.ascii)
                                print(kellzurü.text)
                    elif inner_choice == "Klo":
                        klo = classklo()
                        print(klo.ascii)
                        print(klo.text)
                    elif inner_choice == "raus":
#                        choice = input("raus")
                        innezurü = classdraußen()
                        print(draußen.ascii)
                        print(draußen.text)
                    else:
                        print("Ungültige Eingabe!")

            else:
                print("Ungültige Eingabe!")

if __name__ == "__main__":
    main_menu()
