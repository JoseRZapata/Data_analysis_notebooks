#!/usr/bin/env python
# coding: utf-8

"""[Actualizacion Bar Chart Race]

por: Jose R. Zapata - https://joserzapata.github.io/

https://joserzapata.github.io/post/covid19-visualizacion/

Ejemplo:
python Covid19_Update.py [chart_studio username] [chart_studio password]

https://github.com/CSSEGISandData/COVID-19

Actualizaciones:
- 31/May/2020 bar chart race
"""


import numpy as np
import pandas as pd

# %%
# Leer datos

confirmed = pd.read_csv(
    "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
)
death = pd.read_csv(
    "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
)
recovered = pd.read_csv(
    "https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
)


# %%
confirmed = confirmed.drop(columns=["Lat", "Long", "Province/State"])
death = death.drop(columns=["Lat", "Long", "Province/State"])
recovered = recovered.drop(columns=["Lat", "Long", "Province/State"])
# %%
# ### Personas Activas
active = confirmed.copy()
# Calcular el numero de casos activos
active.iloc[:, 1:] = active.iloc[:, 1:] - death.iloc[:, 1:] - recovered.iloc[:, 1:]

# %% [markdown]
# ### Consolidar datos

# %%
active_group = active.groupby(by="Country/Region")
active_group = active_group.aggregate(np.sum)
active_group = active_group.T
active_group.index.name = "date"
active_group = active_group.reset_index()

# %% [markdown]
# ### Datos Mundiales

# #Evolución Animada de casos activos por pais
active_evol = active_group.set_index("date")
active_evol.index = pd.to_datetime(active_evol.index)
active_evol.plot_animated(
    filename="evolucion_casos_activos.gif",
    n_bars=8,
    n_visible=8,
    title="Evolución en el tiempo de Casos Activos COVID-19 por pais \n https://joserzapata.github.io/",
    period_label={"x": 0.99, "y": 0.25, "ha": "right", "va": "center"},
    dpi=100,
    period_fmt="%B %d, %Y",
    period_summary_func=lambda v: {
        "x": 0.99,
        "y": 0.18,
        "s": f"Total Activos: {v.nlargest(8).sum():,.0f}",
        "ha": "right",
        "size": 9,
        "family": "Courier New",
    },
)

print("Bar chart Race actualizada \U0001f600")
print("https://joserzapata.github.io/")
