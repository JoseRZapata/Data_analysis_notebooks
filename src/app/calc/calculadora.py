"""archivo: calculadora.py"""


def sumar(a: int | float, b: int | float) -> int | float:
    """Suma dos números.

    Args:
        a (int, float): El primer número.
        b (int, float): El segundo número.

    Returns:
        int, float: La suma de los dos números.
    """
    return a + b


def restar(a: int | float, b: int | float) -> int | float:
    """Resta dos números.

    Args:
        a (int, float): El primer número.
        b (int, float): El segundo número.

    Returns:
        int, float: La resta de los dos números.
    """
    return a - b


def multiplicar(a: int | float, b: int | float) -> int | float:
    """Multiplica dos números.

    Args:
        a (int, float): El primer número.
        b (int, float): El segundo número.

    Returns:
        int, float: La multiplicación de los dos números.
    """
    return a * b


def dividir(a: int | float, b: int | float) -> int | float:
    """Divide dos números.

    Args:
        a (int, float): El primer número.
        b (int, float): El segundo número.

    Returns:
        int, float: La división de los dos números.

    Raises:
        ValueError: Si el segundo número es cero.
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
