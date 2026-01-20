import pytest

from src.app.calc.calculadora import dividir


def test_division_por_cero() -> None:
    """Test de la función dividir cuando se intenta dividir por cero."""
    with pytest.raises(ValueError) as excinfo:
        dividir(10, 0)

    assert "No se puede dividir por cero" in str(excinfo.value)


def test_division_correcta() -> None:
    """Test de la función dividir con valores válidos."""
    assert dividir(10, 2) == 5
    assert dividir(-10, 2) == -5
    assert dividir(5, 2) == 2.5
