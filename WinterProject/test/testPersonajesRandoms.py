import pytest
from WinterProject.WinterProject.start_Mode.personajeRonadom import randChr
from test.casos import *

@pytest.mark.dict_null
def test_dict_null():
    assert IndexError

@pytest.mark.personaje_easy
def test_personaje_easy():
    assert randChr(chrDict=easyChr)

@pytest.mark.personaje_hard
def test_personaje_hard():
    assert randChr(chrDict=hardChr)