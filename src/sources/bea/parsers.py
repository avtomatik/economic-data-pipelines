from pathlib import Path

import pandas as pd


def build_bea_read_csv_kwargs(file_path: Path):

    NAMES = ["source_id", "series_id", "period", "subperiod", "value"]
    USECOLS = [0, 14, 15, 16, 17]

    return {
        "filepath_or_buffer": file_path,
        "header": 0,
        "names": NAMES,
        "index_col": 2,
        "usecols": USECOLS,
    }


def pivot_bea_series(df: pd.DataFrame, series_id: str) -> pd.DataFrame:
    """
    Retrieve Yearly Data for BEA Series ID
    """
    df = df[df.loc[:, "series_id"] == series_id]
    source_ids = sorted(set(df.loc[:, "source_id"]))
    chunk = pd.concat(
        map(
            lambda _: df[df.loc[:, "source_id"] == _]
            .iloc[:, [-1]]
            .drop_duplicates(),
            source_ids,
        ),
        axis=1,
        sort=True,
    )
    chunk.columns = map(
        lambda _: "".join((_.split()[1].replace(".", "_"), series_id)),
        source_ids,
    )
    return chunk
