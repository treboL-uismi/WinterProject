import random
import reflex as rx

from WinterProject.start_Mode.easy_game import action_bar as easy_action
from WinterProject.start_Mode.hard_game import action_bar as hard_action

def randChr(chrDict: dict[str, list[str]]) -> str:
    chr = random.choice(list(chrDict.items()))
    nombre = chr[0]
    #caractList = chr[1]
    
    return nombre

def getInputEasy():
    ...

def getInputHard():
    ...
    