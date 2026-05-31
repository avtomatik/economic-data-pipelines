from pathlib import Path

import pandas as pd

from core.io import read_csv, write_parquet
from core.paths import BRONZE_DIR, DATA_DIR
from datasets.statcan.parsers import build_statcan_read_csv_kwargs
from datasets.statcan.schemas import SCHEMA, TABLE_ID
from datasets.statcan.selectors import filter_manufacturing


def run(
    source_path: Path = DATA_DIR / f"dataset_can_{TABLE_ID:08n}-eng.zip",
    output_dir: Path = BRONZE_DIR,
) -> None:
    df = read_csv(
        source_path,
        **build_statcan_read_csv_kwargs(TABLE_ID, SCHEMA),
    ).pipe(filter_manufacturing)

    df["value"] = df["value"].apply(pd.to_numeric, errors="coerce")

    wide = df.pivot(
        index="period", columns="series_id", values="value", aggfunc="first"
    )

    wide = wide.groupby(wide.index.year).mean()
    wide["def"] = wide.iloc[:, 0].div(wide.iloc[:, 1])
    wide = wide.div(wide.loc[2012, :])
    wide["real_rebased"] = wide.iloc[:, 1].mul(wide.iloc[:, -1])

    write_parquet(df, output_dir / "statcan_canada.parquet")
