import random

def randChr(chrDict: dict[str, list[str]]) -> str:
    chr = random.choice(list(chrDict.items()))
    nombre = chr[0]
    caractList = chr[1]
    
    return nombre