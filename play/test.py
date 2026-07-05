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
from workflow.analyze_workflow import AnalyzeWorkflow 


def main():
    db = MySQLConnection()
    startup = Startup(db)
    metadata_service = MetadataService(db)
    analyze_workflow = AnalyzeWorkflow(metadata_service)
    navigator = Navigator(analyze_workflow) 
    renderer = CLIRenderer()
    application = Application(
        startup,
        navigator,
        renderer
    )
    application.start()


if __name__ == "__main__":
    main()