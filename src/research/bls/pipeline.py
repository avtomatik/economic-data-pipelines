import io

import requests

from core.io import read_csv
from datasets.bls.constants import (BASE_API_URL, BASE_API_URLS,
                                    BLS_READ_KWARGS, contents_table)


def run() -> None:
    for line in contents_table.split("\n"):
        response = requests.get("/".join((BASE_API_URL, line.split()[-1])))

        df = read_csv(io.BytesIO(response.content))
        print(df.head())

    for url in BASE_API_URLS:
        response = requests.get(url)
        print(response.content)

        df = read_csv(io.StringIO(response.content), **BLS_READ_KWARGS)
        print(df.head())
