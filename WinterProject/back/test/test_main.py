import pytest
from src.main import *

@pytest.mark.dict_null
def test_dict_null():
    assert randChr(None)

@pytest.mark.personaje_easy
def test_personaje_easy():
    assert randChr(easyChr)

@pytest.mark.personaje_hard
def test_personaje_hard():
    assert randChr(hardChr)