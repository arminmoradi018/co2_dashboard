import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"

def load_data():
    """
    Load and clean CO2 emissions data from OWID.
    Returns a DataFrame with columns: country, iso_code, year, co2.
    """
    try:
        df = pd.read_csv(DATA_URL)
        df = df[["country", "iso_code", "year", "co2"]]
        df["co2"] = pd.to_numeric(df["co2"], errors="coerce")
        df = df.dropna(subset=["iso_code", "co2"])
        df = df[(df["co2"] > 0) & (df["iso_code"].str.len() == 3)]
        return df
    except Exception as e:
        print(f"Error while loading or processing CO2 data: {e}")
        return pd.DataFrame(columns=["country", "iso_code", "year", "co2"])

_co2_data_cache = None
def get_co2_data():
    """
    Return cached CO2 data if available; otherwise load it.
    """
    global _co2_data_cache
    if _co2_data_cache is None:
        _co2_data_cache = load_data()
    return _co2_data_cache

co2_data = get_co2_data()
countries = sorted(co2_data["country"].unique())