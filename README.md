# economic-data-pipelines

Reproducible ingestion and normalization pipelines for public macroeconomic datasets.

Currently includes:

- BEA (Bureau of Economic Analysis)
- IMF World Economic Outlook
- Federal Reserve
- Statistics Canada

## Requirements

- Python 3.12+
- uv

## Installation

```bash
uv sync
````

## Usage

Run a pipeline:

```bash
uv run python -m src.cli.main
```

## Repository Structure

```text
src/
├── core/
├── datasets/
└── cli/

data/
├── external/
├── raw/
├── bronze/
└── silver/
```

## Output

Pipelines write normalized parquet datasets into:

```text
data/bronze/
```

## License

MIT License. See the [LICENSE](LICENSE) file for more details.

---
