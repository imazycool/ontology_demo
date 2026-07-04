


class Application:

    def __init__(self, startup, navigator, renderer):
        self.startup = startup
        self.navigator = navigator
        self.renderer = renderer
        self.session = None



    def start(self):
        self.startup.initialize(self)
        menu = self.navigator.get_main_menu()
        choice = self.renderer.display(menu)
        print(choice)
        
        
        
        
        