# Back.BLACK + Fore.WHITE (inn print nai)
import time
import colorama
from colorama import init, Back, Fore
from mapareale.auswahl_drinks import auswahldrinks
class classordern:
    def __init__(self):
        classordern.ascii = """\n\n\n\n
,\________________________________
 [___     [-]   
 |   |     |       |     |
 |   |   Bestellskript
`_  _|_   _|_     _|/   _|/
"""
        classordern.text = "bestell was"
 #       self.text = "Text für das Draußen-Areal"
        ordern = input("[ordern] ")
        if ordern == "ordern":
            print("\n       Okeh. Bestellen.\n\n")
            time.sleep(1)
            
#           getraenk_waehlen()

        else:
            print(Back.BLACK + Fore.WHITE + "\n")
            print("     \n",
                    "     Keine Bestellung??!raus?\n\n\n\n")
            def getraenk_waehlen():
                print(Back.BLACK + Fore.WHITE + auswahldrinks) # druckt was
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
                classdraußen() #!!!
                print(".\n\n\n\n \n\n\n\n")
            getraenk_waehlen()


            
        getraenk_waehlen()
