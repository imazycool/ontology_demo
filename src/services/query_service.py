

class QueryService:

    def __init__(self, db):
        self.db = db

    def execute(self, sql):
        return self.db.execute_sql(sql)