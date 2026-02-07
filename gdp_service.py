from pathlib import Path
import pandas as pd

def obtener_datos_del_PIB():
    ruta = Path(__file__).parent / "data" / "datos_pib.csv.csv"
    df = pd.read_csv(ruta)
    return df
