from pathlib import Path

import pandas as pd

from core.io import read_csv


def parse_frb_csv(file_path: Path) -> pd.DataFrame:
    metadata = read_csv(file_path)

    value_columns = range(5, metadata.shape[1])

    df = (
        read_csv(
            file_path,
            index_col=0,
            usecols=value_columns,
        )
        .transpose()
        .rename_axis("period")
    )

    df.index = pd.to_datetime(df.index)

    return df
