from typing import Any


def build_statcan_read_csv_kwargs(
    table_id: int, schema: dict
) -> dict[str, Any]:
    return {
        "header": 0,
        "names": schema[table_id]["columns"].keys(),
        "index_col": 0,
        "usecols": schema[table_id]["columns"].values(),
        "parse_dates": schema[table_id]["parse_dates"],
    }
