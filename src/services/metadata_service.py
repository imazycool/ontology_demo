from repository import metadata_queries 

class MetadataService:

    def __init__(self, db):
        self.db = db
        
        
    
    def get_entity_names(self):
        rows=self.db.execute_query(metadata_queries.GET_ENTITY_NAMES) 
        return [ row[0] for row in rows]
    
    
    
    def get_metrics(self, entity_name: str):
        rows = self.db.execute_query(
            metadata_queries.GET_ENTITY_METRICS,
            (entity_name,)
        )
        return [row[0] for row in rows]
    
    
    
    def get_entity(self, entity_name):
        pass

    def get_attribute(self, attribute_name):
        pass

    def get_metric(self, metric_name):
        pass

    def get_business_term(self, term):
        pass

    def normalize_value(self, attribute_name, value):
        pass

    def get_business_relationship(self, entity_name):
        pass

    def get_join_path(self, source_entity, target_entity):
        pass

    def list_metrics(self):
        pass

    def list_dimensions(self):
        pass

    def list_filterable_attributes(self):
        pass