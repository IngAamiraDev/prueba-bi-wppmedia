import pandas as pd

def validate_data(df):

    df["impresiones"] = pd.to_numeric(df["impresiones"], errors="coerce")
    df["clics"] = pd.to_numeric(df["clics"], errors="coerce")
    df["costo"] = pd.to_numeric(df["costo"], errors="coerce")

    df = df.drop_duplicates()

    return df