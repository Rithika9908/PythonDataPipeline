
import json
import logging
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR / "config.json") as f:
    config = json.load(f)

log_path = BASE_DIR / config["log_file"]
log_path.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def read_data(file_path):
    path = BASE_DIR / file_path

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if path.stat().st_size == 0:
        raise ValueError("Input file is empty")

    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    elif path.suffix.lower() == ".json":
        return pd.read_json(path)
    else:
        raise ValueError("Only CSV and JSON files are supported")

def clean_data(df):
    df.columns = df.columns.str.strip().str.lower()

    required = {"name", "age", "salary", "department"}
    if not required.issubset(df.columns):
        raise ValueError("Required columns are missing")

    if config.get("remove_duplicates", True):
        df = df.drop_duplicates().copy()

    df["name"] = df["name"].fillna("Unknown").astype(str).str.strip()
    df["department"] = df["department"].fillna("Unknown").astype(str).str.strip()

    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

    df["age"] = df["age"].fillna(config["missing_age"])
    df["salary"] = df["salary"].fillna(config["missing_salary"])

    df = df[(df["age"] >= 0) & (df["salary"] >= 0)].copy()

    df["age"] = df["age"].astype(int)
    df["salary"] = df["salary"].astype(float)

    return df

def main():
    try:
        logging.info("Pipeline started")
        df = read_data(config["input_file"])
        logging.info("Loaded %d rows", len(df))

        df = clean_data(df)

        output = BASE_DIR / config["output_file"]
        output.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output, index=False)

        logging.info("Pipeline completed successfully")
        print("Data processing completed successfully!")
        print(df.to_string(index=False))
        print(f"Output saved to: {output}")

    except Exception as error:
        logging.exception("Pipeline failed")
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
