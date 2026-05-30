import zipfile

import pandas as pd

from core.io import read_excel, write_parquet
from core.paths import BRONZE_DIR, DATA_DIR


def read_bea_metadata_sheet(
    xl_file: pd.ExcelFile, sheet_name: str
) -> pd.DataFrame:
    """
    Retrieves pd.DataFrame for Meta Information from Bureau of Economic Analysis Zip Archives

    Parameters
    ----------
    xl_file : ExcelFile
    sheet_name : str

    Returns
    -------
    pd.DataFrame
        ================== =================================
        df.index           Index
        df.iloc[:, 0]      Table
        df.iloc[:, 1]      Measure Unit
        df.iloc[:, 2]      Frequency Period
        df.iloc[:, 3]      Service
        df.iloc[:, 4]      Data Published
        df.iloc[:, 5]      File Created
        ================== =================================
    """
    kwargs = {
        "sheet_name": sheet_name,
        "header": None,
        "nrows": 6,
        "usecols": range(1),
    }
    return read_excel(xl_file, **kwargs).transpose()


def normalize_bea_metadata(
    df: pd.DataFrame, wb_name: str, sheet_name: str
) -> pd.DataFrame:
    df.columns = (
        "table",
        "unit",
        "frequency_period",
        "service",
        "data_published",
        "file_created",
    )
    df["file_created"] = (
        df["file_created"]
        .str.replace("File created ", "")
        .apply(pd.to_datetime)
    )
    df["wb_name"] = wb_name
    df["sheet_name"] = sheet_name
    return df


def main(
    archive_name: str = "dataset_usa_bea-release-2015-02-27-SectionAll_xls_1969_2015.zip",
    file_name: str = "usa_bea_release-2015-02-27_meta.xlsx",
) -> None:
    with zipfile.ZipFile(DATA_DIR / archive_name) as archive:
        df = pd.DataFrame()
        for wb_name in archive.namelist():
            print("{:=^50}".format("New File"))
            with pd.ExcelFile(archive.open(wb_name)) as xl_file:
                df = pd.concat(
                    [
                        df,
                        pd.concat(
                            map(
                                lambda _: read_bea_metadata_sheet(
                                    xl_file, _
                                ).pipe(normalize_bea_metadata, wb_name, _),
                                xl_file.sheet_names[1:],
                            )
                        ),
                    ]
                )

    df.pipe(write_parquet, BRONZE_DIR / file_name, index=False)
