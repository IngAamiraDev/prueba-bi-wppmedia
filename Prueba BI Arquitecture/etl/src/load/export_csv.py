from utils.paths import RESULT_DIR

def export_csv(df):

    output_file = RESULT_DIR / "consolidated_campaign_data.csv"

    df.to_csv(output_file, index=False)

    print("Archivo generado:", output_file)