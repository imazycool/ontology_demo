from app.session import Session


class Startup:

    def __init__(self, db):
        self.db = db


    def initialize(self, application):
        self.db.connect()
        application.session = Session()
        