from pathlib import Path

import pandas as pd

from core.paths import BASE_DIR, DATA_DIR
from sources.bea.constants import SERIES_IDS
from sources.bea.parsers import build_bea_read_csv_kwargs, pivot_bea_series


def export_series_fragments(df: pd.DataFrame, series_ids: tuple[str]) -> None:
    for series_id in series_ids:
        kwargs = {
            "path_or_buf": BASE_DIR
            / f"dataset_usa_bea-nipa-2015-05-01-{series_id}.csv"
        }
        df.pipe(pivot_bea_series, series_id=series_id).to_csv(**kwargs)


def filter_annual_observations(
    df: pd.DataFrame, column: str = "subperiod"
) -> pd.DataFrame:
    # =========================================================================
    # Yearly Data
    # =========================================================================
    return df[df.loc[:, column] == 0].drop(column, axis=1)


def main(
    file_path: Path = DATA_DIR / "dataset_usa_bea-nipa-2015-05-01.zip",
) -> None:

    pd.read_csv(**build_bea_read_csv_kwargs(file_path)).pipe(
        filter_annual_observations
    ).pipe(export_series_fragments, SERIES_IDS)
