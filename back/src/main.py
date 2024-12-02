import random
import reflex as rx
from src.list_names import easyChr

def randChr(chrDict: dict[str, list[str]]) -> str:
    chr = random.choice(list(chrDict.items()))
    nombre = chr[0]
    #caractList = chr[1]
    
    return nombre


def filterCharact(caracteristica: str) -> str:
    charactList = easyChr[randChr(easyChr)]
    for charact in charactList:
        if caracteristica == charact:
            print("Si")
            break
        else:
            print("No")
            break