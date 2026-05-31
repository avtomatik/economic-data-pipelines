import zipfile
from pathlib import Path
from typing import BinaryIO, Sequence

import pandas as pd
from lxml import etree

from core.io import read_csv, read_xml
from datasets.frb.constants import DEFAULT_OBSERVATION_COLUMNS


def _largest_archive_member(
    archive: zipfile.ZipFile,
) -> zipfile.ZipInfo:
    """Return the largest file contained in an archive."""
    return max(
        archive.infolist(),
        key=lambda member: member.file_size,
    )


def _open_largest_member(
    archive: zipfile.ZipFile,
) -> BinaryIO:
    member = _largest_archive_member(archive)
    return archive.open(member)


def read_archived_csv(file_path: Path) -> pd.DataFrame:
    with zipfile.ZipFile(file_path) as archive:
        with _open_largest_member(archive) as stream:
            return read_csv(
                stream,
                index_col=0,
                skiprows=4,
            )


def read_archived_xml(
    file_path: Path,
    xpath: str,
    namespaces: dict[str, str],
) -> pd.DataFrame:
    with zipfile.ZipFile(file_path) as archive:
        with _open_largest_member(archive) as stream:
            return read_xml(
                stream,
                index_col=0,
                skiprows=4,
                xpath=xpath,
                namespaces=namespaces,
            )


def read_api_response(
    archive_content,
    columns: Sequence[str] = DEFAULT_OBSERVATION_COLUMNS,
) -> pd.DataFrame:
    with zipfile.ZipFile(archive_content) as archive:
        with _open_largest_member(archive) as stream:
            root = etree.parse(stream)

    records = []

    for obs in root.xpath('//*[local-name()="Obs"]'):
        records.append(
            (
                obs.get("TIME_PERIOD"),
                obs.get("OBS_VALUE"),
            )
        )

    return pd.DataFrame(records, columns=columns)
