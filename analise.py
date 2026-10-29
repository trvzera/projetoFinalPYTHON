import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px


path = "Tabela 1.1.1.xls"

bruto = pd.read_excel(path, header=None)
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
    

# ========= BRASIL ==========

brasil = indicador_1.loc[indicador_1["uf_regiao"] == "Brasil"].iloc[0]

homens = (brasil["homem_branca"] + brasil["homem_preta_parda"]) / 2 # Todos homens brasil
mulheres = (brasil["mulher_branca"] + brasil["mulher_preta_parda"]) / 2 # Todas mulheres brasil

mulher_homem_preto_pardo = (brasil["homem_preta_parda"] + brasil["mulher_preta_parda"]) / 2 # Todas pessoas pretas/pardas brasil
mulher_homem_branca = (brasil["homem_branca"] + brasil["mulher_branca"]) # Todas pessoas brancas brasil

# =========== RONDONIA ============



