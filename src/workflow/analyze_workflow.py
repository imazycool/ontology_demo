from models.menu import Menu 


class AnalyzeWorkflow:

    def __init__(self, metadata_service):
        self.metadata_service = metadata_service


    def start(self):
        return self.get_entity_menu()


    def get_entity_menu(self)-> Menu:
        entities = self.metadata_service.get_entity_names()
        return Menu(
            title="Business Entities",
            message="Select a business entity to analyze.",
            options=entities
        )
        
        
    def get_metric_menu(self, entity_name: str) -> Menu:
        metrics = self.metadata_service.get_metrics(entity_name)
        return Menu(
            title=f"{entity_name} Metrics",
            message="Select a business metric to analyze.",
            options=metrics
        )




