from typing import Any

import pandas as pd

from core.paths import DATA_DIR


def filter_series(df: pd.DataFrame, series_id: str) -> pd.DataFrame:
    """


    Parameters
    ----------
    df : pd.DataFrame
        ================== =================================
        df.index           Period
        df.iloc[:, 0]      Series IDs
        df.iloc[:, 1]      Values
        ================== =================================
    series_id : str

    Returns
    -------
    pd.DataFrame
        ================== =================================
        df.index           Period
        df.iloc[:, 0]      Series
        ================== =================================
    """
    assert df.shape[1] == 2
    return (
        df[df.iloc[:, 0] == series_id]
        .iloc[:, [1]]
        .rename(columns={"value": series_id})
    )


def pull_imf_can_gdp_by_series_id(
    df: pd.DataFrame, series_id: str
) -> pd.DataFrame:

    chunk = df[df.iloc[:, 4] == series_id]
    chunk.columns = ("period", series_id)
    chunk = chunk.drop(
        chunk[chunk.iloc[:, 11] == "Estimates Start After"].index
    )
    chunk = chunk.iloc[:, (11, 12)]
    chunk.iloc[:, 1] = chunk.iloc[:, 1].astype(float)
    return chunk.set_index("period")


def get_kwargs_imf_gdp():

    FILE_NAME = "dataset_world_imf-WEOApr2018all.xls"

    file_path = DATA_DIR / FILE_NAME
    kwargs = {"filepath_or_buffer": file_path, "low_memory": False}

    FILE_NAME = "dataset World IMF World Economic Outlook.csv"
    file_path = DATA_DIR / FILE_NAME
    return {"filepath_or_buffer": file_path, "low_memory": False}


def combine_imf_can_gdp_for_year_base(year_base: int) -> pd.DataFrame:

    SERIES_IDS = ["NGDP_R", "NGDP", "NGDPD", "NGDP_D"]

    df = pd.read_csv(**get_kwargs_imf_gdp())
    df = df[
        df.iloc[:, 1]
        == f"International Monetary Fund, World Economic Outlook Database, April {year_base}"
    ]
    df = df[df.iloc[:, 3] == "CAN"]
    return pd.concat(
        map(lambda _: df.pipe(pull_imf_can_gdp_by_series_id, _), SERIES_IDS),
        axis=1,
        sort=True,
    )


def get_kwargs_can() -> dict[str, Any]:

    SCHEMA = {
        3790031: {
            "columns": {
                "period": 0,
                "geo": 1,
                "seas": 2,
                "prices": 3,
                "naics": 4,
                "series_id": 5,
                "value": 7,
            },
            "parse_dates": True,
        }
    }

    FILE_NAME = f"dataset_can_{3790031:08n}-eng.zip"
    file_path = DATA_DIR / FILE_NAME
    return {
        "filepath_or_buffer": file_path,
        "header": 0,
        "names": SCHEMA[3790031]["columns"].keys(),
        "index_col": 0,
        "usecols": SCHEMA[3790031]["columns"].values(),
        "parse_dates": SCHEMA[3790031]["parse_dates"],
    }


def filter_df(df: pd.DataFrame) -> pd.DataFrame:
    FILTER = (df.loc[:, "naics"] == "All industries (x 1,000,000)") & (
        df.loc[:, "series_id"] != "v65201756"
    )
    FILTER = (df.loc[:, "naics"] == "Manufacturing (x 1,000,000)") & (
        df.loc[:, "series_id"] != "v65201809"
    )
    return df[FILTER].iloc[:, -2:]


def main():
    _df = pd.read_csv(**get_kwargs_can()).pipe(filter_df)
    # =============================================================================
    # Kludge
    # =============================================================================
    _df.iloc[:, -1] = _df.iloc[:, -1].apply(pd.to_numeric, errors="coerce")

    df = pd.concat(
        map(
            lambda _: _df.pipe(filter_series, _),
            sorted(set(_df.loc[:, "series_id"])),
        ),
        axis=1,
        sort=True,
    )
    df = df.groupby(df.index.year).mean()
    df["def"] = df.iloc[:, 0].div(df.iloc[:, 1])
    df = df.div(df.loc[2012, :])
    df["real_rebased"] = df.iloc[:, 1].mul(df.iloc[:, -1])

    file_name = "dataset_can_cansim.csv"
    df.to_csv(file_name)

    df = combine_imf_can_gdp_for_year_base(2015)
