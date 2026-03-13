import pandas as pd
from utils.paths import DATA_DIR

def extract_meta_ads():

    df = pd.read_csv(DATA_DIR / "Meta.csv")

    return df