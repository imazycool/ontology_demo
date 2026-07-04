

from models.menu import Menu
from services.metadata_service import MetadataService


class Navigator:

    def __init__(self, metadata_service: MetadataService):
        self.metadata_service = metadata_service

    def get_main_menu(self):
        return Menu(
            title="Ontology Analytics Assistant",
            message="How can I help you today?",
            options=[
                "Analyze Business Data",
                "Explore Business Metadata",
                "Administration"
            ]
        )