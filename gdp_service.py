import pandas as pd
from pathlib import Path

def obtener_datos_del_PIB():
    ruta = Path(__file__).parent / "datos" / "gdp_data.csv"

    df = pd.read_csv(ruta)

    df = df.melt(
        id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
        var_name="year",
        value_name="gdp"
    )

    df = df.dropna(subset=["gdp"])
    df["year"] = df["year"].astype(int)

    return df

