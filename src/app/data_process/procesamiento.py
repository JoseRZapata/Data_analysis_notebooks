"""archivo: procesamiento.py"""

import pandas as pd


def normalizar(serie: pd.Series) -> pd.Series:
    """Normaliza una serie a valores entre 0 y 1.

    Args:
        serie (pd.Series): Serie de datos

    Returns:
        pd.Series: Serie normalizada
    """
    minimo = serie.min()
    maximo = serie.max()
    if maximo == minimo:
        return serie * 0  # Retorna serie de ceros si no hay variación
    return (serie - minimo) / (maximo - minimo)


def calcular_outliers_iqr(serie: pd.Series, factor: float = 1.5) -> pd.Series:
    """Identifica outliers usando el método IQR

    Args:
        serie (pd.Series): Serie de datos
        factor (float, optional):   Factor de multiplicación para el IQR.
                                    Default 1.5.

    Returns:
        pd.Series: Serie con los valores identificados como outliers
    """
    cuartil_1 = serie.quantile(0.25)
    cuartil_3 = serie.quantile(0.75)
    rango_intercuartil = cuartil_3 - cuartil_1
    limite_inferior = cuartil_1 - factor * rango_intercuartil
    limite_superior = cuartil_3 + factor * rango_intercuartil
    return serie[(serie < limite_inferior) | (serie > limite_superior)]
    return serie[(serie < limite_inferior) | (serie > limite_superior)]
