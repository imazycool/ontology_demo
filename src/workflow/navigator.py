

from models.menu import Menu
from workflow.analyze_workflow import AnalyzeWorkflow 

class Navigator:

    def __init__(self, analyze_workflow: AnalyzeWorkflow):
        self.analyze_workflow = analyze_workflow
        
        

    def get_main_menu(self):
        return Menu(
            title="Ontology Analytics Assistant",
            message="How can I help you today?",
            options=[
                "Start Analyzing Business Data",
                "Explore & Understand Business Metadata",
                "Administer Metadata"
            ]
        )
    
    

    def navigate(self, choice: int) -> Menu | None:
        if choice == 1:
            return self.analyze_workflow.start()
        elif choice == 2:
            return Menu(
                title="Business Metadata Explorer",
                message="This module is under development.",
                options=[]
            )
        elif choice == 3:
            return Menu(
                title="Metadata Administration",
                message="This module is under development.",
                options=[]
            )
        elif choice == 0:
            return None
        else:
            return self.get_main_menu() 