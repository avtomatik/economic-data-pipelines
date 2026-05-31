import pandas as pd


def normalize_frb_table(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.dropna(axis=1, how="all").transpose().iloc[3:].rename_axis("period")
    )
