import io

import pandas as pd
import requests

from sources.bls.constants import bls_urls, contents_table, kwargs, url_root


def main() -> None:
    for line in contents_table.split("\n"):
        response = requests.get("/".join((url_root, line.split()[-1])))

        df = pd.read_csv(io.BytesIO(response.content))

    for url in bls_urls:
        response = requests.get(url)

        print(response.content)

        kwargs["filepath_or_buffer"] = io.StringIO(response.content)
        print(pd.read_csv(**kwargs))
