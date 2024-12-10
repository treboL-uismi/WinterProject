def buscar_caracteristicas(personajes: dict, caracteristica: str):
    resultado = []
    for personaje, caracteristicas in personajes.items():
        if caracteristica.lower() in [c.lower() for c in caracteristicas]:
            resultado.append(personaje)
    return resultado

def buscar_sin_caracteristica(personajes: dict, caracteristica: str):
    resultado = []
    for personaje, caracteristicas in personajes.items():
        if caracteristica.lower() not in [c.lower() for c in caracteristicas]:
            resultado.append(personaje)
    return resultado

def tiene_caracteristica(personajes: dict, personaje: str, caracteristica: str) -> bool:
    caracteristicas = personajes.get(personaje, [])
    return caracteristica.lower() in [c.lower() for c in caracteristicas]


