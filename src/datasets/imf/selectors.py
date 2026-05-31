import pandas as pd

from datasets.imf.constants import WEO_SERIES_IDS


def filter_country(df: pd.DataFrame, iso3: str) -> pd.DataFrame:
    return df[df["weo_country_code"] == iso3]


def filter_release(df: pd.DataFrame, year_base: int) -> pd.DataFrame:
    return df[
        df["release"]
        == f"International Monetary Fund, World Economic Outlook Database, April {year_base}"
    ]


def filter_series(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["weo_subject_code"].isin(WEO_SERIES_IDS)]


def filter_actual_observations(
    df: pd.DataFrame,
) -> pd.DataFrame:
    return df[
        df["source"] != "Estimates Start After"
    ]
