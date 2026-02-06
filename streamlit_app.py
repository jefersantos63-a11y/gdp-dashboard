import streamlit as st
import pandas as pd
from services.gdp_service import obtener_datos_del_PIB

st.set_page_config(page_title="GDP Dashboard", layout="wide")

st.title("📊 GDP Dashboard")

@st.cache_data
def cargar_datos():
    return obtener_datos_del_PIB()

df = cargar_datos()

# Selector de país
paises = sorted(df["Country Name"].unique())
pais_seleccionado = st.selectbox(
    "🌍 Selecciona un país",
    paises
)

# Filtrar datos del país
df_pais = df[df["Country Name"] == pais_seleccionado]

# Gráfica
st.subheader(f"Evolución del PIB – {pais_seleccionado}")

st.line_chart(
    df_pais.set_index("year")["gdp"]
)
