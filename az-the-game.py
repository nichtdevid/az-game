#!/usr/bin/env python
# az the game by nichtdevid


import time
import sys
import random
import threading
import pygame
import colorama
from colorama import init, Back, Fore
from PIL import Image



# Hintergrundmusik laden
pygame.init()
pygame.mixer.music.load("./sounds/3.0_3-black0ut.dmf_ftt-filtered.mp3")
pygame.mixer.music.play(-1)  # -1 sorgt dafür, dass die Musik in einer Schleife abgespielt wird
door_sound = pygame.mixer.Sound("./sounds/tuer.mp3")
trap_sound = pygame.mixer.Sound("./sounds/trap.mp3")
free_sound = pygame.mixer.Sound("./sounds/free.mp3")
ja_sound = pygame.mixer.Sound("./sounds/ja.mp3")
nein_sound = pygame.mixer.Sound("./sounds/nein.mp3")
sms = pygame.mixer.Sound("./sounds/sms-sound.mp3")
vib_sound = pygame.mixer.Sound("./sounds/vib-sound.mp3")     



def animate_intro():
    for line in intro:
        for char in line:
            print(char, end="", flush=True)
            time.sleep(0.001)  # Anpassen der Animationsgeschwindigkeit
        print()
        time.sleep(0.001)  # Verzögerung zwischen den Zeilen

# ASCII-Intro
intro = [Back.BLACK + Fore.RED +"""                                                                      
                     :~7777777777777~:.   . .^!77777777:    :~:...                   
                   .~77777777777777777!^..:!77777777777~    !7777!.                  
                  .!7777777777!~^~~!!!!~^^~!77777777777~ .:.!77777!.                 
       .^!?JYY7:  !777777777~^!5B&@@@@@#BGY!^~7777777!!^ .~.~~!^~~~.                 
   ^?5P#&GB@@&&&7 ~~~~~~~!!:7B@&BBB&@@@@@@@@B!:!!!!~^7JY5GB#&&@B!GBBG!.5GP5:         
   .P&B&@J^?@&&@&~~#BBGP5J~J@@J  . .?@&BJ~!&@@?~!7!.G@@@@@@@@@@#?@@@@75@@@P          
    !@@@@#: J@@@@BP@@@G!#@@@@@!:^G:  G!.  .#&@#@@@#Y@@@@#P5Y77! ~@@@&B@@@B:.         
     5@@@@G:!&@@@#&@@@? G@@@@@@@P~  7@@P  .#@@@@@@@B&@@@G?YY5GBYJ@&@@@@@&~B#BP5J7:   
     .B@@@@&@@@@&5&@@@BP&&&@@&PPY7  ^&@B  .#@@@@@@@&B@@@@@@@@@@@G&G@@@@@@!:G@@@##~   
      ~@@@@&@BY?^7@@@&Y@@&#@@#  :B. .#@B  .#@&@B&@PB&@@@&##GP5J^?@&@&B@@@B:#@@5 .    
       J@@@@@5   Y@&@P^@@@G5@&~  ^  7@@G  .&@&B!G@@@@@@@@Y:^~!7?G@@&B~@@@@G@@&^      
       .G@@@@@7  B@@@??@@@Y J#&BP555&@@&Y5P@@B^ P@@&@@@@@&&&#&&@@@PYP.JBB&@@@Y       
        ^#@@@@&^ !?JY:!PGP~  :J#@@@@@@@@@@#5!  P@@&BB&@@@@@@@@&&B7       ?#&#:       
         7&@@@@5            .: .~?YPPP5J7:   . 7?7!^ ~PGPYJ7!~:..          ::        
         .?7!~:.           .~7!^.        .:^!!    ..                      ..         
                            !7!777!~~~~!!77777!!!777!~~^^!7^  .                      
                            ~7^.^!7777777777777777777~. .77. .                       
                            .::   .^!77777777777777!:   .!! .                        
                                    .!77777!77!:::.      !!                          
                                     ~777!^.!7~          !!..                        
                                     :77^   !7~         .7!.                         
                                     .77:   !7!         .7!.                         
                                      !7:   :~:         .7^                          
                                      ~7:                :.                          
                                      ~7.                                            
                                      ~7..                                           
                                      ~7..                                           
                                      ~7..                                           
"""]

def animate_intro_plus():
    for line in intro_plus:
        for char in line:
            print(char, end="", flush=True)
            time.sleep(0.001)  # Anpassen der Animationsgeschwindigkeit
        print()
        time.sleep(0.001)  # Verzögerung zwischen den Zeilen      

intro_plus = [Back.BLACK + Fore.RED +"""
~    AZ _ the Game    ~
Idee&Code:   Nichtdévid
"""]

# Back.BLACK + Fore.WHITE (inn print nai)
ascii_draussen = """\n\n\n\n
                                    ___...--'     -  .` `.`.
           __..--'_______________ -         _  .`  _   `.   - 
      .` -   _ /  \_     -   .`  _         .` | PROJEKT31 |`
    .`-    _  /   /\   -   .`        _   .`   |___________|  `
  .`________ /__ /_ \____.`____________.`     ___       ___  - 
    |   -   _  -|    | - | __  |   | |  _    |   |  _  |   | 
    |      |___| |   |___|     |___|    |
           |---| |  _|---|     |---|_   |
           |   | |   |   |_  _ |   |    |
"""

ascii_drinnen = """\n\n\n\n
,\________________________________
 [_____________________________
 |  [_]   [_]     [-]   [-]   
 |   |     |       |     |
 |   |     |       |     |
`_  _|_   _|_     _|/   _|/
"""

ascii_getraenke = """\n\n\n\n
 _ __ ___   __ __
 __ ____ _____
   COLA, Mate
       
   H²0 & BIER
 _   _ _
"""

ascii_bestellt = """
                    //
              _____||
         ,-'''     ||`-.
        (          ||   )
        |`-..._____,..-'|
        |          ||   |
        |     _____||   |
        |,-''_   ~ ||`-.|
        |  ~ / `-.\ ,-'\|
        |`-...___/__,.-'|
        | -'  ~~    || .|
        (   ~     ~   ~~)
         `-...______,.-'
"""

print("\n" * 100)  # leert die Konsole



# Spielstart
animate_intro() # animiert was
time.sleep(3) # wartet etwas
print("\n" * 100) # Konso leeren
animate_intro_plus() # animiert was
time.sleep(2) # wartet etwas
print("\n" * 100) # Konso leeren
vib_sound.play()
sms.play()


def raum_draussen(): #!!!
    print(Back.BLACK + Fore.WHITE + ascii_draussen) # druckt was
    frage_raus = input("\n\n\n\n( rein / raus ) \n\n\n\n")

    ## .lower() wandelt den string in lowercase um.
    if frage_raus.lower() == "rein":
        ja_sound.play()
        print("\n\n\n\nDu gehst nun hinein.\n\n\n\n")
        time.sleep(1)

    else:
        print("\n" * 100)  # leert die Konsole
        nein_sound.play()
        print("\n\n\n\nDu bist schon draußen.\n\n\n\n")
        time.sleep(1)
        raum_draussen()
raum_draussen()


# drinnen dann
print("\n\n\n\nWillkommen im AZ.")

def raum_drinnen():
    print(Back.BLACK + Fore.WHITE + ascii_drinnen) # druckt was
    print("\n\n\n\numsehen(?) bestellen(?)\n\n\n\n")
    frage_bestellen = input()
    if frage_bestellen == "umsehen":
        door_sound.play()
        print("\n       Da ist bloß eine Theke.\n\n")
        time.sleep(1)
        raum_drinnen() #!!!
    else:
        print(Back.BLACK + Fore.WHITE + "\n")
        trap_sound.play()
        print("     \n",
            "     Eine Bestellung?\n\n\n\n")
        def getraenk_waehlen():
            print(Back.BLACK + Fore.WHITE + ascii_getraenke) # druckt was
            time.sleep(1)

            getraenke = ["Bier", "Cola", "Mate", "Wasser", "Spezi\n\n\n\n"]

            print("\n\n\n\nOkeh. Was magst du?\n\n\n\n")
            #for x in getränke:
            #	print(x)
            for c in range(len(getraenke)):
                print("[" +str(c+1) +"] " +getraenke[c])

            inp = input(">> ").lower()
            #inp = inp.lower()

            ## try it with "try" and "expect"
            #if type(inp) != int:
            #	print("unknown input")

            artikel = ["Dein", "Deine"]
            x = 1

            print(Back.BLACK + Fore.WHITE + "\n\n\n\n Hier \n\n\n\n" +ascii_bestellt +artikel[x] +" " +getraenke[int(inp)-1])
            raum_drinnen() #!!!
            print(".\n\n\n\n \n\n\n\n")
        getraenk_waehlen()
raum_drinnen()



#    sys.exit()



print(""
"     ____      ____      /\n",
"   |    |    |    |    /\n",
"   |  * |    |  * |   /\n",
"___|____|____|____|__/\n\n",
"   \n\n        Ein Blick über deine Schulter zeigt dir die Türen, von denen du kamst.\n\n") #!!!

time.sleep(1)

print("         Möchtest du schon gehen?\n\n( bleiben / gehen )\n\n")
weg = input()

if weg == "bleiben":
    time.sleep(1)
    print("Du bleibst. Voll cool.")
    door_sound.play()
    print(Back.BLACK + Fore.WHITE + "     \n...\n..\n\n.\n~~(hier-muss-der-Drinnen-Raum-geladen-werden).]\n")
    time.sleep(1)
    free_sound.play()
    time.sleep(1)


else:
    time.sleep(1)
    print(Back.BLACK + Fore.RED + "\n"
    "     __      _ _    /\n",
    "                  /\n",
    "  *   *  *     * /\n",
    "________________/\n\n",
          "       \n        (wieder raus)")
    trap_sound.play()
    print("       [insert Gameplay here] .\n")
    time.sleep(1)
    print("    _ _\n\n")
    raum_draussen()
    time.sleep(1)
    raum_draussen()
# sys.exit()

# Ende

time.sleep(1)

print(Back.BLACK + Fore.RESET + "\n\n\n~•♦  \n   ♦•~\n\n~\n~\n\n")