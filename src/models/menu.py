


class Menu:

    def __init__(
        self,
        menu_id: str,
        title: str,
        message: str,
        options: list[str]
    ):
        self.menu_id = menu_id
        self.title = title
        self.message = message
        self.options = options
        
        