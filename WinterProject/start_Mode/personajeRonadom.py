import random

def personajeRandom(personajes) -> str:
    return random.choice(list(personajes.keys()))
