import random
from list_names import easyChr, hardChr

def randChr(chrDict: dict[str, list[str]]) -> str:
    chr = random.choice(list(chrDict.items()))
    nombre = chr[0]
    caractList = chr[1]
    
    return nombre

if __name__ == "__main__":
    print(randChr(easyChr))