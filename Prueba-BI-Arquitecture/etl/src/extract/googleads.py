import pandas as pd
from utils.paths import DATA_DIR

def extract_google_ads():

    df = pd.read_excel(DATA_DIR / "Googleads.xlsx")

    return df