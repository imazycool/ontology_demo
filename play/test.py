from pathlib import Path
import sys

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Source Directory
SRC_DIR = PROJECT_ROOT / "src"

# Add src to Python Path (only once)
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from db.mysql_connection import MySQLConnection


def main():
    db = MySQLConnection()
    print(db.connection)


if __name__ == "__main__":
    main()