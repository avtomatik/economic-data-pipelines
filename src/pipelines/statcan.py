import pandas as pd

from core.io import read_csv
from core.paths import DATA_DIR
from sources.imf.selectors import filter_df
from sources.statcan.parsers import build_statcan_read_csv_kwargs
from sources.statcan.schemas import SCHEMA, TABLE_ID


def run() -> None:
    df = read_csv(
        DATA_DIR / f"dataset_can_{TABLE_ID:08n}-eng.zip",
        **build_statcan_read_csv_kwargs(TABLE_ID, SCHEMA),
    ).pipe(filter_df)
    # =============================================================================
    # Kludge
    # =============================================================================
    df["value"] = df["value"].apply(pd.to_numeric, errors="coerce")

    wide = df.pivot(
        index="period", columns="series_id", values="value", aggfunc="first"
    )

    wide = wide.groupby(wide.index.year).mean()
    wide["def"] = wide.iloc[:, 0].div(wide.iloc[:, 1])
    wide = wide.div(wide.loc[2012, :])
    wide["real_rebased"] = wide.iloc[:, 1].mul(wide.iloc[:, -1])
