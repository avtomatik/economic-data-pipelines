import pandas as pd

from core.frame import set_period_index
from sources.imf.constants import WEO_SERIES_IDS


def extract_series(df: pd.DataFrame, series_id: str) -> pd.DataFrame:

    chunk = df[df["weo_subject_code"] == series_id]
    chunk.columns = ("period", series_id)
    chunk = chunk.drop(
        chunk[chunk.iloc[:, 11] == "Estimates Start After"].index
    )
    chunk = chunk.iloc[:, (11, 12)]
    chunk.iloc[:, 1] = chunk.iloc[:, 1].astype(float)
    return set_period_index(chunk)


def build_wide_table(df: pd.DataFrame) -> pd.DataFrame:
    frames = []

    for series_id in WEO_SERIES_IDS:
        frames.append(extract_series(df, series_id))

    return pd.concat(frames, axis=1, sort=True)
