import pytest
from src.main import randChr
from src.main import filterCharact
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

@pytest.mark.caracteristicaSiEsta
def test_caracteristica_esta():
    assert filterCharact("cabeza ancha") == "Si"

@pytest.mark.caracteristicaNoEsta
def test_caracteristica_no_esta():
    assert filterCharact("pelo castaño") == "Si"