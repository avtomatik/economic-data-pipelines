import zipfile
from pathlib import Path

import pandas as pd
import requests

from core.paths import BRONZE_DIR, RAW_DIR
from econdata.providers.statcan.schemas import DEFAULT_SCHEMA, STATCAN_SCHEMAS

BASE_URL = "https://www150.statcan.gc.ca/n1/tbl/csv/"


class StatCanProvider:

    def load_table(
        self,
        archive_id: int,
        use_cache: bool = True,
    ) -> pd.DataFrame:

        parquet_path = BRONZE_DIR / f"{archive_id}.parquet"

        # ============================================================
        # Fast path
        # ============================================================

        if use_cache and parquet_path.exists():
            return pd.read_parquet(parquet_path)

        # ============================================================
        # Ensure raw archive exists
        # ============================================================

        zip_path = self.ensure_raw_exists(archive_id)

        # ============================================================
        # Parse raw archive
        # ============================================================

        df = self.parse_zip(
            archive_id,
            zip_path,
        )

        # ============================================================
        # Persist bronze cache
        # ============================================================

        df.to_parquet(parquet_path)

        return df

    def ensure_raw_exists(
        self,
        archive_id: int,
    ) -> Path:

        zip_path = RAW_DIR / f"{archive_id:08d}-eng.zip"

        if zip_path.exists():
            return zip_path

        self.download_archive(
            archive_id,
            zip_path,
        )

        return zip_path

    def download_archive(
        self,
        archive_id: int,
        destination: Path,
    ) -> None:

        url = f"{BASE_URL}" f"{archive_id:08d}-eng.zip"

        response = requests.get(
            url,
            timeout=120,
        )

        response.raise_for_status()

        destination.write_bytes(response.content)

    def parse_zip(
        self,
        archive_id: int,
        zip_path: Path,
    ) -> pd.DataFrame:

        schema = STATCAN_SCHEMAS.get(
            archive_id,
            DEFAULT_SCHEMA,
        )

        columns = schema["columns"]

        with zipfile.ZipFile(zip_path) as zf:

            csv_name = f"{archive_id:08d}.csv"

            with zf.open(csv_name) as f:

                return pd.read_csv(
                    f,
                    header=0,
                    names=list(columns.keys()),
                    usecols=list(columns.values()),
                    index_col=0,
                    parse_dates=schema["parse_dates"],
                )
