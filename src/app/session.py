

class Session:

    def __init__(self):
        
        # -------------------------
        # Business Selection
        # -------------------------
        self.selected_entity = None
        self.selected_metric = None
        self.selected_dimensions = []
        self.selected_filters = {}

        # -------------------------
        # Metadata Exploration
        # -------------------------
        self.selected_attribute = None
        self.selected_relationship = None

        # -------------------------
        # Query
        # -------------------------
        self.generated_sql = None
        self.query_result = None
        
        
        
        