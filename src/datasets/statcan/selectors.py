import pandas as pd


def filter_manufacturing(df: pd.DataFrame) -> pd.DataFrame:
    mask = (
        (df["naics"] == "All industries (x 1,000,000)")
        & (df["series_id"] != "v65201756")
    ) | (
        (df["naics"] == "Manufacturing (x 1,000,000)")
        & (df["series_id"] != "v65201809")
    )

    return df.loc[mask, ["series_id", "value"]]
