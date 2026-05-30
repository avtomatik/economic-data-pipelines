import pandas as pd


def pivot_series(df: pd.DataFrame, series_id: str) -> pd.DataFrame:
    """
    Retrieve Yearly Data for BEA Series ID
    """
    df = df[df["series_id"] == series_id]

    source_ids = sorted(df["source_id"])

    frames = []

    for source_id in source_ids:
        frame = (
            df[df["source_id"] == source_id].iloc[:, [-1]].drop_duplicates()
        )
        frames.append(frame)

    wide = pd.concat(frames, axis=1, sort=True)
    wide.columns = map(
        lambda _: "".join((_.split()[1].replace(".", "_"), series_id)),
        source_ids,
    )
    return wide
