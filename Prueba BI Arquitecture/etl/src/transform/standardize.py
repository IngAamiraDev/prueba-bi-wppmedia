import pandas as pd

def standardize_google_ads(df):

    df = df.rename(columns={
        "date": "fecha",
        "campaign_name": "campaña",
        "impressions": "impresiones",
        "clicks": "clics",
        "media_cost": "costo"
    })

    df["plataforma"] = "Google Ads"

    df = df[
        ["plataforma", "fecha", "campaña", "impresiones", "clics", "costo"]
    ]

    df["fecha"] = pd.to_datetime(df["fecha"], dayfirst=True)
    df["fecha"] = df["fecha"].dt.strftime("%Y-%m-%d")

    return df


def standardize_meta_ads(df):

    df = df.rename(columns={
        "Date": "fecha",
        "Campaign Name": "campaña",
        "Impressions": "impresiones",
        "Clicks": "clics",
        "Media Cost": "costo"
    })

    df["plataforma"] = "Meta Ads"

    df = df[
        ["plataforma", "fecha", "campaña", "impresiones", "clics", "costo"]
    ]

    df["fecha"] = pd.to_datetime(df["fecha"], dayfirst=True)
    df["fecha"] = df["fecha"].dt.strftime("%Y-%m-%d")

    return df


def standardize_youtube_ads(df):

    df = df.rename(columns={
        "Date": "fecha",
        "Campaign Name": "campaña",
        "Impressions": "impresiones",
        "Clicks": "clics",
        "Media Cost": "costo"
    })

    df["plataforma"] = "YouTube"

    df = df[
        ["plataforma", "fecha", "campaña", "impresiones", "clics", "costo"]
    ]

    df["fecha"] = pd.to_datetime(df["fecha"], dayfirst=True)
    df["fecha"] = df["fecha"].dt.strftime("%Y-%m-%d")

    return df