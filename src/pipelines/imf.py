from core.io import read_csv
from core.paths import DATA_DIR
from sources.imf.constants import COUNTRY_CANADA
from sources.imf.selectors import filter_country, filter_release
from sources.imf.transforms import build_wide_table


def run() -> None:
    # "dataset_world_imf-WEOApr2018all.xls"

    read_csv(
        DATA_DIR / "dataset World IMF World Economic Outlook.csv",
        low_memory=False,
    ).pipe(filter_release, 2015).pipe(filter_country, COUNTRY_CANADA).pipe(
        build_wide_table
    )
