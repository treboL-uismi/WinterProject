import pytest
from WinterProject.src.main import filterCharact

@pytest.mark.caracteristicaNoEsta
def test_caracteristica_no_esta():
    assert filterCharact("pelo castaño") == "No"