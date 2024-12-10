import reflex as rx
from WinterProject.WinterProject.start_Mode.personajeRonadom import randChr
from WinterProject.WinterProject.start_Mode.list_names import easyChr

def filterCharact(caracteristica: str) -> str:
    charactList = easyChr[randChr(easyChr)]
    for charact in charactList:
        if caracteristica == charact:
            print("Si")
            break
        else:
            print("No")
            break