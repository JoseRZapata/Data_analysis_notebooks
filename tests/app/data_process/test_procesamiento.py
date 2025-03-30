"""tests/app/data_process/test_procesamiento.py
Pruebas unitarias para el módulo de procesamiento de datos.
"""

import numpy as np
import pandas as pd
import pytest

from src.app.data_process.procesamiento import calcular_outliers_iqr, normalizar


# pylint: disable=redefined-outer-name
@pytest.fixture
def df_con_nulos() -> pd.DataFrame:
    return pd.DataFrame({
        "A": [1, 2, np.nan, 4, 5],
        "B": ["1", "2.5", "texto", "4", None],
        "C": [True, False, True, False, True],
    })


def test_normalizar() -> None:
    """
    Verifica que la función `normalizar` normaliza una serie de datos.
    """
    serie = pd.Series([10, 20, 30, 40, 50])
    normalizada = normalizar(serie)

    # Los valores deben estar entre 0 y 1
    assert normalizada.min() == 0
    assert normalizada.max() == 1

    # Verificar valores específicos
    assert normalizada.iloc[0] == 0
    assert normalizada.iloc[-1] == 1
    assert normalizada.iloc[2] == 0.5


def test_normalizar_serie_constante() -> None:
    """
    Verifica que la función `normalizar` normaliza una serie de datos.
    """
    serie = pd.Series([5, 5, 5, 5])
    normalizada = normalizar(serie)

    # Si todos los valores son iguales, todos se convierten a 0
    assert (normalizada == 0).all()


def test_calcular_outliers() -> None:
    """
    Verifica que la función `calcular_outliers_iqr` detecta correctamente
    los valores atípicos.
    """
    # Serie con un outlier extremo
    serie = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 100])
    outliers = calcular_outliers_iqr(serie)

    # Debería detectar el valor 100 como outlier
    assert len(outliers) == 1
    assert outliers.iloc[0] == 100

    # Serie con valores más dispersos para probar factores diferentes
    serie_dispersa = pd.Series([1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

    # Con el factor por defecto (1.5), el valor 89 ya es detectado como outlier
    outliers_estandar = calcular_outliers_iqr(serie_dispersa)
    assert len(outliers_estandar) == 1
    assert 89 in outliers_estandar.values

    # Con un factor más pequeño, debería detectar más outliers
    outliers_ampliados = calcular_outliers_iqr(serie_dispersa, factor=0.3)
    assert len(outliers_ampliados) > 1

    # Verificar que los valores 55 y 89 están entre los outliers
    assert 55 in outliers_ampliados.values
    assert 89 in outliers_ampliados.values
