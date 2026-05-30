import xml.etree.ElementTree as et
import zipfile
from pathlib import Path
from xml import etree

import pandas as pd


def read_frb_xml(file_path: Path) -> None:
    with zipfile.ZipFile(file_path) as archive:
        MAP_FILES = {_.filename: _.file_size for _ in archive.filelist}
        # =====================================================================
        # Select the Largest File with min() Function
        # =====================================================================
        with archive.open(min(MAP_FILES)) as f:
            kwargs = {
                "path_or_buffer": f,
                "xpath": ".//frb:DataSet",
                "namespaces": {
                    "kf": "http://www.federalreserve.gov/structure/compact/G17_IP_MAJOR_INDUSTRY_GROUPS"
                },
            }
            df = pd.read_xml(**kwargs)
            kwargs = {"path_or_buffer": f, "index_col": 0, "skiprows": 4}
            df = pd.read_xml(**kwargs).dropna(axis=1, how="all").transpose()
            df.drop(df.index[:3], inplace=True)
            df.rename_axis("period")


def read_frb_csv(file_path: Path) -> pd.DataFrame:
    kwargs = {"filepath_or_buffer": file_path}
    # =====================================================================
    # Load
    # =====================================================================
    df = pd.read_csv(**kwargs)
    kwargs["index_col"] = 0
    kwargs["usecols"] = range(5, df.shape[1])
    # =====================================================================
    # Re-Load
    # =====================================================================
    df = pd.read_csv(**kwargs).transpose().rename_axis("period")
    df.index = pd.to_datetime(df.index)
    return df


def read_usa_frb_archive(file_path: Path) -> None:
    kwargs = {"index_col": 0, "skiprows": 4}
    with zipfile.ZipFile(file_path) as archive:
        # =====================================================================
        # Select the Largest File with min() Function
        # =====================================================================
        with archive.open(
            min({_.filename: _.file_size for _ in archive.filelist})
        ) as f:
            kwargs["filepath_or_buffer"] = f
            df = pd.read_csv(**kwargs).dropna(axis=1, how="all").transpose()
            return df.drop(df.index[:3]).rename_axis("period")
            # =================================================================
            # TODO: Further Development
            # =================================================================
            xtree = et.parse(min(MAP_FILES))
            xroot = xtree.getroot()


def read_xml_from_response_with_columns(
    file, columns_expected: list[str] = ["TIME_PERIOD", "IP.B50001.S"]
):
    with zipfile.ZipFile(file) as archive:
        # =========================================================================
        # Select the Largest File with min() Function
        # =========================================================================
        with archive.open(
            min({_.filename: _.file_size for _ in archive.filelist})
        ) as f:
            tree = etree.parse(f)
            doc = tree.getroot()

            # the base xpath expression
            expr = '//*[local-name()="Obs"]'
            rows = []
            for r in doc.xpath(expr):
                row = []

                # use more xpath expressions to get to the target attributes
                row.extend(
                    [
                        r.xpath(".//@TIME_PERIOD")[0],
                        r.xpath(".//@OBS_VALUE")[0],
                    ]
                )
                rows.append(row)
            return pd.DataFrame(rows, columns=columns_expected)
