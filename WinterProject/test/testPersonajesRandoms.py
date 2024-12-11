import pytest
from WinterProject.start_Mode.personajeRonadom import personajeRandom
from casos import *

@pytest.mark.dict_null
def test_dict_null():
    assert IndexError

@pytest.mark.personaje_easy
def test_personaje_easy():
    assert personajeRandom(personajes=easyChr) in nameEasy_list

@pytest.mark.personaje_hard
def test_personaje_hard():
    assert personajeRandom(personajes=hardChr) in nameHard_list