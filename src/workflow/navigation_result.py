


from models.menu import Menu


class NavigationResult:

    def __init__(
        self,
        menu: Menu | None = None,
        message: str | None = None
    ):
        self.menu = menu
        self.message = message