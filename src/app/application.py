
from ui.renderer import Renderer

class Application:

    def __init__(self, startup, navigator, renderer: Renderer):
        self.startup = startup
        self.navigator = navigator
        self.renderer = renderer
        self.session = None



    def start_archß(self):
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
            current_menu = self.navigator.navigate(choice)
        
        
        
        