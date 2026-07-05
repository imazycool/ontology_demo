from models.menu import Menu 


class AnalyzeWorkflow:

    def __init__(self, metadata_service):
        self.metadata_service = metadata_service

    def start(self):
        entities = self.metadata_service.get_entity_names()
        return Menu(
            title="Business Entities",
            message="Select a business entity to analyze.",
            options=entities
        )