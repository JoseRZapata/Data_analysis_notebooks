"""test_parametrizado.py"""

import pytest

from src.app.calc.calculadora import sumar


@pytest.mark.parametrize(
    "a, b, esperado", [(3, 5, 8), (-1, 1, 0), (0, 0, 0), (-5, -5, -10)]
)
def test_sumar_parametrizado(
    a: int | float, b: int | float, esperado: int | float
) -> None:
    """Test de la función sumar parametrizada."""
    assert sumar(a, b) == esperado
