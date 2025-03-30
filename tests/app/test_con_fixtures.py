import numpy as np
import pandas as pd
import pytest


# pylint: disable=redefined-outer-name
@pytest.fixture
def datos_ejemplo() -> pd.DataFrame:
    """Fixture que genera un DataFrame de ejemplo."""
    return pd.DataFrame({
        "A": np.random.rand(5),
        "B": np.random.rand(5),
        "C": np.random.rand(5),
    })


def test_suma_columnas(datos_ejemplo: pd.DataFrame) -> None:
    """Test de la suma de columnas."""
    # La fixture 'datos_ejemplo' se pasa automáticamente como argumento
    resultado = datos_ejemplo["A"] + datos_ejemplo["B"]
    assert len(resultado) == 5
    assert isinstance(resultado, pd.Series)


def test_media_columna(datos_ejemplo: pd.DataFrame) -> None:
    """Test de la media de columnas."""
    media = datos_ejemplo["C"].mean()
    assert 0 <= media <= 1
