from models.menu import Menu 


class AnalyzeWorkflow:

    def __init__(self, metadata_service):
        self.metadata_service = metadata_service


    def start(self):
        return self.get_entity_menu()


    def get_entity_menu(self)-> Menu:
        entities = self.metadata_service.get_entity_names()
        return Menu(
            menu_id="ENTITY_MENU",
            title="Business Entities",
            message="Select a business entity to analyze.",
            options=entities
        )
        
        
    def get_metric_menu(self, entity_name: str) -> Menu:
        metrics = self.metadata_service.get_metrics(entity_name)
        return Menu(
            menu_id="METRIC_MENU",
            title=f"{entity_name} Metrics",
            message="Select a business metric to analyze.",
            options=metrics
        )


    def get_dimension_menu(self, entity_name):
        dimensions = self.metadata_service.get_dimensions(entity_name)
        return Menu(
            menu_id="DIMENSION_MENU",
            title=f"{entity_name} Dimensions",
            message="Select one or more dimensions.",
            options=dimensions
        )

    def review_query(self, session):
        return Menu(
            menu_id="REVIEW_MENU",
            title="Review Analysis",
            message=(
                f"Entity    : {session.selected_entity}\n"
                f"Metric    : {session.selected_metric}\n"
                f"Dimension : {session.selected_dimensions[0]}"
            ),
            options=[
                "Generate SQL"
            ]
        )

    


