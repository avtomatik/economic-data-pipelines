from openpyxl import load_workbook


from pathlib import Path


def get_sheet_names(file_path: Path) -> list[str]:
    workbook = load_workbook(file_path, read_only=True)
    return workbook.sheetnames