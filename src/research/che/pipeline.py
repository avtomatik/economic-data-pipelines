from core.io import read_excel
from research.che.readers import get_sheet_names


from pathlib import Path


def run(data_dir: Path) -> None:
    dataset_files = list(data_dir.glob("dataset_che_*.xls"))

    if not dataset_files:
        return

    for file_path in dataset_files:
        sheet_names = get_sheet_names(file_path)

        for sheet_name in sheet_names:
            df = read_excel(file_path, sheet_name=sheet_name)
            print(df.head())