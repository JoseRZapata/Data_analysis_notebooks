"""test_calculadora_clase.py"""

import pytest

from src.app.calc.calculadora import dividir, multiplicar, restar, sumar


class TestCalculadora:
    """Clase de pruebas para la calculadora."""

    def test_sumar(self) -> None:
        """Test de la función sumar."""
        assert sumar(3, 2) == 5
        assert sumar(-1, 1) == 0

    def test_restar(self) -> None:
        """Test de la función restar."""
        assert restar(5, 3) == 2
        assert restar(3, 5) == -2

    def test_multiplicar(self) -> None:
        """Test de la función multiplicar."""
        assert multiplicar(2, 3) == 6
        assert multiplicar(-2, 3) == -6

    def test_dividir(self) -> None:
        """Test de la función dividir."""
        assert dividir(6, 3) == 2
        assert dividir(5, 2) == 2.5

    def test_division_por_cero(self) -> None:
        """Test de la función dividir por cero."""
        with pytest.raises(ValueError):
            dividir(5, 0)
