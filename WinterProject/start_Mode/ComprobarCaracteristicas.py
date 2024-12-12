def tiene_caracteristica(personajes: dict, personaje: str, caracteristica: str) -> bool:
    caracteristicas = personajes.get(personaje, [])
    return caracteristica.lower() in [c.lower() for c in caracteristicas]


