

class SQLBuilder:

    def __init__(self, metadata_service):
        self.metadata_service = metadata_service



    def build(self, session):
        entity = self.metadata_service.get_entity(
            session.selected_entity
        )
        metric = self.metadata_service.get_metric_definition(
            session.selected_metric
        )
        attribute = self.metadata_service.get_attribute(
            session.selected_entity,
            session.selected_dimensions[0]
        )
        table = entity[4]
        formula = metric[1]
        dimension = attribute[1]
        sql = f"""
            SELECT
                {dimension},
                {formula} AS metric_value
            FROM {table}
            GROUP BY {dimension}
            """
        return sql.strip()