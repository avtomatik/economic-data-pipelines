from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"

RAW_DIR = DATA_DIR / "raw"
BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"

for path in (RAW_DIR, BRONZE_DIR, SILVER_DIR):
    path.mkdir(parents=True, exist_ok=True)
