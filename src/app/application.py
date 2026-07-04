


class Application:

    def __init__(self, startup):
        self.startup = startup
        self.entities = None
        self.session = None



    def start(self):
        self.startup.initialize(self)
        print("===================================")
        print(" Ontology Analytics Assistant")
        print("===================================")
        print("\nAvailable Business Entities\n")
        for index, entity in enumerate(self.entities, start=1):
            print(f"{index}. {entity}")
        
        
        
        
        