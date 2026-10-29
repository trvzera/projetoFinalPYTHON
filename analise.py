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
    


# ========= BAHIA ==========

bahia = indicador_1.loc[indicador_1["uf_regiao"] == "Bahia"].iloc[0]

# ---- GENERO
bahia_homens = (bahia["homem_branca"] + bahia["homem_preta_parda"]) / 2 # Todos homens bahia
bahia_mulheres = (bahia["mulher_branca"] + bahia["mulher_preta_parda"]) / 2 # Todas mulheres bahia

# ---- RAÇA
bahia_preto_pardo = bahia["total_preta_parda"] # Todas pessoas pretas/pardas bahia
bahia_branca = bahia["total_branca"] # Todas pessoas brancas bahia

# ---- GENERO E RAÇA
bahia_homens_pretos_pardos = bahia["homem_preta_parda"]
bahia_homens_brancos = bahia["homem_branca"]
bahia_mulheres_pretas_pardas = bahia["mulher_preta_parda"]
bahia_mulheres_brancas = bahia["mulher_branca"]



# =========== PERNAMBUCO ============

pernambuco = indicador_1.loc[indicador_1["uf_regiao"] == "Pernambuco"].iloc[0]

# ---- GENERO
pernambuco_homens = (pernambuco["homem_branca"] + pernambuco["homem_preta_parda"]) / 2 # Todos homens pernambuco
pernambuco_mulheres = (pernambuco["mulher_branca"] + pernambuco["mulher_preta_parda"]) / 2 # Todas mulheres pernambuco

# ---- RAÇA
pernambuco_preto_pardo = pernambuco["total_preta_parda"] # Todas pessoas pretas/pardas pernambuco
pernambuco_branca = pernambuco["total_branca"] # Todas pessoas brancas pernambuco

# ---- GENERO E RAÇA
pernambuco_homens_pretos_pardos = pernambuco["homem_preta_parda"]
pernambuco_homens_brancos = pernambuco["homem_branca"]
pernambuco_mulheres_pretas_pardas = pernambuco["mulher_preta_parda"]
pernambuco_mulheres_brancas = pernambuco["mulher_branca"]



# =========== AMAZONAS ============

amazonas = indicador_1.loc[indicador_1["uf_regiao"] == "Amazonas"].iloc[0]

# ---- GENERO
amazonas_homens = (amazonas["homem_branca"] + amazonas["homem_preta_parda"]) / 2 # Todos homens amazonas
amazonas_mulheres = (amazonas["mulher_branca"] + amazonas["mulher_preta_parda"]) / 2 # Todas mulheres amazonas

# ---- RAÇA
amazonas_preto_pardo = amazonas["total_preta_parda"] # Todas pessoas pretas/pardas amazonas
amazonas_branca = amazonas["total_branca"] # Todas pessoas brancas amazonas

# ---- GENERO E RAÇA
amazonas_homens_pretos_pardos = amazonas["homem_preta_parda"]
amazonas_homens_brancos = amazonas["homem_branca"]
amazonas_mulheres_pretas_pardas = amazonas["mulher_preta_parda"]
amazonas_mulheres_brancas = amazonas["mulher_branca"]



# =========== CEARÁ ============

ceara = indicador_1.loc[indicador_1["uf_regiao"] == "Ceará"].iloc[0]

# ---- GENERO
ceara_homens = (ceara["homem_branca"] + ceara["homem_preta_parda"]) / 2 # Todos homens ceara
ceara_mulheres = (ceara["mulher_branca"] + ceara["mulher_preta_parda"]) / 2 # Todas mulheres ceara

# ---- RAÇA
ceara_preto_pardo = ceara["total_preta_parda"] # Todas pessoas pretas/pardas ceara
ceara_branca = ceara["total_branca"] # Todas pessoas brancas ceara

# ---- GENERO E RAÇA
ceara_homens_pretos_pardos = ceara["homem_preta_parda"]
ceara_homens_brancos = ceara["homem_branca"]
ceara_mulheres_pretas_pardas = ceara["mulher_preta_parda"]
ceara_mulheres_brancas = ceara["mulher_branca"]
