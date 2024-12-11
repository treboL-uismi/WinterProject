import reflex as rx
from WinterProject.start_Mode.personajeRonadom import personajeRandom
from WinterProject.start_Mode.list_names import easyChr

def filterCharact(caracteristica: str) -> str:
    charactList = easyChr[personajeRandom(easyChr)]
    for charact in charactList:
        if caracteristica == charact:
            return "Si"
        else:
            return "No"