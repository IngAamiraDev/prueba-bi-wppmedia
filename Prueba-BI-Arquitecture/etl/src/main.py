import pandas as pd

from extract.googleads import extract_google_ads
from extract.meta import extract_meta_ads
from extract.youtube import extract_youtube_ads

from transform.standardize import (
    standardize_google_ads,
    standardize_meta_ads,
    standardize_youtube_ads
)

from transform.validate import validate_data
from load.export_csv import export_csv


def main():

    print("EXTRACT")

    google_raw = extract_google_ads()
    meta_raw = extract_meta_ads()
    youtube_raw = extract_youtube_ads()

    print("TRANSFORM")

    google_df = standardize_google_ads(google_raw)
    meta_df = standardize_meta_ads(meta_raw)
    youtube_df = standardize_youtube_ads(youtube_raw)

    print("CONSOLIDATE")

    consolidated_data = pd.concat(
        [google_df, meta_df, youtube_df],
        ignore_index=True
    )

    consolidated_data = validate_data(consolidated_data)

    print("LOAD")

    export_csv(consolidated_data)

    print("Proceso ETL finalizado")
    print("Total registros:", len(consolidated_data))


if __name__ == "__main__":
    main()