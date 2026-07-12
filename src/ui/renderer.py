from models.menu import Menu




class Renderer:

    def display(self, menu: Menu) -> int:
        raise NotImplementedError()

    def show_message(self, message: str) -> None:
        raise NotImplementedError()
    
    # def show_table(self, rows):
    #     raise NotImplementedError()
    
    def show_table(self, headers: list[str], rows: list):
        raise NotImplementedError()