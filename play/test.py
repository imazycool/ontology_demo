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
from workflow.navigator import  Navigator
from ui.cli_renderer import CLIRenderer 


def main():
    db = MySQLConnection()
    metadata_service = MetadataService(db)
    startup = Startup(db)
    navigator = Navigator(metadata_service)
    renderer = CLIRenderer()
    application = Application(
        startup,
        navigator,
        renderer
    )
    application.start()


if __name__ == "__main__":
    main()