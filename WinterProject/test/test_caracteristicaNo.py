import pytest
from WinterProject.start_Mode.list_names import easyChr
from WinterProject.start_Mode.ComprobarCaracteristicas import tiene_caracteristica

@pytest.mark.caracteristicaSiEsta
def test_caracteristica_esta():
    assert tiene_caracteristica(easyChr, "Herman", "mujer") == False