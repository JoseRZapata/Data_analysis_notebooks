#!/usr/bin/env python

"""[Visualizacion del Coronavirus (COVID19) Mundial]

por: Jose R. Zapata - https://joserzapata.github.io/

https://joserzapata.github.io/post/covid19-visualizacion/

Ejemplo:
python Covid19_Update.py [chart_studio username] [chart_studio password]


https://github.com/CSSEGISandData/COVID-19

Actualizaciones:
- 25/May/2020 agregar datos de personas recuperadas
"""

import sys

import chart_studio
import chart_studio.plotly as py
import numpy as np
import pandas as pd
import plotly.express as px

username = sys.argv[1]  # chart studio usuario
api_key = sys.argv[2]  # chart studio clave

chart_studio.tools.set_credentials_file(username=username, api_key=api_key)


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


confirmed = confirmed.drop(columns=["Lat", "Long", "Province/State"])


# %%
death = death.drop(columns=["Lat", "Long", "Province/State"])
recovered = recovered.drop(columns=["Lat", "Long", "Province/State"])
# %%
# ### Personas Activas
active = confirmed.copy()
# Calcular el numero de casos activos
active.iloc[:, 1:] = confirmed.iloc[:, 1:] - death.iloc[:, 1:] - recovered.iloc[:, 1:]

# %% [markdown]
# ### Consolidar datos

# %%
confirmed_group = confirmed.groupby(by="Country/Region")
confirmed_group = confirmed_group.aggregate(np.sum)
confirmed_group = confirmed_group.T
confirmed_group.index.name = "date"
confirmed_group = confirmed_group.reset_index()


# %%
death_group = death.groupby(by="Country/Region")
death_group = death_group.aggregate(np.sum)
death_group = death_group.T
death_group.index.name = "date"
death_group = death_group.reset_index()
# %%
recovered_group = recovered.groupby(by="Country/Region")
recovered_group = recovered_group.aggregate(np.sum)
recovered_group = recovered_group.T
recovered_group.index.name = "date"
recovered_group = recovered_group.reset_index()

# %%
active_group = active.groupby(by="Country/Region")
active_group = active_group.aggregate(np.sum)
active_group = active_group.T
active_group.index.name = "date"
active_group = active_group.reset_index()


# %%
confirmed_melt = confirmed_group.melt(id_vars="date").copy()
confirmed_melt.rename(columns={"value": "Confirmados", "date": "Fecha"}, inplace=True)


# %%
death_melt = death_group.melt(id_vars="date")
death_melt.rename(columns={"value": "Muertos", "date": "Fecha"}, inplace=True)

# %% [markdown]
# ### Datos Mundiales

# %%
# Numero de Casos confirmados por dia en el mundo

column_names = ["Fecha", "Confirmados", "Recuperados", "Muertos"]
world = pd.DataFrame(columns=column_names)
world["Fecha"] = confirmed_group["date"].copy()
world["Confirmados"] = confirmed_group.iloc[:, 1:].sum(1)
world["Muertos"] = death_group.iloc[:, 1:].sum(1)
world["Recuperados"] = recovered_group.iloc[:, 1:].sum(1)
world["Activos"] = active_group.iloc[:, 1:].sum(1)

# %% [markdown]
# # Visualizacion con Plotly
# %% [markdown]
# ## Valores Mundiales de Confirmados y Muertos
#

# %%
temp = pd.DataFrame(world.iloc[-1, :]).T
tm = temp.melt(
    id_vars="Fecha", value_vars=["Confirmados", "Activos", "Recuperados", "Muertos"]
)
fig = px.bar(
    tm,
    x="variable",
    y="value",
    color="variable",
    text="value",
    color_discrete_sequence=["teal", "navy", "green", "coral"],
    height=500,
    width=600,
    title=f"Total de Casos Mundiales de COVID 19 - {str(world.iloc[-1,0])}",
)
fig.update_traces(textposition="outside")  # poner los valores de las barras fuera
fig.add_annotation(
    x="Muertos",
    y=tm["value"].max(),
    text="https://joserzapata.github.io/",
    showarrow=False,
)
fig.layout.update(
    showlegend=False,
    yaxis={"title": {"text": "Numero de Personas"}},  # Cambiar texto eje y
    xaxis={"title": {"text": ""}},  # Esconder nombre eje x
)
# grabar grafica en chart-studio si se proporciona el api-key
if api_key:
    py.plot(fig, filename="total_casos_general", auto_open=False)
# fig.show()

# %% [markdown]
# ## Mapa Mundial de Confirmados por Pais

# %%
confirmed_melt["Fecha"] = pd.to_datetime(confirmed_melt["Fecha"])
confirmed_melt["Fecha"] = confirmed_melt["Fecha"].dt.strftime("%m/%d/%Y")

max_Fecha = confirmed_melt["Fecha"].iloc[-1]
conf_max = confirmed_melt[confirmed_melt["Fecha"] == max_Fecha].copy()
conf_max.dropna(inplace=True)  # eliminar filas con valores faltantes

fig = px.choropleth(
    conf_max,
    locations="Country/Region",
    locationmode="country names",
    color=np.log10(conf_max["Confirmados"]),
    hover_name="Country/Region",
    hover_data=["Confirmados"],
    projection="natural earth",
    width=900,
    color_continuous_scale=px.colors.sequential.Jet,
    title="Mapa de Confirmados COVID 19 por Pais",
)
fig.add_annotation(x=0.5, y=0, text="https://joserzapata.github.io/", showarrow=False)
fig.update(layout_coloraxis_showscale=False)
# grabar grafica en chart-studio si se proporciona el api-key
if api_key:
    py.plot(fig, filename="mapa_confirmados_pais", auto_open=False)
# fig.show()

# %% [markdown]
# # Confirmados vs Muertos por pais

# %%
death_melt["Fecha"] = pd.to_datetime(death_melt["Fecha"])
death_melt["Fecha"] = death_melt["Fecha"].dt.strftime("%m/%d/%Y")

max_Fecha = death_melt["Fecha"].iloc[-1]
death_max = death_melt[death_melt["Fecha"] == max_Fecha].copy()
death_max.dropna(inplace=True)  # eliminar filas con valores faltantes

full_melt_max = pd.merge(
    conf_max[["Country/Region", "Confirmados"]],
    death_max[["Country/Region", "Muertos"]],
    on="Country/Region",
    how="left",
)

fig = px.scatter(
    full_melt_max.sort_values("Muertos", ascending=False).iloc[:15, :],
    x="Confirmados",
    y="Muertos",
    color="Country/Region",
    size="Confirmados",
    height=500,
    width=900,
    text="Country/Region",
    log_x=True,
    log_y=True,
    title=f"Muertos vs Confirmados - {max_Fecha} - (15 Paises)",
)
fig.add_annotation(
    x=0.5,
    y=1,
    xref="paper",
    yref="paper",
    text="https://joserzapata.github.io/",
    showarrow=False,
)
fig.update_traces(textposition="top center")
fig.layout.update(showlegend=False)
# grabar grafica en chart-studio si se proporciona el api-key
if api_key:
    py.plot(fig, filename="scatter_muertos_confirmados", auto_open=False)
# fig.show()

# %% [markdown]
# ## Progresion Mundial en el Tiempo del numero de casos
#

# %%
world_melt = world.melt(
    id_vars="Fecha", value_vars=list(world.columns)[1:], var_name=None
)

fig = px.line(
    world_melt,
    x="Fecha",
    y="value",
    color="variable",
    color_discrete_sequence=["teal", "green", "coral", "navy"],
    title=f"Total de Casos en el tiempo de COVID 19 - {world.iloc[-1,0]}",
)
for n in list(world.columns)[1:]:
    fig.add_annotation(
        x=world.iloc[-1, 0],
        y=world.loc[world.index[-1], n],
        text=n,
        xref="x",
        yref="y",
        showarrow=True,
        ax=-50,
        ay=-20,
    )
# Indicador de numero total de confirmados
fig.add_indicator(
    title={"text": "Confirmados", "font": {"color": "teal"}},
    value=world["Confirmados"].iloc[-1],
    mode="number+delta",
    delta={"reference": world["Confirmados"].iloc[-2], "relative": True},
    domain={"x": [0, 0.25], "y": [0.15, 0.4]},
)
# Indicador numero total de Activos
fig.add_indicator(
    title={"text": "Activos", "font": {"color": "navy"}},
    value=world["Activos"].iloc[-1],
    mode="number+delta",
    delta={"reference": world["Activos"].iloc[-2], "relative": True},
    domain={"x": [0, 0.25], "y": [0.6, 0.85]},
)
# Indicador numero total de Recuperados
fig.add_indicator(
    title={"text": "Recuperados", "font": {"color": "green"}},
    value=world["Recuperados"].iloc[-1],
    mode="number+delta",
    delta={"reference": world["Recuperados"].iloc[-2], "relative": True},
    domain={"x": [0.25, 0.50], "y": [0.6, 0.85]},
)
# Indicador numero total de muertos
fig.add_indicator(
    title={"text": "Muertos", "font": {"color": "coral"}},
    value=world["Muertos"].iloc[-1],
    mode="number+delta",
    delta={"reference": world["Muertos"].iloc[-2], "relative": True},
    domain={"x": [0.25, 0.5], "y": [0.15, 0.4]},
)
fig.add_annotation(
    x=80,
    y=world_melt["value"].max(),
    text="https://joserzapata.github.io/",
    showarrow=False,
)
fig.layout.update(
    showlegend=False,
    yaxis={"title": {"text": "Numero de Personas"}},  # Cambiar texto eje y
)
# grabar grafica en chart-studio si se proporciona el api-key
if api_key:
    py.plot(fig, filename="total_casos_serie", auto_open=False)
# fig.show()

# %% [markdown]
# ## Total Casos Confirmados de COVID 19 por Pais
#

# %%
# df1 = confirmed_group.drop(columns=["China"])
df1 = confirmed_group.copy()
# Cambiar el nombre de la columna
df1.rename(columns={"date": "Fecha"}, inplace=True)
fecha = df1["Fecha"].iloc[-1]  # obtener la fecha del ultimo dato
paises = df1.iloc[-1, 1:]  # obtener la serie sin el primer dato, fecha
paises.sort_values(ascending=False, inplace=True)
top = 10
# keep top countries
df1 = df1[["Fecha"] + list(paises[:top].index)]

if api_key:
    # se toman la serie de tiempo cada 7 dias, por que las graficas
    # grandes no se pueden subir a chart-studio con subscripcion gratuita
    df1 = df1.iloc[::-7].iloc[::-1]

df_melt = df1.melt(id_vars="Fecha", value_vars=list(df1.columns)[1:], var_name=None)

fig = px.line(
    df_melt,
    x="Fecha",
    y="value",
    color="Country/Region",
    color_discrete_sequence=px.colors.qualitative.G10,
    width=900,
    title=f"Total Casos Confirmados de COVID 19 por Pais (Top 10) - {world.iloc[-1,0]}",
)
# top paises mas infectados

mas_infectados = []
for n in range(top):
    fig.add_annotation(
        x=fecha,
        y=paises[n],
        text=paises.index[n],
        showarrow=True,
        ax=+30,
        xref="x",
        yref="y",
    )
    mas_infectados.append(paises.index[n])

fig.layout.update(
    showlegend=False,
    yaxis={"title": {"text": "Numero de Personas"}},  # Cambiar texto eje y
)
fig.add_annotation(
    x=60,
    y=df_melt["value"].max(),
    text="https://joserzapata.github.io/",
    showarrow=False,
)
# grabar grafica en chart-studio si se proporciona el api-key
if api_key:
    py.plot(fig, filename="total_casos_no_china", auto_open=False)

# %% [markdown]
# # Animacion del Mapa de Evolucion Temporal del Codiv 19

# %%
if api_key:
    # se toman la serie de tiempo cada 30 dias, por que las graficas
    # grandes no se pueden subir a chart-studio con subscripcion gratuita
    confirmed_melt = confirmed_group.iloc[::-30].iloc[::-1].melt(id_vars="date").copy()
    confirmed_melt.rename(
        columns={"value": "Confirmados", "date": "Fecha"}, inplace=True
    )

confirmed_melt["Fecha"] = pd.to_datetime(confirmed_melt["Fecha"])
confirmed_melt["Fecha"] = confirmed_melt["Fecha"].dt.strftime("%m/%d/%Y")
confirmed_melt["size"] = confirmed_melt["Confirmados"].pow(0.3)
confirmed_melt.dropna(inplace=True)  # eliminar filas con valores faltantes


fig = px.scatter_geo(
    confirmed_melt,
    locations="Country/Region",
    locationmode="country names",
    color="Confirmados",
    size="size",
    hover_name="Country/Region",
    range_color=[0, max(confirmed_melt["Confirmados"]) + 2],
    projection="natural earth",
    animation_frame="Fecha",
    width=900,
    title="Contagiados COVID 19 en el Tiempo",
)
fig.update(layout_coloraxis_showscale=False)
fig.add_annotation(
    x=0.5, y=-0.1, text="https://joserzapata.github.io/", showarrow=False
)
# grabar grafica en chart-studio si se proporciona el api-key
if api_key:
    py.plot(fig, filename="mapa_evolucion_temporal", auto_open=False)
# fig.show()

# %% [markdown]
# ## Numero de Casos COVID 19 en Colombia

# %%
column_names = ["Fecha", "Confirmados", "Recuperados", "Muertos", "Activos"]
colombia = pd.DataFrame(columns=column_names)
colombia["Fecha"] = confirmed_group["date"]
colombia["Confirmados"] = confirmed_group["Colombia"]
colombia["Muertos"] = death_group["Colombia"]
colombia["Recuperados"] = recovered_group["Colombia"]
colombia["Activos"] = (
    colombia["Confirmados"] - colombia["Recuperados"] - colombia["Muertos"]
)

df_melt3 = colombia.melt(
    id_vars="Fecha", value_vars=list(colombia.columns)[1:], var_name=None
)
fig = px.line(
    df_melt3,
    x="Fecha",
    y="value",
    color="variable",
    color_discrete_sequence=["teal", "green", "coral", "navy"],
    title=f"Corona virus (COVID 19) en Colombia - {colombia.iloc[-1,0]}",
)
# Indicador de numero total de confirmados
fig.add_indicator(
    title={"text": "Confirmados", "font": {"color": "teal"}},
    value=colombia["Confirmados"].iloc[-1],
    mode="number+delta",
    delta={"reference": colombia["Confirmados"].iloc[-2], "relative": True},
    domain={"x": [0, 0.25], "y": [0.15, 0.4]},
)
# Indicador numero total de Activos
fig.add_indicator(
    title={"text": "Activos", "font": {"color": "navy"}},
    value=colombia["Activos"].iloc[-1],
    mode="number+delta",
    delta={"reference": colombia["Activos"].iloc[-2], "relative": True},
    domain={"x": [0, 0.25], "y": [0.6, 0.85]},
)
# Indicador numero total de Recuperados
fig.add_indicator(
    title={"text": "Recuperados", "font": {"color": "green"}},
    value=colombia["Recuperados"].iloc[-1],
    mode="number+delta",
    delta={"reference": colombia["Recuperados"].iloc[-2], "relative": True},
    domain={"x": [0.25, 0.50], "y": [0.6, 0.85]},
)
# Indicador numero total de muertos
fig.add_indicator(
    title={"text": "Muertos", "font": {"color": "coral"}},
    value=colombia["Muertos"].iloc[-1],
    mode="number+delta",
    delta={"reference": colombia["Muertos"].iloc[-2], "relative": True},
    domain={"x": [0.25, 0.5], "y": [0.15, 0.4]},
)
fig.add_annotation(
    x=80,
    y=df_melt3["value"].max(),
    text="https://joserzapata.github.io/",
    showarrow=False,
)
fig.layout.update(
    showlegend=False,
    yaxis={"title": {"text": "Numero de Personas"}},  # Cambiar texto eje y
    xaxis={"title": {"text": "Fecha"}},
)
# grabar grafica en chart-studio si se proporciona el api-key
if api_key:
    py.plot(fig, filename="Colombia_general", auto_open=False)
fig.show()


print("Graficas actualizadas \U0001f600")
print("https://joserzapata.github.io/")
