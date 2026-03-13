import pandas as pd
from utils.paths import DATA_DIR

def extract_youtube_ads():

    df = pd.read_csv(DATA_DIR / "Youtube.csv")

    return df