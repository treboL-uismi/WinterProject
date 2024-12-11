import pytest
from WinterProject.start_Mode.personajeRonadom import personajeRandom

easyChr = {
    "Maria" : ["mujer", "pelo castaño", "gorro verde", "ojos castaños", "pintalabios"],
    "Frans" : ["hombre", "boca pequeña", "ojos castaños", "pelirrojo", "cabeza ancha", "nariz pequeña", "orejas largas"],
    "Herman" : ["hombre", "calvo", "pelirrojo", "nariz gorda", "orejas pequeñas"],
    "Bernard" : ["hombre", "gorro", "pelo castaño", "boca pequeña", "nariz gorda", "cejas castañas"],
    "Philip" : ["hombre", "barba", "pelo castaño", "peludo", "cejas finas"],
    "Eric" : ["hombre", "rubio", "sombrero"],
    "Charles" : ["hombre", "rubio", "bigote"],
    "Peter" : ["hombre" "nariz grande", "boca grande", "pelo blanco"]
}

nameEasy_list = ["Maria", "Frans", "Herman", "Bernard", "Philip", "Eric", "Charles", "Peter"]

@pytest.mark.personaje_easy
def test_personaje_easy():
    assert personajeRandom(personajes=easyChr) in nameEasy_list