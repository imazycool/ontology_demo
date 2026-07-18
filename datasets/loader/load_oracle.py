import os
from pathlib import Path

import pandas as pd
import oracledb

# -----------------------------
# Oracle Connection
# -----------------------------
USERNAME = "your_user"
PASSWORD = "your_password"
HOST = "localhost"
PORT = 1521
SERVICE_NAME = "FREEPDB1"      # Change if required

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_FOLDER = BASE_DIR / "datasets" / "sales_ai"

if not DATASET_FOLDER.exists():
    raise FileNotFoundError(f"Dataset folder not found: {DATASET_FOLDER}")

print(f"Loading dataset from: {DATASET_FOLDER}")

# -----------------------------
# Connect
# -----------------------------
dsn = f"{HOST}:{PORT}/{SERVICE_NAME}"

connection = oracledb.connect(
    user=USERNAME,
    password=PASSWORD,
    dsn=dsn
)

cursor = connection.cursor()

# -----------------------------
# Load Every CSV
# -----------------------------
csv_files = sorted(DATASET_FOLDER.glob("*.csv"))

for csv_file in csv_files:

    table_name = csv_file.stem.upper()

    print(f"\nLoading {table_name}")

    df = pd.read_csv(csv_file)

    columns = list(df.columns)

    placeholders = ",".join(
        [":" + str(i + 1) for i in range(len(columns))]
    )

    sql = f"""
        INSERT INTO {table_name}
        ({",".join(columns)})
        VALUES ({placeholders})
    """

    rows = [
        tuple(None if pd.isna(v) else v for v in row)
        for row in df.values.tolist()
    ]

    cursor.executemany(sql, rows)

    connection.commit()

    print(f"Inserted {cursor.rowcount} rows.")

cursor.close()
connection.close()

print("\nAll CSV files loaded successfully.")