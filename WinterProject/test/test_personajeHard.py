import pytest
from WinterProject.start_Mode.personajeRonadom import personajeRandom

hardChr = {
    "Susan" : ["mujer", "pelo blanco"],
    "Claire" : ["mujer", "sombrero", "gafas"],
    "David" : ["hombre", "perilla", "rubio"],
    "Anne" : ["mujer", "afro", "arietes"],
    "Robert" : ["hombre", "pelo castaño", "ojos"],
    "Anita" : ["mujer", "rubio", "cara rechoncha"],
    "Joe" : ["hombre", "rubio", "gafas rojas"],
    "George" : ["hombre", "pelo blanco", "fedora"],
    "Bill" : ["hombre", "hombre", "calvo", "cabeza huevo"],
    "Alfred" : ["hombre", "pelo largo", "bigote"],
    "Max" : ["hombre", "bigote", "pelo castaño"],
    "Tom" : ["hombre", "calvo", "gafas"],
    "Alex" : ["hombre", "bigote", "pelo corto", "pelo castaño"],
    "Sam" : ["hombre", "calvo", "gafas redondas"],
    "Richard" : ["hombre", "calvo", "barba"],
    "Paul" : ["hombre", "gafas", "pelo blanco", "cejas blancas"]    
}

nameHard_list = ["Susan", "Claire", "David", "Anne", "Robert", "Anita", "Joe", "George", "Bill", "Alfred", "Max", "Tom", "Alex", "Sam", "Richard", "Paul"]

@pytest.mark.personaje_hard
def test_personaje_Hard():
    assert personajeRandom(personajes=hardChr) in nameHard_list