"""test_calculadora.py"""

import pytest

from src.app.calc.calculadora import dividir, multiplicar, restar, sumar


def test_sumar() -> None:
    """Test de la función sumar."""
    assert sumar(3, 2) == 5
    assert sumar(-1, 1) == 0
    assert sumar(-1, -1) == -2


def test_restar() -> None:
    """Test de la función restar."""
    assert restar(5, 3) == 2
    assert restar(3, 5) == -2
    assert restar(0, 0) == 0


def test_multiplicar() -> None:
    """Test de la función multiplicar."""
    assert multiplicar(2, 3) == 6
    assert multiplicar(0, 5) == 0
    assert multiplicar(-2, 3) == -6


def test_dividir() -> None:
    """Test de la función dividir."""
    assert dividir(6, 3) == 2
    assert dividir(5, 2) == 2.5
    assert dividir(-6, 2) == -3


def test_division_por_cero() -> None:
    """Test de la función dividir por cero."""
    with pytest.raises(ValueError):
        dividir(5, 0)
