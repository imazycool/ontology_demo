
from ui.renderer import Renderer
from services.sql_builder import SQLBuilder

class Application:

    def __init__(self, startup, navigator, renderer: Renderer):
        self.startup = startup
        self.navigator = navigator
        self.renderer = renderer
        self.session = None



    def start_arch(self):
        self.startup.initialize(self)
        current_menu = self.navigator.get_main_menu()
        while current_menu:
            choice = self.renderer.display(current_menu)
            result = self.navigator.navigate(choice)
            if result.message:
                self.renderer.show_message(result.message)
            current_menu = result.menu
                
                
    def start(self):
        self.startup.initialize(self)
        current_menu = self.navigator.get_main_menu()
        while current_menu:
            choice = self.renderer.display(current_menu)
            if choice == 0:
                break
            if choice < 0 or choice > len(current_menu.options):
                self.renderer.show_message("Please select a valid option.")
                continue
            
            selected_option = current_menu.options[choice - 1]
            if current_menu.menu_id == "MAIN_MENU":
                current_menu = self.navigator.navigate(choice)
            elif current_menu.menu_id == "ENTITY_MENU":
                self.session.selected_entity = selected_option
                current_menu = self.navigator.analyze_workflow.get_metric_menu(
                    self.session.selected_entity
                )
            elif current_menu.menu_id == "METRIC_MENU":
                self.session.selected_metric = selected_option
                current_menu = (
                    self.navigator.analyze_workflow.get_dimension_menu(
                    self.session.selected_entity
                    )
                )
            elif current_menu.menu_id == "DIMENSION_MENU":
                self.session.selected_dimensions = [selected_option]
                self.renderer.show_message(
                    f"""
                    Analysis Summary
                    Entity     : {self.session.selected_entity}
                    Metric     : {self.session.selected_metric}
                    Dimension  : {self.session.selected_dimensions[0]}
                    """
                    )
                builder = SQLBuilder(self.metadata_service)
                sql = builder.build(self.session)
                self.session.generated_sql = sql
                rows = self.query_service.execute(sql)
                self.session.query_result = rows
                self.renderer.show_table(rows)
        
        
        
        