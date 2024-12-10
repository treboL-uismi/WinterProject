import pytest
from src.main import filterCharact
from test.casos import *

@pytest.mark.caracteristicaSiEsta
def test_caracteristica_esta():
    assert filterCharact("cabeza ancha") == "Si"

@pytest.mark.caracteristicaNoEsta
def test_caracteristica_no_esta():
    assert filterCharact("pelo castaño") == "Si"