import streamlit as st
import pandas as pd
from gdp_service import obtener_datos_del_PIB


st.set_page_config(page_title="GDP Dashboard", layout="wide")

st.title("📊 GDP Dashboard")

@st.cache_data
def cargar_datos():
    return obtener_datos_del_PIB()

df = cargar_datos()

st.subheader("📊 Datos del PIB")
st.dataframe(df)


# Selector de país
paises = sorted(df["Country Name"].unique())
pais_seleccionado = st.selectbox(
    "🌍 Selecciona un país",
    paises
)

# Filtrar datos del país
df_pais = df[df["Country Name"] == pais_seleccionado]
df_pais_largo = df_pais.melt(
    id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
    var_name="year",
    value_name="gdp"
)

df_pais_largo = df_pais_largo.dropna(subset=["gdp"])
df_pais_largo["year"] = df_pais_largo["year"].astype(int)


# Gráfica
st.subheader(f"Evolución del PIB – {pais_seleccionado}")

st.line_chart(
    st.line_chart(
    df_pais_largo.set_index("year")["gdp"]
)

)
