from app.session import Session 

class Startup:

    def __init__(self, metadata_service):
        self.metadata_service = metadata_service

    def initialize(self, application):
        application.entities = \
            self.metadata_service.get_entity_names()
        application.session = Session()
    