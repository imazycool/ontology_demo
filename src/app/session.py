

class Session:

    def __init__(self):
        self.selected_entity = None
        self.selected_attribute = None
        self.selected_metric = None
        self.selected_relationship = None
        self.selected_dimensions = []
        self.selected_filters = {}