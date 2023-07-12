import time
import sys
import random
import threading
import pygame
import colorama
from colorama import init, Back, Fore
from PIL import Image


# ASCII-Intro
intro = [Back.BLACK + Fore.RED +"""                                                                              
   .P&B&@J^?@&&@&~~#BBGP5J~J@@J  . .?@&BJ~!&@@?~!7!.G@@@@@@@@@@#?@@@@75@@@P
    !@@@@#: J@@@@BP@@@G!#@@@@@!:^G:  G!.  .#&@#@@@#Y@@@@#P5Y77! ~@@@&B@@@B:.
     5@@@@G:!&@@@#&@@@? G@@@@@@@P~  7@@P  .#@@@@@@@B&@@@G?YY5GBYJ@&@@@@@&~B#BP5J7:
     .B@@@@&@@@@&5&@@@BP&&&@@&PPY7  ^&@B  .#@@@@@@@&B@@@@@@@@@@@G&G@@@@@@!:G@@@##~
      ~@@@@&@BY?^7@@@&Y@@&#@@#  :B. .#@B  .#@&@B&@PB&@@@&##GP5J^?@&@&B@@@B:#@@5 .
       J@@@@@5   Y@&@P^@@@G5@&~  ^  7@@G  .&@&B!G@@@@@@@@Y:^~!7?G@@&B~@@@@G@@&^
       .G@@@@@7  B@@@??@@@Y J#&BP555&@@&Y5P@@B^ P@@&@@@@@&&&#&&@@@PYP.JBB&@@@Y
        ^#@@@@&^ !?JY:!PGP~  :J#@@@@@@@@@@#5!  P@@&BB&@@@@@@@@&&B7       ?#&#:
         7&@@@@5            .: .~?YPPP5J7:   . 7?7!^ ~PGPYJ7!~:..          ::
"""]