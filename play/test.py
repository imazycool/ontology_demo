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
from services.metadata_service import MetadataService 
from app.application import Application
from app.startup import Startup 


def main():
    db = MySQLConnection()
    db.connect()
    metadata_service = MetadataService(db)
    startup = Startup(metadata_service)
    application = Application(startup)
    application.start()
    db.disconnect()



if __name__ == "__main__":
    main()