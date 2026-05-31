import pandas as pd


def build_wide_table(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot(
        index="period", columns="weo_subject_code", values="value"
    ).sort_index()
