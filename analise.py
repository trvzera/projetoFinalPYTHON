import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px


path = "Tabela 1.1.1.xls"

bruto = pd.read_excel(path, engine="xlrd", header=None)
indicador_1 = bruto.iloc[8:41].copy()
indicador_1.columns = [
    "uf_regiao",
    "total",
    "total_branca",
    "total_preta_parda",
    "homem_branca",
    "homem_preta_parda",
    "mulher_branca",
    "mulher_preta_parda",
]
indicador_1 = indicador_1.reset_index(drop=True)

for col in indicador_1.columns[1:]:
    indicador_1[col] = pd.to_numeric(indicador_1[col], errors="coerce")
    


df = pd.DataFrame({
    'Regiao': ['Suldeste', 'Nordeste', 'Sul', 'Norte', 'Centro-Oeste'],
    'Mulheres': [18.5, 19.2, 17.8, 18.0, 17.5],
    'Homens': [10.2, 11.0, 9.8, 10.5, 10.0]
}).melt(id_vars=['Regiao'], var_name='Gênero', value_name='Horas')

fig = px.bar(
    df, 
    x='Regiao', y='Horas', 
    color='Gênero',
    barmode='group',
    orientation='v',
    color_continuous_scale='Viridis',
    title="Horas Dedicadas a Afazeres Domésticos por Região"
)

st.plotly_chart(fig, use_container_width=True)